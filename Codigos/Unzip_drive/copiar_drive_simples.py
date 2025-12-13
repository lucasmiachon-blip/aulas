r"""
Script SIMPLES para copiar arquivos entre contas do Google Drive
ORIGEM: H:\My Drive\ (lucas.miachon@hc.fm.usp.br)
DESTINO: G:\My Drive\Palestras\ (lucasmiachon87@gmail.com)

- Copia arquivos reais (ignora .gdoc, .gsheet, .gslides)
- Processa atalhos .lnk
- Descomprime ZIPs automaticamente
"""
import os
import shutil
import zipfile
import subprocess
from pathlib import Path

# Configurações
ORIGEM = r"H:\My Drive"
DESTINO = r"G:\My Drive\Palestras"

# Extensões do Google para ignorar
EXTENSOES_GOOGLE = {'.gdoc', '.gsheet', '.gslides', '.gdraw', '.gtable', '.gform'}

# Estatísticas
stats = {
    'arquivos_copiados': 0,
    'arquivos_ignorados': 0,
    'zips_descomprimidos': 0,
    'atalhos_processados': 0,
    'erros': []
}

# Set para evitar processar o mesmo caminho duas vezes
processados = set()

def obter_caminho_lnk(caminho_lnk):
    """Resolve um arquivo .lnk usando PowerShell"""
    try:
        ps_cmd = f"$shell = New-Object -ComObject WScript.Shell; $shortcut = $shell.CreateShortcut('{caminho_lnk}'); $shortcut.TargetPath"
        resultado = subprocess.run(
            ['powershell', '-Command', ps_cmd],
            capture_output=True,
            text=True,
            timeout=5
        )
        if resultado.returncode == 0:
            caminho_alvo = resultado.stdout.strip()
            if caminho_alvo and os.path.exists(caminho_alvo):
                return caminho_alvo
    except:
        pass
    return None

def descomprimir_zip(caminho_zip, pasta_destino):
    """Descomprime um arquivo ZIP"""
    try:
        nome_base = os.path.splitext(os.path.basename(caminho_zip))[0]
        pasta_extracao = os.path.join(pasta_destino, nome_base)
        os.makedirs(pasta_extracao, exist_ok=True)
        
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(pasta_extracao)
        
        print(f"  ✓ ZIP descomprimido: {os.path.basename(caminho_zip)}")
        stats['zips_descomprimidos'] += 1
        return True
    except Exception as e:
        stats['erros'].append(f"Erro ao descomprimir {caminho_zip}: {e}")
        return False

def copiar_arquivo(caminho_origem, caminho_destino):
    """Copia um arquivo, renomeando se necessário"""
    pasta_dest = os.path.dirname(caminho_destino)
    os.makedirs(pasta_dest, exist_ok=True)
    
    # Se já existe, renomeia
    if os.path.exists(caminho_destino):
        nome_base, ext = os.path.splitext(os.path.basename(caminho_destino))
        contador = 1
        while os.path.exists(caminho_destino):
            novo_nome = f"{nome_base}_{contador}{ext}"
            caminho_destino = os.path.join(pasta_dest, novo_nome)
            contador += 1
    
    try:
        shutil.copy2(caminho_origem, caminho_destino)
        stats['arquivos_copiados'] += 1
        return True
    except Exception as e:
        stats['erros'].append(f"Erro ao copiar {caminho_origem}: {e}")
        return False

def processar_item(caminho_item, pasta_relativa_destino=""):
    """Processa um item (arquivo ou pasta)"""
    caminho_norm = os.path.normpath(caminho_item)
    
    # Evita processar duas vezes
    if caminho_norm in processados:
        return
    
    # Ignora pastas especiais do Google Drive
    if '.shortcut-targets-by-id' in caminho_norm or 'desktop.ini' in caminho_item.lower():
        return
    
    processados.add(caminho_norm)
    
    nome_item = os.path.basename(caminho_item)
    
    # Se é arquivo .lnk (atalho)
    if caminho_item.lower().endswith('.lnk'):
        caminho_real = obter_caminho_lnk(caminho_item)
        if caminho_real and os.path.exists(caminho_real):
            print(f"📂 Atalho: {nome_item} → {os.path.basename(caminho_real)}")
            stats['atalhos_processados'] += 1
            # Processa o conteúdo do atalho
            if os.path.isdir(caminho_real):
                processar_pasta(caminho_real, pasta_relativa_destino)
            elif os.path.isfile(caminho_real):
                caminho_dest = os.path.join(DESTINO, pasta_relativa_destino, os.path.basename(caminho_real)) if pasta_relativa_destino else os.path.join(DESTINO, os.path.basename(caminho_real))
                copiar_arquivo(caminho_real, caminho_dest)
        return
    
    # Ignora arquivos do Google
    if os.path.isfile(caminho_item):
        ext = os.path.splitext(caminho_item)[1].lower()
        if ext in EXTENSOES_GOOGLE:
            stats['arquivos_ignorados'] += 1
            return
        
        # Calcula destino
        if pasta_relativa_destino:
            caminho_dest = os.path.join(DESTINO, pasta_relativa_destino, nome_item)
        else:
            caminho_dest = os.path.join(DESTINO, nome_item)
        
        # Copia arquivo
        copiar_arquivo(caminho_item, caminho_dest)
        
        # Se é ZIP, descomprime também
        if caminho_item.lower().endswith('.zip'):
            pasta_dest_zip = os.path.dirname(caminho_dest)
            descomprimir_zip(caminho_item, pasta_dest_zip)
        
        return
    
    # Se é pasta, processa recursivamente
    if os.path.isdir(caminho_item):
        processar_pasta(caminho_item, pasta_relativa_destino)

def processar_pasta(caminho_pasta, pasta_relativa=""):
    """Processa uma pasta recursivamente"""
    caminho_norm = os.path.normpath(caminho_pasta)
    
    if caminho_norm in processados:
        return
    
    try:
        items = os.listdir(caminho_pasta)
        
        for item in items:
            caminho_item = os.path.join(caminho_pasta, item)
            
            # Ignora pastas especiais
            if '.shortcut-targets-by-id' in caminho_item or item.lower() in ['desktop.ini', 'thumbs.db']:
                continue
            
            # Calcula pasta relativa de destino
            if pasta_relativa:
                nova_pasta_rel = os.path.join(pasta_relativa, item)
            else:
                nova_pasta_rel = item
            
            processar_item(caminho_item, nova_pasta_rel if os.path.isdir(caminho_item) else pasta_relativa)
    
    except PermissionError:
        stats['erros'].append(f"Sem permissão: {caminho_pasta}")
    except Exception as e:
        stats['erros'].append(f"Erro em {caminho_pasta}: {e}")

def main():
    print("="*70)
    print("🚀 COPIANDO ARQUIVOS ENTRE CONTAS DO GOOGLE DRIVE")
    print("="*70)
    print(f"📁 Origem: {ORIGEM}")
    print(f"📁 Destino: {DESTINO}\n")
    
    if not os.path.exists(ORIGEM):
        print(f"❌ ERRO: Origem não encontrada: {ORIGEM}")
        return
    
    os.makedirs(DESTINO, exist_ok=True)
    
    print("🔄 Iniciando cópia...\n")
    
    # Processa a pasta de origem
    processar_pasta(ORIGEM)
    
    # Resumo
    print("\n" + "="*70)
    print("✅ PROCESSO CONCLUÍDO!")
    print("="*70)
    print(f"✓ Arquivos copiados: {stats['arquivos_copiados']}")
    print(f"⊘ Arquivos ignorados (Google): {stats['arquivos_ignorados']}")
    print(f"📦 ZIPs descomprimidos: {stats['zips_descomprimidos']}")
    print(f"🔗 Atalhos processados: {stats['atalhos_processados']}")
    print(f"✗ Erros: {len(stats['erros'])}")
    
    if stats['erros']:
        print(f"\n⚠️  Primeiros erros:")
        for erro in stats['erros'][:10]:
            print(f"  - {erro}")
    
    print("="*70)

if __name__ == "__main__":
    main()

