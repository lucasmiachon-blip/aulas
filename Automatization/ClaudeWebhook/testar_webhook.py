#!/usr/bin/env python3
"""
🧪 TESTAR WEBHOOK - Python
Verifica se o webhook está funcionando
Funciona em Windows, Linux e Mac!
"""

import requests
import sys
from urllib.parse import quote

N8N_URL = "http://163.176.141.76:5678"
WEBHOOK_PATH = "/webhook/chat"

print()
print("=" * 60)
print("🧪 TESTANDO WEBHOOK DO CLAUDE")
print("=" * 60)
print()

print("🔍 Verificando se n8n está rodando...")

try:
    response = requests.head(N8N_URL, timeout=5)
    print("✅ n8n está online!")
except requests.exceptions.ConnectionError:
    print("❌ n8n não está respondendo!")
    print(f"   URL: {N8N_URL}")
    print()
    print("Verifique:")
    print("   1. n8n está rodando?")
    print("   2. URL está correta?")
    print()
    sys.exit(1)

print()
print("🚀 Testando webhook...")
print()

pergunta = "Olá, você está funcionando?"
pergunta_encoded = quote(pergunta)
url = f"{N8N_URL}{WEBHOOK_PATH}?pergunta={pergunta_encoded}"

print(f"📡 URL: {url}")
print()

try:
    response = requests.get(url, timeout=30)
    
    if response.status_code == 200:
        print("✅ SUCESSO! Webhook está funcionando!")
        print()
        print("📨 Resposta do Claude:")
        print("─" * 60)
        print(response.text)
        print("─" * 60)
        print()
        print("🎉 TUDO OK! Seu webhook está 100% funcional!")
        print()
        print("🌐 Use assim:")
        print(f"   {N8N_URL}{WEBHOOK_PATH}?pergunta=SUA_PERGUNTA")
        print()
        
        # Verificar se ainda está retornando JSON
        if response.text.startswith('{') and '"model"' in response.text:
            print("⚠️  AVISO: Ainda está retornando JSON!")
            print("   Execute: python corrigir_webhook.py")
            print()
    else:
        print(f"⚠️  Webhook retornou código: {response.status_code}")
        print()
        print("Resposta:")
        print(response.text)
        print()
        print("Possíveis causas:")
        print("  - Workflow não está ativo")
        print("  - API Key do Claude incorreta")
        print("  - Webhook não foi criado")
        print()
        
except requests.exceptions.Timeout:
    print("❌ Timeout! O webhook demorou muito para responder.")
    print()
    print("Possíveis causas:")
    print("  - Claude API está lenta")
    print("  - API Key incorreta")
    print("  - Workflow travado")
    print()
except requests.exceptions.RequestException as e:
    print(f"❌ Erro ao testar: {e}")
    print()

print("=" * 60)
print()
