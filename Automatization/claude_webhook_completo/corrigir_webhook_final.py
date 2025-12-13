#!/usr/bin/env python3
"""
🔧 CORRETOR AUTOMÁTICO COM AUTENTICAÇÃO - VERSÃO LIMPA
Corrige o webhook usando API key do n8n
"""

import requests
import json
import sys

N8N_URL = "http://163.176.141.76:5678"

print()
print("=" * 60)
print("🔧 CORRETOR AUTOMÁTICO - Com Autenticação")
print("=" * 60)
print()

# Pedir API key do n8n
print("🔑 Cole a API Key do n8n que você criou:")
print("(A chave que apareceu quando você clicou 'Create an API Key')")
print()
N8N_API_KEY = input("API Key: ").strip()

if not N8N_API_KEY:
    print("❌ Você precisa fornecer a API key!")
    sys.exit(1)

print()
print("✅ API Key recebida!")
print()

# Headers com autenticação
headers = {
    "Content-Type": "application/json",
    "X-N8N-API-KEY": N8N_API_KEY
}

print("🔍 Buscando workflow existente...")

try:
    # Buscar workflows
    response = requests.get(
        f"{N8N_URL}/api/v1/workflows",
        headers=headers
    )
    
    if response.status_code == 401:
        print("❌ API Key inválida ou incorreta!")
        print()
        print("Verifique:")
        print("  1. Copiou a chave corretamente?")
        print("  2. A API está habilitada no n8n?")
        sys.exit(1)
    
    if response.status_code != 200:
        print(f"❌ Erro ao acessar API: {response.status_code}")
        print(f"   {response.text}")
        sys.exit(1)
    
    workflows = response.json().get('data', [])
    
    # Encontrar workflow do Claude
    claude_workflow = None
    for wf in workflows:
        if 'Claude' in wf.get('name', '') or 'claude' in wf.get('name', '').lower():
            claude_workflow = wf
            break
    
    if not claude_workflow:
        print("❌ Não encontrei workflow do Claude!")
        print()
        print("Workflows encontrados:")
        for wf in workflows:
            print(f"   - {wf.get('name', 'Sem nome')}")
        print()
        sys.exit(1)
    
    print(f"✅ Workflow encontrado: {claude_workflow['name']}")
    print(f"   ID: {claude_workflow['id']}")
    print()
    
    # Buscar detalhes completos
    wf_id = claude_workflow['id']
    response = requests.get(
        f"{N8N_URL}/api/v1/workflows/{wf_id}",
        headers=headers
    )
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
        print("   Reconfigurando...")
        
        # Atualizar nó existente
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
        
        # Encontrar nó HTTP Request
        http_node = None
        for node in nodes:
            if 'http' in node.get('type', '').lower() and 'request' in node.get('type', '').lower():
                http_node = node
                break
        
        if not http_node:
            print("❌ Não encontrei nó HTTP Request!")
            sys.exit(1)
        
        # Adicionar novo nó
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
        if http_node_name not in connections:
            connections[http_node_name] = {}
        
        connections[http_node_name]['main'] = [
            [
                {
                    "node": "Respond to Webhook",
                    "type": "main",
                    "index": 0
                }
            ]
        ]
    
    # Atualizar Webhook para usar lastNode
    for i, node in enumerate(nodes):
        if node.get('type') == 'n8n-nodes-base.webhook':
            if 'parameters' not in nodes[i]:
                nodes[i]['parameters'] = {}
            nodes[i]['parameters']['responseMode'] = 'lastNode'
    
    print()
    print("💾 Salvando workflow corrigido...")
    
    # Preparar payload limpo - remover propriedades read-only
    payload = {
        "name": workflow_full.get('name'),
        "nodes": nodes,
        "connections": connections,
        "settings": workflow_full.get('settings', {}),
        "tags": workflow_full.get('tags', [])
    }
    
    # Remover campos opcionais vazios
    if not payload['tags']:
        del payload['tags']
    
    # Ativar workflow separadamente (depois do update)
    activate_payload = {"active": True}
    
    response = requests.put(
        f"{N8N_URL}/api/v1/workflows/{wf_id}",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        print("✅ Workflow atualizado!")
        
        # Ativar workflow separadamente
        print("🟢 Ativando workflow...")
        activate_response = requests.patch(
            f"{N8N_URL}/api/v1/workflows/{wf_id}",
            json=activate_payload,
            headers=headers
        )
        
        if activate_response.status_code == 200:
            print("✅ Workflow ativado!")
        
        print("✅ Workflow corrigido e salvo!")
        print("🟢 Status: ATIVO")
        print()
        print("🎉 PRONTO! Agora vai retornar só texto!")
        print()
        print("🧪 Teste agora:")
        print(f"   {N8N_URL}/webhook/chat?pergunta=Olá Claude!")
        print()
        print("Ou rode:")
        print("   python testar_webhook.py")
        print()
    else:
        print(f"❌ Erro ao salvar: {response.status_code}")
        print(f"   {response.text}")
    
except requests.exceptions.ConnectionError:
    print("❌ Não consegui conectar ao n8n!")
    print(f"   URL: {N8N_URL}")
    print()
    print("Verifique:")
    print("   1. n8n está rodando?")
    print("   2. URL está correta?")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("=" * 60)
print()
