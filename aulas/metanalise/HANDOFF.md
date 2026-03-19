# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** QA slide-a-slide com visual uplift (beleza + GSAP sofisticado)
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides:** 18/18 no deck (ver _manifest.js). Lint PASS. Orphans: 0.
- **Ancora:** Valgimigli 2025 Lancet (PMID 40902613) — IPD-MA, 7 RCTs, 28.982 pts
- **QA pipeline:** [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa). Gates 1-4: 18/18 PASS. Scorecards 14-dim: 3/18 (F1). DONE: 3/18 (s-title, s-hook, s-contrato).
- **Docs:** narrative v2.4, evidence-db v5.4, blueprint v1.9, reading-list v0.4
- **GSAP plugins:** SplitText + Flip + ScrambleTextPlugin (index.template.html)
- **Prompt Gemini:** v6.0 (docs/prompts/gemini-slide-qa.md)
- **Dark-bg:** 6 slides (ver NOTES.md §dark-bg reference map). Novos slides dark = adicionar ID ao seletor em metanalise.css.
- **HEX navy:** #162032 (decisao Lucas)
- **Reveal.js:** REMOVIDO (ERRO-010)
- **Backlog CSS:** ~40 refs `--on-dark` tokens (funcional, naming misleading). Cleanup futuro.
- **Notion Slides DB:** 18/18 slides sincronizados (2026-03-19). Schema correto: Slide ID, Bloco Narrativo MA-F1/I1/F2/I2/F3, Headline PT/EN, Corpo, Speaker Notes EN, Pipeline Status, pos, tempo, animacao, objetivo, GRADE, PMID, DOI, NNT. Bloqueio anterior resolvido: DB nao precisa de prop Aula separada (relation funciona). Scrips: notion_batch_f2f3.cjs (removido pos-execucao).

## Estado dos Slides (maquina de estados — WT-OPERATING.md)

> Estados: BACKLOG → DRAFT → CONTENT → SYNCED → LINT-PASS → QA → DONE
> Verificar 1 a 1 antes de registrar. Nao assumir.

### F1 — Criar importancia (3 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 1 | s-title | DONE | QA.0-QA.4 PASS. Gemini approved (beauty 9, legibility 10). Choreography + masking. |
| 2 | s-hook | DONE | QA.0-QA.4 PASS. Asymmetric grid, countUp GSAP (decimal support), 14-dim avg 9.36. Gemini drove uplift (c400f5a). |
| 3 | s-contrato | DONE | Watermark-only 35% opacity. Gemini R4 APPROVED + all suggestions applied. Lucas approved. |

### I1 — Checkpoint engajamento (1 slide)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 4 | s-checkpoint-1 | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### F2 — Metodologia (8 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 5 | s-rs-vs-ma | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 6 | s-pico | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 7 | s-abstract | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 8 | s-forest-plot | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 9 | s-benefit-harm | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 10 | s-grade | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 11 | s-heterogeneity | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 12 | s-fixed-random | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### I2 — Checkpoint consolidacao (1 slide)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 13 | s-checkpoint-2 | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### F3 — Aplicacao Valgimigli (5 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 14 | s-ancora | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 15 | s-aplicacao | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 16 | s-aplicabilidade | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 17 | s-absoluto | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 18 | s-takehome | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### Resumo

- **DONE (3):** s-title, s-hook, s-contrato — QA full (Opus + Gemini) completo
- **LINT-PASS (15):** restantes — scorecard 14-dim pendente

---

## Histórico

Trabalho completado e decisões tomadas: ver [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)

## Caminho crítico — próximas sessões

### Sessão N+1 (imediata) — QA slide-a-slide com visual uplift
1. **Hardening documental R1+R2+R3 DONE (2026-03-19):** R1 (-903 linhas, XREF rebuilt). R2: MEMORY.md 5 fixes, blueprint v1.9 (stale hook assertion), lessons +3, .gitignore fix. R3: Notion 18 slides synced (Bloco Narrativo MA-*), evidence-db v5.4 (PMID audit: 36 verificados, 2 corrigidos, 1 DOI fix), HANDOFF pendencias 3/5 falsas (verificadas OK).
2. **Pipeline normal** (WT-OPERATING.md §4): proximo slide na fila → QA.0-QA.4 → DONE → proximo.
   - Criterios visuais elevados: beleza avançada + GSAP sofisticado (SplitText, Flip, ScrambleText, custom choreographies)
   - Gemini prompt v6.0 (scorecard 10-dim, 10 lenses, 5 personas, radical ideas forcing, projected scorecard, temp 1.0)
   - Contexto sala: pequena, ~15 pessoas, 1-4m, iluminacao forte, TV LED — legibilidade constraint #1
3. **Dark-bg reference** (sugestao, decide-se por slide):
   - Ja dark: s-checkpoint-1, s-checkpoint-2
   - Propostos dark: s-forest-plot, s-heterogeneity, s-ancora, s-absoluto (CSS pronto)
   - Light: demais (s-rs-vs-ma, s-pico, s-abstract, s-benefit-harm, s-grade, s-fixed-random, s-aplicacao, s-aplicabilidade, s-takehome)
4. **Ordem:** s-checkpoint-1 → F2 em sequencia (F1 completo: s-title, s-hook, s-contrato DONE)

### Sessão N+2
- Fase 4 (Gemini deck-level — este sim em batches)
- Build de producao (`npm run build:metanalise`)
- Merge para main

### Opcional — Merge cirrose→main
- Plano pronto (ver conversa anterior). Elimina WT cirrose permanentemente.
- Sequência: push cirrose → merge --no-ff em main (ALLOW_MAIN_CONTENT=1) → remover WT → atualizar hooks → push

## Bloqueios conhecidos

| Bloqueio | Impacto | Workaround |
|----------|---------|------------|
| Cochrane exemplos visuais | Forest plots e GRADE tables reais precisam de screenshots/crops | Acessar via CAPES e cropar quando iniciar QA visual |

## Pendências para main (Classe B — não editar na WT)

- **lint-slides.js false positive:** `scripts/lint-slides.js:110` — `data-animate="countUp"` sem `data-target` não pula `<script>` blocks. 2 false positives no index.html built. **Fix preparado:** context-aware check (3 linhas antes/depois). Aplicar em main.
- **Scripts orphans (main):** `scripts/attention-insight.js`, `scripts/mcp-attention-insight.js`, `scripts/act1-surgical-qa.mjs`, `scripts/act1-reaudit.mjs` — **confirmed orphan** pelo repo-janitor (2026-03-19). `git rm` preparado.

## Não fazer ainda

- Não tocar em Cirrose
- Não expandir para NMA, IPD, bayesiana
- Não fazer build de producao antes de QA visual completo

> Sessoes anteriores (2026-03-14 a 2026-03-18): [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)
