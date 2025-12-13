#!/bin/bash
#
# 🤖 AUTOMAÇÃO TOTAL - Claude Webhook no n8n
# Cria o workflow automaticamente!
#
# VOCÊ SÓ PRECISA:
# 1. Editar a linha CLAUDE_API_KEY abaixo
# 2. Rodar: bash setup_webhook.sh
# 3. PRONTO!
#

# ====================================
# 🔧 CONFIGURAÇÃO - EDITE AQUI!
# ====================================

# Sua API Key do Claude
CLAUDE_API_KEY="COLOQUE_SUA_API_KEY_AQUI"

# URL do n8n
N8N_URL="http://163.176.141.76:5678"

# ====================================
# 🚀 CÓDIGO AUTOMÁTICO
# ====================================

echo ""
echo "============================================================"
echo "🤖 AUTOMAÇÃO TOTAL - Claude Webhook"
echo "============================================================"
echo ""

# Verificar se configurou a API key
if [ "$CLAUDE_API_KEY" == "COLOQUE_SUA_API_KEY_AQUI" ]; then
    echo "❌ ERRO: Configure sua API Key do Claude!"
    echo ""
    echo "Edite o arquivo setup_webhook.sh e mude:"
    echo 'CLAUDE_API_KEY="sua-chave-aqui"'
    echo ""
    exit 1
fi

echo "📦 Criando workflow no n8n..."
echo ""

# JSON do workflow
WORKFLOW_JSON=$(cat <<EOF
{
  "name": "Claude Chat Webhook (Auto)",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "GET",
        "path": "chat",
        "responseMode": "lastNode"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300],
      "webhookId": "claude-chat",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.anthropic.com/v1/messages",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {"name": "x-api-key", "value": "$CLAUDE_API_KEY"},
            {"name": "anthropic-version", "value": "2023-06-01"},
            {"name": "content-type", "value": "application/json"}
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "{\"model\":\"claude-sonnet-4-5-20250929\",\"max_tokens\":1024,\"messages\":[{\"role\":\"user\",\"content\":\"={{ \\$json.query.pergunta }}\"}]}"
      },
      "name": "HTTP Request Claude",
      "type": "n8n-nodes-base.httpRequest",
      "position": [470, 300],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ \\$json.content[0].text }}",
        "options": {
          "responseHeaders": {
            "entries": [
              {"name": "Content-Type", "value": "text/plain; charset=utf-8"}
            ]
          }
        }
      },
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [690, 300],
      "typeVersion": 1.1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{"node": "HTTP Request Claude", "type": "main", "index": 0}]]
    },
    "HTTP Request Claude": {
      "main": [[{"node": "Respond to Webhook", "type": "main", "index": 0}]]
    }
  },
  "active": true,
  "settings": {"executionOrder": "v1"}
}
EOF
)

# Tentar criar via API
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$N8N_URL/api/v1/workflows" \
  -H "Content-Type: application/json" \
  -d "$WORKFLOW_JSON" 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | head -n-1)

if [ "$HTTP_CODE" == "200" ] || [ "$HTTP_CODE" == "201" ]; then
    echo "✅ Workflow criado com sucesso!"
    echo "🟢 Status: ATIVO"
    echo ""
    echo "🎉 PRONTO! Seu webhook está funcionando!"
    echo ""
    echo "🌐 Teste agora:"
    echo "   $N8N_URL/webhook/chat?pergunta=Olá Claude!"
    echo ""
    echo "📝 Mais exemplos:"
    echo "   $N8N_URL/webhook/chat?pergunta=Qual a capital do Brasil?"
    echo "   $N8N_URL/webhook/chat?pergunta=Me conte uma piada"
    echo ""
else
    echo "⚠️  API do n8n retornou: $HTTP_CODE"
    echo ""
    echo "Isso pode significar que a API não está habilitada."
    echo "Vou criar um arquivo JSON para você importar manualmente."
    echo ""
    
    # Salvar JSON para importação manual
    echo "$WORKFLOW_JSON" > workflow_pronto.json
    
    echo "✅ Arquivo criado: workflow_pronto.json"
    echo ""
    echo "📥 Para importar manualmente:"
    echo "   1. Abra n8n: $N8N_URL"
    echo "   2. Clique nos 3 pontinhos (canto superior direito)"
    echo "   3. 'Import from File'"
    echo "   4. Selecione: workflow_pronto.json"
    echo ""
fi

echo "============================================================"
echo ""
