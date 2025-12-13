# 🪟 GUIA PARA WINDOWS - PowerShell

## ✅ VOCÊ ESTÁ NO WINDOWS!

**Sem problemas! Funciona perfeitamente!** 🚀

---

## ⚡ MÉTODO 1 - Python (RECOMENDADO)

**Python funciona igual no Windows!**

### **No PowerShell:**

```powershell
python corrigir_webhook.py
```

**OU:**

```powershell
python3 corrigir_webhook.py
```

**Simples assim!** ✅

---

## ⚡ MÉTODO 2 - PowerShell Nativo

**Use os scripts .ps1 que criei!**

### **1. Permitir execução de scripts (primeira vez):**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

(Digite **S** para confirmar)

### **2. Corrigir o webhook:**

```powershell
.\corrigir_webhook.ps1
```

### **3. Testar:**

```powershell
.\testar_webhook.ps1
```

---

## 📋 COMANDOS COMPLETOS WINDOWS

### **Se ainda não criou o workflow:**

```powershell
# Edite a API key primeiro em setup_claude_webhook.py
python setup_claude_webhook.py
```

### **Corrigir para retornar só texto:**

```powershell
python corrigir_webhook.py
```

**OU:**

```powershell
.\corrigir_webhook.ps1
```

### **Testar:**

```powershell
python testar_webhook.py
```

**OU:**

```powershell
.\testar_webhook.ps1
```

**OU no navegador:**

```
http://163.176.141.76:5678/webhook/chat?pergunta=Olá
```

---

## 🐍 PYTHON NO WINDOWS

### **Verificar se tem Python:**

```powershell
python --version
```

### **Se não tiver Python:**

**Opção A - Microsoft Store:**
1. Abra Microsoft Store
2. Procure "Python"
3. Instale Python 3.12

**Opção B - Site oficial:**
1. Vá em: https://www.python.org/downloads/
2. Baixe Python 3.12
3. **IMPORTANTE:** Marque "Add Python to PATH"

### **Instalar dependências:**

```powershell
pip install requests
```

---

## 📁 ARQUIVOS PARA WINDOWS

```
✅ corrigir_webhook.py    ← Python (funciona em Windows!)
✅ corrigir_webhook.ps1   ← PowerShell nativo
✅ testar_webhook.ps1     ← PowerShell nativo
✅ setup_claude_webhook.py ← Python (funciona em Windows!)
```

---

## 🎯 PASSO A PASSO COMPLETO

### **1. Abra PowerShell**

Pesquise "PowerShell" no menu Iniciar

### **2. Navegue até a pasta dos arquivos**

```powershell
cd C:\caminho\para\os\arquivos
```

### **3. Rode o corretor**

```powershell
python corrigir_webhook.py
```

### **4. Teste**

```powershell
python testar_webhook.py
```

**OU abra no navegador:**
```
http://163.176.141.76:5678/webhook/chat?pergunta=Teste
```

---

## ✅ RESULTADO ESPERADO

**Antes (JSON):** ❌
```json
{"model":"claude-sonnet...","text":"Olá!"}
```

**Depois (Texto puro):** ✅
```
Olá! Como posso ajudá-lo?
```

---

## 🐛 PROBLEMAS COMUNS NO WINDOWS

### **"python não é reconhecido"**

**Solução:**
- Instale Python da Microsoft Store
- OU baixe em python.org
- OU use `python3` em vez de `python`

### **"A execução de scripts foi desabilitada"**

**Solução:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **"Não consegui conectar ao n8n"**

**Solução:**
- Verifique se n8n está rodando
- Tente: `http://localhost:5678` em vez do IP
- Verifique firewall do Windows

---

## 💡 DICA WINDOWS

**Use Python!** É mais simples e funciona igual no Windows:

```powershell
python corrigir_webhook.py
```

**Sem configuração extra!** ✅

---

## 🎉 RESUMO

| **Método** | **Comando** | **Requer** |
|------------|-------------|------------|
| Python | `python corrigir_webhook.py` | Python instalado |
| PowerShell | `.\corrigir_webhook.ps1` | Executar scripts habilitado |
| Navegador | Abrir URL | Nada! |

---

**Escolha o método mais fácil para você!** 🚀

**Todos funcionam no Windows!** 🪟✅
