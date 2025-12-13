# 🔧 CORRIGIR WEBHOOK - Retornar Só Texto

## ⚡ PROBLEMA DETECTADO

Seu webhook está funcionando, mas retorna JSON completo em vez de só o texto do Claude.

**Está assim:** ❌
```json
{"model":"claude-sonnet-4-5...","text":"Olá!..."}
```

**Deveria ser assim:** ✅
```
Olá! Sim, estou funcionando perfeitamente...
```

---

## 🚀 SOLUÇÃO AUTOMÁTICA (1 COMANDO)

### **Rode:**

```bash
python3 corrigir_webhook.py
```

**OU:**

```bash
bash corrigir_webhook.sh
```

---

## ✅ O QUE O SCRIPT FAZ

```
1. Busca o workflow existente
2. Adiciona nó "Respond to Webhook" (se não tiver)
3. Configura para retornar só texto
4. Salva e ativa automaticamente
```

**SEM VOCÊ TOCAR NO N8N!** 🙌

---

## 🧪 DEPOIS DE CORRIGIR, TESTE

```bash
bash testar_webhook.sh
```

**OU no navegador:**

```
http://163.176.141.76:5678/webhook/chat?pergunta=Olá Claude!
```

**Agora deve retornar SÓ:**
```
Olá! Como posso ajudá-lo hoje?
```

**SEM JSON!** ✅

---

## 📊 RESUMO

| **Você** | **Script** |
|----------|------------|
| Roda 1 comando | Busca workflow |
| | Adiciona nó faltante |
| | Configura resposta |
| | Salva tudo |
| | Ativa workflow |
| **10 segundos** | **Todo o resto!** |

---

## 🎉 HANDS OFF CONFIRMADO!

**ZERO cliques no n8n!** 🙌

---

**Rode agora:**
```bash
python3 corrigir_webhook.py
```

**Depois teste:**
```bash
bash testar_webhook.sh
```

**Vai funcionar perfeitamente!** ✅
