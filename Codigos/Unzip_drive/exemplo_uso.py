"""
Exemplos práticos de como usar o GoogleDriveDesktop
"""
from download_google_drive_desktop import GoogleDriveDesktop, formatar_tamanho

# Inicializar (detecta automaticamente o caminho)
drive = GoogleDriveDesktop()

# Ou especificar manualmente:
# drive = GoogleDriveDesktop(r"G:\My Drive")

# 1. Listar todas as pastas
print("=== PASTAS DISPONÍVEIS ===")
pastas = drive.listar_pastas()
for pasta in pastas:
    print(f"- {pasta}")

# 2. Listar arquivos em uma pasta específica
print("\n=== ARQUIVOS EM 'Documentos' ===")
arquivos = drive.listar_arquivos("Documentos")
for arquivo in arquivos[:10]:  # Primeiros 10
    tamanho = formatar_tamanho(arquivo['tamanho'])
    print(f"- {arquivo['nome']} ({tamanho})")

# 3. Buscar arquivos
print("\n=== BUSCANDO ARQUIVOS COM 'relatorio' ===")
resultados = drive.buscar_arquivo("relatorio")
for resultado in resultados:
    print(f"- {resultado['caminho_relativo']}")

# 4. Baixar um arquivo específico
print("\n=== BAIXANDO ARQUIVO ===")
drive.baixar_arquivo("Documentos/meu_arquivo.pdf", "downloads")

# 5. Baixar uma pasta completa
print("\n=== BAIXANDO PASTA ===")
drive.baixar_pasta("Documentos/Fotos", "downloads")

# 6. Obter informações de um arquivo
print("\n=== INFORMAÇÕES DO ARQUIVO ===")
info = drive.obter_info_arquivo("Documentos/meu_arquivo.pdf")
if info:
    print(f"Nome: {info['nome']}")
    print(f"Tamanho: {info['tamanho_mb']} MB")
    print(f"Caminho: {info['caminho_relativo']}")

