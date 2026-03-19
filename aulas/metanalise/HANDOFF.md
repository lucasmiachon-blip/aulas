# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** QA slide-a-slide com **visual uplift** (beleza avançada + GSAP sofisticado). s-title DONE (Gemini). s-hook screenshots+video capturados, Gemini re-eval pendente. Prompt Gemini v3.0 pronto (docs/prompts/gemini-slide-qa.md). Pre-work infra: SplitText importado, dark-bg CSS consolidado (6 slides).
- **HTML cleanup (2026-03-17d):** `data-background-color` removido de 17/18 slides (todos — deck.js ignora). `slide-navy` removido de 16/18 slides light (mantido em CP1+CP2 que TEM bg navy via CSS override). ERRO-009 documentado.
- **QA pipeline:** ver [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa). Gates 1-4: 18/18 PASS. Scorecards formais 14-dim: 3/18 (F1). s-title QA.0-QA.4 PASS (Gemini approved). s-hook QA.0-QA.2 PASS, QA.3 screenshots+video capturados, QA.4 Gemini pendente (materiais prontos). Fase 3 (dynamic): 3 pendentes (hook, CP1, CP2). Fase 4 (Gemini): s-title done, s-hook materiais prontos, demais pendentes.
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides no index.html:** 18 (00-title → 01-hook → 02-contrato → 03-checkpoint-1 → 04-rs-vs-ma → 05-pico → 06-abstract → 07-forest-plot → 08-benefit-harm → 09-grade → 10-heterogeneity → 11-fixed-random → 12-checkpoint-2 → 13-ancora → 14-aplicacao → 15-aplicabilidade → 16-absoluto → 17-takehome)
- **Slides planejados:** 18 (00-17) — ver blueprint.md v1.8
- **Docs fundacionais:** narrative.md (v2.2), evidence-db.md (v5.0 — 26+ refs, hook refs adicionadas), blueprint.md (v1.8), reading-list.md (v0.3)
- **_manifest.js:** CRIADO — 18 slides, fases F1/I1/F2/I2/F3
- **slide-registry.js:** CRIADO — state machines para title (choreography), hook (2-beat: countUp + blackout/verdict), checkpoint-1 (3-beat), checkpoint-2 (4-beat). SplitText disponível globalmente (registrado em index.template.html)
- **Orphan slides:** 0
- **Orphan CSS:** 0
- **Artigo âncora:** ✅ Valgimigli 2025, Clopidogrel vs Aspirina (Lancet, PMID 40902613). IPD-MA, 7 RCTs, 28.982 pts
- **lint:slides:** ✅ PASS (zero FAILs)
- **HEX navy:** #162032 mantido (decisao Lucas — consistencia cross-aula)
- **CSS overrides em metanalise.css vs base.css:** `justify-content: center` restaurado + pseudo-elements desativados (ERRO-005). Checkpoint safe-center pattern proprio (ERRO-006). CSS zoom REMOVIDO — deck.js scale() é o mecanismo correto (ERRO-008). Fixed px tokens mantidos para evitar vw double-scaling. Hook v4: grid assimétrico 2-col (Z-pattern), `.hook-vol-number` 72px mono, verdict brutalismo (`--danger`, border-radius:0), blackout beat 2. Dead CSS removido. **Dark-bg consolidado:** seletor compartilhado para 6 slides (`#s-checkpoint-1/2, #s-forest-plot, #s-heterogeneity, #s-ancora, #s-absoluto`) com `background-color: #162032` + 8 on-dark tokens restaurados. Novos slides dark = adicionar ID ao seletor.
- **Reveal.js:** REMOVIDO desta WT. `package.json` sem reveal, `vite.config.js` exclui frozen aulas (ERRO-010).
- **Backlog CSS:** 13 refs `--on-dark` tokens em CSS de slides light (funcional via stage-c remap, naming misleading). Nao bloqueia QA — registrado para cleanup futuro.

## Estado dos Slides (maquina de estados — WT-OPERATING.md)

> Estados: BACKLOG → DRAFT → CONTENT → SYNCED → LINT-PASS → QA → DONE
> Verificar 1 a 1 antes de registrar. Nao assumir.

### F1 — Criar importancia (3 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 1 | s-title | QA | QA.0-QA.4 PASS. Gemini approved (beauty 9, legibility 10). Choreography + masking. |
| 2 | s-hook | QA | v4: grid assimétrico + blackout + brutalismo + 146 mono (OK — ERRO-010 era Vite, não CSS). Gemini re-eval pendente com server limpo. |
| 3 | s-contrato | QA | Scorecard 14-dim PASS (Opus). Gemini pendente. |

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

- **QA (3):** s-title, s-hook, s-contrato — scorecards 14-dim PASS, Gemini pendente
- **LINT-PASS (15):** restantes — scorecard 14-dim pendente
- **DONE (0):** nenhum slide completou QA full (Opus + Gemini)

---

## O que foi feito

- [x] Narrativa reestruturada (v1): 3 fases + 2 interações
- [x] Docs fundacionais: narrative.md, evidence-db.md, blueprint.md, reading-list.md
- [x] metanalise.css: tokens, layouts (compare, pico-grid, pipeline-flow, anatomy-grid, concept-card, grade-stack, scope-layout, contrato-grid, checkpoint-layout)
- [x] 00-title.html — "Meta-análise: Leitura crítica para decisão clínica" + 3 pilares
- [x] **01-hook.html — REESCRITO (2026-03-13, atualizado 2026-03-16j):** 2-beat state machine, 3 countUp (146/dia, 81%, 10%), 4 PMIDs tier 1
- [x] **02-contrato.html — NOVO (2026-03-13):** 3 cards framework + scope footer. Absorveu 01-objectives.html
- [x] **03-checkpoint-1.html — NOVO (2026-03-13):** cenário MA ilustrativo → "Você muda?" → twist (PICO, comparador, dano)
- [x] 04-rs-vs-ma.html → posição 04 — RS vs MA (compare layout)
- [x] 04-pico.html → posição 05 — PICO grid generalizado
- [x] 05-abstract.html → posição 06 — pipeline PRISMA
- [x] 06-forest-plot.html → posição 07 — anatomia 5 elementos
- [x] 07-benefit-harm.html → posição 08 — benefício vs dano
- [x] 08-grade.html → posição 09 — 4 níveis de certeza
- [x] 09-heterogeneity.html → posição 10 — I² concept card
- [x] 10-fixed-random.html → posição 11 — FE vs RE compare
- [x] **h2 rewrite (2026-03-13):** 9 headlines trocados de framing retórico → assertions técnicas verificáveis
- [x] **CSS fix (2026-03-13):** removido stage-c, slides renderizando corretamente
- [x] index.html migrado para deck.js + engine.js (sem Reveal.js)
- [x] **evidence-db.md v2 (2026-03-13):** 12 refs tier 1 em 4 eixos (volume, qualidade, guidelines, competência)
- [x] **index.html reescrito (2026-03-13):** 12 slides na ordem final do blueprint v1.1
- [x] **QA review pass (2026-03-13):** 15 arquivos auditados, 4 FAILs + 6 WARNs identificados e corrigidos:
  - Orphan files deletados (01-objectives, 02-rs-vs-ma, 03-ancora) — elimina duplicate ID `s-rs-vs-ma`
  - font-weight 300 → 400 (projetor-safe)
  - Dead class `title-hero` removida de 00-title
  - Ícones daltonismo adicionados ao GRADE (✓ ○ ⚠ ✕) + CSS `.grade-icon`
  - Word count trimado em 8 slides (corpo ≤30 palavras)
- [x] **Sessão 2026-03-15 — Notion sync + slides independentes + docs:**
  - narrative.md v2: tese central expandida, 3 perguntas reformuladas, credibility gap, checkpoint-2 recalibrado
  - blueprint.md v1.4: slide 12 recalibrado "falso positivo", slide 17 reformulado, Gemini absorvidas
  - Notion Slides DB: 15 slides MA sincronizados (12 existentes + 3 novos)
  - Notion References DB: 7 refs adicionadas, 3 atualizadas (Aula=Multi)
  - **12-checkpoint-2.html — NOVO:** "falso positivo" do diamante. RR 0,75 + GRADE baixa + NNT 80 → não muda. Arco com CP1
  - **16-absoluto.html — NOVO:** RR→NNT conversion. Baseline 20% → NNT 25 vs 2% → NNT 250
  - **17-takehome.html — NOVO:** 3 perguntas reformuladas (credibilidade, GRADE por desfecho, efeito absoluto)
  - metanalise.css: +120 linhas (checkpoint-steps, conversion-scenarios, takehome-cards)
  - index.html: 15 slides ativos + placeholders para 13-15

## Decisões tomadas

| Decisão | Razão | Data |
|---------|-------|------|
| Artigo âncora = **Valgimigli 2025 (Lancet, clopidogrel vs aspirina)** | IPD-MA, Lancet, N enorme (28.982), tema universal (cardiologia). Lucas escolheu apesar de IPD/HR — ajustes na narrativa amanhã | 2026-03-15 |
| Slide 11 (fixed vs random) MANTÉM como slide dedicado | Lucas override: slide importante para leitura madura. Contra 3 dossiês Gemini que sugeriam substituir | 2026-03-14 |
| 3 fases + 2 interações | Retrieval practice entre blocos | 2026-03-13 |
| h2 = assertion técnica | Cirrose usa claims verificáveis; metanalise deve seguir mesmo padrão | 2026-03-13 |
| Fase 3 bloqueada até artigo definido | Slides 13-17 dependem da escolha | 2026-03-13 |
| Forest plots = imagens cropadas | NUNCA SVG construído do zero | 2026-03-13 |
| 01-objectives absorvido por 02-contrato | Evita redundância; contrato é mais forte pedagogicamente | 2026-03-13 |
| Hook generalizado (sem Musini) | Importância de MA > artigo específico. 4 PMIDs tier 1 sustentam o argumento | 2026-03-13 |

## Caminho crítico — próximas sessões

### Sessão N+1 (imediata) — QA slide-a-slide com visual uplift
1. **Pre-work DONE:** SplitText importado, dark-bg consolidado (6 slides), prompt Gemini v3.0 pronto.
2. **Pipeline normal** (WT-OPERATING.md §4): proximo slide na fila → QA.0-QA.4 → DONE → proximo.
   - Criterios visuais elevados: beleza avançada + GSAP sofisticado (SplitText, custom choreographies)
   - Gemini prompt v3.0 (4 dimensoes, chain-of-thought, exploration mandate GSAP)
   - Contexto sala: pequena, ~15 pessoas, 1-4m, iluminacao forte, TV LED — legibilidade constraint #1
3. **Dark-bg reference** (sugestao, decide-se por slide):
   - Ja dark: s-checkpoint-1, s-checkpoint-2
   - Propostos dark: s-forest-plot, s-heterogeneity, s-ancora, s-absoluto (CSS pronto)
   - Light: demais (s-rs-vs-ma, s-pico, s-abstract, s-benefit-harm, s-grade, s-fixed-random, s-aplicacao, s-aplicabilidade, s-takehome)
4. **Ordem:** s-hook (Gemini re-eval pendente) → s-contrato (Gemini pendente) → s-checkpoint-1 → F2 em sequencia

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

- **lint-slides.js false positive:** `scripts/lint-slides.js:110` — `data-animate="countUp"` sem `data-target` não pula `<script>` blocks. 2 false positives no index.html built.
- ~~**docs/XREF.md:** Adicionar arquivos metanalise~~ ✅ Feito na WT (autorização Lucas 2026-03-17)
- ~~**docs/README.md:** Adicionar WT-OPERATING.md~~ ✅ Feito na WT (autorização Lucas 2026-03-17)
- ~~**CLAUDE.md root:31:** "QA parcial" → atualizar~~ ✅ Feito na WT (autorização Lucas 2026-03-17)

## Não fazer ainda

- Não tocar em Cirrose
- Não expandir para NMA, IPD, bayesiana
- Não fazer build de producao antes de QA visual completo

> Sessoes anteriores (2026-03-14 a 2026-03-18): [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)
