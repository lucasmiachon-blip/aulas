# 🔧 CORRETOR AUTOMÁTICO - PowerShell
# Corrige o webhook para retornar só texto

$N8N_URL = "http://163.176.141.76:5678"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🔧 CORRETOR AUTOMÁTICO - Respond to Webhook" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "🔍 Buscando workflow existente..." -ForegroundColor Yellow

try {
    # Buscar workflows
    $response = Invoke-RestMethod -Uri "$N8N_URL/api/v1/workflows" -Method Get -ErrorAction Stop
    
    # Encontrar workflow do Claude
    $workflow = $response.data | Where-Object { $_.name -like "*Claude*" -and $_.name -like "*Webhook*" } | Select-Object -First 1
    
    if (-not $workflow) {
        Write-Host "❌ Não encontrei o workflow do Claude!" -ForegroundColor Red
        Write-Host ""
        Write-Host "Workflows encontrados:" -ForegroundColor Yellow
        foreach ($wf in $response.data) {
            Write-Host "   - $($wf.name)"
        }
        Write-Host ""
        Write-Host "💡 Rode primeiro: python setup_claude_webhook.py" -ForegroundColor Yellow
        exit 1
    }
    
    Write-Host "✅ Workflow encontrado: $($workflow.name)" -ForegroundColor Green
    Write-Host "   ID: $($workflow.id)"
    Write-Host ""
    
    # Buscar detalhes completos
    $workflowFull = Invoke-RestMethod -Uri "$N8N_URL/api/v1/workflows/$($workflow.id)" -Method Get
    $workflowData = $workflowFull.data
    
    Write-Host "📊 Nós atuais: $($workflowData.nodes.Count)" -ForegroundColor Cyan
    foreach ($node in $workflowData.nodes) {
        Write-Host "   - $($node.name) ($($node.type))"
    }
    Write-Host ""
    
    # Verificar se já tem Respond to Webhook
    $hasRespond = $workflowData.nodes | Where-Object { $_.name -like "*Respond*" }
    
    if ($hasRespond) {
        Write-Host "✅ Já tem nó Respond to Webhook!" -ForegroundColor Green
        Write-Host "   Reconfigurando para retornar só texto..." -ForegroundColor Yellow
        Write-Host ""
        
        # Atualizar nó existente
        for ($i = 0; $i -lt $workflowData.nodes.Count; $i++) {
            if ($workflowData.nodes[$i].name -like "*Respond*") {
                $workflowData.nodes[$i].parameters = @{
                    respondWith = "text"
                    responseBody = "={{ `$json.content[0].text }}"
                    options = @{
                        responseHeaders = @{
                            entries = @(
                                @{
                                    name = "Content-Type"
                                    value = "text/plain; charset=utf-8"
                                }
                            )
                        }
                    }
                }
            }
        }
    }
    else {
        Write-Host "🔧 Adicionando nó Respond to Webhook..." -ForegroundColor Yellow
        Write-Host ""
        
        # Encontrar nó HTTP Request
        $httpNode = $workflowData.nodes | Where-Object { $_.type -like "*httpRequest*" } | Select-Object -First 1
        
        if (-not $httpNode) {
            Write-Host "❌ Não encontrei o nó HTTP Request!" -ForegroundColor Red
            exit 1
        }
        
        # Adicionar novo nó
        $respondNode = @{
            parameters = @{
                respondWith = "text"
                responseBody = "={{ `$json.content[0].text }}"
                options = @{
                    responseHeaders = @{
                        entries = @(
                            @{
                                name = "Content-Type"
                                value = "text/plain; charset=utf-8"
                            }
                        )
                    }
                }
            }
            id = "respond-node-auto"
            name = "Respond to Webhook"
            type = "n8n-nodes-base.respondToWebhook"
            typeVersion = 1.1
            position = @(690, 300)
        }
        
        $workflowData.nodes += $respondNode
        
        # Conectar HTTP Request → Respond to Webhook
        if (-not $workflowData.connections) {
            $workflowData.connections = @{}
        }
        
        $workflowData.connections[$httpNode.name] = @{
            main = @(
                @(
                    @{
                        node = "Respond to Webhook"
                        type = "main"
                        index = 0
                    }
                )
            )
        }
    }
    
    # Atualizar Webhook para usar lastNode
    for ($i = 0; $i -lt $workflowData.nodes.Count; $i++) {
        if ($workflowData.nodes[$i].type -eq "n8n-nodes-base.webhook") {
            $workflowData.nodes[$i].parameters.responseMode = "lastNode"
        }
    }
    
    # Ativar workflow
    $workflowData.active = $true
    
    Write-Host "💾 Salvando workflow corrigido..." -ForegroundColor Yellow
    
    # Converter para JSON
    $jsonBody = $workflowData | ConvertTo-Json -Depth 10
    
    # Salvar
    $saveResponse = Invoke-RestMethod -Uri "$N8N_URL/api/v1/workflows/$($workflow.id)" -Method Patch -Body $jsonBody -ContentType "application/json"
    
    Write-Host "✅ Workflow corrigido e salvo!" -ForegroundColor Green
    Write-Host "🟢 Status: ATIVO" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎉 PRONTO! Agora vai retornar só texto!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🧪 Teste agora:" -ForegroundColor Cyan
    Write-Host "   $N8N_URL/webhook/chat?pergunta=Olá Claude!" -ForegroundColor White
    Write-Host ""
    Write-Host "Ou rode:" -ForegroundColor Yellow
    Write-Host "   .\testar_webhook.ps1" -ForegroundColor White
    Write-Host ""
}
catch {
    Write-Host "❌ Erro: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    
    if ($_.Exception.Message -like "*Unable to connect*") {
        Write-Host "Não consegui conectar ao n8n!" -ForegroundColor Yellow
        Write-Host "   URL: $N8N_URL"
        Write-Host ""
        Write-Host "Verifique:" -ForegroundColor Yellow
        Write-Host "   1. n8n está rodando?"
        Write-Host "   2. URL está correta?"
        Write-Host ""
    }
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
