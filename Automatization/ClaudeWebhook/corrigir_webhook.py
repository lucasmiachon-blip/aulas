#!/usr/bin/env python3
"""
🔧 CORRETOR AUTOMÁTICO - Adiciona nó Respond to Webhook
Corrige o workflow para retornar só texto!

VOCÊ SÓ RODA: python3 corrigir_webhook.py
"""

import requests
import json
import sys

N8N_URL = "http://163.176.141.76:5678"

print()
print("=" * 60)
print("🔧 CORRETOR AUTOMÁTICO - Respond to Webhook")
print("=" * 60)
print()

print("🔍 Buscando workflow existente...")

try:
    # Buscar todos os workflows
    response = requests.get(f"{N8N_URL}/api/v1/workflows")
    
    if response.status_code != 200:
        print("❌ Não consegui acessar API do n8n!")
        print(f"   Status: {response.status_code}")
        print()
        print("💡 A API está habilitada?")
        print("   Veja: Settings → API → Enable")
        sys.exit(1)
    
    workflows = response.json().get('data', [])
    
    # Encontrar workflow do Claude
    claude_workflow = None
    for wf in workflows:
        if 'Claude' in wf.get('name', '') and 'Webhook' in wf.get('name', ''):
            claude_workflow = wf
            break
    
    if not claude_workflow:
        print("❌ Não encontrei o workflow do Claude!")
        print()
        print("Workflows encontrados:")
        for wf in workflows:
            print(f"   - {wf.get('name', 'Sem nome')}")
        print()
        print("💡 Rode primeiro: python3 setup_claude_webhook.py")
        sys.exit(1)
    
    print(f"✅ Workflow encontrado: {claude_workflow['name']}")
    print(f"   ID: {claude_workflow['id']}")
    print()
    
    # Buscar detalhes completos do workflow
    wf_id = claude_workflow['id']
    response = requests.get(f"{N8N_URL}/api/v1/workflows/{wf_id}")
    workflow_full = response.json().get('data', claude_workflow)
    
    nodes = workflow_full.get('nodes', [])
    connections = workflow_full.get('connections', {})
    
    print(f"📊 Nós atuais: {len(nodes)}")
    for node in nodes:
        print(f"   - {node.get('name')} ({node.get('type')})")
    print()
    
    # Verificar se já tem Respond to Webhook
    has_respond = any('respond' in node.get('name', '').lower() for node in nodes)
    
    if has_respond:
        print("✅ Já tem nó Respond to Webhook!")
        print("   Vou reconfigurar para retornar só texto...")
        print()
        
        # Atualizar o nó existente
        for i, node in enumerate(nodes):
            if 'respond' in node.get('name', '').lower():
                nodes[i]['parameters'] = {
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
                }
    else:
        print("🔧 Adicionando nó Respond to Webhook...")
        print()
        
        # Encontrar o nó HTTP Request
        http_node = None
        for node in nodes:
            if 'http' in node.get('type', '').lower():
                http_node = node
                break
        
        if not http_node:
            print("❌ Não encontrei o nó HTTP Request!")
            sys.exit(1)
        
        # Adicionar novo nó Respond to Webhook
        respond_node = {
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
            "id": "respond-node-auto",
            "name": "Respond to Webhook",
            "type": "n8n-nodes-base.respondToWebhook",
            "typeVersion": 1.1,
            "position": [690, 300]
        }
        
        nodes.append(respond_node)
        
        # Conectar HTTP Request → Respond to Webhook
        http_node_name = http_node.get('name')
        connections[http_node_name] = {
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
    
    # Atualizar Webhook para usar lastNode
    for i, node in enumerate(nodes):
        if node.get('type') == 'n8n-nodes-base.webhook':
            nodes[i]['parameters']['responseMode'] = 'lastNode'
    
    # Salvar workflow atualizado
    print("💾 Salvando workflow corrigido...")
    
    workflow_full['nodes'] = nodes
    workflow_full['connections'] = connections
    workflow_full['active'] = True
    
    response = requests.patch(
        f"{N8N_URL}/api/v1/workflows/{wf_id}",
        json=workflow_full,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        print("✅ Workflow corrigido e salvo!")
        print("🟢 Status: ATIVO")
        print()
        print("🎉 PRONTO! Agora vai retornar só texto!")
        print()
        print("🧪 Teste agora:")
        print(f"   {N8N_URL}/webhook/chat?pergunta=Olá Claude!")
        print()
        print("Ou rode:")
        print("   bash testar_webhook.sh")
        print()
    else:
        print(f"❌ Erro ao salvar: {response.status_code}")
        print(f"   {response.text}")
        print()
    
except requests.exceptions.ConnectionError:
    print("❌ Não consegui conectar ao n8n!")
    print(f"   URL: {N8N_URL}")
    print()
    print("Verifique:")
    print("   1. n8n está rodando?")
    print("   2. URL está correta?")
    print()
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
    import traceback
    traceback.print_exc()
    print()
    sys.exit(1)

print("=" * 60)
print()
