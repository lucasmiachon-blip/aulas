"""
Script simples para descompactar arquivos ZIP no seu drive na nuvem
Funciona com OneDrive, Google Drive Desktop, e qualquer pasta sincronizada
"""

import os
import zipfile
from pathlib import Path
import sys


def descompactar_zip(caminho_zip, pasta_destino=None, listar_arquivos=True):
    """
    Descompacta um arquivo ZIP
    
    Args:
        caminho_zip: Caminho para o arquivo ZIP
        pasta_destino: Onde extrair (None = mesma pasta do ZIP)
        listar_arquivos: Se True, mostra cada arquivo sendo extraído
    
    Returns:
        True se sucesso, False se erro
    """
    caminho_zip = Path(caminho_zip)
    
    # Verifica se arquivo existe
    if not caminho_zip.exists():
        print(f"❌ Erro: Arquivo não encontrado: {caminho_zip}")
        return False
    
    # Verifica se é um ZIP válido
    if not zipfile.is_zipfile(caminho_zip):
        print(f"❌ Erro: {caminho_zip.name} não é um arquivo ZIP válido")
        return False
    
    # Define pasta de destino
    if pasta_destino is None:
        # Cria pasta com o nome do arquivo ZIP (sem extensão)
        pasta_destino = caminho_zip.parent / caminho_zip.stem
    else:
        pasta_destino = Path(pasta_destino)
    
    # Cria pasta de destino se não existir
    pasta_destino.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"\n📦 Descompactando: {caminho_zip.name}")
        print(f"📁 Destino: {pasta_destino}\n")
        
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            arquivos = zip_ref.namelist()
            total = len(arquivos)
            
            print(f"Total de arquivos no ZIP: {total}")
            print("-" * 60)
            
            for i, arquivo in enumerate(arquivos, 1):
                if listar_arquivos:
                    print(f"[{i}/{total}] Extraindo: {arquivo}")
                zip_ref.extract(arquivo, pasta_destino)
            
            print("-" * 60)
            print(f"✅ Concluído! {total} arquivos extraídos")
            print(f"📂 Localização: {pasta_destino.absolute()}")
            
            return True
            
    except zipfile.BadZipFile:
        print("❌ Erro: Arquivo ZIP corrompido")
        return False
    except PermissionError:
        print("❌ Erro: Sem permissão para escrever na pasta de destino")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False


def descompactar_varios(pasta_com_zips, pasta_destino=None):
    """
    Descompacta todos os arquivos ZIP em uma pasta
    
    Args:
        pasta_com_zips: Pasta contendo os arquivos ZIP
        pasta_destino: Pasta base para extrair (None = mesma pasta)
    """
    pasta = Path(pasta_com_zips)
    
    if not pasta.exists() or not pasta.is_dir():
        print(f"❌ Erro: Pasta não encontrada: {pasta}")
        return
    
    # Encontra todos os arquivos ZIP
    zips = list(pasta.glob("*.zip"))
    
    if not zips:
        print(f"⚠️  Nenhum arquivo ZIP encontrado em: {pasta}")
        return
    
    print(f"\n📦 Encontrados {len(zips)} arquivo(s) ZIP")
    print("=" * 60)
    
    sucesso = 0
    falha = 0
    
    for zip_file in zips:
        if descompactar_zip(zip_file, pasta_destino, listar_arquivos=False):
            sucesso += 1
        else:
            falha += 1
        print()
    
    print("=" * 60)
    print(f"✅ Sucesso: {sucesso} | ❌ Falha: {falha}")


def descompactar_recursivo(pasta_raiz, pasta_destino=None):
    """
    Busca e descompacta TODOS os arquivos ZIP em uma pasta e suas subpastas
    Perfeito para descompactar diversos ZIPs espalhados em várias pastas
    
    Args:
        pasta_raiz: Pasta inicial para buscar ZIPs (busca em todas subpastas)
        pasta_destino: Pasta base para extrair (None = mesma pasta de cada ZIP)
    """
    pasta = Path(pasta_raiz)
    
    if not pasta.exists() or not pasta.is_dir():
        print(f"❌ Erro: Pasta não encontrada: {pasta}")
        return
    
    print(f"\n🔍 Procurando arquivos ZIP em: {pasta}")
    print("   Buscando em todas as subpastas...")
    print("=" * 60)
    
    # Busca recursiva por todos os ZIPs
    zips = list(pasta.rglob("*.zip"))
    
    if not zips:
        print(f"⚠️  Nenhum arquivo ZIP encontrado em {pasta} e subpastas")
        return
    
    print(f"\n📦 Encontrados {len(zips)} arquivo(s) ZIP no total!")
    print("\n📋 Lista de arquivos encontrados:")
    print("-" * 60)
    
    for i, zip_file in enumerate(zips, 1):
        # Mostra caminho relativo para ficar mais legível
        try:
            rel_path = zip_file.relative_to(pasta)
            print(f"  {i}. {rel_path}")
        except:
            print(f"  {i}. {zip_file.name}")
    
    print("-" * 60)
    resposta = input("\n▶ Descompactar todos esses arquivos? (S/N): ").strip().upper()
    
    if resposta != 'S':
        print("❌ Operação cancelada")
        return
    
    print("\n" + "=" * 60)
    print("🚀 INICIANDO DESCOMPACTAÇÃO EM LOTE")
    print("=" * 60)
    
    sucesso = 0
    falha = 0
    
    for i, zip_file in enumerate(zips, 1):
        print(f"\n[{i}/{len(zips)}] Processando: {zip_file.name}")
        print(f"📁 Localização: {zip_file.parent}")
        
        if descompactar_zip(zip_file, pasta_destino, listar_arquivos=False):
            sucesso += 1
        else:
            falha += 1
    
    print("\n" + "=" * 60)
    print("🏁 PROCESSAMENTO CONCLUÍDO")
    print("=" * 60)
    print(f"✅ Sucesso: {sucesso} arquivo(s)")
    print(f"❌ Falha: {falha} arquivo(s)")
    print(f"📊 Total processado: {len(zips)} arquivo(s)")
    print("=" * 60)


def menu_interativo():
    """Menu interativo para usar o script"""
    print("=" * 60)
    print("  DESCOMPACTADOR DE ARQUIVOS ZIP - DRIVE NA NUVEM")
    print("=" * 60)
    print("\n1 - Descompactar um arquivo ZIP específico")
    print("2 - Descompactar todos os ZIPs de uma pasta (sem subpastas)")
    print("3 - Descompactar TODOS os ZIPs (busca em subpastas) ⭐")
    print("4 - Sair")
    
    escolha = input("\n▶ Escolha uma opção: ").strip()
    
    if escolha == "1":
        caminho = input("\n📁 Caminho completo do arquivo ZIP: ").strip().strip('"')
        destino = input("📂 Pasta de destino (Enter = mesma pasta): ").strip().strip('"')
        
        if not destino:
            destino = None
        
        descompactar_zip(caminho, destino)
    
    elif escolha == "2":
        pasta = input("\n📁 Caminho da pasta com os ZIPs: ").strip().strip('"')
        destino = input("📂 Pasta base de destino (Enter = mesma pasta): ").strip().strip('"')
        
        if not destino:
            destino = None
        
        descompactar_varios(pasta, destino)
    
    elif escolha == "3":
        pasta = input("\n📁 Caminho da pasta raiz do Google Drive: ").strip().strip('"')
        print("\n💡 Dica: Use algo como 'G:\\My Drive' ou 'C:\\Users\\lucas\\Google Drive'")
        
        if not pasta:
            print("❌ Caminho não pode ser vazio!")
            return
        
        destino = input("📂 Pasta base de destino (Enter = mesma pasta): ").strip().strip('"')
        
        if not destino:
            destino = None
        
        descompactar_recursivo(pasta, destino)
    
    elif escolha == "4":
        print("\n👋 Até logo!")
        return
    else:
        print("\n❌ Opção inválida!")


if __name__ == "__main__":
    # Se recebeu argumentos pela linha de comando
    if len(sys.argv) > 1:
        caminho_zip = sys.argv[1]
        pasta_destino = sys.argv[2] if len(sys.argv) > 2 else None
        descompactar_zip(caminho_zip, pasta_destino)
    else:
        # Modo interativo
        menu_interativo()
