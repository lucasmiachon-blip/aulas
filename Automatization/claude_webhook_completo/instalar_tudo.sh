#!/bin/bash
#
# 🚀 INSTALADOR AUTOMÁTICO COMPLETO
# Instala dependências e configura tudo!
#

echo ""
echo "============================================================"
echo "🚀 INSTALADOR AUTOMÁTICO - Claude Webhook"
echo "============================================================"
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado!"
    echo "   Instale com: sudo apt install python3"
    exit 1
fi

echo "✅ Python3 encontrado!"
echo ""

# Instalar pip se não estiver instalado
if ! command -v pip3 &> /dev/null; then
    echo "📦 Instalando pip..."
    sudo apt install -y python3-pip
fi

echo "✅ pip encontrado!"
echo ""

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install -r requirements.txt --quiet

echo "✅ Dependências instaladas!"
echo ""

# Verificar se API key foi configurada
if grep -q "COLOQUE_SUA_API_KEY_AQUI" setup_claude_webhook.py; then
    echo "⚠️  ATENÇÃO: Você precisa configurar sua API Key!"
    echo ""
    echo "Por favor:"
    echo "1. Abra o arquivo: setup_claude_webhook.py"
    echo "2. Encontre: CLAUDE_API_KEY = \"COLOQUE_SUA_API_KEY_AQUI\""
    echo "3. Mude para: CLAUDE_API_KEY = \"sua-chave-real\""
    echo "4. Salve o arquivo"
    echo "5. Rode novamente: bash instalar_tudo.sh"
    echo ""
    exit 1
fi

echo "✅ API Key configurada!"
echo ""

# Rodar o script de setup
echo "🚀 Criando workflow automaticamente..."
echo ""

python3 setup_claude_webhook.py

echo ""
echo "============================================================"
echo "✅ INSTALAÇÃO CONCLUÍDA!"
echo "============================================================"
echo ""
