# AUDIT-VISUAL — Meta-análise

> Scorecard por slide. 14 dimensões. Atualizado a cada QA pass.
> Pendente: audit final Gemini (Gate 4) para todas as dims.
> Pipeline: ver [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa)
> Screenshots: **DOIS formatos por estado** — `S0.png` (1280x720 apresentação) + `S0-fullscreen.png` (1920x1080 inspeção). Ver WT-OPERATING.md §4 QA.2.

---

## Cobertura

| Fase | Slides | Scorecard formal | QA session |
|------|--------|-----------------|------------|
| F1 | s-title, s-hook, s-contrato | s-title DONE, s-hook DONE, s-contrato DONE | 2026-03-16e / 2026-03-17 / 2026-03-19 |
| I1 | s-checkpoint-1 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F2 | s-rs-vs-ma → s-fixed-random (8) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |
| I2 | s-checkpoint-2 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F3 | s-ancora → s-takehome (5) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |

**Nota:** Sessao 2026-03-16j fez QA slide-a-slide (h2 assertion, word count, refs, notes) para 17/18 slides — PASS.
Scorecards formais de 14 dimensoes existem para s-title, s-hook, s-contrato (batch 1).
Demais slides passaram constraint check + review manual, mas sem scorecard 14-dim registrado.
Scorecards formais serao preenchidos durante ralph-qa batches 2-6 (proximas sessoes).

**HTML cleanup (2026-03-17d):** `data-background-color` removido de 17/18 slides (deck.js ignora — atributo morto). `slide-navy` removido de 16/18 slides light (mantido em CP1+CP2 que tem bg navy via CSS override). Nao altera scorecards existentes — so remove dead attributes. ERRO-009 documentado em ERROR-LOG.

**Visual uplift infra (2026-03-19c):** Dark-bg CSS consolidado para 6 slides (CP1, CP2, forest-plot, heterogeneity, ancora, absoluto). SplitText disponivel globalmente. Prompt Gemini v6.0 com 10 dimensoes + exploration mandate GSAP. Criterios visuais elevados a partir desta sessao. Scorecards anteriores permanecem validos — re-audit sob criterios novos acontece quando slide entra no pipeline.

---

## s-title (00-title.html)

**Status:** PASS (QA.0-QA.4 completo 2026-03-18c — Gemini approved, beauty 9/10, legibility 10/10)
**Archetype:** title — dims E, M, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | h1 64px/400 > subtitle 20px/600 uppercase > pillars 20px/500 uppercase > author 20px/500 > affil 18px/400 muted — inverted weight hierarchy (Gemini bold idea #1) |
| T (tipografia) | 9 | DM Sans throughout (stage-c). Inverted weight: h1 light 400, subtitle bold 600 uppercase. 5 tratamentos diferenciados |
| E (layout fill) | 4 | ~30% — intencional para title |
| C (cor/contraste) | 9 | h1 17.58:1, subtitle 13.82:1, author 17.58:1, affil 8.62:1 — todos AAA. Verificado via Playwright + a11y-contrast MCP |
| V (visuais) | 8 | Pillar masking reveal (overflow:hidden + GSAP yPercent). Dots optically centered. Sem divider (removido — era AI marker) |
| K (consistencia) | 9 | Padrao de capa. Pillars ecoam s-contrato e s-takehome |
| S (sofisticacao) | 9 | Custom choreography via slide-registry.js. Failsafes .no-js e @media print. Sem AI markers |
| M (comunicacao) | 5 | h1 = rotulo — correto para archetype |
| I (interacoes) | 9 | Full choreography: h1 fade+rise (0s) → subtitle (0.3s) → pillar masking (0.6s) → dots fade (0.8s) → identity (1.4s). Sem click-reveals |
| D (dados) | N/A | Title — sem dados clinicos |
| A (acessibilidade) | 9 | Todos pares >= 8.62:1 (AAA). aria-hidden nos dots decorativos |
| L (carga cognitiva) | 9 | Minimo — titulo + 3 palavras + identidade |
| P (andragogia) | 6 | Sem decisao clinica — esperado. Pillars orientam framework |
| N (arco narrativo) | 8 | Abertura limpa. Pillars (Perguntar/Estimar/Decidir) mapeiam 3 fases |

**Gemini QA.3 (2026-03-18c) — model gemini-2.5-pro (2 rounds):**
- Round 1: beauty 8.5/10, legibility 9/10. 4 issues + 3 bold ideas propostas
- Bold ideas aplicadas: #1 inverted weight hierarchy (h1 400/64, subtitle 600/20 uppercase), #2 merged identity block, #3 pillar masking reveal (overflow:hidden + GSAP yPercent)
- Round 2 (re-eval com screenshots + video pos-fix): beauty 9/10, legibility 10/10, verdict **approve**
- Custo estimado: ~$0.15 (2 chamadas API)

**QA.4 fixes (2026-03-18c):**
- Pillar-dot: `transform: translateY(1px)` para alinhamento optico com uppercase
- Choreography: slide-registry.js reescrito — h1/subtitle/identity animados via GSAP (antes so pillars). `data-animate="fadeUp"` removido do HTML (custom anim controla tudo)
- CSS: `#s-title h1, .title-subtitle, .title-identity { opacity: 0 }` + `.no-js` + `@media print` failsafes

**Fix history:** specificity bumps (03-18b), h1 64px + divider removido (03-18), on-dark→light tokens (03-16e). Detalhes: `git log --oneline -- aulas/metanalise/metanalise.css`

**Screenshots:** `qa-screenshots/s-title/S0.png` (1280x720), `qa-screenshots/s-title/S0-fullscreen.png` (1920x1080)
**Videos:** `qa-screenshots/s-title/video-v2.webm` (animacao completa pos-Gemini)

---

## s-hook (01-hook.html)

**Status:** PASS (QA.0-QA.4 completo 2026-03-19. Gemini QA.3 drove uplift. Opus QA.4 re-audit PASS. Decimal countUp fix 03-19.)
**Archetype:** cards — asymmetric grid "volume vs reality" with countUp GSAP
**History:** Rewrite edb2e2f (sober 3-card), uplift c400f5a (Gemini QA.3 → asymmetric grid, typographic deconstruction, divider, tags), decimal countUp fix (03-19: 33,8% animates with parseFloat+data-decimals)

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Hero 96px "80" dominates left; 72px secondary nums right; h2 34px top-left anchor |
| T (tipografia) | 9 | JetBrains Mono nums (96/72px), DM Sans labels (20px), affix smaller (36/32px). Tabular-nums lining-nums |
| E (layout fill) | 9 | CSS Grid 1fr-auto-1fr. Vertical divider 200px. ~60% fill — hook sweet spot |
| C (cor/contraste) | 10 | h2 17.58:1, nums 9.99:1, labels 13.82:1, muted 8.62:1 — ALL AAA. Verified via Playwright + a11y-contrast MCP |
| V (visuais) | 9 | Numbers ARE the visual evidence. AMSTAR-2/GRADE tags = credibility markers. No images needed |
| K (consistencia) | 9 | Same bg surface + h2 position as s-title. Mono nums, source-tag convention |
| S (sofisticacao) | 9 | Asymmetric grid, typographic deconstruction (big num + small affix), editorial divider, countUp choreography, tags |
| M (comunicacao) | 10 | Volume vs quality gap = clear message. Asymmetric layout reinforces narrative |
| I (interacoes) | 9 | CountUp choreography: volume→divider→facts. Timeline: tl.to chain. No click-reveals (appropriate for hook) |
| D (dados) | 10 | 3 sourced data points (Hoffmann, Bojcic, Siedler). PMIDs in notes. Murad 2014 framework. No invented data |
| A (acessibilidade) | 10 | All AAA. no-js failsafe (HTML has final values). stage-bad failsafe. @media print failsafe |
| L (carga cognitiva) | 9 | 3 data points in 2 chunks (Cowan OK). Labels concise. Body word count within 30-word limit |
| P (andragogia) | 9 | Engages via surprise gap (volume high, quality low). Relevant to daily practice |
| N (arco narrativo) | 10 | Tension 2. Creates cognitive dissonance → motivates entire deck |

**Average: 9.36/10 — All dimensions >= 9. PASS.**

**QA.3 Gemini (2026-03-19, gemini-2.5-pro):**
- Input: fullscreen PNG (1920x1080) + full code context (HTML + CSS + JS)
- Gemini scored original 3-card layout 4.4/10. Proposed 6 changes.
- Accepted: asymmetric grid, countUp GSAP, typographic deconstruction, editorial divider, AMSTAR-2/GRADE tags
- Rejected: danger color for 81% (--danger semantics = clinical harm, not quality assessment)
- Projected scorecard: 9.2/10

**QA.4 re-audit (2026-03-19, Opus):**
- Fresh screenshots at 1280x720 + 1920x1080 post-uplift
- 5 contrast checks via a11y-contrast MCP — all AAA
- 14-dim scorecard: all >= 9. PASS.

**Scorecard anterior (pre-rewrite, referencia historica):** avg 8.6/10. Detalhes em HANDOFF-ARCHIVE.md.

**Screenshots:** `qa-screenshots/s-hook/QA4-1280x720.png`, `qa-screenshots/s-hook/QA4-1920x1080.png`
**Screenshots anteriores (historico):** S0.png, S0-fullscreen.png (pre-uplift), S0-v2.png, S0-v2-fullscreen.png (post-uplift), video.webm

---

## s-contrato (02-contrato.html)

**Status:** DONE — Gemini R4 APPROVED (beauty 9, legibility 8.5). All Gemini suggestions applied. Watermark 35% opacity (azul forte). Lucas approved.
**Archetype:** cards (setup) — dim D = N/A (sem dados clinicos)
**History:** flex:1 fix (03-17b), visual uplift Gemini R1 (03-19: grid+subgrid, bleeding watermarks, left-align, custom GSAP choreography), cards 2&3 fix (03-19: skill 12px, text-wrap balance), watermark-only redesign (03-19: remove small numbers, keep only ::after 14rem at 12% opacity, grid 2 rows)

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Bleeding watermark (14rem mono, 12% opacity) > pergunta (26px serif) > skill (12px sans uppercase). Watermark-only = cleaner hierarchy. |
| T (tipografia) | 9 | Instrument Serif perguntas, JetBrains Mono numerais+watermark, DM Sans skills. text-wrap:balance evita orfaos. |
| E (layout fill) | 9 | CSS Grid repeat(3,1fr) + subgrid 2 rows. margin-top/bottom:auto centraliza. Fill ~65%. |
| C (cor/contraste) | 9 | numero --ui-accent vs white 8.8:1, pergunta --text-primary vs white 15.5:1, skill --text-secondary vs white 9.13:1. Todos AAA. |
| V (visuais) | 9 | Bleeding watermark numbers (14rem, 12% opacity) = sole numeral layer. Layered shadow (3-tier). Subgrid cross-card alignment. Cleaner without small inline numbers. |
| K (consistencia) | 9 | Echo direto com s-takehome (slide 17, shared .contrato-grid). Archetype cards. |
| S (sofisticacao) | 10 | Custom GSAP choreography: cards rise+scale (watermark appears with card) → questions fadeUp → skills slideX. Failsafes .no-js, .stage-bad, [data-qa], @media print. Bleeding watermark via ::after pseudo. |
| M (comunicacao) | 9 | h2 = assercao verificavel. 3 cards x ~12 palavras (Cowan). Left-align facilita scanning. |
| I (interacoes) | 9 | Custom choreography via slide-registry.js. clickReveals: 0. Sem click handlers. |
| D (dados) | N/A | Slide de setup — sem dados numericos clinicos. |
| A (acessibilidade) | 9 | Contraste minimo 8.8:1 (todos pares). Failsafes completos. aside.notes hidden. |
| L (carga cognitiva) | 9 | 1 conceito central: framework de 3 perguntas. 3 chunks visuais. Choreography sequencial. |
| P (andragogia) | 9 | "3 perguntas que voce faz" = imperativo. Contrato com audiencia. Echo takehome. |
| N (arco narrativo) | 9 | narrativeRole: setup. tensionLevel: 1. Resolve ansiedade do hook. Espelha takehome. |

**Gemini QA.3 (2026-03-19, gemini-2.5-pro):**
- Round 1: Proposed grid+subgrid, left-align, bleeding watermarks, 3-tier shadow, custom GSAP choreography, skill uppercase+border-top
- All proposals accepted + radical (bleeding watermark). Implemented in 2038185.
- Round 2: re-eval com screenshots pos-fix. Score 9.25/10. Verdict: **APPROVED**.
- Round 3: re-eval apos cards 2&3 fix (skill 12px, text-wrap balance). Score 9.5/10. Verdict: **APPROVED** (beauty 9.5, legibility 10).
- Round 4: re-eval watermark-only design. Score beauty 9, legibility 8.5. Verdict: **APPROVED**. Suggested: card border, skill 600, fadeUp skills, accent +. All applied.
- Round 5 (Lucas tuning): watermark opacity 0.12→0.15→0.20→0.35 (azul forte). Lucas APPROVED.

**Fix history:** slide-navy removed (03-17), flex:1→cards 248px + token ui-accent (03-17b), visual uplift grid+subgrid+watermark+GSAP (03-19 2038185), cards 2&3 fix: skill 15→12px, text-wrap:balance (03-19 f38eb90), watermark-only: remove contrato-number spans, grid 2 rows (03-19 f2d3785), Gemini polish: border divider, skill 600, fadeUp skills, accent +, watermark 35% (03-19).

**Screenshots:** `qa-screenshots/s-contrato/s-contrato-1280x720-r5-opacity35.png` (final). Historico: S0→S5-fixed, r4, r5.

---

## Template — Scorecard 14-dim (copiar para cada slide)

> Copiar bloco abaixo ao iniciar QA.2 de um slide. Preencher notas e scores.

```markdown
## s-{id} (NN-slug.html)

**Status:** [QA em andamento]
**Archetype:** [tipo]

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | ?/10 | |
| T (tipografia) | ?/10 | |
| E (layout fill) | ?/10 | |
| C (cor/contraste) | ?/10 | |
| V (visuais) | ?/10 | |
| K (consistencia) | ?/10 | |
| S (sofisticacao) | ?/10 | |
| M (comunicacao) | ?/10 | |
| I (interacoes) | ?/10 | |
| D (dados) | ?/10 | |
| A (acessibilidade) | ?/10 | |
| L (carga cognitiva) | ?/10 | |
| P (andragogia) | ?/10 | |
| N (arco narrativo) | ?/10 | |

**Average: ?/10**

**QA.3 Gemini (DATE, MODEL):**
- Input: [PNGs, video, code]
- Score: ?/10. Verdict: [ITERATE/APPROVED]
- Accepted: [list]
- Rejected: [list]

**QA.4 fixes:**
- [list of changes]

**Screenshots:** `qa-screenshots/s-{id}/S0.png` (1280x720), `qa-screenshots/s-{id}/S0-fullscreen.png` (1920x1080)
```

### Fila QA (15 slides pendentes — copiar template acima ao iniciar cada)

| Ordem | Slide ID | Arquivo | Fase | Prioridade |
|-------|----------|---------|------|------------|
| 1 | s-checkpoint-1 | 03-checkpoint-1.html | I1 | Próximo |
| 2 | s-rs-vs-ma | 04-rs-vs-ma.html | F2 | — |
| 3 | s-pico | 05-pico.html | F2 | — |
| 4 | s-abstract | 06-abstract.html | F2 | — |
| 5 | s-forest-plot | 07-forest-plot.html | F2 | — |
| 6 | s-benefit-harm | 08-benefit-harm.html | F2 | — |
| 7 | s-grade | 09-grade.html | F2 | — |
| 8 | s-heterogeneity | 10-heterogeneity.html | F2 | — |
| 9 | s-fixed-random | 11-fixed-random.html | F2 | — |
| 10 | s-checkpoint-2 | 12-checkpoint-2.html | I2 | — |
| 11 | s-ancora | 13-ancora.html | F3 | — |
| 12 | s-aplicacao | 14-aplicacao.html | F3 | — |
| 13 | s-aplicabilidade | 15-aplicabilidade.html | F3 | — |
| 14 | s-absoluto | 16-absoluto.html | F3 | — |
| 15 | s-takehome | 17-takehome.html | F3 | — |
