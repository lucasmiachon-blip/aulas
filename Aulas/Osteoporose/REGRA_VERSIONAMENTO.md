# 🔄 REGRA DE VERSIONAMENTO - Viewer

## ✅ REGRA SIMPLES:

**SEMPRE que Auto fizer mudança no `viewer_v2_XX.html`:**

1. ✅ **Atualizar versão** (v2.35 → v2.36 → v2.37...)
2. ✅ **Atualizar em 3 lugares:**
   - Título: `<title>Osteoporose v2.XX - 64 slides</title>`
   - Header: `<h1>📊 Slides Osteoporose - v2.XX (64 slides)</h1>`
   - Comentário do slide: `<!-- SLIDE X - v2.XX - [descrição] -->`
3. ✅ **Atualizar CHANGELOG_VIEWER.md**
4. ✅ **Fazer commit** com mensagem descritiva

---

## 📝 EXEMPLO DE COMMIT:

```bash
git add viewer_v2_35.html CHANGELOG_VIEWER.md
git commit -m "fix(slide7): [descrição] - v2.36"
```

---

## 🎯 VERSÃO ATUAL: **v2.36**

**Próxima versão:** v2.37 (quando fizer nova mudança)

---

**Auto sempre seguirá esta regra automaticamente!** ✅
