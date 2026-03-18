# QA Workflow — Meta-analise

> **DEPRECATED** — O workflow de QA agora e definido por [WT-OPERATING.md](WT-OPERATING.md) secao 4 (QA Sub-Loop).
> Este arquivo mantido como referencia de tooling, execution logs, e status tracker historico.

> Pipeline de QA visual, slide a slide, fase a fase.
> Threshold: todas 14 dimensoes >= 9 para PASS. Archetype-adjusted para title/hook/checkpoint/recap.
> Ferramentas: Playwright (screenshots, contraste in-browser, console, video), a11y-contrast MCP, lighthouse MCP, lint:slides.
> Criado: 2026-03-16. Reescrito: 2026-03-17 (workflow executavel autonomo, baseado no QA real de F1).

---

## Workflow Operacional

```
POR SLIDE:
  Gate 1: Constraint Check (grep + lint)
    ↓ PASS
  Gate 2: Visual Audit (Playwright screenshot + contraste in-browser + score 14-dim)
    ↓ PASS (todas dims >= 9)
  Gate 3: Fix Loop (se dim < 9: fix → re-screenshot → re-score, max 3 iteracoes)
    ↓ PASS
  Gate 4: Docs + Commit (AUDIT-VISUAL + HANDOFF + CHANGELOG + git commit)

POR FASE (apos todos slides da fase PASS):
  Fase 3: Dynamic Gate (slides com animacao: timing assertions + click-reveal + video)

POR DECK (apos todas fases PASS):
  Fase 4: Deck-Level Audit (Gemini cross-slide: grid thumbnails + video)
```

**Ordem:** F1 (3 slides) -> I1 (1) -> F2 (8 slides) -> I2 (1) -> F3 (5 slides)
**Regra:** Fase N+1 so comeca quando TODOS slides da Fase N tem PASS.

---

## Gate 1 — Constraint Check

Automatizado via grep + lint. **Se qualquer check falhar → fix ANTES de Gate 2.**

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
| Console errors = 0 | Playwright `page.on('console')` | S |

---

## Gate 2 — Visual Audit

3 passos sequenciais. Dev server ativo (`npm run dev`).

### Passo 1 — Screenshot + Contraste (Playwright)

1. Navegar ao slide via Playwright (deck.js hash nav + `waitForSelector('.slide-inner')`)
2. Screenshot 1280x720
3. Testar contraste via JavaScript injection no browser:

```js
// Para cada par texto/bg visivel no slide:
// 1. getComputedStyle() para cor do texto e bg
// 2. Converter para luminance relativa
// 3. Calcular ratio WCAG
// Thresholds:
//   Texto primario (h2, hero numbers, punchlines): >= 7:1
//   Texto secundario (labels, source-tags, footers): >= 6:1
//   Large text (>= 24px ou >= 18.66px bold): >= 4.5:1 (AA)
```

**Todos pares PASS → prosseguir. Qualquer FAIL → fix imediato antes de score.**

Fallback: `a11y-contrast` MCP para checks pontuais (quando Playwright nao estiver disponivel).

### Passo 2 — Score 14 dimensoes

Avaliar baseado em: screenshot + HTML source + CSS da aula.
Usar rubrica AUDIT-VISUAL.md (14 dims, 1-10, threshold 9).

| Dim | Nome | O que avaliar |
|-----|------|---------------|
| H | Hierarquia | Von Restorff: 1 hero element 2-3x maior |
| T | Tipografia | 3+ tamanhos distintos, serif/sans/mono adequados |
| E | Layout/fill | Fill ratio 65-90% (ajustado por archetype) |
| C | Cor/contraste | Passo 1 PASS + semantica clinica correta |
| V | Visuais | Graficos, icones, dados visuais (se aplicavel) |
| K | Consistencia | Tokens, spacing, patterns iguais ao resto do deck |
| S | Sofisticacao | Sem AI markers, failsafes, declarativo |
| M | Comunicacao | h2 assertion, sem listas, corpo <= 30 palavras |
| I | Interacoes | click-reveal, animacoes, data-animate correto |
| D | Dados clinicos | PMID verificado, Tier 1, [TBD] so em notes |
| A | Acessibilidade | Contraste PASS, aria, notes hidden |
| L | Carga cognitiva | Cowan 4±1, chunks, extraneous load minimo |
| P | Andragogia | Retrieval practice, expertise-reversal, relevancia |
| N | Arco narrativo | narrativeRole, tensionLevel, posicao no arco |

**Archetype adjustments** (dims que podem ficar abaixo de 9 sem bloquear):

| Archetype | Dims baixas OK | Razao |
|-----------|----------------|-------|
| title | E, M, P | Fill 30%, h1=rotulo, sem decisao clinica |
| hook | E, P | Respiro dramatico, provocacao > andragogia |
| checkpoint | I alto obrigatorio | Interacao e a razao de existir |
| cards/setup | D = N/A | Sem dados clinicos no slide |

Registrar score em AUDIT-VISUAL.md com formato padrao (ver template abaixo).

### Passo 3 — Console errors

Via Playwright `page.on('console')` durante navegacao ao slide.
- Zero errors = PASS
- Warnings = registrar mas nao bloquear

---

## Gate 3 — Fix Loop

```
dim < 9 (ou < threshold archetype)?
  → Identificar causa (CSS? HTML? conteudo?)
  → Propor fix cirurgico
  → Se HTML muda: pedir aprovacao do usuario
  → Aplicar fix
  → npm run build:metanalise
  → Re-screenshot (Passo 1)
  → Re-score dims afetadas (Passo 2)
  → Repetir ate PASS ou max 3 iteracoes
  → Se nao convergir: registrar em HANDOFF.md com [NAO-CONVERGIU]
```

**Regra de escopo:** "So ajusta X" = escopo e APENAS X (E20). Nao expandir fix para alem da dim afetada.

---

## Gate 4 — Docs + Commit

Apos PASS (ou max iteracoes):

```
1. AUDIT-VISUAL.md: scorecard 14-dim (copiar template abaixo)
2. HANDOFF.md: status do slide → DONE
3. CHANGELOG.md: registrar fix (se houve)
4. ERROR-LOG.md: registrar erro (se houve — novo ERRO-NNN)
5. git commit: fix(metanalise): s-{id} QA — {resumo 1 linha}
```

### Template scorecard (copiar para AUDIT-VISUAL.md)

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

## Fase 3 — Dynamic Gate (Animacoes)

**Quando:** Apos todos slides de uma fase passarem Gates 1-4.

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
Salvar em `qa-videos/{slide-id}.webm` para Fase 4 Gemini.

---

## Fase 4 — Deck-Level Audit (Gemini)

**Quando:** Apos TODOS slides passarem Gates 1-4 + Fase 3.

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

## Extensoes Futuras

> Estas extensoes serao implementadas quando houver tooling automatizado.
> Ate la, o workflow operacional acima e suficiente.

- **Metrics JSON automatizado:** fill ratio, bounding boxes, gaps via script Playwright (`page.evaluate` com `getBoundingClientRect`). Output em `qa-screenshots/{slide-id}/metrics.json`.
- **Claude Vision 7-dim como prompt separado:** hoje absorvido pelo score 14-dim manual. Quando disponivel como API automatizada, rodar como passo dedicado antes do score.
- **chrome-devtools MCP:** substituido por Playwright `page.on('console')` + `page.evaluate(getComputedStyle)`. Re-avaliar se MCP ganhar features de profiling.
- **Script automatizado de extracao:** batch screenshots + metrics + contraste em um so comando (`node qa-run.js --aula metanalise`).

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

## Status Tracker

### F1 — Criar importancia (3 slides)

| # | Slide | Gates 1-4 | Fase 3 | Status |
|---|-------|-----------|--------|--------|
| 1 | s-title | PASS | N/A | DONE |
| 2 | s-hook | PASS | pendente | parcial |
| 3 | s-contrato | PASS | N/A | DONE |

### I1 — Checkpoint engajamento (1 slide)

| # | Slide | Gates 1-4 | Fase 3 | Status |
|---|-------|-----------|--------|--------|
| 4 | s-checkpoint-1 | PASS | pendente | parcial |

### F2 — Metodologia (8 slides)

| # | Slide | Gates 1-4 | Fase 3 | Status |
|---|-------|-----------|--------|--------|
| 5 | s-rs-vs-ma | PASS | N/A | DONE |
| 6 | s-pico | PASS | N/A | DONE |
| 7 | s-abstract | PASS | N/A | DONE |
| 8 | s-forest-plot | PASS | N/A | DONE |
| 9 | s-benefit-harm | PASS | N/A | DONE |
| 10 | s-grade | PASS | N/A | DONE |
| 11 | s-heterogeneity | PASS | N/A | DONE |
| 12 | s-fixed-random | PASS | N/A | DONE |

### I2 — Checkpoint consolidacao (1 slide)

| # | Slide | Gates 1-4 | Fase 3 | Status |
|---|-------|-----------|--------|--------|
| 13 | s-checkpoint-2 | PASS | pendente | parcial |

### F3 — Aplicacao Valgimigli (5 slides)

| # | Slide | Gates 1-4 | Fase 3 | Status |
|---|-------|-----------|--------|--------|
| 14 | s-ancora | PASS | N/A | DONE |
| 15 | s-aplicacao | PASS | N/A | DONE |
| 16 | s-aplicabilidade | PASS | N/A | DONE |
| 17 | s-absoluto | PASS | N/A | DONE |
| 18 | s-takehome | PASS | N/A | DONE |

### Deck-Level (Fase 4) — PENDENTE

**Resumo:** 18/18 PASS Gates 1-4. 3 slides com Fase 3 pendente (hook, CP1, CP2). Fase 4 bloqueada ate Fase 3 concluir.

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

## Referencia

- AUDIT-VISUAL.md — rubrica 14 dimensoes + scorecards
- HANDOFF.md — estado e caminho critico
- .claude/rules/motion-qa.md — heuristics de animacao
- .claude/rules/design-principles.md — 27 principios (Duarte, Tufte, Sweller, Knowles)
