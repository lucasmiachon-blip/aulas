# Changelog - Aula GRADE HTML

Todas as mudanças notáveis serão documentadas aqui.

---

## [0.2.0] - 2025-01-10

### Adicionado
- **assets/css/colors.css** — Variáveis CSS da paleta Navy/Gold
- **assets/css/typography.css** — Fontes Georgia (títulos) + Lato fallback (corpo)
- **assets/css/styles.css** — Layout de slides, cards, tabelas, animações
- **assets/js/navigation.js** — Navegação com setas ← →, teclado, touch
- **index.html** — Índice de navegação com lista de slides
- **viewer.html** — Visualizador fullscreen com 4 slides iniciais:
  - Slide 0: Capa
  - Slide 1: "Que sais-je?" (Montaigne)
  - Slide 2: Nossa Travessia (1993-2025)
  - Slide 3: Fundadores GRADE (Guyatt, Schünemann)

### Funcionalidades
- Navegação por teclado (setas, Home, End, PageUp/Down, Espaço)
- Navegação touch (swipe) para mobile
- URL hash (#1, #2, etc) para slides específicos
- Barra de progresso visual
- HUD com contador de slides
- F11 para fullscreen
- Responsivo (desktop, tablet, mobile)

---

## [0.1.0] - 2025-01-10

### Adicionado
- Estrutura base do projeto HTML
- README.md com visão geral
- docs/PALETA_CORES.md (guia completo de cores)
- CONTEXT.md para referência do Claude
- PROJECT_CONTEXT.md para Claude Project
- Diretórios organizados:
  - `/slides` — Slides HTML individuais
  - `/assets/css` — Estilos (colors, typography, styles)
  - `/assets/js` — JavaScript de navegação
  - `/assets/images` — Recursos visuais
  - `/docs` — Documentação

### Decisões de Design
- Paleta: Navy (#152432) + Gold (#D4AF37) como cores principais
- Tipografia: Georgia (títulos) + Lato (corpo)
- Arquitetura: HTML standalone → futuro PowerPoint
- Sem frameworks (HTML/CSS/JS puro)

---

## Planejado

### [0.2.0] - Estrutura HTML Completa
- [ ] index.html (navegação principal)
- [ ] viewer.html (visualizador de apresentação)
- [ ] assets/css/colors.css (variáveis CSS)
- [ ] assets/css/typography.css (fontes)
- [ ] assets/css/styles.css (estilos gerais)
- [ ] assets/js/navigation.js (setas ← →)

### [0.3.0] - Slides Iniciais (Ato I)
- [ ] 00-capa.html
- [ ] 01-que-sais-je.html (Montaigne)
- [ ] 02-nossa-travessia.html
- [ ] 03-fundadores.html (Guyatt, Schünemann)
- [ ] 04-evolucao-br.html (1993-2025)

### [0.4.0] - Interatividade
- [ ] Sistema de cards conceituais
- [ ] Pause and think (pausas estratégicas)
- [ ] Escolha de caminhos (A/B/C)

### [1.0.0] - Versão HTML Completa
- [ ] 49 slides mapeados (ver ESTRUTURA_VISUAL.md)
- [ ] Navegação fluida
- [ ] Responsivo (desktop + tablet)
- [ ] Testes de acessibilidade

### [2.0.0] - Migração PowerPoint
- [ ] Templates .pptx com paleta idêntica
- [ ] Slides convertidos mantendo visual
- [ ] Master slides reutilizáveis

---

## Convenções de Versionamento

**MAJOR.MINOR.PATCH**

- **MAJOR:** Mudanças estruturais (ex: HTML → PowerPoint)
- **MINOR:** Novos slides, features
- **PATCH:** Correções, ajustes visuais

Exemplos:
- `0.1.0` → Estrutura base
- `0.2.0` → HTML completo
- `1.0.0` → Versão HTML final
- `2.0.0` → Versão PowerPoint

---

## Tipos de Mudanças

- **Adicionado** — Novos recursos, slides
- **Modificado** — Mudanças em funcionalidade existente
- **Descontinuado** — Recursos que serão removidos
- **Removido** — Recursos removidos
- **Corrigido** — Correções de bugs, erros
- **Segurança** — Vulnerabilidades

---

## Roadmap Visual

```
v0.1 ─── v0.2 ─── v0.3 ─── v0.4 ─── v1.0 ─── v2.0
 │        │        │        │        │        │
Base    HTML    Slides   Inter-   HTML     PowerPoint
      completo  iniciais  ativo   final     migração
```

---

**Última atualização:** 2025-01-10
