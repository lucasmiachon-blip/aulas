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

#### DONE nesta sessão (03-21b)
- Notion sync completo: 4 slides + 9 references
- 5 PMIDs corrigidos via PubMed MCP (ERRO-011). evidence-db v5.7
- Mapa de fontes para retórica documentado (HANDOFF §Mapa de fontes)
- ERROR-LOG, CHANGELOG, lessons.md atualizados

#### Pipeline QA (caminho crítico)
Proximo: s-checkpoint-1 (screenshots + scorecard 14-dim) → F2 em sequencia.
- Criterios visuais elevados: beleza avancada + GSAP sofisticado
- Gemini prompt v6.0 (10-dim, 5 personas, radical ideas forcing, temp 1.0)
- Contexto sala: pequena, ~15 pessoas, 1-4m, iluminacao forte, TV LED — legibilidade constraint #1

#### Dark-bg reference (decide-se por slide)
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

## Mapa de fontes — retórica e conhecimento

> Onde buscar informação para preparar a aula, responder arguição, e enriquecer slides.

### Fontes internas (repo)

| Fonte | Conteúdo | Quando usar |
|-------|----------|-------------|
| `references/evidence-db.md` | Todos dados clínicos verificados, PMIDs, números, Scite tallies | **Fonte canônica** para qualquer número em slide ou notes. Verificar aqui PRIMEIRO |
| `references/research-accord-valgimigli.md` | Briefing narrativo ACCORD + Valgimigli (3 partes) + PDFs para NotebookLM | Prep arguição, entender contexto profundo dos 2 papers-âncora |
| `references/narrative.md` | Arco narrativo, beats de tensão, papel de cada slide | Entender POR QUE cada slide existe, qual o punchline |
| `references/blueprint.md` | Mapa slide-a-slide com evidências associadas | Visão global: qual slide cobre qual conceito |
| `references/reading-list.md` | Pre-reading recomendado (4 papers) | Antes de começar a preparar a apresentação |
| Speaker notes nos slides | Script retórico com timing [0:00-0:30] | Durante ensaio e apresentação. Inclui pausas, perguntas, ênfases |
| `references/archetypes.md` | 6 layout patterns visuais | Referência de design ao criar/revisar slides |

### Fontes externas (MCPs — verificação e aprofundamento)

| MCP | O que faz | Quando usar | Auth |
|-----|-----------|-------------|------|
| **PubMed** | Metadata de artigos, busca por autor/título, verificação PMID | Verificar QUALQUER PMID antes de usar. Buscar papers novos | Sem auth |
| **Scite** | Citation tallies (supporting/contrasting/mentioning), smart citations | Quanto um paper é contestado? Quem o apoia/questiona? | OAuth premium |
| **Perplexity** | Respostas rápidas com citações, pesquisa profunda | "O que sabemos sobre X?" — factos rápidos, estado da arte | API key |
| **Consensus** | Consenso da literatura sobre uma pergunta | "A evidência apoia X?" — visão quantitativa do campo | OAuth |
| **Scholar Gateway** | Busca semântica em literatura | Busca exploratória por conceito (não por autor/PMID) | Sem auth |

### Fontes externas (fora MCPs)

| Fonte | O que faz | Quando usar |
|-------|-----------|-------------|
| **NotebookLM** | Q&A grounded em full-text de papers carregados | Perguntas profundas sobre um paper específico (ex: "qual foi a análise de sensibilidade do ACCORD?") |
| **CAPES/USP** | Acesso a PDFs completos | Quando precisa ler o paper inteiro, cropar forest plots |
| **Cochrane Library** | SRs exemplares, GRADE tables, forest plots | Exemplos visuais para slides de metodologia (F2) |

### Fluxo de prep retórica (sugerido)

1. **Ler** `narrative.md` → entender o arco (por que esta ordem?)
2. **Ler** `evidence-db.md` → dominar os números (vão te perguntar)
3. **Ler** `research-accord-valgimigli.md` → contexto profundo dos 2 papers-âncora
4. **Ensaiar** com speaker notes dos slides (timing real)
5. **Se pergunta surgir** → Perplexity (rápido) ou PubMed+Scite (verificado)
6. **Se dado contestado** → Scite tallies (quantos suportam vs questionam)
7. **Se precisar aprofundar** → NotebookLM (Q&A grounded no full-text)

---

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
