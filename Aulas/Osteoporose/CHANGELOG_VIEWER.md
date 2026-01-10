# 📋 CHANGELOG - Viewer Osteoporose

Histórico de versões e mudanças do arquivo `viewer_v2_XX.html`

---

## v2.36 (Janeiro 2025) - ✅ ATUAL

### Mudanças:
- ✅ **Slide 7:** Layout 60/40 funcionando (grid 3fr 2fr)
- ✅ **Slide 7:** JavaScript ajusta overflow-y: auto para não cortar conteúdo
- ✅ **Slide 7:** Box DXA com margin-bottom: 20px (não corta mais)
- ✅ **Slide 7:** Título simplificado para "Caso Clínico"
- ✅ **Slide 7:** Removida palavra "OSTEOPENIA" do box DXA
- ✅ **Slide 7:** Removidos valores FRAX, mantido apenas link

### Commits:
- `fix(slide7): corrigir margem inferior box azul DXA + overflow auto`
- `fix(slide7): ajustar margin-bottom box DXA e remover margin-top`

### Status:
- ✅ Layout 60/40 funcionando
- ✅ Box azul não corta mais
- ✅ Margem inferior corrigida

---

## v2.35 (Anterior)

### Mudanças:
- Layout 50/50 no Slide 7
- Box DXA cortado
- Valores FRAX exibidos

---

## 📝 REGRA DE VERSIONAMENTO

**SEMPRE que fizer mudança no viewer:**
1. ✅ Atualizar versão no título (v2.XX)
2. ✅ Atualizar versão no header (v2.XX)
3. ✅ Atualizar comentário do slide modificado
4. ✅ Adicionar entrada neste CHANGELOG
5. ✅ Fazer commit com mensagem descritiva

**Formato de commit:**
```
fix(slide7): [descrição da mudança] - v2.36
```

---

**Última atualização:** Janeiro 2025
