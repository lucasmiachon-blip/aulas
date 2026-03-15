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

### ERRO-003 · HIGH · Slide 01 (hook)
**Descrição:** Dados clínicos no hook não correspondem às referências citadas ou estão desatualizados.
**Detalhes:**
- "80/dia" → dado de 2019 (Hoffmann PMID 34091022). Em 2021 já eram ~146/dia (53.208 SRs no PubMed). Apresentar como "hoje" em 2026 é understatement significativo.
- "88% qualidade criticamente baixa" → paper citado (Siemens PMID 33741503) diz 90%, não 88%. E é específico de câncer avançado, não geral.
- "8,5% LoE A" → correto para ACC/AHA (Fanaroff PMID 30874755), mas slide não especifica que é só cardiologia. ESC = 14,2%. Dado geral (JGIM 2025): 10%.
**Root cause:** Dados inseridos sem verificação cruzada com o paper original e sem discussão com o usuário.
**Fix:** PENDENTE — aguardando decisão do Lucas sobre novos números e referências.
**Regra derivada:** (1) Todo dado numérico DEVE ser verificado no paper original (PMID → PubMed → abstract) antes de entrar no slide. (2) Dados devem ser discutidos com o usuário antes de serem implementados. (3) Ano do dado deve ser explicitado quando diferente do ano da aula.
**Data:** 2026-03-15

### ERRO-004 · MEDIUM · Vite config
**Descrição:** `npm run dev` abria cirrose em vez de metanalise nesta worktree.
**Root cause:** `vite.config.js` tinha `open: '/aulas/cirrose/index.html'` hardcoded.
**Fix:** Trocado para `open: '/aulas/metanalise/index.html'` (quick fix WT).
**Regra derivada:** Pendência para main (Classe B): auto-detect aula via branch name em `vite.config.js`.
**Data:** 2026-03-15

---

*Append-only. Não remover erros antigos.*
