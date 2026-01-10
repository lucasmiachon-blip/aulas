# 📋 PROMPT PARA CLAUDE: Como Trabalhar com Git

## 🎯 CONTEXTO:

Auto (Cursor AI) já está fazendo commits locais no branch `main`.

**Se você (Claude) adicionar mudanças que conflitem com as do Auto, remova as mudanças do Auto e mantenha as suas.**

---

## 📍 ONDE AUTO ESTÁ TRABALHANDO:

- **Branch:** `main`
- **Local:** `C:\Users\lucas\OneDrive\LM\Documentos\Ignis_Animi\Aulas\Osteoporose`
- **Arquivo principal:** `viewer_v2_35.html` (versão v2.36)
- **Commits recentes:** Ver `git log --oneline -10`

---

## 🔄 SE HOUVER CONFLITOS:

**REGRA: Priorizar Claude sobre Auto**

```bash
# Remover mudanças do Auto e manter as suas
git checkout --theirs arquivo.html
git add arquivo.html
git commit -m "fix: [descrição] - removidas mudanças do Auto, priorizando Claude"
```

---

## 📚 ANTES DE FAZER MUDANÇAS:

1. Leia `RESUMO_PARA_CLAUDE.md` (entenda o que Auto fez)
2. Verifique `git log --oneline -10` (veja commits do Auto)
3. Se necessário, veja `git show HEAD` (veja últimas mudanças)

---

## ✅ RESUMO:

- Auto commitando em `main`
- Se conflitar: **remova do Auto, mantenha suas**
- Prioridade: **Claude > Auto**
- Documente no commit quando priorizar suas mudanças

---

**Leia também:** `CLAUDE_COMO_TRABALHAR_GIT.md` (documentação completa)
