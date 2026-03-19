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
**Descrição:** 3 dados do hook incorretos/desatualizados (80/dia, 88%, 8.5%).
**Fix:** 80→146/dia (Hoffmann 2021), 88→81% (Bojcic PMID 37931822), 8.5→10% (Qureshi PMID 41428154).
**Regra derivada:** Todo dado numérico DEVE ser verificado no paper original antes de entrar no slide. Discutir com usuário. Explicitar ano do dado.
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
**Descrição:** Layout 2.25x maior que correto em fullscreen (zoom × scale = double-scaling).
**Root cause:** CSS `zoom` em body conflitava com deck.js `transform: scale()`. `vw` tokens computavam no viewport, não no canvas.
**Fix:** Removido `zoom` do body. Mantido fixed px tokens. Selectors `<p>` bumped para vencer base.css.
**Regra derivada:** (1) NUNCA `zoom` com deck.js (já escala via transform). (2) Usar fixed px, não `vw`, em aulas deck.js. (3) `<p>` em `#deck` herda de `.stage-c #deck p` — precisa de especificidade `#deck p.className`.
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

### Nota: codigos cross-project

Alguns docs (CHANGELOG, AUDIT-VISUAL) referenciam ERRO-034 (data-background-color em deck.js). Este codigo vive em `aulas/cirrose/ERROR-LOG.md`. Equivalente local: ERRO-009 (mesma root cause, contexto metanalise).

---

*Append-only. Não remover erros antigos.*
