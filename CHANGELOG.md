# Changelog — aulas-magnas

## [Unreleased]

### Added (2026-03-17 — Gemini MCP)
- **.cursor/mcp.json:** Servidor `gemini` adicionado (`@rlabs-inc/gemini-mcp`). Usa `GEMINI_API_KEY` do env — key não fica no repo.

### Changed (2026-03-17 — MCP cleanup)
- **.mcp.json:** Simplificado de ~30 servers para 5 npx-only (a11y-contrast, a11y, lighthouse, frontend-review, frontend-design-audit). Removidos todos `uvx`-based (biomcp, pubmed-simple, zotero, semantic-scholar, arxiv) — Windows Defender bloqueava executáveis Python.

### Fixed (2026-03-17 — Diagnóstico MDs: 8 correções)
- **package.json:** Removida chave duplicada `build:metanalise` (echo sobrescrevia script PowerShell). `npm run build:metanalise` agora executa build-html.ps1.
- **README.md:** "12 slides" → "18 slides" (metanalise).
- **docs/metanalise-scope.md:** Âncora [TBD] → Valgimigli 2025 (Lancet, PMID 40902613).
- **CLAUDE.md:** Removido "build script pendente" da tabela metanalise.
- **.cursor/rules/slide-identity.mdc:** `build:cirrose` → `build:{aula}` (5 ocorrências) + legenda {aula}.
- **docs/XREF.md:** slide-identity referencia deck-patterns.md (removido reveal-patterns obsoleto).
- **tasks/lessons.md:** Lição build:metanalise atualizada — RESOLVIDO, regra genérica.
- **docs/archive/AGENTS.md:** Banner ARQUIVADO (mar/2026, superseded por CLAUDE.md).

### Changed (2026-03-16i — Notion sync completo: Slides + References DB)
- **Notion Slides DB:** 18/18 slides sincronizados (13 atualizados, 5 criados). Campos: Headline PT, Speaker Notes, Pipeline Status, Visual QA, Tipo, Animação, Checkpoint, Objetivo Cognitivo, Tempo, PMID, Effect Size, IC 95%, GRADE Certainty, NNT/NNH.
- **Notion References DB:** 25 novas entries criadas + 2 existentes atualizadas (Hoffmann, Lakhlifi). Todas com Citation AMA, PMID, DOI, Year, Journal, Aula, Evidence Level, Tier, Tipo Ref, Relevância.
- `HANDOFF.md`: sessão 2026-03-16i documentada.
- Pendente: limpeza duplicata Lakhlifi no Notion References DB.

### Fixed (2026-03-16h — hook layout: centering + spacing)
- `metanalise.css`: `.hook-data` container added (flex column, `align-items: center`, `width: 100%`) — verdict centers under numbers.
- `metanalise.css`: `.hook-data-grid` gets `width: 100%` — grid spans full slide width.
- `metanalise.css`: `.hook-data-item` gets `flex: 1; min-width: 0` — 3 equal-width columns for symmetric horizontal centering.
- `metanalise.css`: `.hook-question` changed from `justify-content: center` to flex-start — question text sits higher.
- `metanalise.css`: verdict `margin-top: 80px` — visual separation from numbers grid.
- `metanalise.css`: grid gap reduced `--space-lg` → `--space-md` (40→24px) — tighter grouping.
- Verified at 1920x1080 on stage-c (cream bg, dark text).

### Fixed (2026-03-16g — ERRO-008: double-scaling at fullscreen)
- **Root cause:** CSS `zoom` on body conflicted with deck.js `transform: scale()` — 1.5 × 1.5 = 2.25x. Cards clipped, h2 above viewport, source-tag below.
- `metanalise.css`: removed `body { zoom }` entirely — deck.js handles viewport scaling.
- `metanalise.css`: fixed px token overrides retained (`--text-h2: 34px` etc.) — `vw` clamp still double-scales via viewport reference.
- `metanalise.css`: `#deck p.hook-question-text` and `#deck p.hook-verdict` selectors bumped for specificity vs `.stage-c #deck p`.
- `ERROR-LOG.md`: ERRO-008 documented with investigation trail and 4 derived rules.
- Verified at 1920x1080: all 3 slides (title, hook, contrato) render correctly.

### Changed (2026-03-16f — QA slide-a-slide: s-hook)
- `metanalise.css`: source-tag selector bumped to `#deck p.source-tag` + `max-width: none; width: 100%` — fixes left-alignment caused by `.stage-c #deck p { max-width: 56ch }` in base.css.
- `01-hook.html`: beat-0 text "publicadas hoje" → "por dia — só em 2019" (Hoffmann data is from 2019; ~146/dia by 2021). Label "SRs por dia" → "SRs/dia em 2019".
- `01-hook.html`: speaker notes updated — growth context (80→146/dia) + verification date.
- `index.html`: mirror of all hook changes.
- `AUDIT-VISUAL.md`: s-hook scorecard updated — 4 new fixes + serif font legibility as Gemini pendency.
- `evidence-db.md`: Bojcic/Qureshi promoted CANDIDATO → EM USO (v4.1).
- `narrative.md`: hook data refs updated (was [TBD]).

### Changed (2026-03-16e — QA slide-a-slide: s-title)
- `metanalise.css`: title slide tokens corrigidos para stage-c — `--text-on-dark-*` → `--text-secondary/primary/muted`. Pilares peso 400→500 (legibilidade projetor).
- `AUDIT-VISUAL.md`: CRIADO — scorecard 14 dimensões, s-title PASS. Pendências Gemini anotadas.

### Changed (2026-03-16d — housekeeping + ERRO-003 research)
- Deleted `PROMPT-SCALING-MAIN.md` (temporary file, already executed on main + absorbed via merge).
- `aulas/metanalise/ERROR-LOG.md`: ERRO-003 updated with 2 verified candidate PMIDs (Bojcic 37931822, Qureshi 41428154). Slide implementation pending Lucas decision.
- `aulas/metanalise/references/evidence-db.md`: added Bojcic 2024 (PMID 37931822) and Qureshi 2025 (PMID 41428154) as hook data candidates (CANDIDATO tag).
- `aulas/metanalise/HANDOFF.md`: session summary + pending decisions for Lucas documented.

### Fixed (2026-03-17 — Achados audit-rules e docs-audit)
- `aulas/cirrose/ERROR-LOG.md`: ERRO-033 (stopPropagation) e ERRO-034 (data-background-color deck.js) registrados — refs em slide-editing.md agora válidas.
- `docs/README.md`: link metanalise HANDOFF → CLAUDE.md (HANDOFF pendente); link grade HANDOFF adicionado; osteoporose em backlog.
- `docs/XREF.md`: seção metanalise — HANDOFF.md marcado como pendente.

### Added (2026-03-17 — Docs audit)
- `docs/docs-audit-report-2026-03-17.md`: relatório de auditoria docs/*.md (batches 1–4). Links, redundancy, verbosity, tokens, structure.

### Added (2026-03-16 — Max security: 7 Guards + back-port Class B)
- `scripts/pre-commit.sh`: Guard 5 — bloqueia Classe A/B (governança/infra) em feature branches. Bypass: `ALLOW_AB_ON_WT=1`.
- `.cursor/rules/slide-identity.mdc`: back-port de cirrose — regra 9-superfícies (176 linhas).
- `README.md` root: back-port de cirrose — quick start, stack, links.
- `docs/XREF.md`: back-port de cirrose — Guards 1-4 documentados, post-merge.sh.
- `core-constraints.mdc`: ERROR-LOG path corrigido para `aulas/*/ERROR-LOG.md`.
- `CLAUDE.md`: `tasks/lessons.md` na tabela Classe A, slide-identity ref adicionada.
- `.gitignore`: `*.png` na raiz (screenshots de debug).

### Changed (2026-03-16d — A/B sync WT↔main)
- Merged main into feat/metanalise-mvp: post-merge hook (Guard 4), JS deck scaling, design-system flex-start, lessons.md QA Metanalise session.
- Fixed docs/XREF.md: added metanalise HANDOFF to root CLAUDE.md reference table.
- Fixed docs/README.md: grade/osteoporose HANDOFFs now use markdown links (consistency).

### Fixed (2026-03-16 — Governança: anti-crosspath rule)
- `core-constraints.mdc`: regra "Isolamento de workspace" — agente em main NUNCA editar arquivos em `../wt-*` via paths absolutos.
- `CLAUDE.md`: regra "Anti-crosspath" no Worktree Protocol.
- `tasks/lessons.md`: 5 lições da sessão (scaling, GSAP overflow, flex-wrap, slide-integrity, violação worktree).

### Fixed (2026-03-16c — fullscreen zoom + MCP cleanup)
- `metanalise.css`: `body { zoom: min(calc(100vw / 1280px), calc(100vh / 720px)); }` — deck fills screen on any aspect ratio (16:10, 3:2, etc). Pending for main via base.css.
- `.cursor/mcp.json`: removed 5 uv/uvx-based MCPs (biomcp, pubmed-simple, zotero, semantic-scholar, arxiv) — Windows Defender blocks uv-spawned Python executables. All npx/node MCPs retained.
- Deleted `scripts/fix-defender.ps1` (temporary, already used).

### Fixed (2026-03-16 — JS deck scaling + anti-rollback hook)
- `shared/css/base.css`: CSS `zoom` substituido por `transform: scale()` via JS. `#deck` agora `position: absolute` centralizado.
- `shared/js/deck.js`: `scaleDeck()` com `Math.min(w/1280, h/720)` + `translate(-50%,-50%)`. Handles resize + fullscreen.
- `scripts/post-merge.sh`: Guard 4 — detecta slide count loss E alteracoes de conteudo HTML apos merge (anti-rollback silencioso).
- `scripts/install-hooks.sh`: instala post-merge hook.

### Fixed (2026-03-16 — P0 safe-center: elimina clipping simétrico)
- `shared/css/base.css`: `.slide-inner` `justify-content: center` → `flex-start` + pseudo-elements `::before/::after { flex: 1 0 0px }` para centering seguro. Conteúdo centra quando cabe; quando extravasa, overflow é apenas na base (preserva h2 e "ATO" no topo). 3 slides que tinham overflow marginal (meld, a3-06, app-alb) agora cabem perfeitamente.

### Fixed (2026-03-16 — Fullscreen zoom + letterbox) [SUPERSEDED by JS scaling above]
- `shared/css/base.css`: zoom simplificado para width-only `calc(100vw / 1280px)` (alinha com metanalise).
- `shared/css/base.css`: `html { background: var(--bg-black) }` — letterbox preto explícito.
- `shared/css/base.css`: removido `background: var(--bg-surface)` do body — causava ilusão de "conteúdo cortado" em monitores 16:10 (letterbox cream indistinguível do slide).

### Fixed (2026-03-16 — Full revert of destructive safe-center commit 5222929)
- `shared/css/base.css`: reverted all 3 destructive rules from commit 5222929:
  (1) `justify-content: flex-start` → restored to `center`
  (2) `::before/::after { flex: 1 0 0px }` pseudo-element spacers removed
  (3) `> * { flex-shrink: 0 }` removed
  Efeitos: metanalise h2 variava 42-221px; cirrose layout quebrado com scroll/clipping.
- `shared/css/base.css`: `html { background: #000 }` — letterbox preto ao redor do deck.

### Added (2026-03-16 — 3 worktree guards no pre-commit)
- `scripts/pre-commit.sh`: Guard 2 — bloqueia edits em `shared/` em worktrees (bypass: `ALLOW_SHARED_EDIT=1`).
- `scripts/pre-commit.sh`: Guard 3 — bloqueia commit se slide count em disco < manifest (catches silent rollback após merge, bypass: `ALLOW_SLIDE_LOSS=1`).

### Fixed (2026-03-16 — P0 safe-center: elimina clipping simétrico) [REVERTED]
- `shared/css/base.css`: `.slide-inner` `justify-content: center` → `flex-start` + pseudo-elements. **Totalmente revertido acima** — causava layout quebrado em ambos projetos.

### Fixed (2026-03-16b — h2 alignment: override base.css safe-center for metanalise)
- `metanalise.css`: restored `justify-content: center` on `.slide-inner` — base.css safe-center pseudo-elements (`::before/::after { flex: 1 }`) competed with `flex: 1` content components (compare-layout, pico-grid, etc), causing h2 headings to shift 100-180px down and vary between slides
- `metanalise.css`: `::before, ::after { display: none }` — disables safe-center spacers for metanalise (cirrose still uses them from base.css)
- Result: 16/16 h2 slides now at consistent 67px from top (was 42-221px, inconsistent). Checkpoints unaffected (own safe-center pattern)
- Root cause: base.css commit "P0 safe-center" changed `justify-content: center` → `flex-start` + spacers. This is correct for fixed-content slides (cirrose) but breaks metanalise where layout components have `flex: 1`, making spacers share remaining space 3 ways instead of centering content

### Fixed (2026-03-16a — checkpoint padding + heading alignment)
- `metanalise.css`: `.checkpoint-layout` — removed `justify-content: center` (caused center-overflow pushing content above viewport), added `min-height: 0` (prevents flex min-height: auto from inflating layout past 640px container)
- `metanalise.css`: `.checkpoint-scenario` — added `margin-top: auto` (safe-center: centers when content fits, collapses to 0 when it overflows)
- `metanalise.css`: `.checkpoint-layout p { margin: 0 }` — resets browser default `margin: 1em` on `<p>` elements inside flex layout (was adding ~240px of hidden vertical space)
- `metanalise.css`: `.checkpoint-question` — removed redundant `margin-top: var(--space-md)` (double-counted with layout `gap`)
- CP1: content now perfectly centered (scrollHeight 640 = available space); before: 42px overflow, content at 25px from top
- CP2: scenario at 40px from top (was -75px, literally clipped above viewport); verdict now visible at 682px (was clipped)

### Fixed (2026-03-15j — scroll fix + notes hiding)
- `aulas/metanalise/metanalise.css`: added `body { margin: 0; overflow: hidden; }` — eliminates scrollbar caused by browser default 8px margin
- `aulas/metanalise/metanalise.css`: added `aside.notes { display: none; }` — hides 18 speaker notes that were rendered as visible text blocks (no CSS existed for notes in entire codebase)

### Added (2026-03-15j — ERROR-LOG + data audit)
- `aulas/metanalise/ERROR-LOG.md`: created with 4 errors (ERRO-001 to ERRO-004): stage-c missing, scroll/notes, hook data mismatch, vite config
- `tasks/lessons.md`: 3 lessons added (stage class required, deck.js ignores data-background-color, CSS specificity #id > .class)
- Hook data audit: identified 3 data issues — 80/day outdated (2019→2021 ~146/day), 88% doesn't match paper (Siemens=90%, cancer-only), 8.5% domain-specific (ACC/AHA only). Fix pending user decision.

### Fixed (2026-03-15i — stage-c rendering fix)
- `aulas/metanalise/index.html`: added `class="stage-c"` to `<body>` — fixes white-bg rendering (tokens now remap correctly for Plan C light mode)
- Root cause: missing stage class → `:root` defaults → `#deck` color won over `.slide-navy`, `data-background-color` ignored by deck.js, cards used dark navy in light context
- `vite.config.js`: `open` path changed to `/aulas/metanalise/index.html` (WT-scoped quick fix)

### Fixed (2026-03-15h — MD audit para merge seguro)
- `CLAUDE.md` (root): tabela Projects metanalise 15→18 slides; público generalizado (não só hepatologistas)
- `aulas/metanalise/CLAUDE.md`: Fase 3 [TBD] → Valgimigli 2025
- `aulas/metanalise/HANDOFF.md`: bloqueios HEX navy e CSS órfão marcados resolvidos; repo janitor WARN atualizado
- `aulas/metanalise/references/blueprint.md`: header Fase 3 atualizado (Valgimigli decidido); remoção de "decisão pendente"
- `docs/README.md`: HANDOFF metanalise adicionado à hierarquia
- `docs/XREF.md`: seção metanalise expandida (HANDOFF, narrative, evidence-db, blueprint, _manifest.js); manifesto metanalise na tabela canônicos

### Added (2026-03-15g — Meta-análise QA loop + infra)
- `aulas/metanalise/slides/_manifest.js`: source of truth — 18 slides, fases F1/I1/F2/I2/F3, headlines, timing, customAnim
- `aulas/metanalise/references/sources/README.md`: convenção de nomes para full-text PDFs (gitignored)
- `.gitignore`: `**/references/sources/*.pdf`

### Changed (2026-03-15g — Meta-análise cleanup)
- `aulas/metanalise/metanalise.css`: removidas 8 classes CSS órfãs (scope-layout/col/label/item/out, pipeline-number, hook-question-sub)
- `aulas/metanalise/CLAUDE.md`: status atualizado 15→18 slides
- `aulas/metanalise/references/evidence-db.md`: Musini reclassificado como "exemplo visual" (âncora = Valgimigli)
- `aulas/metanalise/references/narrative.md`: changelog v2.2 (Valgimigli decidido)
- `aulas/metanalise/HANDOFF.md`: caminho crítico atualizado (QA batches 2-6 pendentes)

### Fixed (2026-03-14 — P0 document scroll + section clipping)
- `shared/css/base.css`: added `html, body { margin: 0; padding: 0 }` — eliminates 16px document scroll from browser default margins.
- `shared/css/base.css`: removed `overflow: hidden` from `#slide-viewport > section` (commit 8683c45) — causava clipping de conteúdo no bottom de 5+ slides. Viewport já provê clipping.

### Added (2026-03-14 — Classe C guard)
- `scripts/pre-commit.sh`: hook versionado que bloqueia commits de conteúdo (slides, CSS, JS, references) em `main`. Bypass: `ALLOW_MAIN_CONTENT=1`.
- `scripts/install-hooks.sh`: atualizado para delegar pre-commit a `scripts/pre-commit.sh` (mesmo padrão do pre-push).
- `docs/SETUP.md`: seção 1b documentando instalação de hooks.

### Fixed (2026-03-14 — Doc chain hardening)
- `CLAUDE.md`: adicionados `lint:case-sync` e `lint:narrative-sync` nos Commands; Worktree Protocol com Classe C guard e hook install.
- `docs/XREF.md`: skills 13→18; seção `scripts/` (git hooks versionados); seção `aulas/metanalise/`; data revisão 03-14.
- `docs/README.md`: metanalise adicionada em Estado/handoff e HANDOFFs hierarchy.
- `tasks/lessons.md`: lições Classe C guard + metanalise invisível.

### Fixed (2026-03-05 — Bloco 1 HTML fixes)
- `aulas/cirrose/slides/06-a1-etiologias.html` (I4): redesign completo — tabela 3→10 etiologias em grid 2×5 compacto com `etio-grid`; Álcool/MASLD/HCV destacados; `archetype-metrics` adicionado
- `aulas/cirrose/slides/05-a1-infeccao.html` (I3+S3): `archetype-metrics` adicionado para fill ratio; stagger delay 0.3→0.2
- `aulas/cirrose/cirrose.css` (I4): adicionado `.etio-grid` + `.etio-item` + `.etio-item--major` + `.etio-name` + `.etio-tx` (grid 2×5 compacto)
- `.gitignore`: adicionado `.playwright-mcp/`

### Fixed (2026-03-05 — Docs cleanup + D'Amico CSS bug)
- `aulas/cirrose/cirrose.css`: 1-char CSS bug `#s-a1-damico.archetype-flow` → `#s-a1-damico .archetype-flow` (descendant selector was broken — grid-template-rows never applied to D'Amico slide)
- `aulas/cirrose/AUDIT-VISUAL.md`: trimmed 574→479 lines — added SYS-1/2/3 systemic issues block; condensed 28 per-slide sections to use SYS-N references and backlog IDs instead of verbose repetitions
- `docs/biblia-narrativa.md`: added Índice TOC (9 sections); replaced duplicated NNT/NNH table with link to canonical `evidence-db.md`
- `aulas/cirrose/HANDOFF.md`: marked priority #5 (conflicts) as DONE — 7 pairs verified, no conflicts found

### Added (2026-03-05 — Análise HTML externo)
- `docs/insights-html-cirrose-2026.md`: Análise de HTML Gemini (18 slides), 14 trials 2025 a verificar, insights de interação priorizados, QA visual via Playwright (21 screenshots)

### Removed (2026-03-05 — Codebase health cleanup)
- `aulas/cirrose/index.stage-b.html` — deprecated Plan B entry point (46 KB)
- `aulas/cirrose/index.stage-c.html` — deprecated entry point, replaced by modular `index.html` (52 KB)
- `aulas/cirrose/scripts/split-slides.js` — one-off migration script, dependent on deleted stage-c
- `scripts/transcribe-lecture.js` — one-off transcript tool, not in build pipeline (14 KB)
- `scripts/qa-pdf-stage-b.js` — QA for deprecated Stage B (1.6 KB)
- `scripts/migrate-grade-slides.js` — one-off migration, complete (4.5 KB)
- `scripts/migrate-osteoporose-slides.js` — one-off migration, complete (5.5 KB)
- `package.json`: removed `"transcribe"` script entry

### Fixed (2026-03-05 — Data conflict + dedup)
- `docs/biblia-narrativa.md`: Cr 3,1 → Cr 2,8 for CP2 (lines 24, 154) — aligned with `_manifest.js` and `14-cp2.html`
- `aulas/cirrose/references/narrative.md`: same Cr fix (lines 82, 119)
- `docs/biblia-narrativa.md`: replaced duplicated "TABELA DE EVIDENCIAS" and "TBDs RESOLVIDOS" sections with links to canonical `evidence-db.md`
- `scripts/export-pdf.js`: removed Plan B (`index.stage-b.html`) from PDF export loop
- `CLAUDE.md`, `AGENTS.md`, `aulas/cirrose/CLAUDE.md`: removed references to deleted files

### Added (2026-03-04 — Flip patch + QA fixes)
- `slide-registry.js`: importou `Flip` from 'gsap/Flip'; `advance()` captura `Flip.getState(formulaBlock)` antes de `showEra(5)`; `runEra5Anims(preFlipState)` usa `Flip.from → fireCountUps` com fallback `gsap.from`
- `index.template.html`: import `Flip` + `gsap.registerPlugin(SplitText, Flip)`

### Fixed (2026-03-04 — QA visual — panel overlap + Era 5 layout)
- `archetypes.css`: `--panel-width` de 140px → 200px; `.reveal.has-panel .slide-inner` agora left-aligned (`margin: 0 0 0 2rem`) com `max-width: calc(100% - var(--panel-width) - 3rem)` — elimina sobreposição de headline com case-panel em todos os slides
- `archetypes.css`: `.case-panel .panel-field-value` font-size 15px → 13px + `text-align: right` — evita transbordamento de valores longos
- `cirrose.css`: `.damico-dataset .pathway-track { display:flex }` + `.damico-dataset .pathway-stage { flex:1; flex-direction:column }` — Era 5 layout horizontal corrigido (antes herdava `display:block` do `archetype-flow`)
- `cirrose.css`: `.scores-era { overflow-y: hidden }` (era `auto`) — elimina scrollbar em Era 1 (CTP limitações) e Era 5
- `cirrose.css`: `.scores-limitations { gap:4px; margin-top: var(--space-xs) }` + `.limitation { padding:4px var(--space-sm) }` — compacta limitações CTP para caber na track de 720px
- `cirrose.css`: `.scores-era[data-era="5"] { gap:4px }` + `.damico-dataset .pathway-value { font-size: var(--text-small) }` — compacta Era 5 para acomodar dois datasets
- `slides/_manifest.js`: `stage: 'cACLD → CSPH'` → `'cACLD/CSPH'` — corrige truncamento no panel-field

### BUG CONHECIDO (não corrigido — ver HANDOFF)
- `cirrose.css` linha 1823: `#s-a1-damico.archetype-flow` (sem espaço) nunca casa → `grid-template-rows: auto auto 1fr auto` não aplica → scores-era-track fica em `height: auto` (~267px) → Era 5 dataset 2014 clippado. Fix: adicionar espaço → `#s-a1-damico .archetype-flow`

### Added (2026-03-04 — Screening + Escores Prognósticos)
- `aulas/cirrose/slides/02c-a1-screening.html` — Novo slide "Rastreamento cACLD" (5 estados, archetype-flow); PMID 38934697; âncora narrativa Antônio
- `aulas/cirrose/slides/02b-a1-damico.html` — Reescrito como "Escores Prognósticos": 6 eras Child→CTP→MELD→MELDNa→MELD3.0→D'Amico; 4 limitações CTP em stagger; PMIDs 4541913, 11172350, 16697729, 34481845
- `_manifest.js`: slot `s-a1-screening` inserido entre damico e fib4; 30 slides total
- `slide-registry.js`: `s-a1-screening` adicionado (CountUp 83%, stagger critérios, flipIn cards); `s-a1-damico` reescrito (6 eras, era-swap state machine, reset na re-entrada)
- `cirrose.css`: CSS `screening-*`, `scores-era-*`, `limitation-*`, `scores-formula`, `ctp-class`, failsafes Plan B
- `evidence-db.md`: PMID 38934697 + nota TBD CTP interobserver

### Fixed
- `s-a1-screening`: justify-content:center → flex-start (overflow não empurrava headline acima do viewport)
- `slide-registry.js`: reset de display/opacity no init das funções para evitar persistência de estado em re-entrada de slide

### Added (previous)
- `tasks/PLAN-AUDIT-PENDING.md` — Plano execução paralela (4 tracks)
- `tasks/NNT-IC95-REPORT.md` — Relatório IC 95% NNT (6 slides)
- `docs/AUDIT-BATCHES.md` — Relatório auditoria em batches
- `docs/README.md` — Índice docs por propósito
- `tasks/lessons.md` — Padrões aprendidos
- `.cursor/rules/motion-qa.mdc`, `reveal-patterns.mdc`, `design-system.mdc` (migrados de .claude)
- `.claude/rules/README.md`, `.claude/skills/README.md` — Avisos depreciação
- base.css: tokens `--shadow-subtle`, `--shadow-soft`, `--overlay-border`
- `docs/ECOSYSTEM.md` — Registro de ferramentas, MCPs, GitHub
- `tasks/todo.md` — Checklist auditoria batches
- `docs/prompts/weekly-updates.md` — Prompt para busca semanal de atualizações
- `docs/SKILLS.md` — Melhores práticas para Cursor skills
- `docs/RULES.md` — Melhores práticas para Cursor rules
- `docs/SUBAGENTS.md` — Melhores práticas para subagents (mcp_task)
- core-constraints.mdc: regra Context Window (≥70% informar, ≥85% recomendar, ≥95% parar)
- docs/README.md: MD Auditoria via skill/subagent (não manual)
- .cursor/skills/docs-audit/, .claude/skills/docs-audit/: reescrito conforme best practices mar/2026 (Anthropic, Cursor, OpenAI). SKILL.md conciso + reference.md progressive disclosure. Espelho para Claude Code.
- docs/SUBAGENTS-PROPOSAL.md: proposta consolidada (Cursor, Opus, Anthropic). Verifier adicionado. agents/README.md: pipeline humano ≠ subagents.
- .claude/commands/audit-docs.md: comando /audit-docs

### Changed
- CLAUDE.md: Repo Structure (archetypes/cirrose em aulas/*/), hierarquia docs
- meld-calc.js: removidos fallbacks HEX
- base.css: card-metric, slide-figure — oklch → var(--shadow-*)
- preview.html: section erro com notes
- medical-data.mdc, slide-editing.mdc, css-errors.mdc: conteúdo ampliado
- docs/SKILLS.md: tabela skills
- docs/archive/README.md: descrição
- docs/RULES.md, docs/SUBAGENTS.md: referência Context Window
- docs/SYNC-NOTION-REPO.md: autoridade em conflito — Composer/Opus prevalece
- notion-mcp.mdc: IDs referenciam SYNC-NOTION-REPO; regra de conflito
- `aulas/cirrose/HANDOFF.md` — Próxima sessão: auditoria batches
- `aulas/cirrose/HANDOFF-CLAUDE-AI.md` — Próxima sessão
- `docs/HANDOFF.md` — Próxima sessão, data 03/mar
- `.cursor/rules/cirrose-design.mdc` — Tokens alinhados com base.css (--bg-surface, --safe, --warning, --danger)
- `.cursor/rules/core-constraints.mdc` — Description preenchida
- `.cursor/rules/medical-data.mdc` — Description preenchida
- `.cursor/rules/css-errors.mdc` — Description refinada
- `.cursor/rules/design-principles.mdc` — Description com referência docs
- `.cursor/skills/medical-slide/SKILL.md` — Referência docs/SKILLS.md
- `.cursor/skills/visual-qa/SKILL.md` — Referência docs/SKILLS.md
- docs/SKILLS.md, RULES.md: links ~/.cursor/ substituídos por nota (paths externos)
- docs/README.md: archive/ → archive/README.md
- .claude/skills/docs-audit/: stub, fonte canônica em .cursor
- CLAUDE.md, docs/SETUP.md, docs/ECOSYSTEM.md: datas/paths generalizados
- 09-a2-tips, 21-app-tips: NNT 4 com IC 95% 2,1–50 (García-Pagán 2010)

### Fixed
- lint:slides — 6 erros (NOTES preview, COLOR base.css) resolvidos
