# ERROR LOG — Meta-análise

> Atualizar a cada sessão. Cada erro vira regra que previne repetição.
> **Path:** `aulas/metanalise/ERROR-LOG.md` · Referência: `CHANGELOG.md`

---

## Formato

```
[ERRO-NNN] Severidade | Slide | Descrição | Root cause | Regra derivada
```

Severidades: CRITICAL (bloqueia projeção), HIGH (prejudica leitura), MEDIUM (estética), LOW (cosmético)

---

## Registro

### ERRO-001 · CRITICAL · Todos os slides
**Descrição:** Slides renderizando com fundo branco em vez de light gray (stage-c). Tokens de cor incorretos, headlines dark quando deveriam ser dark-on-light-bg, cards navy em contexto light.
**Root cause:** `<body>` em `index.html` sem `class="stage-c"`. Sem stage class, `:root` defaults aplicados → `#deck { color: var(--text-primary) }` (dark) ganha de `.slide-navy h1 { color: var(--text-on-dark) }` (light) por especificidade. `data-background-color` ignorado por deck.js (convenção Reveal.js não implementada).
**Fix:** Adicionado `class="stage-c"` ao `<body>` em `aulas/metanalise/index.html`.
**Regra derivada:** Toda nova aula DEVE ter `<body class="stage-c">` (ou `stage-a`). Sem stage class = renderização quebrada. Registrado em `tasks/lessons.md`.
**Data:** 2026-03-15

### ERRO-002 · HIGH · Todos os slides
**Descrição:** Scrollbar visível na página. Conteúdo excede viewport, slides não ficam contidos no canvas fixo 1280×720.
**Root cause 1:** `body` sem `margin: 0` — browser default `margin: 8px` empurra `#deck` (720px) para baixo, totalizando 736px com zoom.
**Root cause 2:** `<aside class="notes">` sem `display: none` em nenhum CSS. Speaker notes renderizadas como blocos de texto visíveis dentro de cada section. Embora clipped por `#deck { overflow: hidden }`, contribuem para layout.
**Fix:** Adicionado em `metanalise.css`: `body { margin: 0; overflow: hidden; }` e `aside.notes { display: none; }`.
**Regra derivada:** (1) Slides são canvas fixo — `overflow-y: hidden` obrigatório. (2) `aside.notes` DEVE ser hidden via CSS. (3) Pendência para main: mover estas regras para `shared/css/base.css` para todas as aulas.
**Data:** 2026-03-15

### ERRO-003 · HIGH · Slide 01 (hook) — ✅ CORRIGIDO
**Descrição:** Dados clínicos no hook não correspondem às referências citadas ou estão desatualizados.
**Detalhes:**
- "80/dia" → dado de 2019 (Hoffmann PMID 34091022). Em 2021 já eram ~146/dia (53.208 SRs no PubMed). Apresentar como "hoje" em 2026 é understatement significativo.
- "88% qualidade criticamente baixa" → paper citado (Siemens PMID 33741503) diz 90%, não 88%. E é específico de câncer avançado, não geral.
- "8,5% LoE A" → correto para ACC/AHA (Fanaroff PMID 30874755), mas slide não especifica que é só cardiologia. ESC = 14,2%. Dado geral (JGIM 2025): 10%.
**Root cause:** Dados inseridos sem verificação cruzada com o paper original e sem discussão com o usuário.
**Fix:** ✅ APLICADO (sessão 2026-03-16f):
- 88% → 81% (Bojcic et al. J Clin Epidemiol 2024, PMID 37931822 — 35/43 SRs, cross-field, AMSTAR-2)
- 8,5% → 10% (Qureshi et al. JGIM 2025, PMID 41428154 — 768/7.582 recomendações, 23 sociedades EUA)
- 80/dia → 146/dia: atualizado para dado de 2021 (Hoffmann PMID 34091022: 53.208 SRs em 2021). Label "SRs/dia em 2021". Beat-0 texto atualizado. Decisão Lucas (sessão 2026-03-16j)
- evidence-db.md: Bojcic/Qureshi promovidos de CANDIDATO → EM USO
- narrative.md: dados do hook atualizados
**Regra derivada:** (1) Todo dado numérico DEVE ser verificado no paper original (PMID → PubMed → abstract) antes de entrar no slide. (2) Dados devem ser discutidos com o usuário antes de serem implementados. (3) Ano do dado deve ser explicitado quando diferente do ano da aula.
**Data:** 2026-03-15 | Corrigido: 2026-03-16

### ERRO-004 · MEDIUM · Vite config
**Descrição:** `npm run dev` abria cirrose em vez de metanalise nesta worktree.
**Root cause:** `vite.config.js` tinha `open: '/aulas/cirrose/index.html'` hardcoded.
**Fix:** Trocado para `open: '/aulas/metanalise/index.html'` (quick fix WT).
**Regra derivada:** Pendência para main (Classe B): auto-detect aula via branch name em `vite.config.js`.
**Data:** 2026-03-15

### ERRO-005 · HIGH · Todos os slides (regressão de layout)
**Descrição:** Todos os h2 headings desalinhados verticalmente — posições variavam de 42px a 221px entre slides (deveriam ser consistentes a ~67px). Conteúdo empurrado para baixo em slides com menos conteúdo.
**Root cause:** `shared/css/base.css` (commit "P0 safe-center" em main) trocou `.slide-inner { justify-content: center }` por `justify-content: flex-start` + pseudo-elements `::before, ::after { flex: 1 0 0px }` para centering seguro. Pattern correto para slides com conteúdo fixo (cirrose), mas em metanalise os componentes de layout (`.compare-layout`, `.pico-grid`, `.contrato-grid`, etc) têm `flex: 1` — os spacers competem com eles, dividindo espaço em 3 partes iguais em vez de centrar.
**Fix:** Override em `metanalise.css`: (1) `justify-content: center` restaurado no `.slide-inner`, (2) `::before, ::after { display: none }` para desativar spacers. Scoped — cirrose não afetada.
**Regra derivada:** (1) Safe-center com pseudo-elements NÃO funciona quando children têm `flex: 1` — os spacers competem pelo espaço restante. (2) Sempre testar layout patterns do base.css em TODAS as aulas após merge de main. (3) Ao absorver main em WT, verificar se `.slide-inner` behavior mudou — medir h2 positions programaticamente.
**Data:** 2026-03-16

### ERRO-006 · MEDIUM · Checkpoints 03, 12
**Descrição:** Checkpoint slides sem padding superior e conteúdo desalinhado. CP1: conteúdo a 25px do topo (deveria estar centrado). CP2: cenário a -75px (acima do viewport, cortado).
**Root cause:** `.checkpoint-layout { justify-content: center; flex: 1 }` — com conteúdo que overflow, `justify-content: center` distribui espaço simetricamente, empurrando metade do overflow ACIMA do viewport. Agravado por: (a) `min-height: auto` inflando layout, (b) browser default `<p> { margin: 1em }` adicionando ~240px invisíveis, (c) `margin-top` redundante com `gap`.
**Fix:** (1) Removido `justify-content: center` do `.checkpoint-layout`, (2) `min-height: 0` para prevenir inflação, (3) `margin-top: auto` no `.checkpoint-scenario` (safe-center pattern interno), (4) `.checkpoint-layout p { margin: 0 }`, (5) removido `margin-top` redundante do `.checkpoint-question`.
**Regra derivada:** (1) `justify-content: center` em flex containers com overflow = clipping simétrico. Usar `margin-top: auto` no primeiro child em vez de `justify-content: center`. (2) Reset `p { margin: 0 }` dentro de flex layouts que usam `gap`. (3) Nunca duplicar espaçamento (`gap` + `margin`).
**Data:** 2026-03-16

### ERRO-007 · MEDIUM · Slide 01 (hook) — ✅ CORRIGIDO
**Descrição:** Source-tag (referências no rodapé) alinhada à esquerda em vez de centralizada.
**Root cause:** `.stage-c #deck p` em `shared/css/base.css` tem `max-width: 56ch` com especificidade (0,1,1,1). O seletor `#deck .source-tag` em `metanalise.css` tem (0,1,1,0) — perde a cascata. O `<p>` fica com 56ch de largura máxima, posicionado em flex-start (esquerda). `text-align: center` centraliza dentro dos 56ch, mas o elemento não é full-width.
**Fix:** Seletor bumped para `#deck p.source-tag` (0,1,1,1) — vence por cascade order (metanalise.css carrega depois de base.css). Adicionado `max-width: none; width: 100%`.
**Regra derivada:** (1) Qualquer `<p>` dentro de `#deck` herda `max-width: 56ch` de base.css. Para `<p>` que precisa ser full-width (footers, centered text), sobrescrever com `max-width: none; width: 100%`. (2) Ao debugar alinhamento, sempre verificar computed `max-width` — pode estar limitando o elemento invisívelmente.
**Data:** 2026-03-16

### ERRO-008 · CRITICAL · Todos os slides (double-scaling at fullscreen) — ✅ CORRIGIDO
**Descrição:** Slides renderizando com fontes e layout 2.25x maiores que o correto em viewports > 1280px (ex: 1920x1080 fullscreen). Cards clipped horizontalmente, h2 acima do viewport, source-tag abaixo do viewport.
**Root cause:** `body { zoom: min(100vw/1280, 100vh/720) }` em metanalise.css conflitava com `#deck { transform: translate(-50%, -50%) scale(S) }` de deck.js. Ambos escalavam para o viewport: zoom 1.5 × scale 1.5 = 2.25x. Além disso, `vw`-based clamp tokens computavam no viewport (1920), não no canvas (1280), causando double-scaling em qualquer resolução.
**Investigação:**
- Primeiro tentou-se fixar tokens de px (parcialmente correto)
- Depois fixar body width: 1280px (não resolveu — getBoundingClientRect mostrava 2880px)
- Debug do #deck revelou `style="transform: translate(-50%, -50%) scale(1.5)"` — deck.js já escalava
- CSS zoom era 100% redundante e conflitante
**Fix:**
1. **Removido** `zoom` do body em metanalise.css — deck.js handles scaling
2. **Mantido** fixed px tokens no `#deck` — `vw` units still reference viewport, not canvas
3. Selectors `#deck p.hook-question-text` e `#deck p.hook-verdict` bumped para vencer `.stage-c #deck p` de base.css
**Regra derivada:**
(1) NUNCA usar CSS `zoom` em aulas com deck.js — deck.js já aplica `transform: scale()` no `#deck`.
(2) Tokens com `vw` em clamp() computam no viewport, não no canvas escalado — usar fixed px em aulas com deck.js.
(3) Todo `<p>` dentro de `#deck` herda styles de `.stage-c #deck p` — selectors de `<p>` precisam de especificidade `#deck p.className`.
(4) Antes de adicionar zoom/scale, verificar se deck.js já escala (inspecionar `#deck.style.transform`).
**Data:** 2026-03-16

### ERRO-009 · HIGH · Checkpoints 03, 12 (contraste destruído)
**Descrição:** Checkpoint slides com `slide-navy` + `data-background-color` mas sem CSS `background-color` = texto on-dark sobre fundo light = contraste destruído. Texto praticamente invisível em projeção.
**Root cause:** Três fatores combinados:
1. `data-background-color` é convenção Reveal.js — deck.js ignora este atributo completamente.
2. `.slide-navy` em `base.css` só remapeia variáveis de texto para on-dark (não aplica `background-color`).
3. `stage-c` remapeia `--text-on-dark` para valor escuro (correto para fundo light). Resultado: texto escuro sobre fundo light, mas tokens on-dark referenciados no CSS da aula (borders, labels) ficam com valores de light-mode.
Sem regra CSS explicitando `background-color` no slide, o fundo permanece light (creme stage-c), mas texto e decoração ficam com tokens on-dark remapeados = contraste inconsistente.
**Fix:**
1. CSS override com `#s-checkpoint-1 .slide-inner, #s-checkpoint-2 .slide-inner { background-color: #162032; }` + token restoration scope (8 tokens on-dark re-declarados no seletor para sobrescrever o remap de stage-c).
2. `data-background-color` removido de TODOS os 18 slides (atributo morto em deck.js).
3. `slide-navy` removido de 16 slides light (mantido apenas em CP1 e CP2 que TÊM bg navy via CSS override).
**Regra derivada:**
(1) Slides navy em deck.js DEVEM ter background via CSS seletor de ID (`#slide-id .slide-inner { background-color: #HEX }`) — NUNCA via `data-background-color`.
(2) Quando um slide deck.js precisa de bg escuro em stage-c, DEVE incluir token restoration scope (re-declarar on-dark tokens no seletor CSS do slide) para sobrescrever o remap de stage-c.
(3) `slide-navy` só deve ser usado em slides que efetivamente têm fundo navy via CSS.
**Data:** 2026-03-17

### ERRO-010 · CRITICAL · Todos os slides
**Descrição:** Tela preta. Dev server renderiza 0 slides. `#deck` não existe no DOM. Reveal.js CSS (`section { display: none }`) injected.
**Root cause:** Vite dep cache poisoned. `node_modules/.vite/deps/` continha `reveal__js.js` pre-bundled porque `discoverEntries()` em `vite.config.js` escaneava grade/osteoporose (frozen, Reveal.js). O cache serviu inline script de outra worktree (`wt-cirrose`) com `import Reveal from 'reveal.js'`. Reveal.css colapsou todas as `<section>`.
**Fix:** (1) Removido `reveal.js` de `package.json`. (2) `FROZEN_AULAS` excluídos de `discoverEntries()` no `vite.config.js`. (3) `npm install` invalidou lockfile hash → Vite rebuild cache limpo.
**Regra derivada:**
(1) Worktrees deck.js NÃO devem ter `reveal.js` em dependencies.
(2) `vite.config.js` DEVE excluir aulas frozen/Reveal de entry discovery (`FROZEN_AULAS`).
(3) Se tela preta em dev: verificar `node_modules/.vite/deps/` por entradas inesperadas ANTES de debugar CSS.
(4) Sempre rodar `npx vite --force` ao trocar entre WTs ou após `npm install`.
**Data:** 2026-03-19

---

*Append-only. Não remover erros antigos.*
