#!/bin/bash
#
# 🧪 TESTAR WEBHOOK - Verifica se está funcionando
#

N8N_URL="http://163.176.141.76:5678"
WEBHOOK_PATH="/webhook/chat"

echo ""
echo "============================================================"
echo "🧪 TESTANDO WEBHOOK DO CLAUDE"
echo "============================================================"
echo ""

echo "🔍 Verificando se n8n está rodando..."

if curl -s --head "$N8N_URL" | head -n 1 | grep -q "200\|301\|302"; then
    echo "✅ n8n está online!"
else
    echo "❌ n8n não está respondendo em $N8N_URL"
    echo "   Verifique se o n8n está rodando!"
    exit 1
fi

echo ""
echo "🚀 Testando webhook..."
echo ""

PERGUNTA="Olá, você está funcionando?"
URL="$N8N_URL$WEBHOOK_PATH?pergunta=$(echo $PERGUNTA | sed 's/ /%20/g')"

echo "📡 URL: $URL"
echo ""

RESPONSE=$(curl -s -w "\n%{http_code}" "$URL" 2>&1)
HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | head -n-1)

if [ "$HTTP_CODE" == "200" ]; then
    echo "✅ SUCESSO! Webhook está funcionando!"
    echo ""
    echo "📨 Resposta do Claude:"
    echo "────────────────────────────────────────"
    echo "$BODY"
    echo "────────────────────────────────────────"
    echo ""
    echo "🎉 TUDO OK! Seu webhook está 100% funcional!"
    echo ""
    echo "🌐 Use assim:"
    echo "   $N8N_URL$WEBHOOK_PATH?pergunta=SUA_PERGUNTA"
    echo ""
else
    echo "⚠️  Webhook retornou código: $HTTP_CODE"
    echo ""
    echo "Resposta:"
    echo "$BODY"
    echo ""
    echo "Possíveis causas:"
    echo "  - Workflow não está ativo"
    echo "  - API Key do Claude incorreta"
    echo "  - Webhook não foi criado"
    echo ""
    echo "Verifique no n8n:"
    echo "  1. Workflow está ACTIVE (verde)?"
    echo "  2. API Key está correta?"
    echo "  3. Webhook está no path correto?"
    echo ""
fi

echo "============================================================"
echo ""
