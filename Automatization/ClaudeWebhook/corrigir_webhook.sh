#!/bin/bash
#
# 🔧 CORRETOR AUTOMÁTICO (Bash)
# Adiciona nó Respond to Webhook
#

N8N_URL="http://163.176.141.76:5678"

echo ""
echo "============================================================"
echo "🔧 CORRETOR AUTOMÁTICO - Respond to Webhook"
echo "============================================================"
echo ""

echo "🔍 Buscando workflow existente..."

# Buscar workflows
WORKFLOWS=$(curl -s "$N8N_URL/api/v1/workflows" 2>&1)

if [ $? -ne 0 ]; then
    echo "❌ Não consegui conectar ao n8n!"
    echo "   URL: $N8N_URL"
    echo ""
    exit 1
fi

# Encontrar workflow do Claude (procura por ID ou nome)
WF_ID=$(echo "$WORKFLOWS" | grep -o '"id":"[^"]*"' | grep -B5 -A5 "Claude\|Webhook" | grep '"id"' | head -1 | cut -d'"' -f4)

if [ -z "$WF_ID" ]; then
    echo "❌ Não encontrei o workflow do Claude!"
    echo ""
    echo "💡 Rode primeiro: python3 setup_claude_webhook.py"
    echo ""
    exit 1
fi

echo "✅ Workflow encontrado!"
echo "   ID: $WF_ID"
echo ""

echo "📝 Criando workflow corrigido..."

# Criar workflow corrigido completo
WORKFLOW_CORRECTED=$(cat <<'EOF'
{
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
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.anthropic.com/v1/messages",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {"name": "x-api-key", "value": ""},
            {"name": "anthropic-version", "value": "2023-06-01"},
            {"name": "content-type", "value": "application/json"}
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "{\"model\":\"claude-sonnet-4-5-20250929\",\"max_tokens\":1024,\"messages\":[{\"role\":\"user\",\"content\":\"={{ $json.query.pergunta }}\"}]}"
      },
      "name": "HTTP Request Claude",
      "type": "n8n-nodes-base.httpRequest",
      "position": [470, 300],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $json.content[0].text }}",
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
  "active": true
}
EOF
)

echo "💾 Salvando workflow corrigido..."

RESPONSE=$(curl -s -w "\n%{http_code}" -X PATCH "$N8N_URL/api/v1/workflows/$WF_ID" \
  -H "Content-Type: application/json" \
  -d "$WORKFLOW_CORRECTED" 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)

if [ "$HTTP_CODE" == "200" ]; then
    echo "✅ Workflow corrigido e salvo!"
    echo "🟢 Status: ATIVO"
    echo ""
    echo "🎉 PRONTO! Agora vai retornar só texto!"
    echo ""
    echo "🧪 Teste agora:"
    echo "   $N8N_URL/webhook/chat?pergunta=Olá Claude!"
    echo ""
    echo "Ou rode:"
    echo "   bash testar_webhook.sh"
    echo ""
else
    echo "⚠️  Status: $HTTP_CODE"
    echo ""
    echo "Vou tentar via Python..."
    python3 corrigir_webhook.py
fi

echo "============================================================"
echo ""
