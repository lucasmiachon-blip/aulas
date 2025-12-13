r"""
Script para copiar arquivos entre duas contas do Google Drive
ORIGEM: H:\My Drive\ (conta lucas.miachon@hc.fm.usp.br)
DESTINO: G:\My Drive\Palestras\ (conta lucasmiachon87@gmail.com)

Trata atalhos do Google Drive e ignora arquivos do Google (Docs, Sheets, Slides)
"""
import os
import shutil
import subprocess
from pathlib import Path
from typing import Set, Dict, Optional

class CopiadorGoogleDrive:
    """Classe para copiar arquivos entre contas do Google Drive"""
    
    # Extensões de arquivos do Google que devem ser ignorados
    EXTENSOES_GOOGLE_IGNORAR = {'.gdoc', '.gsheet', '.gslides', '.gdraw', '.gtable', '.gform', '.gmap', '.gscript'}
    
    # Extensões de shortcuts (arquivos .lnk do Windows no Google Drive)
    EXTENSOES_SHORTCUT = {'.shortcut', '.gshortcut', '.lnk'}
    
    def __init__(self, origem: str, destino: str):
        """
        Inicializa o copiador.
        
        Args:
            origem: Caminho da pasta de origem
            destino: Caminho da pasta de destino
        """
        self.origem = os.path.normpath(origem)
        self.destino = os.path.normpath(destino)
        self.arquivos_copiados = 0
        self.arquivos_ignorados = 0
        self.atalhos_processados = 0
        self.erros = []
        self.nomes_usados: Dict[str, int] = {}  # Para rastrear nomes duplicados
        self.caminhos_processados: Set[str] = set()  # Para evitar recursão infinita
        
        if not os.path.exists(self.origem):
            raise FileNotFoundError(f"Origem não encontrada: {self.origem}")
        
        # Cria a pasta de destino se não existir
        os.makedirs(self.destino, exist_ok=True)
        
        print(f"📍 Origem: {self.origem}")
        print(f"📍 Destino: {self.destino}\n")
    
    def is_arquivo_google(self, caminho: str) -> bool:
        """Verifica se é um arquivo do Google que deve ser ignorado"""
        extensao = os.path.splitext(caminho)[1].lower()
        return extensao in self.EXTENSOES_GOOGLE_IGNORAR
    
    def is_shortcut(self, caminho: str) -> bool:
        """Verifica se é um atalho do Google Drive"""
        if os.path.isfile(caminho):
            extensao = os.path.splitext(caminho)[1].lower()
            if extensao in self.EXTENSOES_SHORTCUT:
                return True
            
            # Verifica se é um arquivo pequeno (~4KB) que pode ser atalho
            try:
                tamanho = os.path.getsize(caminho)
                if 3000 <= tamanho <= 5000:  # Atalhos do Google Drive são ~4KB
                    return True
            except:
                pass
        
        return False
    
    def obter_caminho_shortcut(self, caminho_shortcut: str) -> Optional[str]:
        """
        Tenta obter o caminho real apontado por um shortcut usando PowerShell.
        """
        # Usa PowerShell para resolver o link .lnk
        try:
            ps_script = f"""
            $shell = New-Object -ComObject WScript.Shell
            $shortcut = $shell.CreateShortcut('{caminho_shortcut}')
            $shortcut.TargetPath
            """
            
            resultado = subprocess.run(
                ['powershell', '-Command', ps_script],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if resultado.returncode == 0:
                caminho_alvo = resultado.stdout.strip()
                if caminho_alvo and os.path.exists(caminho_alvo):
                    return caminho_alvo
        except subprocess.TimeoutExpired:
            pass
        except Exception:
            pass
        
        # Método alternativo: Tenta usar win32com se disponível
        try:
            import win32com.client
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(caminho_shortcut)
            caminho_alvo = shortcut.TargetPath
            
            if caminho_alvo and os.path.exists(caminho_alvo):
                return caminho_alvo
        except ImportError:
            pass
        except Exception:
            pass
        
        # No Google Drive File Stream, os .lnk apontam para pastas em .shortcut-targets-by-id
        # Tenta encontrar na pasta especial do Google Drive
        pasta_pai = os.path.dirname(caminho_shortcut)
        nome_base = os.path.splitext(os.path.basename(caminho_shortcut))[0]
        
        # Procura na pasta .shortcut-targets-by-id na raiz do drive
        if os.path.exists("H:\\.shortcut-targets-by-id"):
            try:
                for root, dirs, files in os.walk("H:\\.shortcut-targets-by-id"):
                    for dir_name in dirs:
                        if nome_base.lower() in dir_name.lower():
                            caminho_candidato = os.path.join(root, dir_name)
                            if os.path.isdir(caminho_candidato):
                                return caminho_candidato
            except:
                pass
        
        return None
    
    def obter_nome_unico(self, nome_arquivo: str, pasta_destino: str) -> str:
        """Obtém um nome único para o arquivo, adicionando _1, _2, etc se necessário"""
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        if not os.path.exists(caminho_destino):
            return nome_arquivo
        
        # Já existe, precisa renomear
        nome_base, extensao = os.path.splitext(nome_arquivo)
        contador = 1
        
        while True:
            novo_nome = f"{nome_base}_{contador}{extensao}"
            novo_caminho = os.path.join(pasta_destino, novo_nome)
            
            if not os.path.exists(novo_caminho):
                return novo_nome
            
            contador += 1
    
    def copiar_arquivo(self, caminho_origem: str, caminho_destino: str) -> bool:
        """Copia um arquivo individual"""
        try:
            nome_arquivo = os.path.basename(caminho_origem)
            pasta_destino = os.path.dirname(caminho_destino)
            
            # Garante que a pasta de destino existe
            os.makedirs(pasta_destino, exist_ok=True)
            
            # Obtém nome único se necessário
            nome_unico = self.obter_nome_unico(nome_arquivo, pasta_destino)
            caminho_destino_final = os.path.join(pasta_destino, nome_unico)
            
            shutil.copy2(caminho_origem, caminho_destino_final)
            
            if nome_unico != nome_arquivo:
                print(f"  ↻ Copiado (renomeado): {os.path.relpath(caminho_origem, self.origem)} → {os.path.relpath(caminho_destino_final, self.destino)}")
            else:
                print(f"  ✓ Copiado: {os.path.relpath(caminho_origem, self.origem)}")
            
            self.arquivos_copiados += 1
            return True
            
        except Exception as e:
            erro_msg = f"Erro ao copiar {caminho_origem}: {e}"
            self.erros.append(erro_msg)
            print(f"  ✗ {erro_msg}")
            return False
    
    def processar_item(self, caminho_item: str, pasta_relativa_origem: str = ""):
        """
        Processa um item (arquivo ou pasta) da origem
        """
        # Normaliza o caminho para evitar duplicatas
        caminho_item_norm = os.path.normpath(caminho_item)
        
        # Evita recursão infinita - ignora se já foi processado
        if caminho_item_norm in self.caminhos_processados:
            return
        
        # Ignora pastas especiais do Google Drive
        if '.shortcut-targets-by-id' in caminho_item_norm:
            return
        
        nome_item = os.path.basename(caminho_item)
        
        # Ignora arquivos do sistema
        if nome_item.lower() == 'desktop.ini' or nome_item.lower() == 'thumbs.db':
            return
        
        # Ignora arquivos do Google
        if os.path.isfile(caminho_item) and self.is_arquivo_google(caminho_item):
            self.arquivos_ignorados += 1
            return
        
        # Se é um shortcut, processa o conteúdo
        if self.is_shortcut(caminho_item):
            # Marca como processado para evitar loop
            self.caminhos_processados.add(caminho_item_norm)
            
            caminho_real = self.obter_caminho_shortcut(caminho_item)
            if caminho_real and os.path.exists(caminho_real):
                caminho_real_norm = os.path.normpath(caminho_real)
                # Se o caminho real já foi processado, pula
                if caminho_real_norm in self.caminhos_processados:
                    return
                
                print(f"📂 Processando atalho: {nome_item} → {os.path.relpath(caminho_real, self.origem)}")
                self.atalhos_processados += 1
                self.caminhos_processados.add(caminho_real_norm)
                self.processar_pasta(caminho_real, pasta_relativa_origem)
            else:
                print(f"  ⚠ Atalho não resolvido: {nome_item}")
            return
        
        # Se é uma pasta, processa recursivamente
        if os.path.isdir(caminho_item):
            self.caminhos_processados.add(caminho_item_norm)
            self.processar_pasta(caminho_item, pasta_relativa_origem)
            return
        
        # Se é um arquivo normal, copia
        if os.path.isfile(caminho_item):
            self.caminhos_processados.add(caminho_item_norm)
            # Calcula o caminho relativo para manter estrutura
            if pasta_relativa_origem:
                caminho_destino = os.path.join(self.destino, pasta_relativa_origem, nome_item)
            else:
                caminho_destino = os.path.join(self.destino, nome_item)
            
            self.copiar_arquivo(caminho_item, caminho_destino)
    
    def processar_pasta(self, caminho_pasta: str, pasta_relativa: str = ""):
        """
        Processa recursivamente uma pasta
        """
        caminho_pasta_norm = os.path.normpath(caminho_pasta)
        
        # Evita processar pastas já processadas
        if caminho_pasta_norm in self.caminhos_processados and pasta_relativa:
            return
        
        try:
            items = os.listdir(caminho_pasta)
            
            for item in items:
                caminho_item = os.path.join(caminho_pasta, item)
                caminho_item_norm = os.path.normpath(caminho_item)
                
                # Ignora pastas especiais do Google Drive
                if '.shortcut-targets-by-id' in caminho_item_norm:
                    continue
                
                # Calcula o caminho relativo para manter estrutura
                if pasta_relativa:
                    nova_pasta_relativa = os.path.join(pasta_relativa, item)
                else:
                    nova_pasta_relativa = item
                
                # Verifica se é arquivo do Google
                if os.path.isfile(caminho_item) and self.is_arquivo_google(caminho_item):
                    self.arquivos_ignorados += 1
                    continue
                
                # Processa o item
                if os.path.isfile(caminho_item):
                    self.processar_item(caminho_item, pasta_relativa)
                else:
                    self.processar_item(caminho_item, nova_pasta_relativa)
        
        except PermissionError:
            self.erros.append(f"Sem permissão para acessar: {caminho_pasta}")
        except Exception as e:
            self.erros.append(f"Erro ao processar pasta {caminho_pasta}: {e}")
    
    def copiar_tudo(self):
        """Inicia o processo de cópia de tudo da origem para o destino"""
        print("="*70)
        print("🚀 INICIANDO CÓPIA DE ARQUIVOS ENTRE CONTAS DO GOOGLE DRIVE")
        print("="*70)
        print(f"\n📁 Processando: {self.origem}\n")
        
        # Processa a pasta de origem
        self.processar_pasta(self.origem)
        
        # Mostra resumo
        print("\n" + "="*70)
        print("✅ PROCESSO CONCLUÍDO!")
        print("="*70)
        print(f"✓ Arquivos copiados: {self.arquivos_copiados}")
        print(f"⊘ Arquivos ignorados (Google Docs/Sheets/Slides): {self.arquivos_ignorados}")
        print(f"🔗 Atalhos processados: {self.atalhos_processados}")
        print(f"✗ Erros: {len(self.erros)}")
        
        if self.erros:
            print(f"\n⚠️  ERROS ENCONTRADOS:")
            for erro in self.erros[:10]:  # Mostra apenas os primeiros 10
                print(f"  - {erro}")
            if len(self.erros) > 10:
                print(f"  ... e mais {len(self.erros) - 10} erros")
        
        print("="*70)


def main():
    """Função principal"""
    origem = r"H:\My Drive"
    destino = r"G:\My Drive\Palestras"
    
    try:
        copiador = CopiadorGoogleDrive(origem, destino)
        copiador.copiar_tudo()
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

