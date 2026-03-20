# CHANGELOG — Meta-analise

> Historico de batches. Append-only (novos no topo). Estado → HANDOFF.md
> Detalhes CSS/HTML: `git show <commit>`. Decisoes relevantes: HANDOFF-ARCHIVE.md.

---

## 2026-03-20c — qa-video.js 3 bug fixes (deck.js compat)

### Fixes (scripts/qa/qa-video.js)
- **FRAMEWORK invertido:** cirrose removido da condição Reveal.js — só grade/osteoporose são Reveal legacy
- **goToSlide broken:** `window.deck.goTo()` não existe (ESM puro). Substituído por DOM manipulation (slide-active swap + dispatch slide:changed/slide:entered)
- **getRevealCount classe errada:** `section.active` → `section.slide-active` (classe real do deck.js)

### Verificação
- `grep "window.deck"` → 0 matches
- `grep "slide-active"` → 4 matches (correto)
- `--aula=metanalise` → FRAMEWORK=deck, `--aula=grade` → FRAMEWORK=reveal

---

## 2026-03-20b — s-checkpoint-1 ACCORD rewrite + research deep dive

### Slide rewrite
- `03-checkpoint-1.html`: reescrito inteiro — ACCORD trap com dados reais (Ray 2009 PMID 19465231, ACCORD 2008 PMID 18539917)
- Visual "liquidificador": diamante simplificado dissolve → 4 trial markers (UKPDS, ADVANCE, VADT, ACCORD em danger)
- 3-beat state machine: cenário (auto) → pergunta (click) → twist ACCORD (click)
- `metanalise.css`: +110 linhas (`.ck1-*` classes, forest visual, trial positions, failsafes)
- `slide-registry.js`: handler reescrito (diamond fade, trial stagger, ACCORD emphasis)
- `_manifest.js`: headline atualizada

### Docs
- `narrative.md` v2.5: I1 reescrito com ACCORD, visual liquidificador, changelog
- `evidence-db.md` v5.5: seção "Checkpoint 1 — ACCORD trap" com tabelas Ray/ACCORD
- `blueprint.md` v2.0: slide 03 atualizado (evidência, status, nota dados reais)

### Verificação
- Build: 18 slides OK. Lint: clean. Integrity: 18/18 match. Narrative-sync: 0 errors.
- Slide-punch: 6/6 PASS, veredicto ENCAIXADO.

### Research — arguição prep
- Deep research: MAs controle glicêmico intensivo 2009-2024. 10 papers verificados.
- Achado: **ZERO** fizeram GRADE formal (Ray, CONTROL, Boussageon, Hemmingsen Cochrane, Kunutsor 2024)
- Boussageon 2011 (PMID 21791495): NNT 117-150 (IAM) vs NNH 15-52 (hipoglicemia). Crítica mais forte.
- Kunutsor 2024 (PMID 38409644): update 51.469 pts — IAM reduzido, MACE NS, sem GRADE.
- Scite tallies Ray 2009: 889 citações (23 supporting, 5 contrasting, 806 mentioning)
- Tese/antítese/síntese preparada para arguição + 6 perguntas de banca com respostas

### Infra
- `.mcp.json`: Scite MCP adicionado (streamableHttp → api.scite.ai/mcp). Perplexity: config OK, API key pendente.

---

## 2026-03-20a — Gemini CLI headless migration (5 items)

Commits: `b496462`, `38599cf`

- `scripts/gemini.mjs`: rewrite — model `gemini-3.1-pro-preview`, multimodal (--png/--mp4), auto-save `.audit/`, template loading from `docs/prompts/gemini-slide-qa.md`
- `scripts/qa/qa-video.js`: deck.js support (`--aula=metanalise`), framework auto-detect, 15s max recording, BASE_URL parametrizado
- `.audit/`: diretorio criado (.gitkeep tracked, *.json gitignored)
- `WT-OPERATING.md` §4 QA.3: CLI invocation, WebM/MP4 codec limitation documented
- `CLAUDE.md` (aula): secao "Auditoria Visual — Gemini CLI" adicionada
- MCP Gemini: **zero** referencias em .mcp.json ou .mcp-profiles/. Acesso exclusivo via CLI.

---

## 2026-03-19j — Doc hardening session: PMIDs, lessons reorg, ERROR clusters, QA template

- **Batch 1:** Siedler PMID 40969451 verified + framing corrected. Higgins DOI verified. Gemini model discrepancy documented. evidence-db v5.3, blueprint v1.9.
- **Batch 2:** lessons.md reorganized by scope (9 sections). HANDOFF cleaned (stale items removed). ERROR-LOG: 3 error clusters extracted. AUDIT-VISUAL: scorecard template + 15-slide QA queue.

---

## 2026-03-19i — s-hook QA UPLIFT: asymmetric layout, countUp, editorial typography

Commit: `c400f5a` · QA.0-QA.2 PASS (14 dims >=9, contraste AAA 8.61-17.58:1)

Gemini-driven: 3 cards iguais → grid assimétrico "fenômeno vs realidade" (1fr/auto/1fr). Números isolados de affixes (96/72px mono). GSAP custom timeline (countUp + stagger + divider scaleY). Tags AMSTAR-2/GRADE como pills. Cor danger REJEITADA (violaria semântica). Layout "Trust Blackout" simplificado para timeline sequencial.

---

## 2026-03-19h — s-hook REWRITE: sober 3-card metrics

Commit: `edb2e2f`

Lucas rejeitou tom alarmista (VITALITY "1.330 retratados", UTI, verdict vermelho). Novo: 3 metric cards sober (~80/dia, 81% AMSTAR-2, 33.8% GRADE). State machine inteira removida (-117 linhas registry, -132 linhas CSS). `data-animate="stagger"` declarativo. Scorecard anterior invalidado.

---

## 2026-03-19g — Gemini prompt v4.0 → v6.0

Prompt reescrito absorvendo cirrose v6: 5 personas (was 3), scorecard numérico 10 dimensões, 10 lenses granulares, 8 steps, temperature 1.0 + topP 0.95. Output schema rígido com 6 seções obrigatórias.

---

## 2026-03-19f — s-hook Gate 3 scorecard + QA.4 fixes

14-dim scorecard: avg 8.6. Verdict contrast 3.67→7.78:1 (explicit oklch override, bypasses stage-c remap). SplitText word-break fix (`type: 'words,chars'`). Root cause: stage-c remaps `--text-on-dark` to dark text.

---

## 2026-03-19e — s-hook content rewrite: VITALITY backbone

Beat 0: "1.330 trials retratados → 3.902 MAs" (VITALITY BMJ 2025). Beat 1: "20% mudam resultado, 157 guidelines". Beat 2: NICE-SUGAR chain (Wiener → NICE-SUGAR → Griesdale). evidence-db v5.1: +8 refs verificadas. reading-list v0.4: +3 pre-reading.

---

## 2026-03-19d — Hardening documental + GSAP toolkit

Flip + ScrambleTextPlugin importados em index.template.html. Gemini prompt v3.0→v4.0 (CoT 5-step, code-grounded API table, few-shot, self-critique). `references/archetypes.md` criado (6 layout patterns extraídos de 18 slides).

---

## 2026-03-19c — Visual uplift pre-work (infra + prompt v3.0)

SplitText importado. Dark-bg CSS consolidado: 2→6 slides (#162032 + 8 on-dark overrides). Gemini prompt v3.0 (role priming, CoT 4 dimensões, exploration mandate GSAP).

---

## 2026-03-19b — s-hook Gemini materials captured

Screenshots 3 beats + vídeo .webm (413KB) para QA.3 Gemini.

---

## 2026-03-19a — Reveal.js purge + Vite cache fix

Root cause: Vite cache poisoning (Reveal.js pre-bundled de grade/osteoporose → `section { display: none }`). Fix: Reveal removido de dependencies, FROZEN_AULAS excluídas de discoverEntries().

---

## 2026-03-18e — s-hook v4 (grid + blackout + brutalismo)

Grid 2-col assimétrico (Z-pattern). Beat 2 blackout (opacity 0.12). Verdict brutalismo (--danger bg, Instrument Serif italic). Gemini: beauty 6.5, legibility 9.0 (ITERATE).

---

## 2026-03-18d — s-hook refactor (hero 41%)

3-column grid → hero number (41% Windish). Trials concretos (TRH, rosiglitazona, glicemia intensiva, 396 reversões). evidence-db v5.0: +6 refs. QA.0-QA.2 PASS (14 dims >=8, hero 14.15:1 AAA).

---

## 2026-03-18c — s-title QA.3-QA.4 (Gemini approved)

Gemini 2 rounds → beauty 9/10, legibility 10/10, approved. Custom choreography: h1→subtitle→pillars(masking)→dots→identity. Inverted weight hierarchy (h1 400/64px, subtitle 600/20px uppercase).

---

## 2026-03-18 — QA + specificity fixes + merge main

Specificity fixes (#deck selectors). QA s-title QA.0-2 PASS (AAA). Merge main: 4 commits A/B (medical-researcher, final-pass v3, slide-punch, new-skill v2).

---

## Entries 2026-03-17 (colapsados)

| Data | Resumo |
|------|--------|
| 03-17h | Verificação documental: XREF +8 files metanalise, README +WT-OPERATING, CLAUDE.md root status |
| 03-17g | Doc sync: 6 inconsistências factuais corrigidas, 302 linhas cortadas (blueprint/evidence-db/narrative/HANDOFF) |
| 03-17f | WT-OPERATING.md criado (maquina de estados + QA 5-stage). QA-WORKFLOW.md → DEPRECATED |
| 03-17e | MCPs racionalizados: .mcp.json 5→7 servers, 14 removidos (built-ins), ECOSYSTEM.md reescrito |
| 03-17d | HTML cleanup: data-background-color removido 17/18, slide-navy removido 16/18. ERRO-009 |
| 03-17c | QA-WORKFLOW.md reescrito como doc executável (4-gate, template scorecard) |
| 03-17b | QA s-contrato visual fix: flex:1 removido, cards 550→248px, contraste 8.8:1, scorecard re-scored |
| 03-17 | QA s-contrato: h2 assertivo, scope footer removido, slide-navy/data-background-color limpos, scorecard 14-dim PASS |

---

## Entradas anteriores (2026-03-13 a 2026-03-16)

> Arquivadas em [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md).
