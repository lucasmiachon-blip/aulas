# Aula GRADE — Apresentação HTML Interativa

## Sobre

Apresentação HTML interativa sobre metodologia GRADE aplicada à Diretriz Brasileira de Dislipidemia 2025.

**Repositório:** https://github.com/lucasmiachon-blip/aulas  
**Branch:** `aula_grade`  
**Caminho GitHub:** https://github.com/lucasmiachon-blip/aulas/tree/aula_grade/aula_grade

**Público-alvo:** Médicos, residentes, estudantes de medicina  
**Formato:** HTML standalone (funciona offline) → futuro PowerPoint  
**Tecnologia:** HTML5 + CSS3 + JavaScript vanilla

---

## Estrutura do Projeto

```
aula_grade/
├── index.html                    # Índice/navegação principal
├── viewer.html                   # Viewer de apresentação
├── slides/                       # Slides individuais (HTML)
│   ├── 00-capa.html
│   ├── 01-que-sais-je.html
│   ├── 02-nossa-travessia.html
│   └── ...
├── assets/
│   ├── css/
│   │   ├── colors.css           # Paleta de cores
│   │   ├── typography.css       # Fontes (Georgia + Lato)
│   │   └── styles.css           # Estilos gerais
│   ├── js/
│   │   └── navigation.js        # Navegação entre slides
│   └── images/                  # Recursos visuais
├── docs/
│   ├── PALETA_CORES.md          # Guia de cores do projeto
│   └── ESTRUTURA_VISUAL.md      # Templates de slides
├── CHANGELOG.md                 # Histórico de versões
├── CONTEXT.md                   # Contexto para Claude
├── PROJECT_CONTEXT.md           # Para Claude Project
└── README.md                    # Este arquivo
```

---

## Paleta de Cores

Ver [PALETA_CORES.md](./docs/PALETA_CORES.md) para detalhes.

**Principal:**
- Navy Deep (#152432) — Títulos, backgrounds
- Gold (#D4AF37) — Destaques, call-to-action

**Acentos:**
- Blue (#2563EB) — Dados, certeza ALTA
- Green (#059669) — Benefícios
- Red (#B91C1C) — Riscos, rebaixamento GRADE

---

## Tipografia

- **Títulos:** Georgia (serifa clássica)
- **Corpo:** Lato (sans-serif moderna)

---

## Como Usar

### Desenvolvimento Local
```bash
# Abrir no navegador
open index.html
```

### Apresentação
```bash
# Abrir viewer
open viewer.html
# Usar setas ← → para navegar
# F11 para fullscreen
```

---

## Versão Atual

**v0.1.0** — Estrutura base HTML

**Futuro:** Migração para PowerPoint mantendo identidade visual

Ver [CHANGELOG.md](./CHANGELOG.md) para histórico completo.

---

## Tecnologias

- **HTML5:** Estrutura semântica
- **CSS3:** Variáveis CSS para cores, animações
- **JavaScript:** Navegação e interatividade
- **Sem dependências:** Funciona offline

---

## Desenvolvimento

### Adicionar novo slide
1. Criar HTML em `/slides/`
2. Seguir template de cor/tipografia
3. Atualizar `index.html`

### Modificar cores
Editar `assets/css/colors.css` (variáveis CSS)

### Commits
```bash
git add arquivo.html
git commit -m "feat: adicionar slide sobre ApoB"
git push origin aula_grade
```

Prefixos: `feat:`, `fix:`, `style:`, `docs:`

---

## Roadmap

### Fase 1: HTML (atual)
- [x] Estrutura base
- [ ] 20 slides principais
- [ ] Sistema de navegação
- [ ] Interatividade (cards conceituais)

### Fase 2: PowerPoint (futuro)
- [ ] Migração mantendo paleta
- [ ] Templates reutilizáveis
- [ ] Exportação para apresentação

---

## Licença

Uso educacional livre. Citar fonte ao reutilizar.

---

## Contato

Lucas Miachon  
[Adicionar contato]
