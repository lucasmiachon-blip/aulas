# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** QA slide-a-slide com visual uplift (beleza + GSAP sofisticado)
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides:** 18/18 no deck (ver _manifest.js). Lint PASS. Orphans: 0.
- **Ancora:** Valgimigli 2025 Lancet (PMID 40902613) — IPD-MA, 7 RCTs, 28.982 pts
- **QA pipeline:** [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa). Gates 1-4: 18/18 PASS. Scorecards 14-dim: 3/18 (F1). DONE: 3/18 (s-title, s-hook, s-contrato).
- **Docs:** narrative v2.5, evidence-db v5.7, blueprint v2.0, reading-list v0.4, research-accord-valgimigli v1.0
- **GSAP plugins:** SplitText + Flip + ScrambleTextPlugin (index.template.html)
- **Gemini:** CLI headless (`scripts/gemini.mjs`, model `gemini-3.1-pro-preview`). Prompt v6.0 (`docs/prompts/gemini-slide-qa.md`). Output: `.audit/{id}_result.json`.
- **Dark-bg:** 6 slides (ver NOTES.md §dark-bg reference map). Novos slides dark = adicionar ID ao seletor em metanalise.css.
- **HEX navy:** #162032 (decisao Lucas)
- **Reveal.js:** REMOVIDO (ERRO-010)
- **Backlog CSS:** ~40 refs `--on-dark` tokens (funcional, naming misleading). Cleanup futuro.
- **Notion Slides DB:** 18/18 slides sincronizados (2026-03-21). 4 slides atualizados (Speaker Notes EN): s-checkpoint-1, s-ancora, s-aplicacao, s-aplicabilidade.
- **Notion References DB:** 9 papers criados (2026-03-21): ACCORD 2008, Ray 2009, ACCORD 5yr, ACCORD 9yr, VADT 15yr, Riddle 2010, Bonds 2010, Giacoppo 2025, Valgimigli reply 2026. 5 PMIDs corrigidos via PubMed MCP.

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
| 4 | s-checkpoint-1 | QA | Reescrito com ACCORD trap (Ray 2009 + ACCORD 2008). 3-beat liquidificador. Build+lint PASS. Slide-punch 6/6 PASS (ENCAIXADO). Notes enriquecidas com NNH 95, paradoxo A1C, follow-ups, 4 hipoteses. Scorecard 14-dim + screenshots pendentes. |

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
| 14 | s-ancora | LINT-PASS | Gates 1-4 PASS. Notes enriquecidas: 7 RCTs nomeados, modelo IPD, Scite status, Giacoppo BMJ. Scorecard 14-dim pendente. |
| 15 | s-aplicacao | LINT-PASS | Gates 1-4 PASS. Notes enriquecidas: NICE gap, custo, lacuna GRADE. Scorecard 14-dim pendente. |
| 16 | s-aplicabilidade | LINT-PASS | Gates 1-4 PASS. Notes enriquecidas: CYP2C19, generalizacao geografica. Scorecard 14-dim pendente. |
| 17 | s-absoluto | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 18 | s-takehome | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### Resumo

- **DONE (3):** s-title, s-hook, s-contrato — QA full (Opus + Gemini) completo
- **QA (1):** s-checkpoint-1 — reescrito ACCORD, slide-punch PASS, screenshots pendentes
- **LINT-PASS (14):** restantes — scorecard 14-dim pendente

---

## Histórico

Trabalho completado e decisões tomadas: ver [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)

## Caminho crítico — próximas sessões

### Sessão N+1 (imediata) — QA s-checkpoint-1 + F2

#### 1. MCPs acadêmicos — DONE (2026-03-21)
- Scite, Perplexity, Consensus: todos funcionando e testados
- Buscas realizadas: Scite tallies ACCORD (7.335/2.399), Ray (1.318/889), Valgimigli (não indexado)
- evidence-db v5.6: NNH 95, paradoxo A1C, follow-ups, 7 RCTs, CYP2C19, Giacoppo
- research-accord-valgimigli.md: briefing narrativo completo + PDFs para NotebookLM
- Notes de s-checkpoint-1, s-ancora, s-aplicacao, s-aplicabilidade enriquecidas

#### 2. Pipeline QA (caminho crítico)
Proximo: s-checkpoint-1 (screenshots + scorecard 14-dim) → F2 em sequencia.
- Criterios visuais elevados: beleza avancada + GSAP sofisticado
- Gemini prompt v6.0 (10-dim, 5 personas, radical ideas forcing, temp 1.0)
- Contexto sala: pequena, ~15 pessoas, 1-4m, iluminacao forte, TV LED — legibilidade constraint #1

#### 4. Dark-bg reference (decide-se por slide)
- Ja dark: s-checkpoint-1, s-checkpoint-2
- Propostos dark: s-forest-plot, s-heterogeneity, s-ancora, s-absoluto (CSS pronto)
- Light: demais

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
- **3 orphan scripts:** `scripts/browser-qa-act1.mjs`, `scripts/vote-final-qa.mjs`, `scripts/qa/qa-static.js` — zero refs, remover em main.

## Não fazer ainda

- Não tocar em Cirrose
- Não expandir para NMA, IPD, bayesiana
- Não fazer build de producao antes de QA visual completo

> Sessoes anteriores (2026-03-14 a 2026-03-21): [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)
