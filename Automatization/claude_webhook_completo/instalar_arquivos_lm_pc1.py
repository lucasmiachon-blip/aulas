#!/usr/bin/env python3
"""
📦 INSTALADOR AUTOMÁTICO - LM-PC1
Extrai e organiza todos os arquivos no caminho correto!

RODE NO POWERSHELL:
python instalar_arquivos_lm_pc1.py
"""

import os
import shutil
import zipfile
import sys
from pathlib import Path

# Configuração LM-PC1
CAMINHO_DESTINO = r"C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization"
NOME_PASTA = "ClaudeWebhook"

print()
print("=" * 70)
print("📦 INSTALADOR AUTOMÁTICO - Claude Webhook")
print("🖥️  Computador: LM-PC1")
print("=" * 70)
print()

# Caminho completo
caminho_completo = os.path.join(CAMINHO_DESTINO, NOME_PASTA)

print(f"📁 Destino: {caminho_completo}")
print()

# Criar pasta se não existir
try:
    os.makedirs(caminho_completo, exist_ok=True)
    print("✅ Pasta criada/verificada!")
except Exception as e:
    print(f"❌ Erro ao criar pasta: {e}")
    print()
    print("💡 Verifique se o caminho existe:")
    print(f"   {CAMINHO_DESTINO}")
    print()
    sys.exit(1)

print()
print("📋 Lista de arquivos a serem instalados:")
print()

# Lista de arquivos
arquivos = [
    # Scripts Python (principais)
    ("corrigir_webhook.py", "🔧 Corrige webhook para retornar só texto"),
    ("testar_webhook.py", "🧪 Testa se o webhook está funcionando"),
    ("setup_claude_webhook.py", "🚀 Cria workflow automaticamente"),
    
    # Scripts PowerShell
    ("corrigir_webhook.ps1", "🔧 Versão PowerShell do corretor"),
    ("testar_webhook.ps1", "🧪 Versão PowerShell do teste"),
    
    # Scripts Bash (para referência)
    ("corrigir_webhook.sh", "🐚 Versão Bash (Linux/Mac)"),
    ("testar_webhook.sh", "🐚 Versão Bash (Linux/Mac)"),
    ("setup_webhook.sh", "🐚 Versão Bash (Linux/Mac)"),
    ("instalar_tudo.sh", "🐚 Instalador Bash (Linux/Mac)"),
    
    # Documentação
    ("POWERSHELL.md", "📖 Guia para PowerShell (LEIA ESTE!)"),
    ("WINDOWS.md", "📖 Guia completo Windows"),
    ("LEIA_PRIMEIRO.md", "📖 Início rápido"),
    ("CORRIGIR.md", "📖 Como corrigir webhook"),
    ("INÍCIO_RÁPIDO.md", "📖 Guia super rápido"),
    ("INSTRUÇÕES.md", "📖 Instruções detalhadas"),
    ("README.md", "📖 Visão geral"),
    
    # Configuração
    ("workflow_claude_webhook.json", "⚙️ Workflow n8n (backup)"),
    ("requirements.txt", "📝 Dependências Python"),
]

# Diretório atual (onde está o script)
dir_atual = os.path.dirname(os.path.abspath(__file__))

# Verificar se tem arquivo ZIP
arquivo_zip = os.path.join(dir_atual, "claude_webhook_completo.zip")
tem_zip = os.path.exists(arquivo_zip)

if tem_zip:
    print("📦 Arquivo ZIP encontrado! Extraindo...")
    print()
    
    try:
        with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
            zip_ref.extractall(caminho_completo)
        
        print("✅ Todos os arquivos extraídos com sucesso!")
        print()
    except Exception as e:
        print(f"❌ Erro ao extrair ZIP: {e}")
        print()
        tem_zip = False

# Se não tem ZIP, copiar arquivos individuais
if not tem_zip:
    print("📄 Copiando arquivos individuais...")
    print()
    
    arquivos_copiados = 0
    arquivos_faltando = []
    
    for arquivo, descricao in arquivos:
        origem = os.path.join(dir_atual, arquivo)
        destino = os.path.join(caminho_completo, arquivo)
        
        if os.path.exists(origem):
            try:
                shutil.copy2(origem, destino)
                print(f"✅ {arquivo}")
                print(f"   {descricao}")
                arquivos_copiados += 1
            except Exception as e:
                print(f"❌ {arquivo}: {e}")
        else:
            arquivos_faltando.append(arquivo)
    
    print()
    
    if arquivos_faltando:
        print("⚠️  Arquivos não encontrados:")
        for arq in arquivos_faltando:
            print(f"   - {arq}")
        print()
        print("💡 Certifique-se de que todos os arquivos estão na mesma pasta que este script!")
        print()
    
    print(f"📊 Resumo: {arquivos_copiados} de {len(arquivos)} arquivos copiados")
    print()

# Criar arquivo de configuração
config_file = os.path.join(caminho_completo, "CONFIG_LM_PC1.txt")
with open(config_file, 'w', encoding='utf-8') as f:
    f.write("# Configuração LM-PC1\n")
    f.write(f"# Caminho: {caminho_completo}\n")
    f.write("# OneDrive: Sincronização ativa\n")
    f.write("# Computador: LM-PC1\n")
    f.write("\n")
    f.write("# Para usar:\n")
    f.write("# 1. python corrigir_webhook.py\n")
    f.write("# 2. python testar_webhook.py\n")

print("✅ Arquivo de configuração criado: CONFIG_LM_PC1.txt")
print()

print("=" * 70)
print("🎉 INSTALAÇÃO COMPLETA!")
print("=" * 70)
print()
print("📁 Arquivos instalados em:")
print(f"   {caminho_completo}")
print()
print("☁️  OneDrive vai sincronizar automaticamente!")
print()
print("🚀 Próximos passos:")
print()
print("1. Abra PowerShell")
print("2. Navegue até a pasta:")
print(f"   cd \"{caminho_completo}\"")
print()
print("3. Edite sua API key em setup_claude_webhook.py (se ainda não criou o workflow)")
print()
print("4. Corrija o webhook:")
print("   python corrigir_webhook.py")
print()
print("5. Teste:")
print("   python testar_webhook.py")
print()
print("📖 Leia também: POWERSHELL.md")
print()
print("=" * 70)
print()
