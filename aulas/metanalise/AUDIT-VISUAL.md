# AUDIT-VISUAL — Meta-análise

> Scorecard por slide. 14 dimensões. Atualizado a cada QA pass.
> Pendente: audit final Gemini (Gate 4) para todas as dims.
> Pipeline: ver [QA-WORKFLOW.md](QA-WORKFLOW.md)

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

---

## s-hook (01-hook.html)

**Status:** PASS (QA slide-a-slide 2026-03-16e)
**Archetype:** hook — dims E, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Pergunta > números (hero 81%) > verdict > source |
| T (tipografia) | 9 | Serif italic provocação, mono números, sans verdict |
| E (layout fill) | 5 | ~50% — intencional para hook (respiro dramático) |
| C (cor/contraste) | 9 | Tokens light-mode, verdict em --ui-accent |
| V (visuais) | 8 | 3 countUp hero numbers — impacto |
| K (consistência) | 9 | Padrão hook |
| S (sofisticação) | 9 | Limpo, dramático, source-tag no rodapé |
| M (comunicação) | 9 | Provocação → dados → punchline — arco completo |
| I (interações) | 9 | 2-beat state machine (beat0 auto, beat1 click) |
| D (dados) | 9 | 3 dados Tier 1 verificados + PMID (ERRO-003 corrigido) |
| A (acessibilidade) | 8 | Bom contraste, labels uppercase legíveis |
| L (carga cognitiva) | 9 | 3 dados + 1 verdict = dentro do 4±1 |
| P (andragogia) | 8 | Retrieval practice (pergunta antes de resposta) |
| N (arco narrativo) | 9 | Hook forte, cria tensão para Fase 1 |

**Fixes aplicados:**
- ERRO-003 corrigido: 88%→81% (Bojcic 2024), 8.5%→10% (Qureshi 2025)
- Especificidade `#deck p` corrigida (question text era 20px, agora --text-h2)
- Tokens: bulk fix --text-on-dark → --text-primary/secondary em TODO o CSS
- Labels encurtadas para fit horizontal
- Source-tag movida para .slide-inner (fora de .hook-question)
- Verdict em --ui-accent (cor sutil de ênfase)
- Source-tag centering fix: `#deck p.source-tag` com `max-width: none; width: 100%` (vence `.stage-c #deck p` de base.css)
- Texto beat-0: "publicadas hoje" → "por dia — só em 2019" (dado Hoffmann é de 2019, hoje >140/dia)
- Label "SRs por dia" → "SRs/dia em 2021" (contexto temporal)
- Speaker notes atualizadas (crescimento 80→146/dia entre 2019→2021)

**Pendências para audit Gemini (Gate 4):**
- Sufixo % nos números (81%, 10%) — avaliar se precisa de tratamento tipográfico (% menor)
- Distribuição vertical no fullscreen — validar em projetor real
- Beat 0 sozinho — avaliar impacto dramático do texto isolado antes do click
- Labels "CRITICAMENTE BAIXAS" e "GUIDELINES COM LOE FORTE" — legibilidade em projetor
- **Instrument Serif italic** na provocação (beat-0) — confirmar legibilidade em TV/projetor a 5m em sala iluminada. Se ilegível, fallback para DM Sans 600 italic
- "só em 2019" como qualificador — avaliar se enfraquece o impacto dramático ou se reforça (implica crescimento)

**Pendências operacionais:**
- Sync Notion References DB: Bojcic e Qureshi mudar de CANDIDATO → EM USO
- narrative.md atualizado (dados do hook)
- evidence-db.md atualizado (Bojcic/Qureshi: CANDIDATO → EM USO)

---

## s-contrato (02-contrato.html)

**Status:** PASS (QA 14-dim 2026-03-17b — re-audit com screenshots Playwright)
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
