# Aulas Magnas

Plataforma de apresentações médicas interativas para hepatologistas seniores (Brasil). Slides assertion-evidence com animações GSAP, navegação custom (`deck.js`), offline-first.

## Stack

deck.js (custom navigation) · GSAP 3.12 · Vite 6.x · Vanilla HTML/CSS/JS · OKLCH · Zero CDN · Offline-first.

## Projetos

| Pasta | Status |
|-------|--------|
| `aulas/cirrose/` | 44 slides, QA visual em andamento |
| `aulas/metanalise/` | 12 slides (Fases 1-2) |
| `aulas/grade/` | 58/58 migrados (frozen, Reveal.js legacy) |
| `aulas/osteoporose/` | 70/70 migrados (frozen, Reveal.js legacy) |

## Quick Start

```bash
npm install
npm run dev              # Vite hot reload (port 3000)
npm run build:cirrose    # Concatena slides → index.html
npm run preview          # Servir localmente
```

## Lint & QA

```bash
npm run lint:slides         # Assertion-evidence linter
npm run lint:case-sync      # CASE.md ↔ _manifest.js sync
npm run lint:narrative-sync # narrative.md ↔ _manifest.js sync
npm run done:cirrose        # Gate check (build + lint + screenshots)
```

## Setup

```bash
bash scripts/install-hooks.sh   # Instala pre-commit, pre-push, post-merge hooks
```

## Docs

Documentação completa em [`docs/README.md`](docs/README.md). Para agentes AI, ver [`CLAUDE.md`](CLAUDE.md).
