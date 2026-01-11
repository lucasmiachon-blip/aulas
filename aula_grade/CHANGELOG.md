# Changelog - Aula GRADE HTML

Todas as mudanças notáveis serão documentadas aqui.

---

## [0.3.0] - 2026-01-11

### Adicionado
- **Slide 2: Objetivos Educacionais** — Novo slide focado em ensinar CORE GRADE através da Diretriz Brasileira de Dislipidemia 2025
  - Objetivo principal: Ensinar princípios fundamentais do CORE GRADE
  - Box "Você aprenderá": Certeza da evidência, 5 domínios, Certeza vs Força, Casos clínicos
  - Box "Foco Metodológico": CAC, PREVENT, Metas, Bempedoico
  - Rodapé inspirador com frase de Gordon Guyatt
- **viewer.html** — Atualizado para 10 slides (era 9)
- **Navegação** — Dropdown atualizado com todos os 10 slides

### Corrigido
- **Layout inconsistente** — Fontes, espaçamentos e padding padronizados
- **Paleta Turner** — Aplicada uniformemente em todos os slides
- **Cards das 5 Recomendações** — Alinhamento perfeito em grid
- **Fontes** — Georgia (títulos 2-3rem) + Lato (corpo 1.1-1.4rem)
- **Espaçamentos** — Padding consistente (35-45px em cards, 80px em slides)
- **Border-radius** — Uniforme em 12px para todos os elementos arredondados
- **Sombras** — Box-shadow sutis e profissionais

### Melhorado
- **Legibilidade** — Fontes maiores e mais claras
- **Hierarquia visual** — Títulos, subtítulos e corpo bem diferenciados
- **Hover effects** — Transições suaves em cards e botões
- **Responsividade** — Grid auto-fit minmax(320px, 1fr)

---

## [0.2.0] - 2025-01-10

### Adicionado
- **assets/css/colors.css** — Variáveis CSS da paleta Navy/Gold
- **assets/css/typography.css** — Fontes Georgia (títulos) + Lato fallback (corpo)
- **assets/css/styles.css** — Layout de slides, cards, tabelas, animações
- **assets/js/navigation.js** — Navegação com setas ← →, teclado, touch
- **index.html** — Índice de navegação com lista de slides
- **viewer.html** — Visualizador fullscreen com 8 slides (Ato I completo):
  - Slide 1: Capa
  - Slide 2: "Que sais-je?" (Montaigne)
  - Slide 3: Nossa Travessia (1993-2025)
  - Slide 4: Fundadores GRADE (Guyatt, Schünemann)
  - Slide 5: Certeza vs Força
  - Slide 6: Lógica da Certeza
  - Slide 7: Símbolos GRADE
  - Slide 8: As 5 Recomendações

### Funcionalidades
- Navegação por teclado (setas, Home, End, PageUp/Down, Espaço)
- Navegação touch (swipe) para mobile
- URL hash (#1, #2, etc) para slides específicos
- Barra de progresso visual
- HUD com contador de slides
- Zoom 40%-200% com botões rápidos
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

### [0.4.0] - Caso CAC Completo
- [ ] Slide 11: O Decreto CAC
- [ ] Slide 12: A Pergunta (PICO CAC)
- [ ] Slide 13: Gramática CAC (5 domínios)
- [ ] Slide 14: Inconsistência
- [ ] Slide 15: Rate Up CAC
- [ ] Slide 16: Viés de Publicação CAC
- [ ] Slide 17: Conclusão CAC

### [0.5.0] - Caso PREVENT
- [ ] Slide 18: Título PREVENT
- [ ] Slide 19: Comparação PREVENT vs PCE vs QRISK
- [ ] Slide 20: Performance PREVENT (Khan 2024)
- [ ] Slide 21: Gramática PREVENT
- [ ] Slide 22: Imprecisão e Calibração
- [ ] Slide 23: Quando usar qual modelo

### [0.6.0] - Caso Bempedoico
- [ ] Slide 24: Título Bempedoico
- [ ] Slide 25: Decreto Bempedoico
- [ ] Slide 26: CLEAR Outcomes
- [ ] Slide 27: Trade-off Benefício vs Gota
- [ ] Slide 28: Gramática MODERADA
- [ ] Slide 29: Algoritmo Bempedoico

### [0.7.0] - Metas Terapêuticas
- [ ] Slide 30: Título Metas
- [ ] Slide 31: CTT Dose-Resposta
- [ ] Slide 32: Trials Aplicáveis Brasil
- [ ] Slide 33: Meta Individualizada
- [ ] Slide 34: NNT Benefício Absoluto

### [0.8.0] - Estratificação
- [ ] Slide 35: Reclassificação CAC
- [ ] Slide 36: Decisão Terapêutica
- [ ] Slide 37: Gramática Estratificação
- [ ] Slide 38: Flowchart Prático

### [1.0.0] - Versão HTML Completa
- [ ] Slide 39: Comparação BR vs ESC vs AACE
- [ ] Slide 40: Take-Home Messages
- [ ] Testes de acessibilidade
- [ ] Navegação fluida otimizada
- [ ] Performance otimizada

### [2.0.0] - Migração PowerPoint
- [ ] Templates .pptx com paleta idêntica
- [ ] Todos os 40 slides convertidos mantendo visual
- [ ] Master slides reutilizáveis
- [ ] Animações PowerPoint equivalentes

---

## Convenções de Versionamento

**MAJOR.MINOR.PATCH**

- **MAJOR:** Mudanças estruturais (ex: HTML → PowerPoint)
- **MINOR:** Novos slides, features, blocos completos
- **PATCH:** Correções, ajustes visuais, bugs

Exemplos:
- `0.1.0` → Estrutura base
- `0.2.0` → HTML + 8 slides iniciais (Ato I)
- `0.3.0` → Slide Objetivos + correções layout
- `0.4.0` → Caso CAC completo
- `1.0.0` → Versão HTML final (40 slides)
- `2.0.0` → Versão PowerPoint

---

## Tipos de Mudanças

- **Adicionado** — Novos recursos, slides
- **Modificado** — Mudanças em funcionalidade existente
- **Descontinuado** — Recursos que serão removidos
- **Removido** — Recursos removidos
- **Corrigido** — Correções de bugs, erros
- **Segurança** — Vulnerabilidades
- **Melhorado** — Otimizações, refinamentos

---

## Roadmap Visual

```
v0.1 ─── v0.2 ─── v0.3 ─── v0.4 ─── v0.5 ─── v0.6 ─── v0.7 ─── v0.8 ─── v1.0 ─── v2.0
 │        │        │        │        │        │        │        │        │        │
Base    Ato I   Objetivos  CAC    PREVENT Bempedoico Metas  Estratif. HTML    PowerPoint
       8 slides  +Layout  completo                                     final    migração
                correto
```

---

## Progresso

- ✅ v0.1.0 — Estrutura base
- ✅ v0.2.0 — Ato I completo (8 slides)
- ✅ v0.3.0 — Objetivos + Layout corrigido (10 slides)
- 🔄 v0.4.0 — Caso CAC (em progresso)
- ⏳ v0.5.0 — PREVENT (planejado)
- ⏳ v0.6.0 — Bempedoico (planejado)
- ⏳ v0.7.0 — Metas (planejado)
- ⏳ v0.8.0 — Estratificação (planejado)
- ⏳ v1.0.0 — HTML final (planejado)
- ⏳ v2.0.0 — PowerPoint (planejado)

**Progresso atual:** 25% (10/40 slides)

---

**Última atualização:** 2026-01-11 00:50 UTC
