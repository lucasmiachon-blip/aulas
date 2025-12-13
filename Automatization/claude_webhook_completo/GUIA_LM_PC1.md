# 🖥️ GUIA ESPECÍFICO - LM-PC1

## 💾 CONFIGURAÇÃO SALVA

```
Computador: LM-PC1
Caminho: C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization
OneDrive: ☁️ Sincronização ativa
Setup: 2 computadores total
```

---

## 📦 INSTALAÇÃO AUTOMÁTICA (RECOMENDADO)

### **1. Baixe o pacote completo:**

**[claude_webhook_completo.zip](computer:///mnt/user-data/outputs/claude_webhook_completo.zip)** ⬇️

### **2. Extraia em qualquer pasta temporária**

Por exemplo: `Downloads`

### **3. Abra PowerShell nessa pasta**

Shift + Botão direito → "Abrir janela do PowerShell aqui"

### **4. Rode o instalador:**

```powershell
python instalar_arquivos_lm_pc1.py
```

**PRONTO!** ✅

O script vai:
- ✅ Criar a pasta: `ClaudeWebhook`
- ✅ Copiar todos os arquivos para: `C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization\ClaudeWebhook`
- ✅ Sincronizar via OneDrive automaticamente
- ✅ Ficará acessível nos seus 2 computadores!

---

## 🚀 DEPOIS DA INSTALAÇÃO

### **Navegue até a pasta:**

```powershell
cd "C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization\ClaudeWebhook"
```

### **Se ainda não criou o workflow:**

```powershell
# Edite a API key primeiro em setup_claude_webhook.py
python setup_claude_webhook.py
```

### **Corrija o webhook (retornar só texto):**

```powershell
python corrigir_webhook.py
```

### **Teste:**

```powershell
python testar_webhook.py
```

---

## 📁 ESTRUTURA DE PASTAS

```
C:\Users\Dell\OneDrive\Documentos\
└── AssistantStack\
    └── MetaVida\
        └── Automatization\
            └── ClaudeWebhook\          ← Arquivos instalados aqui!
                ├── corrigir_webhook.py
                ├── testar_webhook.py
                ├── setup_claude_webhook.py
                ├── POWERSHELL.md
                └── ...todos os outros arquivos
```

---

## ☁️ SINCRONIZAÇÃO ONEDRIVE

**Vantagens:**
- ✅ Arquivos salvos na nuvem
- ✅ Backup automático
- ✅ Acessível nos 2 computadores
- ✅ Histórico de versões
- ✅ Sempre atualizado

**Quando você editar algo no LM-PC1:**
- OneDrive sincroniza automaticamente
- Fica disponível no outro computador
- Sem precisar copiar manualmente!

---

## 🎯 COMANDOS RÁPIDOS LM-PC1

### **Ir para a pasta:**

```powershell
cd "C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization\ClaudeWebhook"
```

### **Corrigir:**

```powershell
python corrigir_webhook.py
```

### **Testar:**

```powershell
python testar_webhook.py
```

---

## 📊 RESUMO DO PROCESSO

| **Passo** | **Ação** | **Tempo** |
|-----------|----------|-----------|
| 1 | Baixar ZIP | 10s |
| 2 | Extrair temporariamente | 5s |
| 3 | Rodar instalador Python | 5s |
| 4 | Navegar até pasta | 5s |
| 5 | Corrigir webhook | 10s |
| 6 | Testar | 5s |
| **TOTAL** | **40 segundos** | **40s** |

---

## ✅ CHECKLIST LM-PC1

```
□ Baixei claude_webhook_completo.zip
□ Extraí em Downloads (ou outra pasta temporária)
□ Rodei: python instalar_arquivos_lm_pc1.py
□ Arquivos foram copiados para OneDrive/Documentos/.../ClaudeWebhook
□ Naveguei até a pasta correta
□ Rodei: python corrigir_webhook.py
□ Rodei: python testar_webhook.py
□ Webhook funcionando! 🎉
```

---

## 💡 DICAS LM-PC1

**Criar atalho no PowerShell:**

```powershell
# Adicione ao seu perfil do PowerShell
function cdclaude { cd "C:\Users\Dell\OneDrive\Documentos\AssistantStack\MetaVida\Automatization\ClaudeWebhook" }
```

**Depois só digita:**
```powershell
cdclaude
```

---

## 🎉 PRONTO PARA O LM-PC1!

**Instalação otimizada para sua configuração!**

**OneDrive sincroniza tudo automaticamente!**

**Acessível nos 2 computadores!**

---

**Baixe o ZIP e rode o instalador!** 📦🚀
