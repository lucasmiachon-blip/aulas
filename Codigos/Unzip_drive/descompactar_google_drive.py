"""
Script para descompactar arquivos ZIP diretamente do Google Drive via API
Descompacta todos os ZIPs encontrados na pasta e subpastas
"""

import io
import os
import zipfile
import pickle
from pathlib import Path

# Verificar se as bibliotecas estão instaladas
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
except ImportError:
    print("❌ Erro: Bibliotecas do Google não instaladas!")
    print("\n📦 Execute este comando para instalar:")
    print("pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    exit(1)

# Configurações
SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_ID = '18hZz5gb-897PFIjpcOZeiA4laIFdp6yL'  # ID da sua pasta


def autenticar_google_drive():
    """Autentica com o Google Drive e retorna o serviço"""
    creds = None
    
    # Token salvo de autenticações anteriores
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Se não há credenciais válidas, faz login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Atualizando credenciais...")
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("\n❌ Arquivo 'credentials.json' não encontrado!")
                print("\n📋 Para obter as credenciais:")
                print("1. Acesse: https://console.cloud.google.com/")
                print("2. Crie um novo projeto ou selecione um existente")
                print("3. Ative a API do Google Drive")
                print("4. Crie credenciais OAuth 2.0 (tipo 'Desktop app')")
                print("5. Baixe o arquivo JSON e salve como 'credentials.json' nesta pasta")
                print(f"   Pasta atual: {Path.cwd()}")
                return None
            
            print("🔐 Fazendo autenticação...")
            print("   Uma janela do navegador será aberta para você autorizar o acesso")
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para próximas execuções
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        print("✅ Autenticação concluída!")
    
    return build('drive', 'v3', credentials=creds)


def listar_arquivos_recursivo(service, folder_id, caminho=""):
    """Lista todos os arquivos em uma pasta e subpastas recursivamente"""
    arquivos_zip = []
    
    try:
        # Lista itens na pasta atual
        query = f"'{folder_id}' in parents and trashed=false"
        results = service.files().list(
            q=query,
            fields="files(id, name, mimeType)",
            pageSize=1000
        ).execute()
        
        items = results.get('files', [])
        
        for item in items:
            item_path = f"{caminho}/{item['name']}" if caminho else item['name']
            
            # Se é uma pasta, busca recursivamente
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                print(f"📁 Explorando: {item_path}")
                arquivos_zip.extend(listar_arquivos_recursivo(service, item['id'], item_path))
            
            # Se é um arquivo ZIP
            elif item['name'].lower().endswith('.zip'):
                arquivos_zip.append({
                    'id': item['id'],
                    'name': item['name'],
                    'path': item_path,
                    'parent_id': folder_id
                })
                print(f"  📦 ZIP encontrado: {item['name']}")
    
    except Exception as e:
        print(f"❌ Erro ao listar pasta: {e}")
    
    return arquivos_zip


def descompactar_zip_no_drive(service, zip_info):
    """Descompacta um arquivo ZIP e faz upload dos arquivos para o Google Drive"""
    try:
        print(f"\n{'='*60}")
        print(f"📦 Processando: {zip_info['name']}")
        print(f"📁 Localização: {zip_info['path']}")
        print(f"{'='*60}")
        
        # 1. Download do arquivo ZIP
        print("⬇️  Baixando arquivo ZIP...")
        request = service.files().get_media(fileId=zip_info['id'])
        zip_data = io.BytesIO()
        downloader = MediaIoBaseDownload(zip_data, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            if status:
                print(f"   Download: {int(status.progress() * 100)}%", end='\r')
        print("\n✅ Download concluído!")
        
        # 2. Criar pasta para os arquivos extraídos (mesmo local do ZIP)
        folder_name = zip_info['name'].replace('.zip', '').replace('.ZIP', '')
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [zip_info['parent_id']]
        }
        
        print(f"📂 Criando pasta: {folder_name}")
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder['id']
        
        # 3. Descompactar e fazer upload dos arquivos
        zip_data.seek(0)
        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            print(f"📋 Total de arquivos no ZIP: {total_files}")
            print(f"{'─'*60}")
            
            for i, file_name in enumerate(file_list, 1):
                # Pula diretórios vazios
                if file_name.endswith('/'):
                    continue
                
                print(f"[{i}/{total_files}] ⬆️  Enviando: {file_name}")
                
                try:
                    # Extrai o arquivo
                    file_data = zip_ref.read(file_name)
                    
                    # Prepara para upload
                    file_metadata = {
                        'name': os.path.basename(file_name),
                        'parents': [folder_id]
                    }
                    
                    media = MediaFileUpload(
                        io.BytesIO(file_data),
                        mimetype='application/octet-stream',
                        resumable=True
                    )
                    
                    # Faz upload
                    service.files().create(
                        body=file_metadata,
                        media_body=media,
                        fields='id'
                    ).execute()
                    
                except Exception as e:
                    print(f"   ⚠️  Erro ao processar {file_name}: {e}")
        
        print(f"{'─'*60}")
        print(f"✅ ZIP descompactado com sucesso!")
        print(f"📂 Arquivos extraídos na pasta: {folder_name}")
        return True
        
    except zipfile.BadZipFile:
        print(f"❌ Erro: {zip_info['name']} não é um arquivo ZIP válido")
        return False
    except Exception as e:
        print(f"❌ Erro ao processar {zip_info['name']}: {e}")
        return False


def main():
    """Função principal"""
    print("=" * 60)
    print("  DESCOMPACTADOR GOOGLE DRIVE - PROCESSAMENTO EM LOTE")
    print("=" * 60)
    print(f"\n📧 Conta: lucasmiachon87@gmail.com")
    print(f"📁 Pasta ID: {FOLDER_ID}")
    
    # Autentica
    print("\n🔐 Autenticando com Google Drive...")
    service = autenticar_google_drive()
    
    if not service:
        return
    
    # Lista todos os ZIPs recursivamente
    print("\n🔍 Buscando arquivos ZIP em todas as subpastas...")
    print("=" * 60)
    
    arquivos_zip = listar_arquivos_recursivo(service, FOLDER_ID)
    
    print("\n" + "=" * 60)
    
    if not arquivos_zip:
        print("⚠️  Nenhum arquivo ZIP encontrado na pasta e subpastas")
        return
    
    # Mostra resumo
    print(f"\n📊 RESUMO:")
    print(f"   Total de arquivos ZIP encontrados: {len(arquivos_zip)}")
    print("\n📋 Lista de arquivos:")
    print("─" * 60)
    
    for i, zip_file in enumerate(arquivos_zip, 1):
        print(f"   {i}. {zip_file['path']}")
    
    print("─" * 60)
    
    # Confirmação
    resposta = input("\n▶ Descompactar todos esses arquivos no mesmo local? (S/N): ").strip().upper()
    
    if resposta != 'S':
        print("❌ Operação cancelada")
        return
    
    # Processa todos os ZIPs
    print("\n" + "=" * 60)
    print("🚀 INICIANDO PROCESSAMENTO EM LOTE")
    print("=" * 60)
    
    sucesso = 0
    falha = 0
    
    for i, zip_file in enumerate(arquivos_zip, 1):
        print(f"\n\n🔄 Processando arquivo {i} de {len(arquivos_zip)}")
        
        if descompactar_zip_no_drive(service, zip_file):
            sucesso += 1
        else:
            falha += 1
    
    # Resumo final
    print("\n\n" + "=" * 60)
    print("🏁 PROCESSAMENTO CONCLUÍDO")
    print("=" * 60)
    print(f"✅ Sucesso: {sucesso} arquivo(s)")
    print(f"❌ Falha: {falha} arquivo(s)")
    print(f"📊 Total processado: {len(arquivos_zip)} arquivo(s)")
    print("=" * 60)
    print("\n💡 Os arquivos foram descompactados no mesmo local dos ZIPs originais")


if __name__ == "__main__":
    main()
