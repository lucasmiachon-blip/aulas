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

**Visual uplift infra (2026-03-19c):** Dark-bg CSS consolidado para 6 slides (CP1, CP2, forest-plot, heterogeneity, ancora, absoluto). SplitText disponivel globalmente. Prompt Gemini v3.0 com 4 dimensoes + exploration mandate GSAP. Criterios visuais elevados a partir desta sessao. Scorecards anteriores permanecem validos — re-audit sob criterios novos acontece quando slide entra no pipeline.

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

**Status:** Gate 3 PASS com issues (2026-03-19f). 1 issue CRITICAL (verdict contrast), 1 MINOR (word-break). QA.4 fixes pendentes.
**Archetype:** hook — dims E, P intencionalmente baixas
**Content rewrite (2026-03-19e):** VITALITY backbone. Beat 0: "1.330 trials retratados → 3.902 MAs, 81% qualidade baixa". Beat 1: "20% das MAs mudam resultado, 157 guidelines contaminadas". Beat 2: NICE-SUGAR cadeia MA (Wiener 2008 → NICE-SUGAR 2009 → Griesdale 2009).
**Refactor anterior (2026-03-18d):** 3-column number grid → hero number pattern. Grid assimétrico 2-col (Z-pattern). Blackout brutalismo.

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 8 | 96px mono hero "1.330"/"20%" → 34px Instrument Serif italic (description) → 20px DM Sans (label) → 14px source-tag. 4 níveis tipográficos distintos. Von Restorff nos números hero. |
| T (tipografia) | 9 | JetBrains Mono 96px/600 (hero numbers), Instrument Serif 34px italic (description + verdict), DM Sans 20px (label). 3 famílias com função semântica clara: mono=impacto, serif=narrativa, sans=informação. |
| E (layout fill) | 5 | Beat 0: ~30% (upper-left, respiro intencional). Beat 1: ~40% (Z-pattern 2-col). Beat 2: ~50% (ghosted + full-width red block). Baixo por design — archetype hook/hero/breathe. |
| C (cor/contraste) | 6 | Beat 0/1 text: "1.330"/"20%" 13.09:1 AAA+, description 13.09:1, secondary 9.05:1 AAA, source-tag 5.32:1 AA. **ISSUE: verdict (beat 2) = oklch(12%) dark text on oklch(50%) danger-red bg = 3.67:1. AA-lg PASS (3:1) mas BELOW 7:1 projector threshold.** Precisa fix: escurecer bg ou forçar texto claro com override. |
| V (visuais) | 8 | Z-pattern grid assimétrico. Blackout beat 2 (opacity 0.04, scale 0.97) = fade dramático. Red verdict block border-radius:0 (brutalismo editorial). Sem decoração. Word-break "paci/entes" desfavorável (minor). |
| K (consistencia) | 9 | Hero number pattern (96px mono) consistente entre "1.330" e "20%". Source-tag pattern igual ao s-title. .no-js + [data-qa] + @media print failsafes. Hook é intencionalmente distinto (correto). |
| S (sofisticacao) | 9 | ScrambleText "1.330" (chars '0123456789.') + "20%" (chars '0123456789%'). SplitText words (beat 0) + chars (beat 2). 3-beat state machine com advance/retreat/cleanup. Blackout via GSAP (opacity+scale, não CSS class). Triple failsafe (.no-js, [data-qa], @media print). |
| M (comunicacao) | 8 | Sem h2 (correto para hook). Arco escalante: contaminação (1.330 retratados) → consequência sistêmica (20% mudam) → exemplo concreto (NICE-SUGAR). Cada beat adiciona camada de urgência. Word-break "paci/entes" interrompe leitura momentaneamente. |
| I (interacoes) | 9 | 3-beat state machine: beat 0 auto (fadeUp + ScrambleText + SplitText words), beat 1 click (ScrambleText "20%" + hero label), beat 2 click (blackout + SplitText chars verdict). 2 click reveals (< Cowan 4±1). Advance/retreat com cleanup completo. |
| D (dados) | 9 | 9 dados Tier 1 verificados: VITALITY PMID 40268307, Bojcic PMID 37931822, INSPECT-SR PMID 40349737, Possamai PMID 40163084, Guyatt PMID 39218429, Wiener MA PMID 18728267, NICE-SUGAR PMID 19318384, Griesdale MA PMID 19318387, Ioannidis PMID 27620683 |
| A (acessibilidade) | 7 | Beat 0/1: todos pares >= 9.05:1 (AAA). Source-tag 5.32:1 (AA — padrão cross-slide). **Verdict 3.67:1 — AA-lg PASS mas abaixo do threshold projector (7:1).** Ghosted elements (beat 2 opacity 0.04) são intencionais, não precisam ser legíveis. Failsafes .no-js presentes. |
| L (carga cognitiva) | 9 | 3 beats × 1-2 elementos cada = within Cowan 4±1 por estado. Beat 0: 1 número + 1 parágrafo (2 chunks). Beat 1: 1 número + 1 label (2 chunks). Beat 2: 1 bloco verdict (1 chunk). Progressive disclosure via state machine. |
| P (andragogia) | 7 | NICE-SUGAR cria "isso afeta MEUS pacientes" (Knowles: relevância para prática). Dados enquadrados como problema sistêmico que afeta decisões diárias do residente. Hook não ensina (correto) — cria motivação. Score esperado baixo para archetype hook. |
| N (arco narrativo) | 9 | narrativeRole: hook, tensionLevel: 3. Escalação: contaminação → consequência → exemplo concreto. Transição para s-contrato: beat 2 termina com urgência → contrato resolve ansiedade com framework. Thread "diamante de verdade ou de vidro" conecta ao deck inteiro. |

**Gate 3 contrast check (2026-03-19f) — Playwright computed styles + WCAG calculator:**

| Elemento | Cor texto | Cor fundo | Ratio | WCAG | Proj 7:1 |
|----------|-----------|-----------|-------|------|----------|
| hook-vol-number (96px mono) | oklch(12%) --text-primary | oklch(95%) --bg-surface | 13.09:1 | AAA | PASS |
| hook-vol-text (34px serif) | oklch(12%) --text-primary | oklch(95%) --bg-surface | 13.09:1 | AAA | PASS |
| hook-vol-ask (34px secondary) | oklch(25%) --text-secondary | oklch(95%) --bg-surface | 9.05:1 | AAA | PASS |
| hook-hero-value (96px mono) | oklch(12%) --text-primary | oklch(95%) --bg-surface | 13.09:1 | AAA | PASS |
| hook-hero-label (20px sans) | oklch(25%) --text-secondary | oklch(95%) --bg-surface | 9.05:1 | AAA | PASS |
| source-tag (14px sans) | oklch(38%) --text-muted | oklch(95%) --bg-surface | 5.32:1 | AA | FAIL |
| **hook-verdict (40px serif)** | **oklch(12%) --text-on-dark** | **oklch(50%) --danger** | **3.67:1** | **AA-lg** | **FAIL** |

**Issues para QA.4:**
1. **CRITICAL — Verdict contrast (3.67:1):** `color: var(--text-on-dark)` em stage-c resolve para oklch(12%) — texto escuro em fundo vermelho escuro. AA-lg (3:1) passa, mas falha projector threshold (7:1). **Fix proposto:** escurecer bg para oklch(~30% 0.16 25) com texto claro forçado (oklch 95%) via override `#s-hook .hook-verdict { color: oklch(95% 0.005 258); background-color: oklch(30% 0.16 25); }`. Estimativa: ~8-9:1 → PASS projector.
2. **MINOR — Word-break "pacientes":** "6.104 paci / entes" quebra no meio da palavra em 40px @ 1280px. Fix: `6.104&nbsp;pacientes` ou reduzir para "6 mil pacientes".
3. **KNOWN — Source-tag 5.32:1:** Abaixo de 7:1 projector mas consistente cross-slide. Padrão aceito.

**Gate 3 wrapping checks (respondendo pendências anteriores):**
- "1.330" em 96px mono: cabe sem wrap, posicionado upper-left. OK.
- "trials retratados já citados em 3.902 meta-análises" em 22ch: wrap natural em 2 linhas. OK.
- Hero label "das MAs mudam de resultado. 157 guidelines contaminadas" em 30ch: wrap em 2 linhas. OK.
- Verdict em 40px: 3 linhas (1280px) / 2 linhas (1920px). Word-break "paci/entes" — ver issue #2.
- Source-tag 4 autores: cabe em 1 linha (ambas resoluções). OK.
- SplitText chars verdict (91 chars): timing adequado para SplitText reveal.

**Screenshots (2026-03-19f):**
- `qa-screenshots/s-hook/beat0-1280x720.png`, `beat0-1920x1080.png`
- `qa-screenshots/s-hook/beat1-1280x720.png`, `beat1-1920x1080.png`
- `qa-screenshots/s-hook/beat2-1280x720.png`, `beat2-1920x1080.png`

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
