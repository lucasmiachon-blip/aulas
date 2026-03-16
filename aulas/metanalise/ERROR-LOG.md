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
- 80/dia: mantido (Hoffmann PMID 34091022) com contexto temporal: "só em 2019" no beat-0 + label "SRs/dia em 2019"
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

---

*Append-only. Não remover erros antigos.*
