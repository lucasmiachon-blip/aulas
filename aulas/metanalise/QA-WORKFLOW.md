# QA Workflow — Meta-analise

> Pipeline de QA visual, slide a slide, fase a fase.
> Threshold: todas 14 dimensoes >= 9 para PASS. Archetype-adjusted para title/hook/checkpoint/recap.
> Ferramentas: Playwright, Claude Vision, Gemini MCP, a11y-contrast MCP, chrome-devtools MCP.
> Criado: 2026-03-16. Baseado no QA-WORKFLOW.md da cirrose.

---

## Visao Geral

Fase 1          Fase 2 (por slide)           Fase 3           Fase 4
Batch        +---------------------+
Screenshots  | Screenshot + Metrics |
     |       |         |            |       Dynamic        Deck-Level
     |       | Constraint Check     |       Gate           Audit
     +------>|         |            |------> (animacoes) ---> (Gemini
     |       | Claude Vision 7-dim  |       por slide      cross-slide)
     |       |         |            |
     |       | Score 14-dim         |
     |       |         |            |
     |       | dim < 9? --YES--> Fix|
     |       |    |                 |
     |       |   NO                 |
     |       |    |                 |
     |       |  PASS -> commit      |
     |       +---------------------+

**Ordem:** F1 (3 slides) -> I1 (1) -> F2 (8 slides) -> I2 (1) -> F3 (5 slides)
**Regra:** Fase N+1 so comeca quando TODOS slides da Fase N tem PASS.

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

---

## Fase 1 — Batch Screenshots

**Objetivo:** Capturar estado final de todos os slides de uma fase.

### Execucao manual (Playwright)

```js
// No terminal com dev server ativo (npm run dev)
// Navegar slide a slide com ArrowRight (deck.js)
// Capturar 1280x720 @2x
```

### Output esperado

qa-screenshots/
  s-title/
    S0.png
    metrics.json
  s-hook/
    S0.png          <- beat 0 (auto)
    S1.png          <- beat 1 (click)
    metrics.json
  s-checkpoint-1/
    S0.png          <- cenario
    S1.png          <- opcoes
    S2.png          <- twist
    metrics.json
  ...

---

## Fase 2 — Per-Slide QA Loop

### Gate 1: Constraint Check (automatizado)

| Check | Metodo | Dim afetada |
|-------|--------|-------------|
| h2 = assercao clinica (nao rotulo) | grep + manual | M, N |
| Zero `<ul>/<ol>` no corpo | grep | M, L |
| `<aside class="notes">` com timing | grep | N |
| `<section>` sem style display (E07) | grep | S |
| Cores via var() — zero HEX hardcoded | grep metanalise.css | C |
| Dados com PMID verificado ou [TBD] | grep notes | D |
| Headline match manifest<->HTML | lint:narrative-sync | N, K |
| Body word count <= 30 | page.evaluate | L, M |
| Console errors = 0 | chrome-devtools MCP | S |

**Se qualquer check falhar -> fix ANTES de Gate 2.**

### Gate 2: Static Visual Audit

**Passo 1 — Layout Metrics (automatizado):**
- Fill ratio (elementos / slide-inner)
- Gaps entre elementos consecutivos
- Alinhamento horizontal
- SEM panel overlap check (metanalise nao tem case panel)

**Passo 2 — Claude Vision (7 dimensoes):**

Enviar screenshot com prompt:

"Analise este screenshot de slide medico para residentes de clinica medica.
Avalie 7 dimensoes (1-5 cada):
1. VISUAL HIERARCHY (Von Restorff) — 1 hero element 2-3x maior
2. SPACING & ALIGNMENT (Gestalt) — gaps consistentes, baseline grid
3. TYPOGRAPHY (Assertion-Evidence) — h2 = assertion, 3+ tamanhos distintos
4. COLOR & CONTRAST (WCAG projetor) — minimo 7:1 texto primario
5. FILL RATIO — 65-90% dependendo do tipo
6. COGNITIVE LOAD (Cowan 4+1) — max 4 grupos, max 30 palavras corpo
7. COMPOSITION (F/Z pattern) — fluxo de leitura claro
Contexto: bg claro, resolucao 1280x720, projetor de boa qualidade.
Publico: residentes clinica medica (basico-intermediario, nao experts).
Responda em JSON: { dim: score, issues: [...] }"

**Passo 3 — a11y-contrast MCP:**
- Texto primario vs bg -> threshold >=7:1
- Texto muted/footer vs bg -> threshold >=6:1
- Hero number vs bg -> threshold >=4.5:1 (large text AA)

**Passo 4 — chrome-devtools MCP:**
- Computed styles: verificar font-size, contraste real
- Console: zero errors/warnings

**Passo 5 — Score 14 dimensoes (AUDIT-VISUAL.md):**

| Origem | Dimensoes |
|--------|-----------|
| Gate 1 (lint) | D, M (parcial), N (parcial) |
| Gate 2 metrics | E, K (parcial) |
| Gate 2 Claude Vision | H, T, E (refina), C, V, S |
| Gate 2 a11y-contrast | C (refina), A |
| Gate 2 chrome-devtools | S (refina) |
| Manual (agente) | M (refina), I, L, P, N (refina) |

### Gate 3: Fix Loop

Se qualquer dimensao < 9 (ou < threshold archetype-adjusted):
1. Identificar dimensoes abaixo do threshold
2. Propor fix cirurgico (CSS, HTML, ou JS)
3. **Pedir aprovacao do usuario** para mudancas em HTML
4. Aplicar fix
5. `npm run build:metanalise`
6. Re-screenshot
7. Re-score dimensoes afetadas
8. Repetir ate PASS

**Max 3 iteracoes por slide.** Se nao convergir, registrar em HANDOFF.md.

### Gate 4: Docs Update

Apos PASS (ou max iteracoes):
1. Atualizar scorecard em AUDIT-VISUAL.md
2. Atualizar status em HANDOFF.md
3. Registrar fix em CHANGELOG.md (se houve mudanca)
4. Commit: `fix(metanalise): s-{id} QA pass — {resumo}`

---

## Fase 3 — Dynamic Gate (Animacoes)

**Quando:** Apos todos slides de uma fase passarem Fase 2.

Slides com animacao na metanalise (3 slides):
- **s-hook:** 2-beat state machine (countUp x3 no beat 1)
- **s-checkpoint-1:** 3-beat (cenario -> opcoes -> twist)
- **s-checkpoint-2:** 4-beat (cenario -> opcoes -> diamante -> NNT)

### Verificacoes por slide animado:

**3a. Timing Assertions (Playwright):**
| Tipo | Duration | Easing |
|------|----------|--------|
| fadeUp | 300-600ms | power2.out |
| countUp | 800-1200ms | power2.out |
| stagger (total) | <=1500ms | power2.out |

**3b. Click-Reveal Sequence:**
1. Estado S0 -> screenshot
2. ArrowRight -> S1 -> screenshot
3. Repetir ate SN
4. Retreat: ArrowLeft -> verificar reset

**3c. Video Recording (Playwright):**
Salvar em `qa-videos/{slide-id}.webm` para Gate 4 Gemini.

---

## Fase 4 — Deck-Level Audit (Gemini)

**Quando:** Apos TODOS slides passarem Fases 2+3.

### 4a. Static Cross-Slide (grid de thumbnails -> Gemini)

Prompt: "Analise esta sequencia de slides para residentes de clinica medica.
Avalie:
1. Consistencia visual cross-slide (tokens, tipografia, spacing)
2. Monotonia visual — slides consecutivos identicos?
3. Densidade cognitiva — distribuicao conteudo pesado vs leve
4. Transicoes entre fases (F1->I1->F2->I2->F3) — claras?
5. Arco didatico — importancia -> metodologia -> aplicacao"

### 4b. Dynamic Cross-Slide (video do deck -> Gemini)

Navegar todos os 18 slides, 3s cada. Enviar .webm com prompt de motion QA.

---

## Status Tracker

### F1 — Criar importancia (3 slides)

| # | Slide | Fase 2 | Fase 3 | Status |
|---|-------|--------|--------|--------|
| 1 | s-title | PASS (archetype) | N/A | DONE |
| 2 | s-hook | PASS | pendente | parcial |
| 3 | s-contrato | PASS | N/A | DONE |

### I1 — Checkpoint engajamento (1 slide)

| # | Slide | Fase 2 | Fase 3 | Status |
|---|-------|--------|--------|--------|
| 4 | s-checkpoint-1 | PASS | pendente | parcial |

### F2 — Metodologia (8 slides)

| # | Slide | Fase 2 | Fase 3 | Status |
|---|-------|--------|--------|--------|
| 5 | s-rs-vs-ma | PASS | N/A | DONE |
| 6 | s-pico | PASS | N/A | DONE |
| 7 | s-abstract | PASS | N/A | DONE |
| 8 | s-forest-plot | PASS | N/A | DONE |
| 9 | s-benefit-harm | PASS | N/A | DONE |
| 10 | s-grade | PASS | N/A | DONE |
| 11 | s-heterogeneity | PASS | N/A | DONE |
| 12 | s-fixed-random | PASS | N/A | DONE |

### I2 — Checkpoint consolidacao (1 slide)

| # | Slide | Fase 2 | Fase 3 | Status |
|---|-------|--------|--------|--------|
| 13 | s-checkpoint-2 | PASS | pendente | parcial |

### F3 — Aplicacao Valgimigli (5 slides)

| # | Slide | Fase 2 | Fase 3 | Status |
|---|-------|--------|--------|--------|
| 14 | s-ancora | PASS | N/A | DONE |
| 15 | s-aplicacao | PASS | N/A | DONE |
| 16 | s-aplicabilidade | PASS | N/A | DONE |
| 17 | s-absoluto | PASS | N/A | DONE |
| 18 | s-takehome | PASS | N/A | DONE |

### Deck-Level (Fase 4) — PENDENTE (todos slides devem passar Fases 2+3 primeiro)

**Resumo:** 17/18 PASS Fase 2 (s-contrato pendente decisao Lucas). 3 slides com Fase 3 pendente (hook, CP1, CP2). Fase 4 bloqueada.

---

## Tooling

| Ferramenta | Disponivel | Uso |
|-----------|-----------|-----|
| Playwright (via npx) | SIM | Screenshots, navegacao, metrics, video |
| Claude Vision (nativo) | SIM | Audit visual 7 dimensoes |
| lint:slides | SIM | Constraint check |
| Gemini MCP (@fre4x/gemini) | SIM | Fase 4: deck-level |
| a11y-contrast MCP | SIM | Fase 2: contraste WCAG |
| frontend-review MCP (Hyperbolic) | PARCIAL | Before/after visual diff |
| chrome-devtools MCP | SIM | Console errors, computed styles, profiling |

---

## Referencia

- AUDIT-VISUAL.md — rubrica 14 dimensoes + scorecards
- HANDOFF.md — estado e caminho critico
- .claude/rules/motion-qa.md — heuristics de animacao
- .claude/rules/design-principles.md — 27 principios (Duarte, Tufte, Sweller, Knowles)
