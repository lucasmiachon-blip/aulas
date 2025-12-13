#!/usr/bin/env python3
"""
🤖 AUTOMAÇÃO TOTAL - Claude Webhook no n8n
Cria o workflow automaticamente via API!

VOCÊ SÓ PRECISA:
1. Colocar sua API key do Claude abaixo
2. Rodar: python3 setup_claude_webhook.py
3. PRONTO! Está funcionando!
"""

import requests
import json
import sys

# ====================================
# 🔧 CONFIGURAÇÃO - EDITE AQUI!
# ====================================

# Sua API Key do Claude (pegue em: https://console.anthropic.com)
CLAUDE_API_KEY = "COLOQUE_SUA_API_KEY_AQUI"

# URL do seu n8n
N8N_URL = "http://163.176.141.76:5678"

# ====================================
# 🚀 CÓDIGO AUTOMÁTICO - NÃO MEXA!
# ====================================

def criar_workflow():
    """Cria o workflow automaticamente via API do n8n"""
    
    print("🚀 Iniciando configuração automática...")
    print()
    
    # Verificar se API key foi configurada
    if CLAUDE_API_KEY == "COLOQUE_SUA_API_KEY_AQUI":
        print("❌ ERRO: Você precisa configurar sua API Key do Claude!")
        print()
        print("Abra o arquivo setup_claude_webhook.py e edite a linha:")
        print('CLAUDE_API_KEY = "sua-chave-aqui"')
        print()
        sys.exit(1)
    
    # Workflow completo
    workflow_data = {
        "name": "Claude Chat Webhook (Auto)",
        "nodes": [
            {
                "parameters": {
                    "httpMethod": "GET",
                    "path": "chat",
                    "responseMode": "lastNode",
                    "options": {}
                },
                "id": "webhook-node",
                "name": "Webhook",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1.1,
                "position": [250, 300],
                "webhookId": "claude-chat"
            },
            {
                "parameters": {
                    "method": "POST",
                    "url": "https://api.anthropic.com/v1/messages",
                    "authentication": "none",
                    "sendHeaders": True,
                    "headerParameters": {
                        "parameters": [
                            {
                                "name": "x-api-key",
                                "value": CLAUDE_API_KEY
                            },
                            {
                                "name": "anthropic-version",
                                "value": "2023-06-01"
                            },
                            {
                                "name": "content-type",
                                "value": "application/json"
                            }
                        ]
                    },
                    "sendBody": True,
                    "specifyBody": "json",
                    "jsonBody": json.dumps({
                        "model": "claude-sonnet-4-5-20250929",
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "role": "user",
                                "content": "={{ $json.query.pergunta }}"
                            }
                        ]
                    }),
                    "options": {}
                },
                "id": "http-node",
                "name": "HTTP Request Claude",
                "type": "n8n-nodes-base.httpRequest",
                "typeVersion": 4.2,
                "position": [470, 300]
            },
            {
                "parameters": {
                    "respondWith": "text",
                    "responseBody": "={{ $json.content[0].text }}",
                    "options": {
                        "responseHeaders": {
                            "entries": [
                                {
                                    "name": "Content-Type",
                                    "value": "text/plain; charset=utf-8"
                                }
                            ]
                        }
                    }
                },
                "id": "respond-node",
                "name": "Respond to Webhook",
                "type": "n8n-nodes-base.respondToWebhook",
                "typeVersion": 1.1,
                "position": [690, 300]
            }
        ],
        "connections": {
            "Webhook": {
                "main": [
                    [
                        {
                            "node": "HTTP Request Claude",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "HTTP Request Claude": {
                "main": [
                    [
                        {
                            "node": "Respond to Webhook",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        },
        "active": True,  # Ativa automaticamente!
        "settings": {
            "executionOrder": "v1"
        },
        "tags": []
    }
    
    print("📦 Criando workflow no n8n...")
    
    try:
        # Criar workflow via API
        response = requests.post(
            f"{N8N_URL}/api/v1/workflows",
            json=workflow_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200 or response.status_code == 201:
            result = response.json()
            workflow_id = result.get('id', 'unknown')
            
            print("✅ Workflow criado com sucesso!")
            print(f"📋 ID: {workflow_id}")
            print(f"🟢 Status: ATIVO")
            print()
            print("🎉 PRONTO! Seu webhook está funcionando!")
            print()
            print("🌐 Teste agora:")
            print(f"   {N8N_URL}/webhook/chat?pergunta=Olá Claude!")
            print()
            print("📝 Exemplos:")
            print(f"   {N8N_URL}/webhook/chat?pergunta=Qual a capital do Brasil?")
            print(f"   {N8N_URL}/webhook/chat?pergunta=Me conte uma piada")
            print()
            
        else:
            print(f"❌ Erro ao criar workflow: {response.status_code}")
            print(f"   {response.text}")
            print()
            print("💡 Possíveis causas:")
            print("   - n8n não está rodando")
            print("   - API do n8n não está habilitada")
            print("   - URL do n8n está incorreta")
            
    except requests.exceptions.ConnectionError:
        print("❌ Não consegui conectar ao n8n!")
        print()
        print("Verifique:")
        print(f"   1. n8n está rodando em {N8N_URL}?")
        print("   2. URL está correta?")
        print()
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        print()

if __name__ == "__main__":
    print()
    print("=" * 60)
    print("🤖 AUTOMAÇÃO TOTAL - Claude Webhook")
    print("=" * 60)
    print()
    
    criar_workflow()
