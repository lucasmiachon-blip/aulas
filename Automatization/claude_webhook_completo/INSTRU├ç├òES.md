# 🚀 INSTRUÇÕES - Claude Chat via Webhook no n8n

## 📥 COMO IMPORTAR O WORKFLOW

### Método 1: Via Interface do n8n (Recomendado)

1. **Abra o n8n** no navegador: `http://163.176.141.76:5678`

2. **Clique no botão "+" no canto superior esquerdo** (criar novo workflow)

3. **Clique nos 3 pontinhos** no canto superior direito

4. **Procure por "Import"** ou **"Import from File"**

5. **Clique em "Select file"** ou arraste o arquivo `workflow_claude_webhook.json`

6. **Pronto! O workflow foi importado!**

---

### Método 2: Colar Diretamente

1. **Abra o n8n**

2. **Crie um novo workflow** (botão +)

3. **Pressione CTRL+A** (selecionar tudo) e **DELETE** (se houver algo)

4. **Clique nos 3 pontinhos** → **"Import from JSON"**

5. **Abra o arquivo `workflow_claude_webhook.json`** em um editor de texto

6. **Copie TODO o conteúdo**

7. **Cole no n8n**

8. **Clique em "Import"**

---

## 🔧 CONFIGURAR SUA API KEY

### **IMPORTANTE: Você precisa adicionar sua chave do Claude!**

1. **Clique no nó "HTTP Request - Claude API"** (o do meio)

2. **Procure por "headerParameters"** ou **"Headers"**

3. **Encontre o header "x-api-key"**

4. **Mude de:**
   ```
   COLOQUE_SUA_API_KEY_AQUI
   ```
   
   **Para:**
   ```
   sua-api-key-real-do-claude
   ```

5. **Clique fora para salvar**

---

## ✅ ATIVAR O WORKFLOW

1. **No canto superior direito, encontre o toggle "Inactive"**

2. **Clique para mudar para "Active"** (deve ficar verde)

3. **Clique no botão "Save"** (botão vermelho/laranja)

4. **Pronto! O workflow está ativo!**

---

## 🌐 TESTAR NO NAVEGADOR

### **URL de Teste:**

```
http://163.176.141.76:5678/webhook/chat?pergunta=Olá Claude, como você está?
```

### **Outros exemplos:**

```
http://163.176.141.76:5678/webhook/chat?pergunta=Qual a capital do Brasil?
http://163.176.141.76:5678/webhook/chat?pergunta=Me conte uma piada
http://163.176.141.76:5678/webhook/chat?pergunta=Explique o que é inteligência artificial
```

---

## 📊 ESTRUTURA DO WORKFLOW

```
┌─────────────┐      ┌──────────────────┐      ┌────────────────────┐
│   Webhook   │─────▶│  HTTP Request    │─────▶│ Respond to Webhook │
│             │      │  (Claude API)    │      │                    │
└─────────────┘      └──────────────────┘      └────────────────────┘
      ↓                       ↓                          ↓
Recebe pergunta       Chama Claude              Retorna resposta
   da URL              via API                   ao navegador
```

---

## ✨ COMO FUNCIONA

1. **Você acessa a URL** com `?pergunta=SUA_PERGUNTA`
2. **Webhook recebe** a pergunta
3. **HTTP Request envia** para API do Claude
4. **Claude processa** e responde
5. **Respond to Webhook retorna** a resposta para seu navegador
6. **Você vê a resposta** diretamente na tela!

---

## 🔍 VERIFICAR SE ESTÁ FUNCIONANDO

### No n8n:

1. **Vá para a aba "Executions"** (ao lado de "Editor")
2. **Teste a URL no navegador**
3. **Volte para "Executions"**
4. **Deve aparecer uma execução com ✅ verde**
5. **Clique nela para ver os detalhes**

### Se der erro:

- ❌ **Vermelha = Erro** (clique para ver qual nó falhou)
- ⚠️ **Amarela = Aviso** (funciona, mas tem sugestões)
- ✅ **Verde = Sucesso!**

---

## 🐛 TROUBLESHOOTING (SOLUÇÃO DE PROBLEMAS)

### **Problema 1: "Página não carrega" ou "Conexão recusada"**
**Solução:** 
- Certifique que o workflow está **Active** (verde)
- Verifique se o n8n está rodando
- Use o IP correto: `163.176.141.76` (não use `localhost`)

---

### **Problema 2: "Erro 401" ou "Authentication failed"**
**Solução:**
- Sua API key está errada
- Verifique se copiou corretamente
- Gere uma nova key em: https://console.anthropic.com

---

### **Problema 3: "Navegador fica carregando infinito"**
**Solução:**
- No nó Webhook, certifique que **"Respond"** está como **"Using 'Respond to Webhook' Node"**
- No último nó, adicione o header `Content-Type: text/plain`

---

### **Problema 4: "Nada acontece"**
**Solução:**
1. Vá em **"Executions"** no n8n
2. Veja se tem alguma execução
3. Se não tem = Webhook não está sendo chamado
4. Se tem vermelha = Clique para ver o erro

---

## 🎯 PRÓXIMOS PASSOS - AUTOMAÇÕES

### **Ideias de expansão:**

1. **Salvar conversas no Google Sheets**
2. **Enviar resposta por email**
3. **Integrar com Slack/Discord**
4. **Criar chatbot de WhatsApp**
5. **Analisar sentimento de textos**
6. **Resumir artigos automaticamente**

---

## 📞 SUPORTE

Se tiver problemas:
1. Verifique os logs em "Executions"
2. Teste cada nó individualmente
3. Confirme que a API key está correta
4. Certifique que está usando o IP correto (não localhost)

---

## ✅ CHECKLIST FINAL

- [ ] Workflow importado
- [ ] API key configurada
- [ ] Workflow ativado (Active = verde)
- [ ] Workflow salvo (Save)
- [ ] Testado no navegador
- [ ] Resposta apareceu
- [ ] Tudo funcionando! 🎉

---

**🎉 PARABÉNS! Agora você tem uma API do Claude funcionando via Webhook!**
