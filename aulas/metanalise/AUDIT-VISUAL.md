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

**Status:** PASS (re-audit 2026-03-18 — Playwright + contraste + fixes)
**Archetype:** title — dims E, M, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | h1 56px 600 > subtitle 20px secondary > pillars 20px uppercase 500 > author 20px primary > affil 16px muted — 5 niveis claros |
| T (tipografia) | 8 | DM Sans throughout (stage-c override). 4 tratamentos: hero 56/600, body 20, uppercase tracking, small 16 muted. Serif indisponivel em stage-c (shared/ READ-ONLY) |
| E (layout fill) | 4 | ~30% — intencional para title |
| C (cor/contraste) | 9 | h1 17.6:1, subtitle 13.8:1, author 17.6:1, affil 8.6:1 — todos AAA. Verificado via Playwright+a11y |
| V (visuais) | 7 | Sem visual dominante — OK para title |
| K (consistência) | 9 | Padrao de capa. Pillars ecoam s-contrato |
| S (sofisticação) | 9 | data-animate declarativo. Failsafes .no-js e print. Sem AI markers. Divider funcional (separador autor) |
| M (comunicação) | 5 | h1 = rotulo — correto para archetype |
| I (interações) | 7 | fadeUp subtitle + stagger pillars + fadeUp identity. Declarativo. QA mode OK |
| D (dados) | N/A | Title — sem dados clinicos |
| A (acessibilidade) | 9 | Axe-core 0 violations. aria-hidden nos dots. Todos pares ≥ 8.6:1 |
| L (carga cognitiva) | 9 | Minimo — titulo + 3 palavras |
| P (andragogia) | 6 | Sem decisao clinica — esperado. Pillars = orientacao framework |
| N (arco narrativo) | 8 | Abertura limpa. Pillars (Perguntar/Estimar/Decidir) mapeiam 3 fases |

**Fixes aplicados (2026-03-18):**
- h1 font-size: 38px → 56px (specificity `#deck .slide-title h1` vence `#deck h1`)
- Author color: --text-secondary → --text-primary (specificity `#deck .title-author` vence `#deck p`)
- Affiliation color: --text-secondary → --text-muted (specificity `#deck .title-affiliation` vence `#deck p`)

**Fixes anteriores (2026-03-16e/17):** tokens on-dark → light-mode. Pilares 400→500. data-background-color removido.

**Pendencias para Gemini (Gate 4):**
- Title divider — AI marker ou separador funcional?
- Fill ratio ~30% — adequado para projecao?
- DM Sans 600 no h1 (stage-c) vs Instrument Serif (design-system) — confirmar legibilidade a 5m
- Author weight 450 (stage-c `#deck p` override) vs 500 intencional — diferenca visivel?

**Screenshots:** `qa-screenshots/s-title/S0.png` (1280x720), `qa-screenshots/s-title/S0-fullscreen.png` (1920x1080). Anteriores: `qa-screenshots/s00-title-qa.png` (pre-fix), `qa-screenshots/s00-title-fix2-qa.png` (pos-fix)

---

## s-hook (01-hook.html)

**Status:** PASS (re-audit 2026-03-18 — Playwright + contraste verificado)
**Archetype:** hook — dims E, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Question 34px italic serif > Values 34-38px mono 600 > Labels 14px uppercase > Verdict 20px accent > Source 14px muted. 81% hero (38px) = Von Restorff |
| T (tipografia) | 9 | 3 familias: Instrument Serif italic (question), JetBrains Mono 600 (numeros), DM Sans (labels/verdict). Excelente contraste tipografico |
| E (layout fill) | 5 | ~50% — intencional para hook (respiro dramatico) |
| C (cor/contraste) | 9 | Question 17.6:1, Values 17.6:1, Labels 13.8:1, Verdict 10.0:1, Source 8.6:1. Todos ≥ 7:1. Verificado via a11y-contrast |
| V (visuais) | 8 | 3 countUp hero numbers — impacto. 81% hero size |
| K (consistência) | 9 | Padrao hook |
| S (sofisticação) | 9 | 2-beat state machine declarativa. .no-js + print fallbacks. Sem AI markers |
| M (comunicação) | 9 | Provocacao → dados → punchline — arco completo em 1 slide |
| I (interações) | 9 | 2-beat state machine (beat0 auto fadeUp, beat1 click reveal + countUp). QA mode: beats forcados via JS (engine.js nao seta [data-qa] — pendencia main) |
| D (dados) | 9 | 3 dados Tier 1 verificados: Hoffmann PMID 34091022, Bojcic PMID 37931822, Qureshi PMID 41428154 |
| A (acessibilidade) | 9 | Todos contrastes ≥ 8.6:1. Axe-core 0 violations. Labels uppercase legiveis |
| L (carga cognitiva) | 9 | 3 dados + 1 verdict = dentro do 4±1 Cowan |
| P (andragogia) | 8 | Retrieval practice (pergunta antes de resposta) |
| N (arco narrativo) | 9 | Hook forte, cria tensao para Fase 1 |

**Fixes aplicados (sessoes anteriores):**
- ERRO-003 corrigido: 88%→81% (Bojcic 2024), 8.5%→10% (Qureshi 2025)
- Especificidade `#deck p` corrigida (question text era 20px, agora --text-h2)
- Tokens: bulk fix --text-on-dark → --text-primary/secondary
- Source-tag centering fix: `#deck p.source-tag` com `max-width: none; width: 100%`

**Fix aplicado (2026-03-18):**
- CSS `[data-qa]` selectors adicionados para `.hook-beat-0`, `.hook-beat-1`, `.hook-verdict` (paridade com checkpoint). Pendente: engine.js setar `[data-qa]` no body (fix para main/shared)

**Pendencias para Gemini (Gate 4):**
- Instrument Serif italic na provocacao — legibilidade a 5m em sala iluminada?
- Labels uppercase 14px ("CRITICAMENTE BAIXAS") — legibilidade em projetor?
- Sufixo % nos numeros — tratamento tipografico?
- Distribuicao vertical — validar em projecao real
- margin-top 80px no verdict — gap adequado?

**Pendencias operacionais:** ✅ TODAS RESOLVIDAS (verificado 2026-03-17)

**Screenshots:** `qa-screenshots/s01-hook-final.png` (estado final forcado via Playwright)
- ~~Sync Notion References DB: Bojcic e Qureshi mudar de CANDIDATO → EM USO~~ ✅ Notion sync feito (2026-03-16i, timestamp 23:16). Bojcic highlight confirma "EM USO no hook".
- ~~narrative.md atualizado (dados do hook)~~ ✅ Linha 51: 146/dia, Bojcic 81%, Qureshi 10%
- ~~evidence-db.md atualizado (Bojcic/Qureshi: CANDIDATO → EM USO)~~ ✅ v4.1 (linhas 126, 137)

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
