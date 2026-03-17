# Reveal.js Legacy Patterns

> FROZEN — grade/osteoporose only. Nao usar para novos projetos.
> Novos decks (cirrose, metanalise) usam deck.js: ver [deck-patterns](deck-patterns.md).
> Codigo: `shared/js/engine.js` (initAula legacy path) + Reveal.js 5.2.

---

## Import

```js
import Reveal from 'reveal.js';
import Notes from 'reveal.js/plugin/notes/notes.esm.js';
import 'reveal.js/dist/reveal.css';
```

---

## Estrutura de Slide

```html
<section data-background-color="#0d1a2d">
  <div class="slide-inner slide-navy">
    <h2>Assercao clinica verificavel</h2>
    <div class="evidence">...</div>
  </div>
  <aside class="notes">
    [0:00-0:30] Hook.
    [DATA] Fonte: ...
  </aside>
</section>
```

### Background
- `data-background-color` HEX literal (Reveal parseia JS-side)
- HEX canonicos: `#0d1a2d` (navy), `#f5f5f7` (surface), `#111111` (deep)

---

## Fragments

Apenas quando guia atencao na ordem da fala.

```html
<p class="fragment fade-up">Primeiro</p>
<p class="fragment fade-up">Segundo</p>
```

Degradacao graciosa: `.no-js .fragment { opacity: 1 }`.

---

## Eventos Reveal.js

| Evento | Quando | Usar para |
|--------|--------|-----------|
| `slidechanged` | Inicio da transicao | Cleanup: `ctx.revert()`, clear timers |
| `slidetransitionend` | Fim da transicao | Iniciar animacoes |
| `ready` | Deck carregou | Animar slide inicial |
| `fragmentshown` | Fragment revelado | Animar conteudo do fragment |
| `fragmenthidden` | Fragment escondido | Reverter animacao |

### viewDistance Warning
Reveal.js recicla DOM de slides distantes (`viewDistance` config). GSAP nao pode calcular bounding box de elemento com `display:none`. Por isso: animacoes so no `slidetransitionend` (slide ja visivel).

---

## PDF Export

Config em engine.js (legacy path):
```js
pdfSeparateFragments: false,
pdfMaxPagesPerSlide: 1,
showNotes: 'separate-page',
```

Workflow: `npm run build && npm run preview` → abrir `?print-pdf` → Chrome Ctrl+P → Landscape, sem margens, background ON.

Em modo print-pdf, engine desabilita animacoes e forca estado final.

---

## Keyboard Bindings (Reveal API)

```js
Reveal.addKeyBinding(
  { keyCode: 84, key: "T", description: "Start timer" },
  () => { /* handler */ }
)
```

---

## Appendice

```html
<section class="appendix" data-visibility="hidden">
  <!-- hidden = removido do DOM, nao navegavel -->
  <!-- ?mode=residencia remove o atributo ANTES do init -->
</section>
```

`hidden` (nao `uncounted`). `uncounted` so funciona no fim do deck.
