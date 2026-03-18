# AUDIT-VISUAL — Meta-análise

> Scorecard por slide. 14 dimensões. Atualizado a cada QA pass.
> Pendente: audit final Gemini (Gate 4) para todas as dims.
> Pipeline: ver [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa)
> Screenshots: **DOIS formatos por estado** — `S0.png` (1280x720 apresentação) + `S0-fullscreen.png` (1920x1080 inspeção). Ver WT-OPERATING.md §4 QA.2.

---

## Cobertura

| Fase | Slides | Scorecard formal | QA session |
|------|--------|-----------------|------------|
| F1 | s-title, s-hook, s-contrato | s-title, s-hook, s-contrato — scorecards abaixo | 2026-03-16e / 2026-03-17 |
| I1 | s-checkpoint-1 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F2 | s-rs-vs-ma → s-fixed-random (8) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |
| I2 | s-checkpoint-2 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F3 | s-ancora → s-takehome (5) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |

**Nota:** Sessao 2026-03-16j fez QA slide-a-slide (h2 assertion, word count, refs, notes) para 17/18 slides — PASS.
Scorecards formais de 14 dimensoes existem para s-title, s-hook, s-contrato (batch 1).
Demais slides passaram constraint check + review manual, mas sem scorecard 14-dim registrado.
Scorecards formais serao preenchidos durante ralph-qa batches 2-6 (proximas sessoes).

**HTML cleanup (2026-03-17d):** `data-background-color` removido de 17/18 slides (deck.js ignora — atributo morto). `slide-navy` removido de 16/18 slides light (mantido em CP1+CP2 que tem bg navy via CSS override). Nao altera scorecards existentes — so remove dead attributes. ERRO-009 documentado em ERROR-LOG.

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

**Fixes anteriores (2026-03-18b) — specificity war `.stage-c #deck p`:**
- Subtitle: selector → `#deck .slide-title p.title-subtitle` (0,1,2,1). Weight 450→600, font-size 20px, uppercase
- Author: selector → `#deck .slide-title p.title-author` (0,1,2,1). Weight 450→500
- Affiliation: selector → `#deck .slide-title p.title-affiliation` (0,1,2,1). Weight 450→400

**Fixes anteriores (2026-03-18):** h1 56px→64px, author --text-primary, affil --text-muted. Divider removido.
**Fixes anteriores (2026-03-16e/17):** tokens on-dark → light-mode. Pilares 400→500. data-background-color removido.

**Screenshots:** `qa-screenshots/s-title/S0.png` (1280x720), `qa-screenshots/s-title/S0-fullscreen.png` (1920x1080)
**Videos:** `qa-screenshots/s-title/video-v2.webm` (animacao completa pos-Gemini)

---

## s-hook (01-hook.html)

**Status:** QA.0-QA.2 PASS (refatorado 2026-03-18d). QA.3-QA.4 Gemini pendente.
**Archetype:** hook — dims E, P intencionalmente baixas
**Refactor (2026-03-18d):** 3-column number grid → hero number pattern. Dados: Bojcic/Qureshi → Windish 41%. Contexto: trials concretos (TRH, rosiglitazona, NICE-SUGAR) + 396 reversoes.

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Question 34px italic serif > Hero 96px mono 600 > Label 20px sans > Context 16px muted > Verdict 24px accent > Source 14px muted. Von Restorff no 41% |
| T (tipografia) | 9 | 3 familias: Instrument Serif italic (question), JetBrains Mono 600 (hero), DM Sans (label/context/verdict). Excelente contraste tipografico |
| E (layout fill) | 5 | ~55% — intencional para hook (respiro dramatico) |
| C (cor/contraste) | 8 | Hero 14.15:1 AAA, Label 9.20:1 AAA, Verdict 10.26:1 AAA, Context/source 5.75:1 AA (WARN: abaixo de 6:1 para projecao). Verificado via a11y-contrast MCP |
| V (visuais) | 8 | Single hero countUp 41% — impacto dominante. Sem imagens (texto-only hook) |
| K (consistencia) | 9 | Padrao hook. Source tag bottom |
| S (sofisticacao) | 9 | 2-beat state machine (slide-registry.js). countUp 1.5s + verdict delay 1.8s. .no-js + [data-qa] + print fallbacks |
| M (comunicacao) | 9 | Provocacao → hero punch → trials concretos → verdict. Arco emocional completo |
| I (interacoes) | 9 | 2-beat state machine (beat0 auto fadeUp, beat1 click → hero + context + verdict delayed). QA mode: [data-qa] selectors |
| D (dados) | 9 | 7 dados Tier 1 verificados: Hoffmann PMID 34091022, Windish PMID 17785646, Herrera-Perez PMID 31182188, WHI PMID 12117397, Nissen PMID 17517853, NICE-SUGAR PMID 19318384, Lakhlifi PMID 37081292 |
| A (acessibilidade) | 9 | Primary text AAA (>9:1). Context/source 5.75:1 AA — marginal para projecao mas aceitavel para texto secundario |
| L (carga cognitiva) | 9 | 1 hero number + 2 context lines + 1 verdict = dentro do 4+-1 Cowan |
| P (andragogia) | 9 | Retrieval practice (pergunta antes de resposta). Trials concretos criam personal stake |
| N (arco narrativo) | 9 | Hook forte — "por que essa aula existe". Transicao natural para s-contrato |

**Pendencias para Gemini (Gate 4):**
- Instrument Serif italic na provocacao — legibilidade a 5m em sala iluminada?
- Hero 96px mono — proporcional ao canvas 1280px?
- Context lines wrapping a 1280px — verificar em projecao real
- "396 praticas revertidas em JAMA, Lancet e NEJM" — Lucas considera abstrato, pode ajustar nos speaker notes
- Verdict delay 1.8s — timing adequado apos countUp?

**Screenshots:** `qa-screenshots/s-hook/beat0-1280x720.png`, `qa-screenshots/s-hook/beat1-final-1280x720.png`, `qa-screenshots/s-hook/beat1-1920x1080.png`

---

## s-contrato (02-contrato.html)

**Status:** PASS (QA 14-dim 2026-03-17b — re-confirmado 2026-03-18, CSS fixes de hoje nao afetam este slide)
**Archetype:** cards (setup) — dim D = N/A (sem dados clínicos)

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Número hero (56px mono) > pergunta (h3 24px serif) > skill (16px sans). Von Restorff nos numerais. |
| T (tipografia) | 9 | Instrument Serif nas perguntas, JetBrains Mono nos numerais, DM Sans nas skills. 3 famílias distintas. |
| E (layout fill) | 9 | Cards 248px (antes 550px — fix flex:1). h2 top 220px, grid 281-529px. Fill 82%. Proporção card adequada. |
| C (cor/contraste) | 9 | número vs card-bg 8.8:1, pergunta vs card-bg 15.5:1, skill vs card-bg 12.2:1. Todos acima de 7:1. |
| V (visuais) | 8 | Numerais 1/2/3 em hero mono funcionam como âncoras visuais. Sem gráfico. Correto para setup. |
| K (consistência) | 9 | Echo direto com s-takehome (slide 17). Archetype cards reutilizado de s-pico. Callbacks perguntas idênticas. |
| S (sofisticação) | 9 | data-animate="stagger" declarativo. Failsafes .no-js e .stage-bad. Sem source-tag (correto — sem dados). Sem AI markers. Token --ui-accent corrigido (era on-dark). |
| M (comunicação) | 9 | h2 = asserção verificável. Sem ul/ol. 45 palavras total mas 3 cards × ~12 palavras (Cowan chunks). |
| I (interações) | 9 | Stagger automático ao entrar. clickReveals: 0 no manifest. Sem click handlers. Sem JS inline. |
| D (dados) | N/A | Slide de setup — sem dados numéricos clínicos. Sem TBD em corpo. |
| A (acessibilidade) | 9 | Contraste mínimo 8.8:1 (todos pares medidos). aside.notes hidden. Console errors: ZERO. |
| L (carga cognitiva) | 9 | 1 conceito central: framework de 3 perguntas. 3 chunks visuais independentes. Stagger revela sequencialmente. |
| P (andragogia) | 9 | "3 perguntas que você faz" = imperativo do residente. Contrato com audiência = técnica andragógica sólida. Echo com takehome cria schema. |
| N (arco narrativo) | 9 | narrativeRole: setup. tensionLevel: 1 — resolve ansiedade do hook. Perguntas espelham takehome (slide 17). Posição correta no arco. |

**Fixes aplicados (2026-03-17):**
- `slide-navy` removido de `.slide-inner` — herança de versão navy anterior. Stage-c = fundo creme.
- `data-background-color="#162032"` removido do `<section>` — ignorado por deck.js (ERRO-034), era legado.

**Fixes aplicados (2026-03-17b):**
- `.contrato-grid`: removido `flex: 1` + `align-items: stretch` — cards de 550→248px.
- `.contrato-card`: adicionado `justify-content: center` + padding vertical `--space-lg`.
- `.contrato-number`: token `--ui-accent-on-dark` → `--ui-accent` (correto para stage-c light bg).

**Gate 1 constraint check: PASS**
- h2 = asserção ✅, zero ul/ol ✅, aside.notes ✅, sem inline style ✅, sem data-background-color ✅, sem slide-navy ✅, lint:slides PASS ✅, console ZERO ✅
- WARN: word count 45 (3 cards × ~12 — dentro do esperado para archetype cards)

**DOC COMPLIANCE:**
- [x] manifest headline == HTML h2: "3 perguntas que você faz a toda meta-análise"
- [x] manifest id == section id: s-contrato
- [x] Notes com timing [0:00-0:15] [0:15-0:30] [0:30-0:45] — sem dados numéricos novos
- [x] Sem [TBD] em corpo projetado

**Screenshots:** `qa-screenshots/s02-contrato-current.png` (pré-fix), `qa-screenshots/s02-contrato-fix1.png` (pós-fix). Ambos 1280×720 via Playwright script.

**Pendências para audit Gemini (Gate 4):**
- Avaliar se cards são distinguíveis em projetor real (contraste de área bg-navy-mid/bg-surface sutil)
- Avaliar timing stagger: 3 cards × 0.15s = 0.45s — adequado para pacing clínico?
- Confirmar legibilidade Instrument Serif nas perguntas dos cards em tela a 5m
