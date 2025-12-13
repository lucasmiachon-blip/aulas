"""
Script para organizar a pasta ACP Meetings 2024:
- Extrai todos os .zip
- Move todos os arquivos para a raiz
- Renomeia duplicados
- Remove pastas vazias
"""
from download_google_drive_desktop import GoogleDriveDesktop

# Inicializar o Google Drive
drive = GoogleDriveDesktop()

# Caminho da pasta a ser organizada
pasta = "Palestras/ACP Meetings 2024"

print("🚀 Iniciando organização da pasta...")
print(f"📁 Pasta: {pasta}\n")

try:
    # Executa todo o processo
    resultado = drive.organizar_pasta_flat(pasta)
    
    print("\n✅ Processo concluído com sucesso!")
    
except FileNotFoundError as e:
    print(f"\n❌ ERRO: {e}")
    print("\nVerifique se a pasta existe no Google Drive.")
except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()

