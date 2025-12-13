# 🤖 AUTOMAÇÃO 100% AUTOMÁTICA - Claude Webhook

## 🎯 O ACORDO: TRABALHO MÍNIMO!

**Você faz:** 1 edição + 1 comando
**Eu faço:** Todo o resto! 🚀

---

## ⚡ OPÇÃO 1 - SUPER RÁPIDO (RECOMENDADO)

### **1. Baixe todos os arquivos** ⬇️

### **2. Edite 1 linha** ✏️

Abra: `setup_claude_webhook.py`

Encontre:
```python
CLAUDE_API_KEY = "COLOQUE_SUA_API_KEY_AQUI"
```

Mude para:
```python
CLAUDE_API_KEY = "sua-chave-real-do-claude"
```

Salve!

### **3. Rode 1 comando** 🚀

```bash
bash instalar_tudo.sh
```

### **PRONTO! ✅**

O script vai:
- ✅ Instalar dependências
- ✅ Criar workflow no n8n
- ✅ Configurar tudo
- ✅ Ativar automaticamente
- ✅ Mostrar URL de teste

---

## ⚡ OPÇÃO 2 - MANUAL (se Opção 1 falhar)

### **1. Edite a mesma linha**

### **2. Rode:**

**Python:**
```bash
pip3 install -r requirements.txt
python3 setup_claude_webhook.py
```

**OU Bash:**
```bash
bash setup_webhook.sh
```

---

## ⚡ OPÇÃO 3 - IMPORTAR (se API do n8n estiver desabilitada)

Se os scripts acima falharem, eles criam automaticamente:

📁 `workflow_pronto.json` ← JÁ COM SUA API KEY DENTRO!

Então você só:
1. Abre n8n
2. Clica nos 3 pontinhos
3. "Import from File"
4. Seleciona `workflow_pronto.json`

**AINDA É AUTOMÁTICO!** 🎉

---

## 📦 ARQUIVOS INCLUÍDOS

```
📁 Claude Webhook Automático/
├── 🚀 instalar_tudo.sh          ← RODE ESTE! (tudo automatico)
├── 🐍 setup_claude_webhook.py   ← Script Python (automático)
├── 🐚 setup_webhook.sh          ← Script Bash (automático)
├── 📋 workflow_claude_webhook.json ← Workflow JSON (backup)
├── 📝 requirements.txt          ← Dependências Python
├── 📖 INÍCIO_RÁPIDO.md          ← Guia super rápido
├── 📚 INSTRUÇÕES.md             ← Guia detalhado
└── 📄 README.md                 ← Este arquivo
```

---

## 🎯 RESUMO DO TRABALHO

| Você | Eu (Script) |
|------|-------------|
| Editar 1 linha | Criar workflow |
| Rodar 1 comando | Configurar nós |
| | Adicionar API key |
| | Conectar nós |
| | Ativar workflow |
| | Configurar webhook |
| | Testar configuração |
| **30 segundos** | **Todo o resto!** |

---

## 🌐 DEPOIS DE RODAR

**Teste:**
```
http://163.176.141.76:5678/webhook/chat?pergunta=Olá Claude!
```

**Exemplos:**
```
.../webhook/chat?pergunta=Qual a capital do Brasil?
.../webhook/chat?pergunta=Me conte uma piada
.../webhook/chat?pergunta=Explique inteligência artificial
```

---

## ✅ TRABALHO MÍNIMO CONFIRMADO!

```
┌──────────────────────────────────────┐
│ ✏️  Edições manuais: 1 linha         │
│ 🖱️  Cliques: 0 (ou 3 se importar)  │
│ ⌨️  Comandos: 1                      │
│ ⏱️  Tempo: 30 segundos               │
│ 🤖 Automação: 99% AUTOMÁTICA         │
└──────────────────────────────────────┘
```

---

## 💪 É ISSO! AUTOMAÇÃO DE VERDADE!

**Sem configurar manualmente no n8n!**
**Sem arrastar nós!**
**Sem conectar nada!**
**Tudo por código!**

---

## 🐛 TROUBLESHOOTING

**Erro "API não habilitada":**
→ O script cria `workflow_pronto.json` automaticamente!
→ Só importar no n8n (3 cliques)

**Erro "Python não encontrado":**
→ Use o script Bash: `bash setup_webhook.sh`

**Erro "requests module not found":**
→ Rode: `pip3 install -r requirements.txt`

---

## 📞 SUPORTE

Qualquer problema, me chama! 💬

Feito com ❤️ para AUTOMAÇÃO TOTAL!

**Lucas está mantendo o acordo! 🤝**
