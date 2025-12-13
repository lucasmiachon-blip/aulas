import os
import shutil
import json
import zipfile
import tarfile
import gzip
import bz2
from pathlib import Path
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

class GoogleDriveDesktop:
    """Classe para acessar arquivos do Google Drive for Desktop"""
    
    def __init__(self, drive_path: Optional[str] = None):
        """
        Inicializa o gerenciador do Google Drive Desktop.
        
        Args:
            drive_path: Caminho personalizado do Google Drive. 
                       Se None, tenta detectar automaticamente.
        """
        self.drive_path = drive_path or self._detectar_caminho_drive()
        
        if not self.drive_path or not os.path.exists(self.drive_path):
            raise FileNotFoundError(
                f"Google Drive não encontrado em: {self.drive_path}\n"
                "Por favor, instale o Google Drive for Desktop ou forneça o caminho manualmente."
            )
        
        print(f"Google Drive encontrado em: {self.drive_path}")
    
    def _detectar_caminho_drive(self) -> Optional[str]:
        """Detecta automaticamente o caminho do Google Drive for Desktop"""
        usuario = os.getenv('USERNAME') or os.getenv('USER')
        
        # Google Drive File Stream geralmente cria uma unidade virtual (G:)
        caminhos_possiveis = [
            # Unidade virtual do Drive File Stream
            r"G:\My Drive",
            # Windows - Localizações comuns
            os.path.join(os.path.expanduser('~'), 'Google Drive'),
            os.path.join(os.path.expanduser('~'), 'GoogleDrive'),
            os.path.join(os.path.expanduser('~'), 'Meu Drive'),
            os.path.join('C:', 'Users', usuario, 'Google Drive'),
            os.path.join('C:', 'Users', usuario, 'GoogleDrive'),
            # Caminhos alternativos
            os.path.join(os.path.expanduser('~'), 'OneDrive', 'Google Drive'),
        ]
        
        # Verifica cada caminho possível
        for caminho in caminhos_possiveis:
            if os.path.exists(caminho):
                return caminho
        
        # Verifica se a unidade G: existe e tem "My Drive"
        if os.path.exists("G:\\"):
            my_drive = os.path.join("G:\\", "My Drive")
            if os.path.exists(my_drive):
                return my_drive
        
        # Tenta encontrar via registro do Windows ou busca em pastas comuns
        return None
    
    def listar_arquivos(self, pasta: str = "", recursivo: bool = False) -> List[dict]:
        """
        Lista arquivos e pastas no Google Drive.
        
        Args:
            pasta: Caminho relativo dentro do Google Drive (ex: "Documentos/Fotos")
            recursivo: Se True, lista recursivamente todas as subpastas
        
        Returns:
            Lista de dicionários com informações dos arquivos
        """
        caminho_completo = os.path.join(self.drive_path, pasta)
        
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError(f"Pasta não encontrada: {caminho_completo}")
        
        arquivos = []
        
        if recursivo:
            for root, dirs, files in os.walk(caminho_completo):
                for file in files:
                    caminho_arquivo = os.path.join(root, file)
                    caminho_relativo = os.path.relpath(caminho_arquivo, self.drive_path)
                    arquivos.append({
                        'nome': file,
                        'caminho_completo': caminho_arquivo,
                        'caminho_relativo': caminho_relativo,
                        'tamanho': os.path.getsize(caminho_arquivo),
                        'pasta': os.path.dirname(caminho_relativo)
                    })
        else:
            try:
                items = os.listdir(caminho_completo)
                for item in items:
                    caminho_item = os.path.join(caminho_completo, item)
                    if os.path.isfile(caminho_item):
                        arquivos.append({
                            'nome': item,
                            'caminho_completo': caminho_item,
                            'caminho_relativo': os.path.relpath(caminho_item, self.drive_path),
                            'tamanho': os.path.getsize(caminho_item),
                            'pasta': pasta
                        })
            except PermissionError:
                print(f"Sem permissão para acessar: {caminho_completo}")
        
        return arquivos
    
    def listar_pastas(self, pasta: str = "") -> List[str]:
        """
        Lista apenas as pastas dentro de um diretório.
        
        Args:
            pasta: Caminho relativo dentro do Google Drive
        
        Returns:
            Lista de nomes de pastas
        """
        caminho_completo = os.path.join(self.drive_path, pasta)
        
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError(f"Pasta não encontrada: {caminho_completo}")
        
        pastas = []
        try:
            items = os.listdir(caminho_completo)
            for item in items:
                caminho_item = os.path.join(caminho_completo, item)
                if os.path.isdir(caminho_item):
                    pastas.append(item)
        except PermissionError:
            print(f"Sem permissão para acessar: {caminho_completo}")
        
        return pastas
    
    def buscar_arquivo(self, nome_arquivo: str, pasta: str = "") -> List[dict]:
        """
        Busca arquivos por nome (busca parcial).
        
        Args:
            nome_arquivo: Nome ou parte do nome do arquivo
            pasta: Pasta onde iniciar a busca (busca recursiva)
        
        Returns:
            Lista de arquivos encontrados
        """
        caminho_completo = os.path.join(self.drive_path, pasta)
        resultados = []
        
        nome_arquivo_lower = nome_arquivo.lower()
        
        for root, dirs, files in os.walk(caminho_completo):
            for file in files:
                if nome_arquivo_lower in file.lower():
                    caminho_arquivo = os.path.join(root, file)
                    caminho_relativo = os.path.relpath(caminho_arquivo, self.drive_path)
                    resultados.append({
                        'nome': file,
                        'caminho_completo': caminho_arquivo,
                        'caminho_relativo': caminho_relativo,
                        'tamanho': os.path.getsize(caminho_arquivo),
                        'pasta': os.path.dirname(caminho_relativo)
                    })
        
        return resultados
    
    def baixar_arquivo(self, caminho_relativo: str, destino: str = "downloads") -> bool:
        """
        Copia um arquivo do Google Drive para uma pasta local.
        
        Args:
            caminho_relativo: Caminho relativo do arquivo no Google Drive
            destino: Pasta de destino para salvar o arquivo
        
        Returns:
            True se o download foi bem-sucedido
        """
        caminho_origem = os.path.join(self.drive_path, caminho_relativo)
        
        if not os.path.exists(caminho_origem):
            print(f"Arquivo não encontrado: {caminho_origem}")
            return False
        
        # Cria a pasta de destino se não existir
        os.makedirs(destino, exist_ok=True)
        
        # Nome do arquivo
        nome_arquivo = os.path.basename(caminho_origem)
        caminho_destino = os.path.join(destino, nome_arquivo)
        
        try:
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Arquivo copiado: {nome_arquivo}")
            print(f"  De: {caminho_origem}")
            print(f"  Para: {caminho_destino}")
            return True
        except Exception as e:
            print(f"Erro ao copiar arquivo: {e}")
            return False
    
    def baixar_pasta(self, caminho_relativo: str, destino: str = "downloads") -> bool:
        """
        Copia uma pasta completa do Google Drive para uma pasta local.
        
        Args:
            caminho_relativo: Caminho relativo da pasta no Google Drive
            destino: Pasta de destino para salvar
        
        Returns:
            True se o download foi bem-sucedido
        """
        caminho_origem = os.path.join(self.drive_path, caminho_relativo)
        
        if not os.path.exists(caminho_origem):
            print(f"Pasta não encontrada: {caminho_origem}")
            return False
        
        if not os.path.isdir(caminho_origem):
            print(f"O caminho não é uma pasta: {caminho_origem}")
            return False
        
        # Nome da pasta
        nome_pasta = os.path.basename(caminho_origem)
        caminho_destino = os.path.join(destino, nome_pasta)
        
        try:
            # Remove a pasta de destino se já existir
            if os.path.exists(caminho_destino):
                shutil.rmtree(caminho_destino)
            
            shutil.copytree(caminho_origem, caminho_destino)
            print(f"Pasta copiada: {nome_pasta}")
            print(f"  De: {caminho_origem}")
            print(f"  Para: {caminho_destino}")
            return True
        except Exception as e:
            print(f"Erro ao copiar pasta: {e}")
            return False
    
    def obter_info_arquivo(self, caminho_relativo: str) -> Optional[dict]:
        """
        Obtém informações detalhadas de um arquivo.
        
        Args:
            caminho_relativo: Caminho relativo do arquivo
        
        Returns:
            Dicionário com informações do arquivo ou None
        """
        caminho_completo = os.path.join(self.drive_path, caminho_relativo)
        
        if not os.path.exists(caminho_completo):
            return None
        
        stat = os.stat(caminho_completo)
        
        return {
            'nome': os.path.basename(caminho_completo),
            'caminho_completo': caminho_completo,
            'caminho_relativo': caminho_relativo,
            'tamanho': stat.st_size,
            'tamanho_mb': round(stat.st_size / (1024 * 1024), 2),
            'modificado': stat.st_mtime,
            'criado': stat.st_ctime,
            'é_pasta': os.path.isdir(caminho_completo)
        }
    
    def encontrar_arquivos_compactados(self, pasta: str = "", recursivo: bool = False) -> List[dict]:
        """
        Encontra todos os arquivos compactados em uma pasta.
        
        Args:
            pasta: Caminho relativo dentro do Google Drive
            recursivo: Se True, busca recursivamente em subpastas
        
        Returns:
            Lista de dicionários com informações dos arquivos compactados
        """
        extensoes_compactadas = ['.zip', '.rar', '.7z', '.tar', '.tar.gz', '.tar.bz2', '.gz', '.bz2']
        arquivos_compactados = []
        
        caminho_completo = os.path.join(self.drive_path, pasta)
        
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError(f"Pasta não encontrada: {caminho_completo}")
        
        if recursivo:
            for root, dirs, files in os.walk(caminho_completo):
                for file in files:
                    _, ext = os.path.splitext(file.lower())
                    if ext in extensoes_compactadas or any(file.lower().endswith(e) for e in ['.tar.gz', '.tar.bz2']):
                        caminho_arquivo = os.path.join(root, file)
                        caminho_relativo = os.path.relpath(caminho_arquivo, self.drive_path)
                        arquivos_compactados.append({
                            'nome': file,
                            'caminho_completo': caminho_arquivo,
                            'caminho_relativo': caminho_relativo,
                            'extensao': ext,
                            'tamanho': os.path.getsize(caminho_arquivo),
                            'pasta': os.path.dirname(caminho_relativo)
                        })
        else:
            try:
                items = os.listdir(caminho_completo)
                for item in items:
                    caminho_item = os.path.join(caminho_completo, item)
                    if os.path.isfile(caminho_item):
                        _, ext = os.path.splitext(item.lower())
                        if ext in extensoes_compactadas or any(item.lower().endswith(e) for e in ['.tar.gz', '.tar.bz2']):
                            caminho_relativo = os.path.relpath(caminho_item, self.drive_path)
                            arquivos_compactados.append({
                                'nome': item,
                                'caminho_completo': caminho_item,
                                'caminho_relativo': caminho_relativo,
                                'extensao': ext,
                                'tamanho': os.path.getsize(caminho_item),
                                'pasta': pasta
                            })
            except PermissionError:
                print(f"Sem permissão para acessar: {caminho_completo}")
        
        return arquivos_compactados
    
    def descomprimir_arquivo(self, caminho_relativo: str, pasta_destino: Optional[str] = None, remover_apos_extracao: bool = False) -> bool:
        """
        Descomprime um arquivo compactado no Google Drive.
        
        Args:
            caminho_relativo: Caminho relativo do arquivo compactado
            pasta_destino: Pasta de destino (None = mesma pasta do arquivo)
            remover_apos_extracao: Se True, remove o arquivo após extrair
        
        Returns:
            True se a descompressão foi bem-sucedida
        """
        caminho_arquivo = os.path.join(self.drive_path, caminho_relativo)
        
        if not os.path.exists(caminho_arquivo):
            print(f"Arquivo não encontrado: {caminho_arquivo}")
            return False
        
        # Define pasta de destino (mesma pasta do arquivo se não especificado)
        if pasta_destino is None:
            pasta_destino = os.path.dirname(caminho_arquivo)
        else:
            pasta_destino = os.path.join(self.drive_path, pasta_destino)
            os.makedirs(pasta_destino, exist_ok=True)
        
        nome_arquivo = os.path.basename(caminho_arquivo)
        _, ext = os.path.splitext(nome_arquivo.lower())
        
        try:
            # Extrai nome base sem extensão para criar pasta
            nome_base = os.path.splitext(nome_arquivo)[0]
            if nome_arquivo.lower().endswith('.tar.gz') or nome_arquivo.lower().endswith('.tar.bz2'):
                nome_base = nome_arquivo.rsplit('.', 2)[0]
            
            pasta_extracao = os.path.join(pasta_destino, nome_base)
            
            # Descomprime baseado na extensão
            if ext == '.zip':
                with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                    zip_ref.extractall(pasta_extracao)
                print(f"✓ Descomprimido: {nome_arquivo} → {pasta_extracao}")
            
            elif ext == '.tar' or nome_arquivo.lower().endswith('.tar.gz') or nome_arquivo.lower().endswith('.tar.bz2'):
                mode = 'r'
                if nome_arquivo.lower().endswith('.tar.gz'):
                    mode = 'r:gz'
                elif nome_arquivo.lower().endswith('.tar.bz2'):
                    mode = 'r:bz2'
                
                os.makedirs(pasta_extracao, exist_ok=True)
                with tarfile.open(caminho_arquivo, mode) as tar_ref:
                    tar_ref.extractall(pasta_extracao)
                print(f"✓ Descomprimido: {nome_arquivo} → {pasta_extracao}")
            
            elif ext == '.gz':
                arquivo_destino = os.path.join(pasta_destino, nome_base)
                with gzip.open(caminho_arquivo, 'rb') as f_in:
                    with open(arquivo_destino, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                print(f"✓ Descomprimido: {nome_arquivo} → {arquivo_destino}")
            
            elif ext == '.bz2':
                arquivo_destino = os.path.join(pasta_destino, nome_base)
                with bz2.open(caminho_arquivo, 'rb') as f_in:
                    with open(arquivo_destino, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                print(f"✓ Descomprimido: {nome_arquivo} → {arquivo_destino}")
            
            else:
                print(f"✗ Formato não suportado: {ext} (arquivo: {nome_arquivo})")
                print("  Formatos suportados: .zip, .tar, .tar.gz, .tar.bz2, .gz, .bz2")
                return False
            
            # Remove arquivo após extração se solicitado
            if remover_apos_extracao:
                os.remove(caminho_arquivo)
                print(f"  Arquivo removido: {nome_arquivo}")
            
            return True
            
        except Exception as e:
            print(f"✗ Erro ao descomprimir {nome_arquivo}: {e}")
            return False
    
    def descomprimir_varios_arquivos(self, pasta: str = "", recursivo: bool = False, remover_apos_extracao: bool = False, max_workers: int = 4) -> dict:
        """
        Descomprime vários arquivos compactados na mesma pasta simultaneamente.
        
        Args:
            pasta: Pasta onde buscar arquivos compactados
            recursivo: Se True, busca recursivamente em subpastas
            remover_apos_extracao: Se True, remove os arquivos após extrair
            max_workers: Número máximo de threads para descompressão paralela
        
        Returns:
            Dicionário com estatísticas: {'total': X, 'sucesso': Y, 'falha': Z}
        """
        print(f"\n🔍 Procurando arquivos compactados em: {pasta or 'raiz'}")
        arquivos = self.encontrar_arquivos_compactados(pasta, recursivo)
        
        if not arquivos:
            print("Nenhum arquivo compactado encontrado!")
            return {'total': 0, 'sucesso': 0, 'falha': 0}
        
        print(f"📦 Encontrados {len(arquivos)} arquivo(s) compactado(s):")
        for arquivo in arquivos:
            tamanho_mb = round(arquivo['tamanho'] / (1024 * 1024), 2)
            print(f"  - {arquivo['nome']} ({tamanho_mb} MB)")
        
        print(f"\n🚀 Iniciando descompressão de {len(arquivos)} arquivo(s)...")
        print(f"   Usando {max_workers} thread(s) paralelas\n")
        
        sucesso = 0
        falha = 0
        
        # Descomprime em paralelo
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.descomprimir_arquivo, arquivo['caminho_relativo'], None, remover_apos_extracao): arquivo 
                for arquivo in arquivos
            }
            
            for future in as_completed(futures):
                arquivo = futures[future]
                try:
                    resultado = future.result()
                    if resultado:
                        sucesso += 1
                    else:
                        falha += 1
                except Exception as e:
                    print(f"✗ Erro ao processar {arquivo['nome']}: {e}")
                    falha += 1
        
        print(f"\n{'='*60}")
        print(f"✅ Descompressão concluída!")
        print(f"   Total: {len(arquivos)}")
        print(f"   ✓ Sucesso: {sucesso}")
        print(f"   ✗ Falha: {falha}")
        print(f"{'='*60}\n")
        
        return {
            'total': len(arquivos),
            'sucesso': sucesso,
            'falha': falha
        }
    
    def organizar_pasta_flat(self, pasta: str) -> dict:
        """
        Organiza uma pasta do Google Drive extraindo ZIPs, movendo tudo para a raiz,
        renomeando duplicados e removendo pastas vazias.
        
        Processo:
        1. Extrai todos os arquivos .zip para suas respectivas pastas
        2. Move todos os arquivos de todas as subpastas para a pasta raiz
        3. Renomeia arquivos duplicados adicionando _1, _2, etc
        4. Remove todas as pastas vazias
        
        Args:
            pasta: Caminho relativo da pasta no Google Drive
        
        Returns:
            Dicionário com estatísticas do processo
        """
        caminho_pasta = os.path.join(self.drive_path, pasta)
        
        if not os.path.exists(caminho_pasta):
            raise FileNotFoundError(f"Pasta não encontrada: {caminho_pasta}")
        
        if not os.path.isdir(caminho_pasta):
            raise ValueError(f"O caminho não é uma pasta: {caminho_pasta}")
        
        print(f"\n{'='*70}")
        print(f"📁 ORGANIZANDO PASTA: {pasta}")
        print(f"{'='*70}\n")
        
        stats = {
            'zips_extraidos': 0,
            'arquivos_movidos': 0,
            'arquivos_renomeados': 0,
            'pastas_removidas': 0,
            'erros': []
        }
        
        # PASSO 1: Extrair todos os arquivos .zip
        print("📦 PASSO 1: Extraindo arquivos .zip...")
        print("-" * 70)
        zip_files = [f for f in os.listdir(caminho_pasta) if f.lower().endswith('.zip') and os.path.isfile(os.path.join(caminho_pasta, f))]
        
        for zip_file in zip_files:
            caminho_zip = os.path.join(caminho_pasta, zip_file)
            caminho_relativo = os.path.relpath(caminho_zip, self.drive_path)
            try:
                if self.descomprimir_arquivo(caminho_relativo, pasta_destino=None, remover_apos_extracao=False):
                    stats['zips_extraidos'] += 1
            except Exception as e:
                stats['erros'].append(f"Erro ao extrair {zip_file}: {e}")
        
        print(f"✓ Extraídos {stats['zips_extraidos']} arquivo(s) .zip\n")
        
        # PASSO 2: Mover todos os arquivos das subpastas para a raiz
        print("📂 PASSO 2: Movendo arquivos das subpastas para a raiz...")
        print("-" * 70)
        
        # Primeiro, coletar todos os arquivos das subpastas
        arquivos_para_mover = []
        
        def coletar_arquivos_subpastas(diretorio_atual: str, raiz: str):
            """Coleta todos os arquivos das subpastas"""
            try:
                items = os.listdir(diretorio_atual)
                
                for item in items:
                    caminho_item = os.path.join(diretorio_atual, item)
                    
                    if os.path.isfile(caminho_item):
                        # É um arquivo - adicionar à lista
                        caminho_relativo_origem = os.path.relpath(caminho_item, self.drive_path)
                        caminho_relativo_destino = os.path.relpath(os.path.join(raiz, item), self.drive_path)
                        arquivos_para_mover.append({
                            'origem': caminho_item,
                            'destino': os.path.join(raiz, item),
                            'nome': item,
                            'origem_relativo': caminho_relativo_origem,
                            'destino_relativo': caminho_relativo_destino
                        })
                    elif os.path.isdir(caminho_item):
                        # É uma pasta - processar recursivamente
                        coletar_arquivos_subpastas(caminho_item, raiz)
            except Exception as e:
                stats['erros'].append(f"Erro ao coletar arquivos de {diretorio_atual}: {e}")
        
        # Coleta todos os arquivos de subpastas
        items_raiz = os.listdir(caminho_pasta)
        for item in items_raiz:
            caminho_item = os.path.join(caminho_pasta, item)
            if os.path.isdir(caminho_item):
                coletar_arquivos_subpastas(caminho_item, caminho_pasta)
        
        # Lista de arquivos que já existem na raiz (para detectar duplicados)
        arquivos_existentes_raiz = set()
        for arquivo_raiz in os.listdir(caminho_pasta):
            caminho_arquivo_raiz = os.path.join(caminho_pasta, arquivo_raiz)
            if os.path.isfile(caminho_arquivo_raiz):
                arquivos_existentes_raiz.add(arquivo_raiz.lower())
        
        # Agora move todos os arquivos coletados
        contador_duplicados_temp = {}
        for arquivo_info in arquivos_para_mover:
            destino_final = arquivo_info['destino']
            nome_arquivo = arquivo_info['nome']
            
            # Se o arquivo já existe na raiz, renomeia temporariamente
            if os.path.exists(destino_final) or nome_arquivo.lower() in arquivos_existentes_raiz:
                nome_base, extensao = os.path.splitext(nome_arquivo)
                # Usa um contador temporário único
                if nome_arquivo.lower() not in contador_duplicados_temp:
                    contador_duplicados_temp[nome_arquivo.lower()] = 0
                contador_duplicados_temp[nome_arquivo.lower()] += 1
                num = contador_duplicados_temp[nome_arquivo.lower()]
                nome_temp = f"{nome_base}_temp_{num}{extensao}"
                destino_final = os.path.join(caminho_pasta, nome_temp)
            
            try:
                shutil.move(arquivo_info['origem'], destino_final)
                stats['arquivos_movidos'] += 1
                if destino_final != arquivo_info['destino']:
                    print(f"  → Movido (renomeado temporariamente): {arquivo_info['origem_relativo']}")
                else:
                    print(f"  → Movido: {arquivo_info['origem_relativo']}")
            except Exception as e:
                stats['erros'].append(f"Erro ao mover {arquivo_info['nome']}: {e}")
        
        print(f"✓ Movidos {stats['arquivos_movidos']} arquivo(s) para a raiz\n")
        
        # PASSO 3: Renomear arquivos duplicados
        print("🔄 PASSO 3: Renomeando arquivos duplicados...")
        print("-" * 70)
        
        # Primeiro, renomeia arquivos temporários (_temp_X) para seus nomes originais
        arquivos_raiz = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
        
        for arquivo in arquivos_raiz[:]:  # Cópia da lista para poder modificar durante iteração
            if '_temp_' in arquivo:
                # Remove o _temp_X do nome
                partes = arquivo.rsplit('_temp_', 1)
                if len(partes) == 2:
                    nome_base_temp = partes[0]
                    resto = partes[1]
                    # Pega a extensão do resto
                    if '.' in resto:
                        num_temp, extensao = resto.rsplit('.', 1)
                        nome_original = f"{nome_base_temp}.{extensao}"
                    else:
                        nome_original = nome_base_temp
                    
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                    novo_caminho = os.path.join(caminho_pasta, nome_original)
                    
                    # Se o nome original já existe, adiciona _temp novamente (será renomeado depois)
                    if os.path.exists(novo_caminho):
                        continue  # Mantém como _temp_ e será tratado depois
                    
                    try:
                        os.rename(caminho_arquivo, novo_caminho)
                    except Exception as e:
                        stats['erros'].append(f"Erro ao renomear temporário {arquivo}: {e}")
        
        # Agora agrupa arquivos por nome (case-insensitive)
        arquivos_raiz = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
        nomes_arquivos = {}
        
        for arquivo in arquivos_raiz:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            # Remove _temp_X do nome para agrupamento
            nome_para_agrupamento = arquivo
            if '_temp_' in arquivo:
                partes = arquivo.rsplit('_temp_', 1)
                if len(partes) == 2 and '.' in partes[1]:
                    nome_para_agrupamento = f"{partes[0]}.{partes[1].rsplit('.', 1)[1]}"
            
            nome_base, extensao = os.path.splitext(nome_para_agrupamento)
            chave = nome_para_agrupamento.lower()
            
            if chave not in nomes_arquivos:
                nomes_arquivos[chave] = []
            nomes_arquivos[chave].append({
                'caminho': caminho_arquivo,
                'nome_original': arquivo,
                'nome_base': nome_base,
                'extensao': extensao
            })
        
        # Renomeia duplicados
        for chave, arquivos_grupo in nomes_arquivos.items():
            if len(arquivos_grupo) > 1:
                # Há duplicados - mantém o primeiro, renomeia os outros
                primeiro = arquivos_grupo[0]
                
                # Se o primeiro tem _temp_, renomeia primeiro
                if '_temp_' in primeiro['nome_original']:
                    novo_nome_primeiro = f"{primeiro['nome_base']}{primeiro['extensao']}"
                    novo_caminho_primeiro = os.path.join(caminho_pasta, novo_nome_primeiro)
                    if not os.path.exists(novo_caminho_primeiro):
                        try:
                            os.rename(primeiro['caminho'], novo_caminho_primeiro)
                            primeiro['caminho'] = novo_caminho_primeiro
                            primeiro['nome_original'] = novo_nome_primeiro
                        except Exception as e:
                            stats['erros'].append(f"Erro ao renomear primeiro {primeiro['nome_original']}: {e}")
                
                # Renomeia os demais
                contador = 1
                for arquivo_info in arquivos_grupo[1:]:
                    novo_nome = f"{arquivo_info['nome_base']}_{contador}{arquivo_info['extensao']}"
                    novo_caminho = os.path.join(caminho_pasta, novo_nome)
                    
                    # Se o novo nome também existe, incrementa
                    while os.path.exists(novo_caminho):
                        contador += 1
                        novo_nome = f"{arquivo_info['nome_base']}_{contador}{arquivo_info['extensao']}"
                        novo_caminho = os.path.join(caminho_pasta, novo_nome)
                    
                    try:
                        os.rename(arquivo_info['caminho'], novo_caminho)
                        stats['arquivos_renomeados'] += 1
                        print(f"  ↻ Renomeado: {arquivo_info['nome_original']} → {novo_nome}")
                    except Exception as e:
                        stats['erros'].append(f"Erro ao renomear {arquivo_info['nome_original']}: {e}")
                    
                    contador += 1
        
        print(f"✓ Renomeados {stats['arquivos_renomeados']} arquivo(s) duplicado(s)\n")
        
        # PASSO 4: Remover pastas vazias
        print("🗑️  PASSO 4: Removendo pastas vazias...")
        print("-" * 70)
        
        def remover_pastas_vazias(diretorio: str) -> int:
            """Remove pastas vazias recursivamente"""
            removidas = 0
            
            if not os.path.isdir(diretorio):
                return removidas
            
            try:
                items = os.listdir(diretorio)
                
                # Primeiro, processa subpastas recursivamente
                for item in items:
                    caminho_item = os.path.join(diretorio, item)
                    if os.path.isdir(caminho_item):
                        removidas += remover_pastas_vazias(caminho_item)
                
                # Depois, verifica se a pasta atual está vazia
                items_restantes = os.listdir(diretorio)
                if not items_restantes:
                    try:
                        os.rmdir(diretorio)
                        removidas += 1
                        caminho_relativo = os.path.relpath(diretorio, self.drive_path)
                        print(f"  ✗ Removida pasta vazia: {caminho_relativo}")
                    except Exception as e:
                        stats['erros'].append(f"Erro ao remover pasta {diretorio}: {e}")
            
            except Exception as e:
                stats['erros'].append(f"Erro ao processar pasta {diretorio}: {e}")
            
            return removidas
        
        stats['pastas_removidas'] = remover_pastas_vazias(caminho_pasta)
        
        print(f"✓ Removidas {stats['pastas_removidas']} pasta(s) vazia(s)\n")
        
        # Resumo final
        print(f"{'='*70}")
        print(f"✅ PROCESSO CONCLUÍDO!")
        print(f"{'='*70}")
        print(f"📦 ZIPs extraídos: {stats['zips_extraidos']}")
        print(f"📂 Arquivos movidos: {stats['arquivos_movidos']}")
        print(f"🔄 Arquivos renomeados: {stats['arquivos_renomeados']}")
        print(f"🗑️  Pastas removidas: {stats['pastas_removidas']}")
        
        if stats['erros']:
            print(f"\n⚠️  ERROS ENCONTRADOS ({len(stats['erros'])}):")
            for erro in stats['erros']:
                print(f"  - {erro}")
        
        print(f"{'='*70}\n")
        
        return stats


def formatar_tamanho(bytes: int) -> str:
    """Formata o tamanho em bytes para formato legível"""
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unidade}"
        bytes /= 1024.0
    return f"{bytes:.2f} TB"


def main():
    """Função principal - exemplos de uso"""
    print("=== Google Drive for Desktop - Acesso Local ===\n")
    
    try:
        # Inicializa o gerenciador
        # Se o caminho padrão não funcionar, você pode especificar manualmente:
        # drive = GoogleDriveDesktop(r"G:\My Drive")
        drive = GoogleDriveDesktop()
        
        print("\n" + "="*50)
        print("EXEMPLOS DE USO:")
        print("="*50 + "\n")
        
        # Exemplo 1: Listar pastas na raiz
        print("1. Pastas na raiz do Google Drive:")
        pastas = drive.listar_pastas()
        for i, pasta in enumerate(pastas[:10], 1):  # Mostra apenas as 10 primeiras
            print(f"   {i}. {pasta}")
        if len(pastas) > 10:
            print(f"   ... e mais {len(pastas) - 10} pastas")
        
        print("\n" + "-"*50 + "\n")
        
        # Exemplo 2: Listar arquivos em uma pasta específica
        print("2. Arquivos na raiz do Google Drive:")
        arquivos = drive.listar_arquivos()
        for i, arquivo in enumerate(arquivos[:5], 1):  # Mostra apenas os 5 primeiros
            tamanho = formatar_tamanho(arquivo['tamanho'])
            print(f"   {i}. {arquivo['nome']} ({tamanho})")
        if len(arquivos) > 5:
            print(f"   ... e mais {len(arquivos) - 5} arquivos")
        
        print("\n" + "-"*50 + "\n")
        
        # Exemplo 3: Buscar arquivos
        print("3. Buscar arquivos (exemplo: 'pdf'):")
        # resultados = drive.buscar_arquivo("pdf")
        # for resultado in resultados[:5]:
        #     print(f"   - {resultado['caminho_relativo']}")
        
        print("\n" + "="*50)
        print("COMANDOS ÚTEIS:")
        print("="*50)
        print("""
# Listar arquivos em uma pasta específica:
arquivos = drive.listar_arquivos("Documentos/Fotos", recursivo=True)

# Buscar arquivo por nome:
resultados = drive.buscar_arquivo("relatorio")

# Baixar um arquivo específico:
drive.baixar_arquivo("Documentos/meu_arquivo.pdf", "downloads")

# Baixar uma pasta completa:
drive.baixar_pasta("Documentos/Fotos", "downloads")

# Obter informações de um arquivo:
info = drive.obter_info_arquivo("Documentos/meu_arquivo.pdf")
print(info)

# DESCOMPRIMIR ARQUIVOS:
# Encontrar arquivos compactados:
compactados = drive.encontrar_arquivos_compactados("Documentos", recursivo=True)

# Descomprimir um arquivo específico:
drive.descomprimir_arquivo("Documentos/arquivo.zip")

# Descomprimir VÁRIOS arquivos na mesma pasta simultaneamente:
drive.descomprimir_varios_arquivos("Documentos", recursivo=False, remover_apos_extracao=False)
        """)
        
    except FileNotFoundError as e:
        print(f"\nERRO: {e}\n")
        print("Para usar um caminho personalizado:")
        print("  drive = GoogleDriveDesktop(r'G:\\My Drive')")
    except Exception as e:
        print(f"\nErro: {e}")


if __name__ == "__main__":
    main()

