# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** HTML cleanup completo. Janela limpa para QA scorecards 14-dim.
- **HTML cleanup (2026-03-17d):** `data-background-color` removido de 17/18 slides (todos — deck.js ignora). `slide-navy` removido de 16/18 slides light (mantido em CP1+CP2 que TEM bg navy via CSS override). ERRO-009 documentado.
- **QA pipeline:** ver [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa). Gates 1-4: 18/18 PASS. Scorecards formais 14-dim: 3/18 (F1). Fase 3 (dynamic): 3 pendentes (hook, CP1, CP2). Fase 4 (Gemini): bloqueada.
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides no index.html:** 18 (00-title → 01-hook → 02-contrato → 03-checkpoint-1 → 04-rs-vs-ma → 05-pico → 06-abstract → 07-forest-plot → 08-benefit-harm → 09-grade → 10-heterogeneity → 11-fixed-random → 12-checkpoint-2 → 13-ancora → 14-aplicacao → 15-aplicabilidade → 16-absoluto → 17-takehome)
- **Slides planejados:** 18 (00-17) — ver blueprint.md v1.7
- **Docs fundacionais:** narrative.md (v2.2), evidence-db.md (v4.3 — 20+ refs, candidatos colapsados), blueprint.md (v1.8), reading-list.md (v0.3)
- **_manifest.js:** CRIADO — 18 slides, fases F1/I1/F2/I2/F3
- **slide-registry.js:** CRIADO — state machines para hook (2-beat), checkpoint-1 (3-beat), checkpoint-2 (4-beat)
- **Orphan slides:** 0
- **Orphan CSS:** 0
- **Artigo âncora:** ✅ Valgimigli 2025, Clopidogrel vs Aspirina (Lancet, PMID 40902613). IPD-MA, 7 RCTs, 28.982 pts
- **lint:slides:** ✅ PASS (zero FAILs)
- **HEX navy:** #162032 mantido (decisao Lucas — consistencia cross-aula)
- **CSS overrides em metanalise.css vs base.css:** `justify-content: center` restaurado + pseudo-elements desativados (ERRO-005). Checkpoint safe-center pattern proprio (ERRO-006). CSS zoom REMOVIDO — deck.js scale() é o mecanismo correto (ERRO-008). Fixed px tokens mantidos para evitar vw double-scaling. Hook: `.hook-data` flex container + `.hook-data-item { flex: 1 }` para colunas iguais + verdict `margin-top: 80px`. Checkpoint navy override: `#s-checkpoint-1/2 .slide-inner { background-color: #162032 }` + 8 on-dark tokens restaurados (ERRO-009).
- **Backlog CSS:** 13 refs `--on-dark` tokens em CSS de slides light (funcional via stage-c remap, naming misleading). Nao bloqueia QA — registrado para cleanup futuro.

## Estado dos Slides (maquina de estados — WT-OPERATING.md)

> Estados: BACKLOG → DRAFT → CONTENT → SYNCED → LINT-PASS → QA → DONE
> Verificar 1 a 1 antes de registrar. Nao assumir.

### F1 — Criar importancia (3 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 1 | s-title | QA | Scorecard 14-dim PASS (Opus). QA.0-QA.2 PASS. QA.3 Gemini pendente. |
| 2 | s-hook | QA | Scorecard 14-dim PASS (Opus). Gemini pendente. |
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

### Sessão N+1 (imediata) — Scorecards formais 14-dim
1. HTML limpo. Zero dead attributes. Checkpoint CSS verificado.
2. **QA slide-a-slide** com Playwright (Gates 1-4 por slide, workflow em WT-OPERATING.md §4):
   - Slide 04 (s-checkpoint-1) → 05 → 06 → ... → 18 (em ordem)
   - Para cada: screenshot + contraste + score 14-dim + fix loop + docs + commit
   - Gemini slide-a-slide (nao em batch)
3. **Fase 3 (dynamic gate):** hook, CP1, CP2 — timing assertions + click-reveal + video

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

> Sessoes anteriores (2026-03-14 a 2026-03-16j): [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)

---

## Sessao 2026-03-16k — Merge main (4 commits A/B)

### O que foi feito
- [x] `git merge main --no-edit` — fast, zero conflitos
- [x] 7 arquivos absorvidos: `.gitignore`, `.mcp.json`, `.mcp-profiles/qa.json`, `.mcp-profiles/full.json`, `.env.example`, `docs/ECOSYSTEM.md`, `docs/MCP-ENV-VARS.md`
- [x] Classe: todos A/B (governanca + infra). Zero Classe C
- [x] .mcp.json validado (12 servers, JSON valido)
- [x] `npm run build:metanalise` — OK (18 slides)
- [x] CLAUDE.md aula atualizado (merge ref 4bda0c1)

### O que NAO foi feito (deliberado)
- QA slides 02-17
- Build de producao

---

## Ultima atualizacao: 2026-03-18 (QA refs + specificity fixes + merge main skills/agents)

---

## Sessao 2026-03-18 — QA refs + specificity fixes + merge main

### O que foi feito
- [x] WT-OPERATING.md §9: refs complementares (qa-engineer, ralph-qa)
- [x] WT-OPERATING.md §4 QA.2: regra dual-format screenshots (1280x720 + 1920x1080)
- [x] AUDIT-VISUAL.md: scorecards s-title/s-hook/s-contrato re-auditados com evidencias
- [x] metanalise.css: specificity fixes (#deck .slide-title h1, #deck .title-author/affiliation)
- [x] metanalise.css: [data-qa] hook fallbacks + --text-muted navy token
- [x] QA s-title: QA.0 PASS, QA.1 PASS, QA.2 PASS (contrastes AAA verificados)
- [x] Investigacao viewport ultrawide: centrado OK em todos aspect ratios
- [x] `git merge main` — merge commit `5406dd8`, zero conflitos
- [x] Classe: todos A/B (4 commits: medical-researcher, final-pass v3, slide-punch, new-skill v2). Zero Classe C
- [x] Build OK (18 slides), lint PASS

### O que NAO foi feito (deliberado)
- QA slides pendentes (15 scorecards 14-dim)
- QA.3 Gemini (s-title, s-hook, s-contrato)
- Build de producao

### Pendencia nova
- Calibracao viewport congresso — Lucas fornece innerWidth x innerHeight da TV/projetor

---

## Sessao 2026-03-17i — Merge main governance + audit interno

### O que foi feito
- [x] `git merge main` — merge commit `a0e3568`, 6 conflitos resolvidos
- [x] Conflitos: CHANGELOG (both kept), CLAUDE.md root (WT status preserved), ECOSYSTEM/README/XREF (WT versions — reflect actual metanalise files), lessons.md (both kept)
- [x] Classe: todos A/B (4 commits governance: C1-C5, H1-H7, M1-M10, audit-rules). Zero Classe C
- [x] Audit interno: 0 broken links, 0 wrong counts, 18 slides = 18 manifest entries
- [x] CLAUDE.md aula: merge hash atualizado (4bda0c1 → a0e3568)

### O que NAO foi feito (deliberado)
- QA slides pendentes (15 scorecards 14-dim)
- Build de producao

---

## Sessao 2026-03-17 — QA s-contrato (scorecard 14-dim)

### O que foi feito
- [x] **s-contrato (02):** slide-navy removido de .slide-inner, data-background-color removido de <section> — heranca de versao navy anterior
- [x] **AUDIT-VISUAL.md:** scorecard 14-dim s-contrato registrado — PASS (9 dims nota 9, 4 dims nota 8, D=N/A)
- [x] **HANDOFF atualizado**

### Status QA F1 completo
- s-title: PASS (scorecard 14-dim)
- s-hook: PASS (scorecard 14-dim)
- s-contrato: PASS (scorecard 14-dim)

### Proximos passos
- QA batches 2-6 (F2/I1/I2/F3) — scorecards formais pendentes
- Build de producao apos QA completo
- Gate 4 Gemini visual (deck completo)

---

## Sessao 2026-03-17e — MCPs racionalizados (.mcp.json)

### O que foi feito
- [x] **`.mcp.json` racionalizado:** 5→7 servers (adicionados perplexity + crossref, mantido frontend-review)
- [x] **14 MCPs removidos:** cobertos por built-ins Claude Code (PubMed, Notion, Scholar Gateway, Consensus, Playwright, Gemini) ou irrelevantes (biomcp, arxiv, zotero, sharp, filesystem, fetch, memory, chrome-devtools)
- [x] **ECOSYSTEM.md reescrito:** seção MCPs com 4 sub-seções (always-on, built-ins, profiles, removidos)
- [x] HANDOFF atualizado

### Decisão
- `frontend-review` (Hyperbolic) MANTIDO por decisão do Lucas — apesar de não aparecer nos deferred tools desta sessão

### O que NAO foi feito (deliberado)
- `.mcp-profiles/` não alterados (servem para ativação sob demanda)
- QA slides pendentes

---

## Sessao 2026-03-17b — QA s-contrato visual fix (Playwright pipeline)

### O que foi feito
- [x] **Screenshots Playwright:** s-contrato capturado 1280x720 (pre e pos fix)
- [x] **Gate 1:** constraint check PASS (lint, h2 assertion, notes, zero ul/ol, zero inline style)
- [x] **Gate 2 metrics:** fill 82%, cards 550→248px (fix), contraste minimo 8.8:1
- [x] **CSS fixes:** contrato-grid flex:1 removido, contrato-card justify-content:center, contrato-number token corrigido (on-dark→ui-accent)
- [x] **AUDIT-VISUAL re-scored:** 13 dims ≥ 9 (E subiu 8→9), V=8 intencional, D=N/A
- [x] **CHANGELOG, HANDOFF atualizados**

### Pendente
- /review skill + MCPs CLI (usuario roda)
- QA I1 (s-checkpoint-1) — proximo slide

---

## Sessao 2026-03-17f — Auditoria docs (sessao de suporte)

### O que foi feito
- [x] **QA-WORKFLOW.md:** cortado de 330→70 linhas. Mantido: DEPRECATED header, Tooling, Template scorecard, Diferencas vs Cirrose. Removido: workflow (duplica WT-OPERATING.md §4), Status Tracker (duplica HANDOFF), Extensoes Futuras, Gates 1-4 (duplicam WT-OPERATING)
- [x] **AUDIT-VISUAL.md:5:** ref QA-WORKFLOW → WT-OPERATING.md §4
- [x] **HANDOFF.md:11,138:** refs QA-WORKFLOW → WT-OPERATING.md §4
- [x] **docs/metanalise-scope.md:** status atualizado (12 slides → 18, ancora Valgimigli); IPD clarificado (usado como exemplo, nao topico)
- [x] **CLAUDE.md aula:58:** removido "sem index.template.html" (arquivo existe)
- [x] **HANDOFF.md:15:** evidence-db v4.0 → v4.2
- [x] **HANDOFF-ARCHIVE.md CRIADO:** sessoes 2026-03-14 a 2026-03-16j movidas (HANDOFF 628→~250 linhas)
- [x] **Pendencias para main registradas:** XREF.md, README.md, CLAUDE.md root
- [x] Zero slides tocados (sessao de suporte autorizada)

### Nota anti-drift
Sessao inteira de docs. Autorizada pelo usuario como pre-requisito para QA limpo.

---

## Sessao 2026-03-17g — Doc sync: inconsistencias + verbosidade

### O que foi feito
- [x] **Batch 1 — 6 inconsistencias factuais corrigidas:**
  - blueprint.md: assertion "80 revisoes" → "146 SRs/dia"; evidencias Siemens/Fanaroff → Bojcic/Qureshi; G3 Yin→Greenwood, G5 Bosco→El-Taji
  - narrative.md: 80→146/dia + contexto (53.208 SRs)
  - reading-list.md: Musini PMC embargo → Valgimigli Lancet; changelog reordenado + v0.3
- [x] **Batch 2 — 302 linhas cortadas:**
  - blueprint.md (-100): mapa migracao, candidatos ancora, propostas absorvidas → colapsados
  - evidence-db.md (-189): S2/A7/F1-F3/G1-G5 → tabela-resumo com PMIDs
  - narrative.md (-8): revisao slides → 1 linha
  - HANDOFF.md (-5): 4 bloqueios resolvidos removidos
- [x] **NOTES.md CRIADO:** placeholder (referenciado por WT-OPERATING.md mas nao existia)
- [x] **evidence-db v4.3**, blueprint v1.8
- [x] Zero slides tocados (sessao de suporte)

### Pendente para proxima sessao
- ~~lessons.md: adicionar licoes de doc sync~~ ✅ Feito (sessao 2026-03-17h)
- Skills: verificacao de coerencia (baixa prioridade)
- ~~AUDIT-VISUAL.md s-hook: verificar sync Notion~~ ✅ Confirmado via Notion search (sessao 2026-03-17h)
- Scorecards 14-dim: 15 slides pendentes (caminho critico)

### Nota anti-drift
Sessao de docs autorizada pelo usuario. Previne regressao de dados em sessoes futuras de QA.

---

## Sessao 2026-03-17h — Verificação documental + pendências para main

### O que foi feito
- [x] **AUDIT-VISUAL.md s-hook:** 3 pendências operacionais verificadas e fechadas (evidence-db ✅, narrative ✅, Notion sync ✅)
- [x] **lessons.md:** 3 lições de doc sync adicionadas (drift dados, verbosidade candidatos, refs cross-doc)
- [x] **docs/XREF.md:** 8 arquivos metanalise adicionados à seção metanalise + canônico Estado Metanalise
- [x] **docs/README.md:** WT-OPERATING.md adicionado à tabela Estado e handoff
- [x] **CLAUDE.md root:** status metanalise atualizado (QA parcial → F1 QA PASS, F2-F3 LINT-PASS)
- [x] **NOTES.md:** verificações registradas
- [x] **HANDOFF.md:** pendências para main marcadas como resolvidas (3/4 — resta lint false positive)
- [x] Zero slides tocados (sessão de suporte)

### Nota
Pendências para main editadas na WT com autorização explícita do Lucas. Merge resolverá.
Único pendente Classe B remanescente: lint-slides.js false positive (requer edição de scripts/).

### Nota anti-drift
Sessão de housekeeping autorizada. Todas pendências documentais do doc sync (2026-03-17g) resolvidas.
