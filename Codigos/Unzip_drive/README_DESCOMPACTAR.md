# 📦 Descompactador de Arquivos ZIP

Script Python para descompactar arquivos ZIP em drives na nuvem (OneDrive, Google Drive, etc.)

## 🚀 Como Usar

### Opção 1: Menu Interativo (Mais Fácil)

Apenas execute o script:

```powershell
python descompactar.py
```

O menu vai te guiar pelas opções!

### Opção 2: Linha de Comando

Descompactar um arquivo específico:

```powershell
python descompactar.py "caminho\para\arquivo.zip"
```

Descompactar para uma pasta específica:

```powershell
python descompactar.py "caminho\para\arquivo.zip" "caminho\destino"
```

### Opção 3: Usar no Seu Código

```python
from descompactar import descompactar_zip, descompactar_varios

# Descompactar um arquivo
descompactar_zip("C:\\Users\\lucas\\OneDrive\\meu_arquivo.zip")

# Descompactar para local específico
descompactar_zip("arquivo.zip", "C:\\destino")

# Descompactar todos os ZIPs de uma pasta
descompactar_varios("C:\\Users\\lucas\\OneDrive\\ZIPs")
```

## 📋 Exemplos Práticos

### Exemplo 1: Descompactar no OneDrive

```powershell
python descompactar.py "C:\Users\lucas\OneDrive\projeto.zip"
```

Cria automaticamente a pasta `C:\Users\lucas\OneDrive\projeto\` com os arquivos.

### Exemplo 2: Processar vários ZIPs

```python
from descompactar import descompactar_varios

# Descompacta todos os ZIPs na pasta Downloads do OneDrive
descompactar_varios(r"C:\Users\lucas\OneDrive\Downloads")
```

### Exemplo 3: Arrastar e Soltar

No Windows Explorer:
1. Arraste o arquivo ZIP
2. Solte em cima do arquivo `descompactar.py`
3. Pronto! ✅

## 💡 Dicas

- O script cria automaticamente uma pasta com o nome do arquivo ZIP
- Funciona com qualquer pasta sincronizada (OneDrive, Google Drive Desktop, Dropbox, etc.)
- Mostra progresso detalhado de cada arquivo extraído
- Tratamento de erros para arquivos corrompidos

## ⚠️ Requisitos

- Python 3.6 ou superior
- Biblioteca `zipfile` (já incluída no Python)

Nenhuma instalação adicional necessária! 🎉
