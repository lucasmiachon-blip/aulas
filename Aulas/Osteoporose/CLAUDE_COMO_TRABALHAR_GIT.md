# 🔧 CLAUDE: Como Trabalhar com Git (Auto já está commitando)

## ⚠️ IMPORTANTE: Auto já está commitando!

**Auto (Cursor AI) já está fazendo commits locais no branch `main`.**

Se você (Claude) adicionar mudanças conflitantes, **remova as mudanças do Auto e mantenha as suas**.

---

## 📍 ONDE AUTO ESTÁ COMITANDO:

### **Branch:**
- `main` (branch principal)

### **Repositório:**
- **Local:** `C:\Users\lucas\OneDrive\LM\Documentos\Ignis_Animi\Aulas\Osteoporose`
- **Remote:** `origin/main` (mas pode não existir ainda)

### **Commits recentes do Auto:**
```
0781582 fix(slide8): corrigir simbolos indevidos e encoding UTF-8 - v2.36
9bb3123 docs: adicionar guia de como Claude deve ler a documentação - v2.36
8482472 docs: adicionar resumo completo para Claude entender trabalho no Slide 7 - v2.36
7722c20 fix(slide7): corrigir margem inferior box azul DXA + overflow auto
9cf3776 fix(slide7): ajustar margin-bottom box DXA
```

---

## 🔄 ESTRATÉGIA DE RESOLUÇÃO DE CONFLITOS:

### **REGRA: Priorizar Claude sobre Auto**

**Se você (Claude) adicionar mudanças que conflitam com as do Auto:**

1. ✅ **Remova as mudanças do Auto**
2. ✅ **Mantenha as suas mudanças**
3. ✅ **Commit com mensagem clara**

**Exemplo:**
```bash
# Se houver conflito em viewer_v2_35.html
git checkout --theirs viewer_v2_35.html  # Usa sua versão (Claude)
# ou
git checkout --ours viewer_v2_35.html    # Usa versão atual (Auto) - NÃO FAÇA ISSO

# Depois
git add viewer_v2_35.html
git commit -m "fix: [sua descrição] - removidas mudanças do Auto, priorizando Claude"
```

---

## 📂 ARQUIVOS QUE AUTO ESTÁ MODIFICANDO:

### **Arquivo principal:**
- `viewer_v2_35.html` - Viewer principal (64 slides)
- Versão atual: **v2.36**

### **Documentação criada pelo Auto:**
- `RESUMO_PARA_CLAUDE.md` - Resumo completo do trabalho do Auto
- `MUDANCAS_PARA_CLAUDE.md` - Mudanças detalhadas para ensino
- `WORKFLOW_AUTO_CLAUDE.md` - Workflow de colaboração
- `CHANGELOG_VIEWER.md` - Histórico de versões
- `REGRA_VERSIONAMENTO.md` - Regra de versionamento
- `COMO_CLAUDE_DEVE_LER.md` - Guia de leitura para Claude

---

## 🎯 COMO VOCÊ (CLAUDE) DEVE PROCEDER:

### **1. ANTES DE FAZER MUDANÇAS:**

```bash
# Verificar status atual
git status

# Ver últimos commits do Auto
git log --oneline -10

# Ver o que o Auto mudou
git diff HEAD~1 viewer_v2_35.html
```

### **2. SE PRECISAR VER O TRABALHO DO AUTO:**

**Leia estes arquivos primeiro:**
1. `RESUMO_PARA_CLAUDE.md` - Visão geral completa
2. `MUDANCAS_PARA_CLAUDE.md` - Mudanças detalhadas
3. `CHANGELOG_VIEWER.md` - Histórico de versões

### **3. SE HOUVER CONFLITOS:**

**Priorize suas mudanças sobre as do Auto:**

```bash
# Opção 1: Usar sua versão (Claude)
git checkout --theirs arquivo.html
git add arquivo.html
git commit -m "fix: [descrição] - priorizando mudanças do Claude"

# Opção 2: Resolver manualmente
# Edite o arquivo, remova mudanças do Auto, mantenha suas
git add arquivo.html
git commit -m "fix: [descrição] - resolvido conflito, priorizando Claude"
```

---

## 🚨 SE O AUTO ADICIONAR COISAS CONFLITANTES:

### **O que fazer:**

1. ✅ **Remova as mudanças do Auto**
2. ✅ **Mantenha as suas**
3. ✅ **Documente no commit que priorizou Claude**

**Template de commit:**
```
fix: [descrição da sua mudança] - v2.36
- Removidas mudanças conflitantes do Auto
- Priorizando mudanças do Claude
```

---

## 📝 EXEMPLO DE FLUXO:

### **Cenário: Você quer corrigir algo no Slide 8**

```bash
# 1. Verificar o que Auto fez
git log --oneline -5

# 2. Ver mudanças recentes do Auto
git show HEAD:viewer_v2_35.html | grep -A 20 "slide-8"

# 3. Fazer suas mudanças
# Editar viewer_v2_35.html

# 4. Se houver conflito com mudanças do Auto
git checkout --theirs viewer_v2_35.html  # Sua versão
# Ou editar manualmente removendo mudanças do Auto

# 5. Commit
git add viewer_v2_35.html
git commit -m "fix(slide8): [sua correção] - removidas mudanças conflitantes do Auto"
```

---

## ✅ CHECKLIST PARA CLAUDE:

Antes de fazer mudanças:

- [ ] Verificou `git status`?
- [ ] Leu `RESUMO_PARA_CLAUDE.md`?
- [ ] Verificou últimos commits do Auto?
- [ ] Entendeu o que Auto está fazendo?

Ao fazer mudanças:

- [ ] Se houver conflito, removeu mudanças do Auto?
- [ ] Manteve suas mudanças?
- [ ] Documentou no commit?

---

## 🎯 RESUMO RÁPIDO:

1. **Auto está commitando em `main`**
2. **Se você adicionar coisas conflitantes: remova as do Auto, mantenha as suas**
3. **Prioridade: Claude > Auto**
4. **Documente no commit quando priorizar suas mudanças**

---

## 💡 DICA IMPORTANTE:

**Se você não tiver certeza do que Auto fez:**

1. Leia `RESUMO_PARA_CLAUDE.md`
2. Veja commits recentes: `git log --oneline -10`
3. Veja mudanças: `git show HEAD`

**Depois, faça suas mudanças com confiança!**

---

**Última atualização:** Janeiro 2025
**Status:** Auto commitando em `main`, Claude pode priorizar suas mudanças
