"""
Exemplo prático: Descomprimir vários arquivos no Google Drive
"""
from download_google_drive_desktop import GoogleDriveDesktop

# Inicializar o Google Drive
drive = GoogleDriveDesktop()

# Exemplo 1: Descomprimir TODOS os arquivos compactados em uma pasta
print("="*60)
print("EXEMPLO 1: Descomprimir todos os arquivos em uma pasta")
print("="*60)

# Descomprimir todos os .zip, .rar, etc. na pasta "Documentos"
resultado = drive.descomprimir_varios_arquivos(
    pasta="Documentos",              # Pasta no Google Drive
    recursivo=False,                 # Não buscar em subpastas (True para buscar recursivamente)
    remover_apos_extracao=False,     # Não remover arquivos após extrair
    max_workers=4                    # Usar 4 threads paralelas
)

print(f"\nResultado: {resultado}")


# Exemplo 2: Encontrar arquivos compactados primeiro
print("\n" + "="*60)
print("EXEMPLO 2: Listar arquivos compactados antes de descomprimir")
print("="*60)

compactados = drive.encontrar_arquivos_compactados("Documentos", recursivo=True)
print(f"\nEncontrados {len(compactados)} arquivo(s) compactado(s):")
for arquivo in compactados:
    print(f"  - {arquivo['nome']} ({arquivo['extensao']}) - {arquivo['pasta']}")


# Exemplo 3: Descomprimir um arquivo específico
print("\n" + "="*60)
print("EXEMPLO 3: Descomprimir um arquivo específico")
print("="*60)

# Descomprimir um arquivo específico
drive.descomprimir_arquivo(
    caminho_relativo="Documentos/meu_arquivo.zip",
    pasta_destino=None,              # None = mesma pasta do arquivo
    remover_apos_extracao=False      # Não remover após extrair
)


# Exemplo 4: Descomprimir com remoção automática
print("\n" + "="*60)
print("EXEMPLO 4: Descomprimir e remover arquivos originais")
print("="*60)

# CUIDADO: Isso remove os arquivos originais após descomprimir!
# resultado = drive.descomprimir_varios_arquivos(
#     pasta="Documentos",
#     recursivo=False,
#     remover_apos_extracao=True,     # Remove arquivos após extrair
#     max_workers=4
# )


# Exemplo 5: Descomprimir recursivamente (em todas as subpastas)
print("\n" + "="*60)
print("EXEMPLO 5: Descomprimir recursivamente em todas as subpastas")
print("="*60)

# resultado = drive.descomprimir_varios_arquivos(
#     pasta="Documentos",
#     recursivo=True,                 # Buscar em todas as subpastas
#     remover_apos_extracao=False,
#     max_workers=4
# )

