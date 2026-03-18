# QA Workflow — Meta-analise

> **DEPRECATED** — O workflow de QA e definido por [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa).
> Este arquivo mantido APENAS como referencia de tooling, template de scorecard, e comparacao com cirrose.
> NAO usar o Status Tracker daqui — fonte de verdade e [HANDOFF.md](HANDOFF.md).

---

## Tooling

| Ferramenta | Status | Uso |
|-----------|--------|-----|
| Playwright (plugin) | CONECTADO | Screenshots, contraste in-browser, console, video |
| a11y-contrast MCP | CONECTADO | Fallback contraste pontual |
| a11y MCP | CONECTADO | Audit a11y geral |
| lighthouse MCP | CONECTADO | Performance + a11y scores |
| lint:slides | INTEGRADO | Constraint check (Gate 1) |
| Gemini MCP | FALHANDO | Fase 4 quando disponivel |

---

## Template scorecard (copiar para AUDIT-VISUAL.md)

```markdown
## s-{id} (NN-slug.html)

**Status:** PASS (QA 14-dim YYYY-MM-DD)
**Archetype:** {archetype} — {dims baixas OK se aplicavel}

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | X | ... |
| T (tipografia) | X | ... |
| E (layout fill) | X | ... |
| C (cor/contraste) | X | ... |
| V (visuais) | X | ... |
| K (consistência) | X | ... |
| S (sofisticação) | X | ... |
| M (comunicação) | X | ... |
| I (interações) | X | ... |
| D (dados) | X | ... |
| A (acessibilidade) | X | ... |
| L (carga cognitiva) | X | ... |
| P (andragogia) | X | ... |
| N (arco narrativo) | X | ... |

**Fixes aplicados:** ...
**Pendências para audit Gemini (Gate 4):** ...
```

---

## Diferencas vs Cirrose

| Aspecto | Cirrose | Meta-analise |
|---------|---------|-------------|
| Slides | 44 | 18 |
| Case panel | Sim (6 estados) | Nao |
| Click-reveals complexos | Muitos (damico 4 estados, etc.) | Poucos (hook 2-beat, CP1 3-beat, CP2 4-beat) |
| Fases narrativas | 3 Atos + 3 Checkpoints | 3 Fases + 2 Interacoes |
| Archetypes dominantes | hero-stat, flow, pillars | compare, cards, hero-stat |
| Background alternation | Navy/surface/deep | Surface principal (light deck) |
| Build command | `npm run build:cirrose` | `npm run build:metanalise` |
| Publico | Hepatologistas seniorissimos | Residentes clinica medica (basico-intermediario) |
| Forest plots | N/A | Imagens cropadas (NUNCA SVG do zero) |
