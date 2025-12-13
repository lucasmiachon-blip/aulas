"""
Script para descompactar arquivos ZIP em drives na nuvem
Suporta Google Drive e OneDrive
"""

import os
import zipfile
import io
from pathlib import Path

# Opção 1: Para arquivos locais sincronizados (OneDrive, Google Drive Desktop)
def unzip_local_sync(zip_path, extract_to=None):
    """
    Descompacta um arquivo ZIP em uma pasta local sincronizada com a nuvem
    
    Args:
        zip_path: Caminho completo para o arquivo ZIP
        extract_to: Pasta de destino (se None, usa a mesma pasta do ZIP)
    """
    zip_path = Path(zip_path)
    
    if not zip_path.exists():
        print(f"Erro: Arquivo {zip_path} não encontrado")
        return False
    
    if extract_to is None:
        extract_to = zip_path.parent / zip_path.stem
    else:
        extract_to = Path(extract_to)
    
    extract_to.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Descompactando {zip_path.name}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Lista arquivos no ZIP
            file_list = zip_ref.namelist()
            print(f"Total de arquivos: {len(file_list)}")
            
            # Extrai todos os arquivos
            for file in file_list:
                print(f"  Extraindo: {file}")
                zip_ref.extract(file, extract_to)
        
        print(f"\n✓ Descompactação concluída!")
        print(f"Arquivos extraídos em: {extract_to}")
        return True
        
    except zipfile.BadZipFile:
        print("Erro: Arquivo ZIP corrompido ou inválido")
        return False
    except Exception as e:
        print(f"Erro ao descompactar: {e}")
        return False


# Opção 2: Para Google Drive usando API
def unzip_google_drive(file_id, credentials_path='credentials.json'):
    """
    Descompacta arquivo ZIP diretamente no Google Drive usando API
    
    Requer instalação: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    
    Args:
        file_id: ID do arquivo ZIP no Google Drive
        credentials_path: Caminho para o arquivo de credenciais da API
    """
    try:
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import pickle
        
        SCOPES = ['https://www.googleapis.com/auth/drive']
        
        creds = None
        # Token salvo de autenticações anteriores
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        # Se não há credenciais válidas, faz login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        service = build('drive', 'v3', credentials=creds)
        
        # Download do arquivo ZIP
        print(f"Baixando arquivo ZIP (ID: {file_id})...")
        request = service.files().get_media(fileId=file_id)
        zip_data = io.BytesIO()
        downloader = MediaIoBaseDownload(zip_data, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%")
        
        # Descompacta o ZIP
        zip_data.seek(0)
        print("\nDescompactando arquivos...")
        
        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            # Pega a pasta pai do arquivo ZIP
            file_metadata = service.files().get(fileId=file_id, fields='parents,name').execute()
            parent_folder = file_metadata['parents'][0] if 'parents' in file_metadata else None
            zip_name = file_metadata['name']
            
            # Cria pasta para os arquivos extraídos
            folder_metadata = {
                'name': zip_name.replace('.zip', ''),
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_folder] if parent_folder else []
            }
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            folder_id = folder['id']
            print(f"Pasta criada: {folder_metadata['name']}")
            
            # Upload de cada arquivo descompactado
            for file_name in zip_ref.namelist():
                print(f"  Enviando: {file_name}")
                file_data = zip_ref.read(file_name)
                
                file_metadata = {
                    'name': os.path.basename(file_name),
                    'parents': [folder_id]
                }
                
                media = MediaFileUpload(
                    io.BytesIO(file_data),
                    mimetype='application/octet-stream',
                    resumable=True
                )
                
                service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()
        
        print("\n✓ Descompactação concluída no Google Drive!")
        return True
        
    except ImportError:
        print("Erro: Instale as bibliotecas necessárias:")
        print("pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False


# Opção 3: Para OneDrive/SharePoint
def unzip_onedrive(zip_path_in_onedrive, extract_to=None):
    """
    Descompacta arquivo em pasta sincronizada do OneDrive
    
    Args:
        zip_path_in_onedrive: Caminho completo para o ZIP no OneDrive local
        extract_to: Pasta de destino (se None, cria pasta com nome do ZIP)
    """
    # OneDrive sincroniza automaticamente, então usamos a função local
    return unzip_local_sync(zip_path_in_onedrive, extract_to)


if __name__ == "__main__":
    print("=" * 60)
    print("DESCOMPACTADOR DE ARQUIVOS EM DRIVE NA NUVEM")
    print("=" * 60)
    print("\nEscolha o método:")
    print("1 - Arquivo local sincronizado (OneDrive, Google Drive Desktop)")
    print("2 - Google Drive direto via API")
    print("3 - Sair")
    
    escolha = input("\nOpção: ").strip()
    
    if escolha == "1":
        zip_path = input("\nCaminho completo do arquivo ZIP: ").strip()
        extract_to = input("Pasta de destino (deixe vazio para mesma pasta): ").strip()
        
        if not extract_to:
            extract_to = None
        
        unzip_local_sync(zip_path, extract_to)
    
    elif escolha == "2":
        print("\nPara usar a API do Google Drive:")
        print("1. Ative a API em: https://console.cloud.google.com/")
        print("2. Baixe o arquivo credentials.json")
        print("3. Coloque-o na mesma pasta deste script")
        
        file_id = input("\nID do arquivo no Google Drive: ").strip()
        unzip_google_drive(file_id)
    
    elif escolha == "3":
        print("Encerrando...")
    else:
        print("Opção inválida!")
