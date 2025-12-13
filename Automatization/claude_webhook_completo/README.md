# 🤖 Claude Chat API via n8n Webhook

## 📦 O QUE ESTÁ INCLUÍDO

```
📁 Arquivos:
├── workflow_claude_webhook.json    ← Workflow completo do n8n
├── INSTRUÇÕES.md                   ← Guia passo a passo detalhado
└── README.md                       ← Este arquivo
```

---

## ⚡ INÍCIO RÁPIDO (3 PASSOS)

### **1. Importar o Workflow**

1. Abra n8n: `http://163.176.141.76:5678`
2. Clique nos **3 pontinhos** (canto superior direito)
3. **"Import from File"** → Selecione `workflow_claude_webhook.json`

---

### **2. Adicionar API Key**

1. Clique no nó **"HTTP Request - Claude API"**
2. Encontre o header **"x-api-key"**
3. Mude `COLOQUE_SUA_API_KEY_AQUI` para sua chave real

---

### **3. Ativar e Testar**

1. Toggle **"Inactive" → "Active"** (verde)
2. Clique em **"Save"**
3. Teste: `http://163.176.141.76:5678/webhook/chat?pergunta=Olá`

---

## 🎯 COMO USAR

### **Formato da URL:**

```
http://163.176.141.76:5678/webhook/chat?pergunta=SUA_PERGUNTA_AQUI
```

### **Exemplos:**

```bash
# Pergunta simples
http://163.176.141.76:5678/webhook/chat?pergunta=Qual a capital do Brasil?

# Pergunta com espaços (automático)
http://163.176.141.76:5678/webhook/chat?pergunta=Me conte uma piada sobre programadores

# Pergunta complexa
http://163.176.141.76:5678/webhook/chat?pergunta=Explique inteligência artificial em 3 linhas
```

---

## ✅ O QUE FAZ

```
Você acessa URL → Claude responde → Aparece no navegador
```

**Simples, rápido, automático!** 🚀

---

## 📚 ESTRUTURA DO WORKFLOW

```
┌─────────────┐      ┌──────────────────┐      ┌────────────────────┐
│   Webhook   │─────▶│  HTTP Request    │─────▶│ Respond to Webhook │
│   (GET)     │      │  (POST Claude)   │      │   (Retorna texto)  │
└─────────────┘      └──────────────────┘      └────────────────────┘
```

### **Nó 1 - Webhook**
- Recebe requisição GET
- Path: `/chat`
- Parâmetro: `?pergunta=...`

### **Nó 2 - HTTP Request**
- Chama API do Claude
- Envia pergunta
- Recebe resposta

### **Nó 3 - Respond to Webhook**
- Pega resposta do Claude
- Retorna como texto puro
- Fecha conexão

---

## 🔧 REQUISITOS

- ✅ n8n rodando
- ✅ API Key do Claude (https://console.anthropic.com)
- ✅ Acesso ao IP do servidor

---

## 🐛 PROBLEMAS COMUNS

| Problema | Solução |
|----------|---------|
| Página não carrega | Workflow está Active? |
| Erro 401 | API Key incorreta |
| Carregando infinito | Verificar configuração do Webhook |
| Nada acontece | Ver aba "Executions" |

**Para mais detalhes:** Leia `INSTRUÇÕES.md`

---

## 🎉 PRONTO!

Depois de importar e configurar:

**✅ API do Claude funcionando**
**✅ Via Webhook GET simples**
**✅ Resposta direta no navegador**
**✅ Sem código manual**
**✅ Totalmente automático!**

---

## 📞 PRÓXIMOS PASSOS

Quer expandir? Adicione:
- 📊 Google Sheets (salvar conversas)
- 📧 Email (enviar respostas)
- 💬 Slack/Discord (chatbot)
- 📱 WhatsApp (assistente)
- 🔄 Tradução automática
- 📝 Resumo de documentos

**O céu é o limite!** 🚀

---

**Criado com ❤️ para automação total no n8n!**
