# 🔒 ENCODING PROTOCOL - CRITICAL FOR CLAUDE

## ⚠️ SEMPRE LER ESTE ARQUIVO ANTES DE CRIAR/EDITAR QUALQUER ARQUIVO

---

## REGRA ABSOLUTA:

**TODOS os arquivos do projeto DEVEM usar UTF-8 encoding.**

---

## CARACTERES PROBLEMÁTICOS (Português BR):

### Vogais acentuadas:
```
á à â ã ä
é è ê ë
í ì î ï
ó ò ô õ ö
ú ù û ü
```

### Cedilha:
```
ç Ç
```

### Til:
```
ã õ Ã Õ
```

### Outros:
```
" " (aspas curvadas)
— – (travessões)
… (reticências)
```

---

## QUANDO CRIAR ARQUIVO NOVO:

### ✅ CORRETO:
```bash
# Ao usar create_file
cat > arquivo.md << 'EOF'
# Conteúdo com acentuação
EOF

# OU explicitamente
echo "Conteúdo" | iconv -t UTF-8 > arquivo.md
```

### ❌ ERRADO:
```bash
# Nunca usar encoding padrão
echo "Conteúdo" > arquivo.md  # PODE DAR ERRADO!
```

---

## QUANDO EDITAR ARQUIVO EXISTENTE:

### ✅ SEMPRE verificar encoding primeiro:
```bash
file -i arquivo.md  # Ver encoding atual
```

### ✅ Se precisar converter:
```bash
iconv -f ISO-8859-1 -t UTF-8 arquivo.md > arquivo_utf8.md
mv arquivo_utf8.md arquivo.md
```

---

## HTML/CSS/JS ESPECÍFICOS:

### HTML - SEMPRE incluir meta tag:
```html
<meta charset="UTF-8">
<!-- OU -->
<meta charset="utf-8"/>
```

### CSS - Adicionar no topo:
```css
@charset "UTF-8";
```

### JavaScript - Salvar como UTF-8 sem BOM

---

## TESTE RÁPIDO:

**Antes de commitar qualquer arquivo, testar:**

```bash
# Se estes aparecerem corretamente, está OK:
grep -n "ç\|ã\|é\|á\|ó" arquivo.md

# Se aparecer algo como: "Ã§" "Ã£" = ENCODING ERRADO!
```

---

## PALAVRAS FREQUENTES NO PROJETO (teste visual):

```
- Diretriz → Se aparecer "Diretriz" está certo
- Função → Se aparecer "FunÃ§Ã£o" está ERRADO
- Ação → Se aparecer "AÃ§Ã£o" está ERRADO
- Decisão → Se aparecer "DecisÃ£o" está ERRADO
- Avaliação → Se aparecer "AvaliaÃ§Ã£o" está ERRADO
```

---

## CHECKLIST ANTES DE QUALQUER CREATE/EDIT:

- [ ] Verifiquei que vou usar UTF-8?
- [ ] Testei com `file -i` se for edição?
- [ ] HTML tem `<meta charset="UTF-8">`?
- [ ] CSS tem `@charset "UTF-8";` no topo?
- [ ] Testei caracteres especiais visualmente?

---

## SE USUÁRIO RECLAMAR DE ENCODING:

**PARE TUDO E:**

1. Verifique este arquivo
2. Rode o teste rápido acima
3. Converta para UTF-8 se necessário
4. Reenvie o arquivo corrigido
5. Peça desculpas e GARANTA que não vai repetir

---

## COMPROMISSO:

**EU, Claude, prometo:**
- ✅ Ler este arquivo ANTES de criar qualquer arquivo
- ✅ SEMPRE usar UTF-8 explicitamente
- ✅ SEMPRE testar encoding antes de entregar
- ✅ NUNCA mais entregar arquivo com encoding errado

**Assinado:** Claude v2.0.0  
**Data:** 2026-01-14

---

**ESTE ARQUIVO É SAGRADO. NÃO IGNORE.**
