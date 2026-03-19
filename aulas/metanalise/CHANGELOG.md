# CHANGELOG — Meta-analise

> Historico de batches. Append-only (novos no topo). Estado → HANDOFF.md
> Detalhes CSS/HTML: `git show <commit>`. Decisoes relevantes: HANDOFF-ARCHIVE.md.

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
