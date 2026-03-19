# CHANGELOG — Meta-analise

> Historico de batches. Append-only (novos no topo). Estado → HANDOFF.md

---

## 2026-03-19a — Reveal.js purge + Vite cache fix + doc P0 fixes

Branch: `feat/metanalise-mvp`

- **ROOT CAUSE encontrado:** "146 mono não renderiza" NÃO era CSS specificity — era Vite cache poisoning. `node_modules/.vite/deps/` tinha Reveal.js pre-bundled (de grade/osteoporose entries). Vite servia inline script ERRADO (da wt-cirrose) com `import Reveal from 'reveal.js'`, que injetava `reveal.css` → `section { display: none }` → tela preta.
- **Fix 1:** Removido `reveal.js` de `package.json` dependencies. `npm install` → node_modules limpo.
- **Fix 2:** `vite.config.js` → `FROZEN_AULAS = ['grade', 'osteoporose']` excluídos de `discoverEntries()`. Previne re-contaminação do dep cache.
- **Fix 3:** WT-OPERATING.md ghost ref a QA-WORKFLOW.md removida (arquivo não existe).
- **Fix 4:** CLAUDE.md aula status atualizado: Gemini s-title PASS, s-hook ITERATE, demais pendentes (era genérico "Gemini pendente").
- 146 mono renderiza corretamente: JetBrains Mono 72px 600w. Verificado via Playwright computed styles.
- Build PASS, lint PASS, 18/18 slides renderizando.

## 2026-03-18e — s-hook v4 (grid + blackout + brutalismo + prompt template)

Branch: `feat/metanalise-mvp`

- s-hook CSS: flex column centered → grid 2-col assimétrico (Z-pattern)
- Provocação esquerda, hero 41% direita, verdict full-width rodapé
- Beat 2 blackout: fade ALL upper content (opacity 0.12), verdict toma foco
- Verdict brutalismo: border-radius:0, padding 16px 56px, --danger bg, Instrument Serif italic
- 146 mono: número em JetBrains Mono 72px (espelhamento tipográfico com 41%)
- HTML: `<p>` provocação → `<div>` com `.hook-vol-number` + `.hook-vol-text` + `.hook-vol-ask`
- slide-registry.js: hero shrink → blackout (querySelectorAll upper), retreat restaura
- Gemini scores: v2 beauty 6.5 legibility 9.5, v3 beauty 6.5 legibility 9.0 (ITERATE)
- Prompt template padronizado: `docs/prompts/gemini-slide-qa.md` (tags XML, rubrica, speaker notes, código pronto)
- Bug pendente: 146 mono não renderiza (specificity CSS — debugar próxima sessão)

## 2026-03-18d — s-hook refactor (hero 41% + trials concretos)

Branch: `feat/metanalise-mvp`

- s-hook HTML refatorado: 3-column number grid → hero number pattern (41% single dominant stat)
- Dados trocados: Bojcic 81%/Qureshi 10% → Windish 41% (avaliacao de evidencia, nao bioestatistica)
- Contexto adicionado: TRH, rosiglitazona, controle glicemico intensivo (trials concretos revertidos)
- 396 praticas revertidas (Herrera-Perez 2019) como supporting context
- Verdict visual: font-size --text-h3, margin-top --space-lg (antes --text-body, 80px)
- metanalise.css: dead CSS removido (.hook-data-grid, .hook-data-item, .hook-data-value, .hook-data-big, .hook-data-label)
- metanalise.css: adicionado .hook-hero (96px mono), .hook-context, .hook-context-line, .hook-context-num
- _manifest.js: headline corrigida ("bioestatistica" → "avaliacao de evidencia")
- evidence-db.md v5.0: 6 novas referencias (Windish, Saposnik, VITALITY/Xu, Possamai, Herrera-Perez, Ioannidis)
- slide-punch: diagnostico ENCAIXADO (0 FAIL, 0 WARN)
- QA.0 Content PASS, QA.1 Constraint PASS, QA.2 Visual PASS (14 dims >= 8)
- Contrastes verificados: hero 14.15:1, label 9.20:1, verdict 10.26:1 (AAA). Context 5.75:1 (AA — WARN marginal)

## 2026-03-18c — s-title QA.3-QA.4 (Gemini approved)

Branch: `feat/metanalise-mvp`

- QA s-title: QA.3 Gemini (2 rounds) → beauty 9/10, legibility 10/10, **approved**
- Bold ideas Gemini: inverted weight hierarchy (h1 400/64px, subtitle 600/20px uppercase), merged identity block, pillar masking reveal
- slide-registry.js: s-title choreography — h1→subtitle→pillars(masking)→dots→identity (5-element stagger)
- metanalise.css: pillar-dot `translateY(1px)` optical align, `#s-title` opacity:0 initial states + .no-js + @media print failsafes
- 00-title.html: `data-animate="fadeUp"` removido de subtitle/identity (custom anim controla)
- narrative.md: titulo corrigido ("Do diamante à decisão" → "Meta-análise — Leitura crítica para decisão clínica")

## 2026-03-18 — Sessão QA + refs + merge main

Branch: `feat/metanalise-mvp`

- WT-OPERATING.md §9: refs complementares (qa-engineer, ralph-qa)
- WT-OPERATING.md §4 QA.2: regra dual-format screenshots (1280x720 + 1920x1080)
- AUDIT-VISUAL.md: scorecards s-title/s-hook/s-contrato re-auditados com evidências
- metanalise.css: specificity fixes (#deck .slide-title h1, #deck .title-author/affiliation)
- metanalise.css: [data-qa] hook fallbacks + --text-muted navy token
- QA s-title: QA.0 PASS, QA.1 PASS, QA.2 PASS (contrastes AAA verificados)
- Merge main: 4 commits Classe A/B (medical-researcher, final-pass v3, slide-punch, new-skill v2, sync-evidence)
- Investigação viewport ultrawide: centrado OK em todos aspect ratios

---

## 2026-03-17h — Verificação documental + pendências para main

Branch: `feat/metanalise-mvp`

### Pendências verificadas e fechadas
- AUDIT-VISUAL.md s-hook: 3 pendências operacionais ✅ (evidence-db, narrative, Notion sync)
- lessons.md: 3 lições doc sync (drift dados, verbosidade candidatos, refs cross-doc)

### Docs atualizados (autorização Lucas — Classe B editada na WT)
- docs/XREF.md: +8 arquivos metanalise + canônico Estado Metanalise
- docs/README.md: +WT-OPERATING.md na tabela
- CLAUDE.md root: status metanalise atualizado
- NOTES.md: verificações registradas
- HANDOFF.md: pendências resolvidas

### Zero slides tocados

---

## 2026-03-17g — Doc sync: 6 inconsistencias + 302 linhas cortadas

Branch: `feat/metanalise-mvp`

### Batch 1 — Inconsistencias factuais (6 edits)
- blueprint.md: assertion hook 80→146/dia, evidencias Siemens→Bojcic + Fanaroff→Qureshi, autores G3/G5 corrigidos
- narrative.md: 80→146/dia com contexto (53.208 SRs indexadas em 2021)
- reading-list.md: nice-to-read Musini PMC → Valgimigli Lancet; changelog reordenado

### Batch 2 — Verbosidade (-302 linhas)
- blueprint.md (-100): mapa migracao concluido, candidatos ancora decididos, propostas absorvidas → colapsados para 1-3 linhas cada
- evidence-db.md v4.3 (-189): 11 candidatos nao selecionados → tabela-resumo com PMIDs
- narrative.md (-8): tabela revisao → 1 linha
- HANDOFF.md (-5): 4 bloqueios resolvidos removidos

### Misc
- NOTES.md criado (placeholder — referenciado por WT-OPERATING.md)
- Zero slides tocados

---

## 2026-03-17f — WT-OPERATING.md + state machine no HANDOFF

Branch: `feat/metanalise-mvp`

### Docs
- **WT-OPERATING.md CRIADO:** maquina de estados (BACKLOG→DONE), checklists de transicao, QA 5-stage com checkpoints humanos, anti-drift embutido, tooling reference. Adaptado de cirrose.
- **HANDOFF.md:** tabela "Estado dos Slides" adicionada (18 slides, 3 QA + 15 LINT-PASS)
- **CLAUDE.md aula:** secao "Documentacao order" + "Arquivos de trabalho" adicionadas
- **QA-WORKFLOW.md:** marcado DEPRECATED — workflow vive no WT-OPERATING.md secao 4

### Adaptacoes cirrose → metanalise
- Paths: `cirrose` → `metanalise` em todos contextos
- Narrativa: acts (s-a1-, s-a2-) → fases (s-title, s-hook, etc.)
- Removidos: archetypes.css, case-panel.js, CASE.md, meld-calc.js, HANDOFF-CLAUDE-AI.md, qa-batch-screenshot.mjs
- Gemini prompt: "hepatic cirrhosis" + hepatologists → "meta-analysis critical reading" + medical residents
- Expertise-reversal: "Congress = zero revisao basica" → "basico-intermediario, sem infantilizar"

---

## 2026-03-17e — MCPs racionalizados (.mcp.json 5→7 servers)

Branch: `feat/metanalise-mvp`

### .mcp.json
- **Adicionados:** perplexity (web search tempo real), crossref (validação DOI)
- **Mantidos:** a11y-contrast, a11y, lighthouse, frontend-review, frontend-design-audit
- **Removidos (cobertos por built-ins):** pubmed, pubmed-simple, notion, semantic-scholar, google-scholar, playwright, gemini, filesystem, fetch, memory, eslint
- **Removidos (irrelevantes):** biomcp, zotero, arxiv, sharp, chrome-devtools

### Docs
- ECOSYSTEM.md: seção MCPs reescrita (always-on, built-ins, profiles, removidos)
- HANDOFF atualizado

---

## 2026-03-17d — HTML cleanup: dead attributes removed + checkpoint navy CSS override

Branch: `feat/metanalise-mvp`

### HTML cleanup (15 slides)
- `data-background-color="#162032"` removido de 15 slides (00-title, 01-hook, 04-rs-vs-ma, 04-pico, 05-abstract, 06-forest-plot, 07-benefit-harm, 08-grade, 09-heterogeneity, 10-fixed-random, 13-ancora, 14-aplicacao, 15-aplicabilidade, 16-absoluto, 17-takehome). Total: 17/18 (CP1+CP2 ja removidos em sessao anterior)
- `slide-navy` removido de `.slide-inner` em 14 slides light (mesmos acima exceto 00-title que ja nao tinha). Total: 16/18 (CP1+CP2 mantidos — TEM bg navy via CSS)

### CSS (ja aplicado, sem mudancas neste commit)
- `#s-checkpoint-1 .slide-inner, #s-checkpoint-2 .slide-inner { background-color: #162032 }` + 8 on-dark tokens restaurados no scope

### Docs
- ERRO-009 registrado (checkpoint contraste destruido por atributos mortos)
- HANDOFF atualizado (estado limpo para QA)
- AUDIT-VISUAL nota de cobertura adicionada

### Verificacao
- `grep data-background-color slides/` → 0 resultados
- `grep slide-navy slides/` → apenas CP1 e CP2
- lint:slides PASS

---

## 2026-03-17c — QA-WORKFLOW.md reescrito como doc executavel autonomo

Branch: `feat/metanalise-mvp`

- **QA-WORKFLOW.md reescrito:** workflow operacional baseado no QA real de F1 (s-title, s-hook, s-contrato)
- Removidas ferramentas nao conectadas (chrome-devtools MCP, Claude Vision 7-dim separado, metrics.json manual)
- Diagrama ASCII substituido por fluxo 4-gate sequencial (Gate 1→2→3→4 por slide, Fase 3 por fase, Fase 4 por deck)
- Gate 2 simplificado de 5 passos para 3 (screenshot+contraste, score 14-dim, console)
- Template scorecard adicionado (copy-paste para AUDIT-VISUAL.md)
- Spec ideal movida para secao "Extensoes Futuras" (nenhuma info perdida)
- Status tracker atualizado: s-contrato DONE, 18/18 Gates 1-4 PASS
- Tooling atualizado com MCPs reais (Gemini marcado FALHANDO)
- HANDOFF atualizado: caminho critico = scorecards formais 14-dim para 15 slides restantes

---

## 2026-03-17b — QA s-contrato visual fix (Playwright + metrics)

Branch: `feat/metanalise-mvp`

### CSS fixes
- `.contrato-grid`: removido `flex: 1` + `align-items: stretch` — cards 550→248px
- `.contrato-card`: `justify-content: center` + padding vertical `--space-lg`
- `.contrato-number`: `--ui-accent-on-dark` → `--ui-accent` (stage-c = light bg)

### QA pipeline
- Screenshots Playwright (3 beats hook + contrato)
- Gate 1 constraint check: PASS (lint, h2, notes, no inline style)
- Gate 2 metrics: fill 82%, contraste mínimo 8.8:1 (todos pares)
- Gate 2 console: ZERO errors
- AUDIT-VISUAL scorecard re-scored: 13 dims ≥ 9, V=8 (intencional), D=N/A

---

## 2026-03-17 — QA s-contrato (edições + scorecard 14-dim)

Branch: `feat/metanalise-mvp`

### Mudanças no slide

- **h2:** "Ao final, 3 perguntas..." → "3 perguntas que você faz a toda meta-análise" (assertion direta)
- **Card 2 skill:** "Forest plot + GRADE por desfecho" → "Forest plot + confiança + heterogeneidade" (GRADE movido para card 3 contexto)
- **Scope footer removido:** `<p class="contrato-scope">` deletado (redundante com notes)
- **slide-navy removido** de `.slide-inner` (herança de versão navy — stage-c = creme)
- **data-background-color removido** de `<section>` (ignorado por deck.js, ERRO-034)

### Cadeia atualizada

- `_manifest.js`: headline atualizado
- `blueprint.md`: h2 e skill atualizados
- `metanalise.css`: dead `.contrato-scope` removido
- `index.html`: rebuild (18 slides)
- `AUDIT-VISUAL.md`: scorecard 14-dim registrado — PASS

### Gate 1 constraint check: PASS

- h2 = asserção (não rótulo)
- Zero `<ul>/<ol>`
- `<aside class="notes">` com timing 3 blocos
- Sem inline style no `<section>`
- CSS 100% tokens (zero HEX inline)
- lint:slides PASS

### Pendência

- Screenshot Playwright CLI = preto (deck.js hash nav requer script com waitForSelector). Referência visual: `qa-screenshots/s02-contrato-final.png` (sessão 16e, pré-edição). Screenshot pós-edição pendente.

---

## 2026-03-16k — Merge main (4 commits A/B absorvidos)

Branch: `feat/metanalise-mvp`

- `git merge main --no-edit` — merge commit `492ca7d`, zero conflitos
- 7 arquivos absorvidos (todos Classe A/B, zero Classe C):
  - `.gitignore` (test-results/)
  - `.mcp.json` (+4 servers visuais: a11y-contrast, gemini, frontend-review, chrome-devtools)
  - `.mcp-profiles/qa.json`, `.mcp-profiles/full.json` (idem)
  - `.env.example` (vars dos novos MCPs)
  - `docs/ECOSYSTEM.md`, `docs/MCP-ENV-VARS.md` (docs sync)
- Total MCP servers pos-merge: 12 (sem duplicatas)
- Build OK: 18 slides
- CLAUDE.md aula + HANDOFF.md atualizados (commit `a6f3821`)

---

## 2026-03-16j — QA full-deck + housekeeping

Branch: `feat/metanalise-mvp`

### Mudancas

- **Hook (01):** 80/dia → 146/dia (Hoffmann 2021, dado atualizado de 2019→2021). countUp target, label, notes atualizados
- **CP1 (03):** Musini PMID atualizado nas notes (pendente → 41065416 verificado)
- **Evidence-db v4.2:** autores corrigidos — G3 Yin→Greenwood H (PMID 38588546), G5 Bosco→El-Taji O (PMID 38842801). Todos 5 PMIDs verificados via PubMed
- **Reading-list:** item 4 atualizado — Musini→Valgimigli 2025 (PMID 40902613). Lacuna de acesso atualizada
- **CSS:** `.checkpoint-teaser` removido (dead selector — nenhum HTML o referenciava)
- **CLAUDE.md aula:** merge ref corrigido 6889ff7→733eb2e
- **CHANGELOG.md:** criado (referenciado por ERROR-LOG/HANDOFF mas nunca existiu)

### QA slide-a-slide (18/18)

| Status | Slides |
|--------|--------|
| PASS | 00, 01, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| Pendente decisao | 02 (contrato) — titulo + word count |

### Repo janitor

- 0 orphan HTML, 0 orphan MDs, 0 broken links, 0 temp files
- 1 dead CSS class removida (.checkpoint-teaser)
- QA screenshots: 5 dirs stale (manter post-fix-scan/ como current)

---

## 2026-03-16i — Notion sync completo

Branch: `feat/metanalise-mvp`

- 18/18 slides sincronizados com Notion Slides DB
- 25 refs adicionadas ao Notion References DB
- ALLOW_AB_ON_WT=1 usado para este CHANGELOG

---

## 2026-03-16h — Hook layout centering

Branch: `feat/metanalise-mvp`

- `.hook-data` flex container + `.hook-data-item { flex: 1 }` = 3 colunas iguais
- `.hook-verdict` margin-top 80px
- Revertido override `.stage-c .slide-navy` erroneo

---

## 2026-03-16 — CSS layout fixes (ERRO-005/006/008)

Branch: `feat/metanalise-mvp`

- ERRO-005: base.css pseudo-elements → override `justify-content: center` + `::before/::after { display: none }`
- ERRO-006: checkpoint centering safe pattern
- ERRO-008: CSS zoom REMOVIDO — deck.js scale() e o mecanismo correto

---

## 2026-03-15g — _manifest.js + QA batch 1

Branch: `feat/metanalise-mvp`

- `_manifest.js` criado: 18 slides, fases F1/I1/F2/I2/F3
- QA visual batch 1 (slides 00-02): PASS
- 8 classes CSS orfas removidas
- `references/sources/` criado com .gitignore

---

## 2026-03-15e — Fase 3 completa (slides 13-15)

Branch: `feat/metanalise-mvp`

- 13-ancora.html: anchor-card + metric-grid (Valgimigli 2025)
- 14-aplicacao.html: beneficio vs dano (MACCE HR 0,86 vs sangramento NS)
- 15-aplicabilidade.html: PICO callback com dados Valgimigli

---

## 2026-03-15 — Notion sync + slides independentes

Branch: `feat/metanalise-mvp`

- 12-checkpoint-2.html: "falso positivo" do diamante
- 16-absoluto.html: RR→NNT conversion
- 17-takehome.html: 3 perguntas reformuladas
- narrative.md v2, blueprint.md v1.4

---

## 2026-03-13 — Deck completo (18 slides)

Branch: `feat/metanalise-mvp`

- 12 slides Fase 2 criados (04-rs-vs-ma ate 10-fixed-random)
- 01-hook.html reescrito: 2-beat state machine, 3 countUp
- 02-contrato.html: 3 cards framework
- 03-checkpoint-1.html: cenario MA ilustrativo
- h2 rewrite: 9 headlines → assertions tecnicas
- evidence-db.md v2: 12 refs tier 1
