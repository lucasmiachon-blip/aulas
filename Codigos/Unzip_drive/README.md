# Google Drive for Desktop - Acesso Local (Sem API)

Script Python para acessar e baixar arquivos do Google Drive for Desktop diretamente do sistema de arquivos, **sem necessidade de API**.

## Requisitos

- Python 3.6+
- Google Drive for Desktop instalado e sincronizado
- **Não precisa de credenciais ou API do Google**

## Instalação

Não são necessárias dependências externas! O script usa apenas bibliotecas padrão do Python.

```bash
# Apenas execute o script
python download_google_drive_desktop.py
```

## Como Funciona

Este script acessa os arquivos que já estão sincronizados localmente pelo Google Drive for Desktop. Ele detecta automaticamente onde o Google Drive está instalado no seu computador.

## Caminhos Detectados Automaticamente

O script detecta automaticamente o Google Drive nestes locais:

1. **Unidade virtual do Drive File Stream** (mais comum):
   - `G:\My Drive`
   - `G:\`

2. **Pastas do usuário**:
   - `C:\Users\[USUARIO]\Google Drive`
   - `C:\Users\[USUARIO]\GoogleDrive`
   - `C:\Users\[USUARIO]\Meu Drive`

Se não encontrar automaticamente, você pode especificar o caminho manualmente:

```python
drive = GoogleDriveDesktop(r"G:\My Drive")
```

## Como Usar

### 1. Listar pastas e arquivos

```python
from download_google_drive_desktop import GoogleDriveDesktop

drive = GoogleDriveDesktop()

# Listar pastas na raiz
pastas = drive.listar_pastas()
print(pastas)

# Listar arquivos em uma pasta específica
arquivos = drive.listar_arquivos("Documentos")

# Listar recursivamente (todas as subpastas)
arquivos = drive.listar_arquivos("Documentos", recursivo=True)
```

### 2. Buscar arquivos

```python
# Buscar arquivos por nome (busca parcial)
resultados = drive.buscar_arquivo("relatorio")
for resultado in resultados:
    print(resultado['caminho_relativo'])
```

### 3. Baixar arquivo

```python
# Baixar um arquivo específico
drive.baixar_arquivo("Documentos/meu_arquivo.pdf", "downloads")

# Os arquivos serão salvos na pasta "downloads"
```

### 4. Baixar pasta completa

```python
# Baixar uma pasta inteira
drive.baixar_pasta("Documentos/Fotos", "downloads")
```

### 5. Obter informações de arquivo

```python
info = drive.obter_info_arquivo("Documentos/meu_arquivo.pdf")
print(f"Nome: {info['nome']}")
print(f"Tamanho: {info['tamanho_mb']} MB")
print(f"Modificado: {info['modificado']}")
```

### 6. Descomprimir arquivos compactados 🆕

```python
# Encontrar arquivos compactados em uma pasta
compactados = drive.encontrar_arquivos_compactados("Documentos", recursivo=True)
for arquivo in compactados:
    print(f"{arquivo['nome']} ({arquivo['extensao']})")

# Descomprimir um arquivo específico
drive.descomprimir_arquivo("Documentos/arquivo.zip")

# Descomprimir VÁRIOS arquivos simultaneamente na mesma pasta
resultado = drive.descomprimir_varios_arquivos(
    pasta="Documentos",
    recursivo=False,              # Buscar em subpastas?
    remover_apos_extracao=False,  # Remover arquivos após extrair?
    max_workers=4                 # Threads paralelas
)

print(f"Descomprimidos: {resultado['sucesso']} de {resultado['total']}")
```

**Formatos suportados:**
- `.zip` - ZIP
- `.tar` - TAR
- `.tar.gz` / `.tgz` - TAR GZIP
- `.tar.bz2` - TAR BZIP2
- `.gz` - GZIP
- `.bz2` - BZIP2

## Exemplos Práticos

- Veja `exemplo_uso.py` para exemplos básicos
- Veja `exemplo_descomprimir.py` para exemplos de descompressão

## Vantagens

✅ **Sem API** - Não precisa de credenciais do Google  
✅ **Sem autenticação** - Acessa arquivos locais diretamente  
✅ **Rápido** - Acesso direto ao sistema de arquivos  
✅ **Simples** - Apenas bibliotecas padrão do Python  
✅ **Detecção automática** - Encontra o Google Drive automaticamente  
✅ **Descompressão paralela** - Descomprime vários arquivos simultaneamente  
✅ **Múltiplos formatos** - Suporta ZIP, TAR, GZIP, BZIP2 e variações  

## Notas

- Os arquivos precisam estar sincronizados localmente pelo Google Drive for Desktop
- Arquivos apenas online (não baixados) podem não estar acessíveis imediatamente
- Certifique-se de que o Google Drive for Desktop está rodando e sincronizado
- O Google Drive File Stream cria uma unidade virtual (geralmente `G:\`) com a pasta "My Drive"

