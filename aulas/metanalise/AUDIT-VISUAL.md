# AUDIT-VISUAL — Meta-análise

> Scorecard por slide. 14 dimensões. Atualizado a cada QA pass.
> Pendente: audit final Gemini (Gate 4) para todas as dims.

---

## s-title (00-title.html)

**Status:** PASS (QA slide-a-slide 2026-03-16e)
**Archetype:** title — dims E, M, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | h1 > subtitle > pillars > author — clara |
| T (tipografia) | 9 | Serif+sans, pesos adequados, uppercase 500 |
| E (layout fill) | 4 | ~30% — intencional para title |
| C (cor/contraste) | 8 | Tokens light-mode corretos (fix session 16e) |
| V (visuais) | 7 | Sem visual dominante — OK para title |
| K (consistência) | 9 | Padrão de capa |
| S (sofisticação) | 8 | Limpo, profissional |
| M (comunicação) | 5 | h1 = rótulo — correto para archetype |
| I (interações) | 6 | fadeUp + stagger presentes |
| D (dados) | N/A | Title — sem dados clínicos |
| A (acessibilidade) | 8 | aria-hidden nos dots, bom contraste |
| L (carga cognitiva) | 9 | Mínimo — título + 3 palavras |
| P (andragogia) | 6 | Sem decisão clínica — esperado |
| N (arco narrativo) | 8 | Abertura limpa, pilares antecipam estrutura |

**Fix aplicado:** tokens `--text-on-dark-*` → tokens light-mode (`--text-secondary`, `--text-primary`, `--text-muted`). Pilares peso 400→500.

**Pendências para audit Gemini (Gate 4):**
- Title divider (linha decorativa) — avaliar se é AI marker ou separação funcional
- Spacing vertical — grupo de conteúdo levemente acima do centro? Avaliar com Gemini
- Fill ratio 30% — confirmar que é adequado para projeção (muito vazio?)
- Tipografia do h1 (Instrument Serif) — confirmar legibilidade em projetor real
