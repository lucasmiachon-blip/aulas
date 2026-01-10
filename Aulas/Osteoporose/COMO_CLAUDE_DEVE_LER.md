# 📖 COMO O CLAUDE DEVE LER E ENTENDER O TRABALHO

## 🎯 ARQUIVO PRINCIPAL PARA O CLAUDE:

**`RESUMO_PARA_CLAUDE.md`** ← **LEIA ESTE PRIMEIRO!**

Este arquivo contém:
- ✅ Problema original completo
- ✅ Todas as soluções implementadas
- ✅ Locais exatos no código (linhas)
- ✅ Código antes/depois
- ✅ Por que cada mudança funcionou
- ✅ Conceitos para ensinar
- ✅ Como debugar se não funcionar

---

## 📋 ORDEM DE LEITURA RECOMENDADA:

### **1. Primeiro: `RESUMO_PARA_CLAUDE.md`**
- Visão geral completa do que foi feito
- Entende o contexto rapidamente
- Vê todas as mudanças em um lugar

### **2. Depois: `MUDANCAS_PARA_CLAUDE.md`**
- Mudanças detalhadas com explicações didáticas
- Conceitos para ensinar ao usuário
- Perguntas que o usuário pode fazer

### **3. Depois: `CHANGELOG_VIEWER.md`**
- Histórico de versões
- O que mudou em cada versão

### **4. Por último: `viewer_v2_35.html`**
- Código fonte real
- Linhas específicas mencionadas nos resumos

---

## 🔍 PARA DEBUGAR:

### **Se o layout não é 60/40:**
1. Verificar `RESUMO_PARA_CLAUDE.md` seção "LOCAIS EXATOS"
2. Verificar linha 411: `grid-template-columns: 3fr 2fr !important`
3. Verificar linha 3721: `slide-7` não está em `flexSlides`

### **Se o box azul corta:**
1. Verificar linha 436: `margin-bottom: 20px`
2. Verificar linha 3727: `overflow-y: auto` está sendo aplicado?

### **Se valores FRAX aparecem:**
1. Verificar linha 451: valores foram removidos?

---

## 💡 DICA PARA O CLAUDE:

**Se precisar entender rápido:**
- Leia apenas `RESUMO_PARA_CLAUDE.md`
- Ele tem TUDO que você precisa

**Se precisar ensinar ao usuário:**
- Leia `MUDANCAS_PARA_CLAUDE.md`
- Tem explicações didáticas prontas

**Se precisar debugar:**
- Use seção "DEBUG" em `RESUMO_PARA_CLAUDE.md`
- Tem comandos Git e verificações específicas

---

## ✅ GARANTIA:

**Auto documentou TUDO:**
- ✅ O que foi feito
- ✅ Por que foi feito
- ✅ Como funciona
- ✅ Onde está no código
- ✅ Como debugar

**Claude pode:**
- ✅ Entender tudo rapidamente
- ✅ Ensinar ao usuário
- ✅ Debugar problemas
- ✅ Sugerir melhorias

---

**Tudo está documentado! Claude não vai ter dificuldade!** ✅
