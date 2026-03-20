---
name: context7
description: Injeta documentação atualizada de bibliotecas no contexto. Ativar automaticamente quando o usuário trabalhar com GSAP, Reveal.js, Vite, OKLCH, ou qualquer lib do projeto. Resolve hallucination de APIs desatualizadas. Usar "/context7 [library]" para busca manual.
version: 2.1.0
context: lazy
agent: general-purpose
allowed-tools: Read, WebSearch, WebFetch
argument-hint: "[library name + version?]"
triggers:
  - gsap
  - reveal.js
  - vite
  - oklch
  - postcss
  - data-animate
---

# Context7 — Docs Verificadas (2026-03-17)

## GSAP 3.14.2

Sem breaking changes desde 3.0. Registry privado `npm.greensock.com` MORTO — todos plugins gratis no npm publico.

### Core
```js
gsap.to(targets, { duration, ease, delay, stagger, onComplete, overwrite: "auto" })
gsap.from(targets, vars)
gsap.fromTo(targets, fromVars, toVars)
```
PROIBIDO: `bounce`, `elastic`, `back` (frivolo). Padrao: `power2.out`.

### Stagger
```js
stagger: { each: 0.15, from: "start", ease: "power2.in" }
```
Quirk: `stagger` no topo ignorado com `keyframes` — mover para `defaults`.
Novo 3.13: `gsap.to(".box", { x: "var(--space-lg)" })`.

### Timeline
```js
const tl = gsap.timeline({ paused: true, defaults: { duration: 0.4, ease: "power2.out" } })
tl.to(el, vars, "<")  // "<" start anterior, ">" end anterior
tl.revert()            // cleanup no slidechanged
```

### Cleanup: `gsap.context()`
```js
let ctx = gsap.context(() => { gsap.to(el, { x: 100 }) }, containerEl)
ctx.revert()  // no slidechanged handler
```

### Reduced motion: `gsap.matchMedia()`
```js
let mm = gsap.matchMedia()
mm.add("(prefers-reduced-motion: no-preference)", () => { gsap.to(el, { y: -20 }) })
```
NAO aninhar matchMedia dentro de context — sao equivalentes.

## Reveal.js 5.2.1 (FROZEN — grade/osteoporose)

### Opcoes relevantes
```js
Reveal.initialize({
  scrollActivationWidth: null,  // v5: DESABILITAR para congresso
  width: 1280, height: 720,
  center: false,                // layout usa align-content:start
  transition: "fade", transitionSpeed: "fast",
  pdfSeparateFragments: false, pdfMaxPagesPerSlide: 1,
})
```

### Eventos
```js
Reveal.on("slidechanged", ({ previousSlide, currentSlide }) => { ctx.revert() })
Reveal.on("slidetransitionend", ({ currentSlide }) => { /* iniciar animacoes */ })
Reveal.on("fragmentshown", ({ fragment }) => { })
```

### data-visibility: sempre `hidden` (nao `uncounted`) para apendice.

### Breaking v4→v5: `?print-pdf` → `?view=print` (antigo ainda funciona). Scroll-view auto <435px.

## Vite 6.x (projeto atual) / Vite 8.0 (disponivel)

### Breaking v5→v6
- Sass API: `css.preprocessorOptions.scss.api: "modern-compiler"` (se usar SCSS)
- `commonjsOptions.strictRequires` default `true`
- postcss-oklab-function sem mudancas

### Vite 8.0 (Rolldown) — estavel desde 2026-03-12
- Substitui esbuild + Rollup por Rolldown (bundler Rust unico)
- 10-30x faster builds (benchmarks: 25x em 19K modules)
- Migration: `build.rollupOptions` → `build.rolldownOptions`
- CommonJS interop mudou: fallback temporario `legacy.inconsistentCjsInterop: true`
- Caminho: v6 → v7 (migration guide) → v8
- **Status projeto:** upgrade nao urgente — 6.x mantido. Avaliar apos QA pipeline estabilizar.

## Fallback
Se docs ficarem desatualizadas: `cat package.json | grep -E "gsap|reveal|vite"` → WebSearch changelog.
