# Deck.js Patterns — Navigation + GSAP

> Canonico para: slides deck.js (cirrose, metanalise). Speaker notes, click-reveal, data-animate.
> Codigo vive em `shared/js/engine.js` + `shared/js/deck.js` + `shared/js/click-reveal.js`.
> Reveal.js legacy (grade, osteoporose): ver [reveal-legacy](reveal-legacy.md).
> Relacionados: [slide-editing](slide-editing.md) · [design-system](design-system.md) · [motion-qa](motion-qa.md)

---

## Import

```js
import { initDeck } from '../../shared/js/deck.js';
import { initAula, createAnimationDispatcher } from '../../shared/js/engine.js';
```

---

## Estrutura de Slide

```html
<section id="s-a1-damico">
  <div class="slide-inner slide-navy">
    <h2>Carvedilol reduz HVPG em 20% vs placebo</h2>
    <div class="evidence" data-animate="stagger">
      <!-- evidencia visual aqui -->
    </div>
  </div>
  <aside class="notes">
    [0:00-0:30] Hook.
    PAUSA 3s.
    [DATA] Fonte: EASL 2024 | Verificado: 2026-02-13
  </aside>
</section>
```

### Regras
- `<h2>` = assercao (NUNCA rotulo generico)
- `<aside class="notes">` obrigatorio em TODO `<section>`
- NUNCA inline style com `display`/`visibility`/`opacity` no `<section>` (E07)
- **Background escuro:** CSS `background-color` com seletor `#slide-id .slide-inner` no arquivo CSS da aula. deck.js NAO parseia `data-background-color`.
- `.slide-navy` no `.slide-inner` quando bg escuro
- Todo `<section>` DEVE ter `id` seguindo convencao `s-{act}-{slug}` (ver [slide-identity](slide-identity.md))

---

## Animacao Declarativa (data-animate)

**NUNCA gsap.to() inline em slide.** Usar atributos declarativos:

```html
<span class="hero-number" data-animate="countUp" data-target="25">0</span>
<div class="cards" data-animate="stagger">...</div>
<svg><path data-animate="drawPath" d="M0,0 L100,50"/></svg>
<div data-animate="fadeUp">...</div>
```

Engine detecta e orquestra via evento `slide:entered`.

### Tipos disponiveis
| `data-animate` | Efeito | Atributos extras |
|----------------|--------|-----------------|
| `countUp` | Numero animado (1.5s, power2.out) | `data-target="25"` `data-decimals="1"` (opcional) |
| `stagger` | Filhos entram sequenciais (0.5s each) | `data-stagger="0.15"` (opcional, default 0.15) |
| `drawPath` | SVG stroke progressivo (1.5s) | — |
| `fadeUp` | Fade + translate Y (0.8s) | — |
| `highlight` | Von Restorff — destaca linha, desfoca resto | `data-highlight-row="3"` |

### Von Restorff Pattern (destaque seletivo)
```html
<table class="tufte" data-animate="highlight" data-highlight-row="3">
  ...
</table>
```
Engine: no `slide:entered`, aplica opacidade 0.35 em todas as linhas exceto a alvo, que recebe scale 1.02.

### CSS Failsafe
```css
[data-animate] { opacity: 0; }
.no-js [data-animate] { opacity: 1; }
```

---

## Click-Reveal (substitui Fragments)

deck.js usa `data-reveal` + `ClickReveal` class em vez de fragments Reveal.js.

```html
<div data-reveal="1">Primeiro (hidden ate click/arrow)</div>
<div data-reveal="2">Segundo</div>
<div data-reveal="3">Terceiro</div>
```

- `data-reveal="N"` define ordem de revelacao (N = inteiro, menor primeiro)
- Arrow right / click avanca um reveal de cada vez
- PageDown pula todos os reveals do slide
- Ao sair do slide, reveals sao resetados
- Maximo 4 reveals por slide (Cowan 4+-1)

### CSS
```css
[data-reveal] { opacity: 0; transform: translateY(8px); }
[data-reveal].revealed { opacity: 1; transform: none; }
```

### Click handlers em slides
Click handlers DENTRO de slides devem usar `stopPropagation()` para nao propagar ao nav layer do deck.js.

---

## Eventos deck.js

| Evento | Quando | Usar para |
|--------|--------|-----------|
| `slide:changed` | Imediato ao navegar | Cleanup: `ctx.revert()`, clear timers |
| `slide:entered` | Apos CSS transition (+ fallback 600ms) | Iniciar animacoes |

### Diferenca vs Reveal.js
- `slide:changed` = equivalente a `slidechanged` do Reveal
- `slide:entered` = equivalente a `slidetransitionend` do Reveal
- Todos os slides existem no DOM o tempo todo (sem `viewDistance` recycling)
- Eventos disparam no `document` (nao no deck instance)

### Custom Animations
```js
const dispatcher = createAnimationDispatcher(gsap);
dispatcher.registerCustom('s-a1-damico', (slide, gsap) => {
  // custom animation logic
});
dispatcher.connect(); // APOS registerCustom
```

**IMPORTANTE:** `registerCustom` (via `wireAll` no slide-registry.js) DEVE ser chamado ANTES de `connect()`.

---

## Appendice (modo residencia)

```html
<section class="appendix" data-visibility="hidden">
  <!-- hidden = removido do deck em congress -->
  <!-- ?mode=residencia: engine.js remove o atributo ANTES do init -->
</section>
```

**IMPORTANT:** `hidden` (nao `uncounted`). engine.js pre-processa `data-visibility` no `initResidenciaMode()`.

---

## Speaker Notes — Formato Canonico

```html
<aside class="notes">
  [0:00-0:30] Hook — numero de impacto.
  PAUSA 3s — deixar absorver.
  PERGUNTAR: "Quantos ja viram isso?"
  ENFASE: "Este dado muda a conduta."
  [DATA] Fonte: EASL 2024, Tab.3 | Verificado: 2026-02-13
</aside>
```

---

## Modos de Palco

| Classe no `<body>` | Uso |
|--------------------|-----|
| `.stage-c` | Plan C (padrao) — light, 1280x720, GSAP ativo |
| `.stage-bad` | Plan B — sala clara, projetor fraco, sem animacao |
| (nenhuma) | Plan A (futuro) — dark, 1920x1080 |

### QA Mode
`?qa=1` forca estado final de todas as animacoes + revela todos `[data-reveal]`.

### Print-PDF
`?print-pdf` ou `?view=print` forca estado final, desabilita animacoes.
