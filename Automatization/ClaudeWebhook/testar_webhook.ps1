# 🧪 TESTAR WEBHOOK - PowerShell
# Verifica se o webhook está funcionando

$N8N_URL = "http://163.176.141.76:5678"
$WEBHOOK_PATH = "/webhook/chat"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🧪 TESTANDO WEBHOOK DO CLAUDE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "🔍 Verificando se n8n está rodando..." -ForegroundColor Yellow

try {
    $testResponse = Invoke-WebRequest -Uri $N8N_URL -Method Head -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ n8n está online!" -ForegroundColor Green
}
catch {
    Write-Host "❌ n8n não está respondendo em $N8N_URL" -ForegroundColor Red
    Write-Host "   Verifique se o n8n está rodando!" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "🚀 Testando webhook..." -ForegroundColor Yellow
Write-Host ""

$pergunta = "Olá, você está funcionando?"
$perguntaEncoded = [System.Web.HttpUtility]::UrlEncode($pergunta)
$url = "$N8N_URL$WEBHOOK_PATH?pergunta=$perguntaEncoded"

Write-Host "📡 URL: $url" -ForegroundColor Cyan
Write-Host ""

try {
    $response = Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing -TimeoutSec 30
    
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ SUCESSO! Webhook está funcionando!" -ForegroundColor Green
        Write-Host ""
        Write-Host "📨 Resposta do Claude:" -ForegroundColor Cyan
        Write-Host "────────────────────────────────────────" -ForegroundColor Gray
        Write-Host $response.Content -ForegroundColor White
        Write-Host "────────────────────────────────────────" -ForegroundColor Gray
        Write-Host ""
        Write-Host "🎉 TUDO OK! Seu webhook está 100% funcional!" -ForegroundColor Green
        Write-Host ""
        Write-Host "🌐 Use assim:" -ForegroundColor Cyan
        Write-Host "   $N8N_URL$WEBHOOK_PATH?pergunta=SUA_PERGUNTA" -ForegroundColor White
        Write-Host ""
    }
    else {
        Write-Host "⚠️  Webhook retornou código: $($response.StatusCode)" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Resposta:" -ForegroundColor Yellow
        Write-Host $response.Content
        Write-Host ""
    }
}
catch {
    Write-Host "❌ Erro ao testar webhook: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possíveis causas:" -ForegroundColor Yellow
    Write-Host "  - Workflow não está ativo"
    Write-Host "  - API Key do Claude incorreta"
    Write-Host "  - Webhook não foi criado"
    Write-Host ""
    Write-Host "Verifique no n8n:" -ForegroundColor Yellow
    Write-Host "  1. Workflow está ACTIVE (verde)?"
    Write-Host "  2. API Key está correta?"
    Write-Host "  3. Webhook está no path correto?"
    Write-Host ""
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
