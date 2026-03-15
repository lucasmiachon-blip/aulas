# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** DECK COMPLETO — 18 slides (00-17). QA parcial (batch 1 aprovado). Build de producao pendente.
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides no index.html:** 18 (00-title → 01-hook → 02-contrato → 03-checkpoint-1 → 04-rs-vs-ma → 05-pico → 06-abstract → 07-forest-plot → 08-benefit-harm → 09-grade → 10-heterogeneity → 11-fixed-random → 12-checkpoint-2 → 13-ancora → 14-aplicacao → 15-aplicabilidade → 16-absoluto → 17-takehome)
- **Slides planejados:** 18 (00-17) — ver blueprint.md v1.7
- **Docs fundacionais:** narrative.md (v2.2), evidence-db.md (v4.0 — 20+ refs), blueprint.md (v1.7), reading-list.md
- **_manifest.js:** CRIADO — 18 slides, fases F1/I1/F2/I2/F3
- **slide-registry.js:** CRIADO — state machines para hook (2-beat), checkpoint-1 (3-beat), checkpoint-2 (4-beat)
- **Orphan slides:** 0
- **Orphan CSS:** 0 (8 classes removidas: scope-*, pipeline-number, hook-question-sub)
- **Artigo âncora:** ✅ Valgimigli 2025, Clopidogrel vs Aspirina (Lancet, PMID 40902613). IPD-MA, 7 RCTs, 28.982 pts
- **lint:slides:** ✅ PASS (zero FAILs)
- **HEX navy:** #162032 mantido (decisao Lucas — consistencia cross-aula)

## O que foi feito

- [x] Narrativa reestruturada (v1): 3 fases + 2 interações
- [x] Docs fundacionais: narrative.md, evidence-db.md, blueprint.md, reading-list.md
- [x] metanalise.css: tokens, layouts (compare, pico-grid, pipeline-flow, anatomy-grid, concept-card, grade-stack, scope-layout, contrato-grid, checkpoint-layout)
- [x] 00-title.html — "Meta-análise: Leitura crítica para decisão clínica" + 3 pilares
- [x] **01-hook.html — REESCRITO (2026-03-13):** 2-beat state machine, 3 countUp (80/dia, 88%, 8.5%), 4 PMIDs tier 1
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

### Sessão N+1 (imediata) — QA visual batches 2-6
1. **QA visual batches 2-6** com Vite aberto (batches de 3 slides, tese por slide, checkpoint sim/nao/pq)
   - Batch 2: slides 03-05 (checkpoint-1, RS vs MA, PICO)
   - Batch 3: slides 06-08 (abstract, forest plot, beneficio-dano)
   - Batch 4: slides 09-11 (GRADE, heterogeneidade, fixed-random)
   - Batch 5: slides 12-14 (checkpoint-2, ancora, aplicacao)
   - Batch 6: slides 15-17 (aplicabilidade, absoluto, takehome)
2. Inserir exemplos visuais Cochrane (forest plot, GRADE table) — PDFs em `references/sources/`

### Sessão N+2
- QA final (Gate 4 Gemini)
- Build de producao
- Merge para main

## Bloqueios conhecidos

| Bloqueio | Impacto | Workaround |
|----------|---------|------------|
| ~~Artigo âncora em deliberação~~ | ~~Dados específicos dos slides 13-15~~ | ✅ RESOLVIDO: Valgimigli 2025 (Lancet, clopidogrel vs aspirina, PMID 40902613) |
| Full-text Musini: PMC embargo até 2026-10-09 | Forest plot e NNT dependem de full-text | ✅ Acessível via Cochrane Library (acordo CAPES/Wiley). PMID 41065416. Musini agora = exemplo visual, não âncora |
| ~~HEX navy `#162032` vs canônico `#0d1a2d`~~ | ~~Inconsistência cross-aula~~ | ✅ RESOLVIDO: #162032 mantido (decisão Lucas 2026-03-15) |
| PMIDs Consensus-sourced não verificados | 3 PMIDs (Aamann, AlSowaiegh, Saleh) pendentes PubMed check | Não-bloqueante: esses candidatos não são top. Verificar se algum for promovido |
| Cochrane exemplos visuais | Forest plots e GRADE tables reais precisam de screenshots/crops | Acessar via CAPES e cropar quando iniciar Fase 3 |

## Pendências para main (Classe B — não editar na WT)

- **lint-slides.js false positive:** `scripts/lint-slides.js:110` — `data-animate="countUp"` sem `data-target` não pula `<script>` blocks. 2 false positives no index.html built.

## Não fazer ainda

- Não tocar em Cirrose
- Não expandir para NMA, IPD, bayesiana
- Não fazer build de producao antes de QA visual completo

---

## Sessão 2026-03-14 — Análise Gemini + busca de candidatos

### O que foi feito
- [x] Analisados 3 dossiês Gemini contra narrative.md e blueprint.md
- [x] Identificadas convergências (credibility gap, tese, 3 perguntas, checkpoint-2)
- [x] Verificados 10 PMIDs citados por Gemini via PubMed MCP (todos ✅)
- [x] Buscados candidatos via PubMed + Consensus: cardiologia, infectologia, hepatologia
- [x] Valgimigli Lancet 2025 (clopidogrel vs aspirina) verificado — PMID 40902613 ✅
- [x] Encontrados 12+ candidatos em cirrose: rifaximin (Cochrane), albumina, TIPS, ATB profilático, beta-bloqueadores, BCAAs
- [x] Blueprint atualizado v1.3 com 18 candidatos em 3 tiers (S/A/B)
- [x] Evidence-db atualizado v3 com refs metodológicas + dados top 3
- [x] Reading-list atualizado v0.2 com Murad JAMA 2014 + Guyatt BMJ 2008

---

## Sessão 2026-03-15 — Notion sync + slides independentes + docs

### O que foi feito
- [x] Notion Slides DB: 15 slides MA sincronizados (12 criados + 3 novos)
- [x] Notion References DB: 7 refs adicionadas, 3 atualizadas (Aula=Multi)
- [x] narrative.md v2: tese central, 3 perguntas reformuladas, credibility gap, checkpoint-2 recalibrado
- [x] blueprint.md v1.4: slide 12 + 17 recalibrados, Gemini absorvidas
- [x] 12-checkpoint-2.html: "falso positivo" — RR 0,75 + GRADE baixa + NNT 80 → não muda
- [x] 16-absoluto.html: RR→NNT conversion (NNT 25 vs 250)
- [x] 17-takehome.html: 3 perguntas reformuladas
- [x] metanalise.css: checkpoint-steps, conversion-scenarios, takehome-cards
- [x] index.html: 15 slides ativos + placeholders 13-15
- [x] HANDOFF atualizado

### O que NÃO foi feito (deliberado)
- Slides 13-15 (Fase 3) — artigo âncora TBD
- 4 PMIDs Consensus-sourced não verificados (Zacharias, Aamann, AlSowaiegh, Saleh)

---

## Repo Janitor — 2026-03-14

**Rodada:** main + wt-cirrose + wt-metanalise em paralelo. Resultado wt-metanalise:

- **FAIL [✅ corrigido]:** `docs/XREF.md` linha 80 — link `pipeline/README.md` inexistente. Corrigido para `archive/pipeline/README.md`.
- **WARN [✅ resolvido]:** 12 slides em `slides/` órfãos (sem `_manifest.js`) — `_manifest.js` criado (sessão 2026-03-15g).
- **WARN [✅ corrigido]:** `03-rs-vs-ma.html` renomeado para `04-rs-vs-ma.html` — prefixo 03 não conflita mais com `03-checkpoint-1.html`.
- **WARN:** 11 classes CSS órfãs em `metanalise.css` (`.scope-*`, `.anchor-*`, `.metric-*`) — retidas para Fase 3. Auditar ao começar.

---

## Sessão 2026-03-15b — QA pass (conteúdo + visual + interações + refs)

### O que foi feito
- [x] Housekeeping: rename 03→04-rs-vs-ma, evidence-db header "Candidato a Âncora", HANDOFF timestamp
- [x] **Contrato (02) alinhado com narrative v2 + takehome (17):** perguntas idênticas nos dois extremos do arco narrativo
- [x] **Checkpoint-1 (03) source-tag genericizado:** removida ref a Musini (regra: nenhum artigo antes Fase 3)
- [x] **GRADE (09) ícones daltonismo:** ✓ ○ ⚠ ✕ adicionados ao HTML (CSS já existia)
- [x] **Checkpoint-2 (12) inline style → CSS class:** `.checkpoint-grade--low` em vez de `style=`
- [x] **slide-registry.js CRIADO:** state machines para hook (2-beat click), checkpoint-1 (3-beat click), checkpoint-2 (4-beat click)
- [x] **CSS:** `.checkpoint--hidden` (initial state), `.checkpoint-grade--low`, print/no-js fallbacks
- [x] PICO (04) notes alinhado com Q1 reformulada
- [x] Fixed-random (10) transition note especificado
- [x] Title (00) notes "objetivos" → "hook" (standalone sync)
- [x] **Refs verificadas:** Zacharias PMID 37467180 ✅, Higgins & Lopez-Lopez 2025 (I² reflections) encontrado e registrado
- [x] Blueprint v1.5: Zacharias PMID atualizado
- [x] Evidence-db v3.2: Higgins 2025 adicionado como ref metodológica
- [x] Descoberto: `aulas/*/index.html` está no `.gitignore` — standalones em `slides/` são o source of truth no Git

### O que NÃO foi feito (deliberado)
- Slides 13-15 (Fase 3) — artigo âncora TBD (Lucas decide)
- _manifest.js — precisa de slides finais
- QA visual com Vite aberto (screenshots, projetor) — próxima sessão

---

---

## Sessão 2026-03-15c — Busca de artigo âncora + docs update

### O que foi feito
- [x] Acesso Cochrane Library verificado: acordo nacional CAPES/Wiley — full-text disponível para todos os candidatos Cochrane
- [x] Musini 2025 PMID encontrado e verificado: **41065416** ✅
- [x] Decisão: Cochrane = exemplos visuais (Fases 1-2), âncora = preferencialmente não-Cochrane
- [x] Decisão: área do Lucas ≠ hepatologia. Artigo pode ser de qualquer área clínica
- [x] 3 finalistas próprios compilados: Pitre/PAC (ICM 2025), Kolkailah/VTE (Cochrane 2024), Carson/transfusão (Cochrane 2025)
- [x] Prompt criado e enviado ao Gemini para busca ampliada
- [x] 5 candidatos Gemini recebidos e verificados: 2 PMIDs corrigidos (McIntyre 37952187, Abdul-Aziz 38864162)
- [x] Análise comparativa dos 2 favoritos do Lucas: β-lactam (Abdul-Aziz) e clopidogrel (Valgimigli)
  - Valgimigli: IPD (não pairwise), HR (não RR), sem GRADE — falha 3 critérios obrigatórios
  - Abdul-Aziz: bayesiano (CrI), sem dano claro, GRADE com pouca variação — funciona mas com ressalvas
- [x] Evidence-db atualizado v4.0: 8 candidatos com PMIDs verificados
- [x] Blueprint atualizado v1.6: recomendação atualizada, Fase 3 com placeholder
- [x] HANDOFF atualizado: caminho crítico para amanhã
- [x] Prosty (bayesiano) removido da lista

### O que NÃO foi feito (deliberado)
- Artigo âncora: Lucas decide durante construção dos slides (amanhã)
- Slides 13-15: começam amanhã com layout genérico
- Verificação PMIDs pendentes: Yin (38588546), Bosco (38842801) — não-bloqueante
- _manifest.js, QA visual, HEX navy — próxima sessão

### Decisões tomadas

| Decisão | Razão | Data |
|---------|-------|------|
| Cochrane = exemplos visuais, não âncora | Contraste didático: Cochrane nas Fases 1-2, artigo de journal na Fase 3 | 2026-03-15 |
| Área do Lucas ≠ hepatologia | Salvar na memória. Artigo pode ser de qualquer área (ambulatório ou hospital) | 2026-03-15 |
| Bayesiano removido (Prosty A2) | Fora do escopo pairwise da aula | 2026-03-15 |
| Slides 13-15 começam sem artigo definido | Estrutura genérica + placeholders. Material suficiente para construir layouts | 2026-03-15 |
| Pitre PAC = recomendado pelo agente | Melhor fit: GRADE com variação, benefício+dano, não-Cochrane, PAC universal | 2026-03-15 |

---

---

## Sessão 2026-03-15e — Slides 13-15 criados (Fase 3 completa)

### O que foi feito
- [x] narrative.md v2.2: Fase 3 atualizada com Valgimigli 2025 (tensões didáticas IPD/HR/GRADE documentadas)
- [x] blueprint.md v1.7: assertions concretas para slides 13-15, status atualizado
- [x] **13-ancora.html — NOVO:** anchor-card + metric-grid (IPD, 7 RCTs, 28.982 pts, 2,3a). Notes explicam IPD vs pairwise e HR vs RR
- [x] **14-aplicacao.html — NOVO:** compare-layout benefício (MACCE HR 0,86) vs dano (sangramento HR 0,94 NS) + GRADE gap callout. Notes ensinam que mesmo Lancet pode omitir GRADE
- [x] **15-aplicabilidade.html — NOVO:** pico-grid callback (eco do slide 05) com dados Valgimigli aplicados. Notes guiam validade externa
- [x] metanalise.css: +7 linhas (compare-footer--gap warning, symbol-neutral)
- [x] index.html: 18 slides ativos (placeholders substituídos)

### O que NÃO foi feito (deliberado)
- QA loop (lint + visual) — próximo passo, com Lucas presente
- _manifest.js — após QA
- HEX navy decision (#162032 vs #0d1a2d)
- Detalhes populacionais Valgimigli — [TBD] até full-text lido
- Exemplos visuais Cochrane (forest plot crops) — requer acesso CAPES

---

## Sessão 2026-03-15f — Parametrização QA multi-aula

### O que foi feito
- [x] **QA infra parametrizada:** 22 arquivos em `.claude/` e `.cursor/` — ZERO caminhos `aulas/cirrose/` hardcoded restantes
- [x] **Agents:** qa-engineer, slide-builder, verifier, notion-sync, repo-janitor, reference-manager — `{aula}` auto-detect via `git branch`
- [x] **Skills:** ralph-qa, final-pass, review, visual-qa, mem-search, gtd, evolve, audit-rules, new-slide, slide-frontend-ux, export — parametrizados
- [x] **Hooks:** build-monitor, check-evidence-db, subagent-stop-log — auto-detect branch → aula
- [x] **Rules:** slide-identity (13 refs → multi-aula), motion-qa (audiência → CLAUDE.md), slide-editing.mdc (glob expandido)
- [x] settings.json hooks (já aula-agnosticos do merge)
- [x] Refs "cirrose" restantes = somente exemplos documentais (ex: `/export cirrose`, case statements multi-aula)

### O que NÃO foi feito (deliberado)
- QA loop visual (lint + screenshots) — próxima sessão, com Lucas presente
- _manifest.js — após QA
- HEX navy decision
- Exemplos visuais Cochrane

---

## Sessão 2026-03-15g — QA loop parcial + _manifest.js + MD audit

### O que foi feito
- [x] `npm run lint:slides` — PASS (zero FAILs)
- [x] HEX navy: decisao #162032 mantido (consistencia cross-aula)
- [x] CSS orphan audit: 8 classes removidas (scope-layout/col/label/item/out, pipeline-number, hook-question-sub)
- [x] QA visual batch 1 (slides 00-02): tese por slide, checklist aprovado
- [x] **_manifest.js CRIADO:** 18 slides, fases F1/I1/F2/I2/F3, headlines, timing, customAnim
- [x] **references/sources/ CRIADO:** pasta para full-text PDFs + README com convenção de nomes
- [x] **.gitignore:** PDFs em references/sources/ adicionados
- [x] **MD audit:** CLAUDE.md aula (status 15→18 slides), evidence-db (Musini→exemplo visual), narrative (changelog v2.2), HANDOFF (caminho critico atualizado)

### O que NÃO foi feito (deliberado)
- QA visual batches 2-6 — proxima sessao
- Exemplos visuais Cochrane — requer PDFs em sources/
- Build de producao — apos QA completo

## Última atualização: 2026-03-15g (QA loop parcial + _manifest.js + MD audit)
