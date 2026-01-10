# CONTEXTO — Aula GRADE HTML (para Claude)

## Localização no GitHub

**Repositório:** `lucasmiachon-blip/aulas`  
**Branch:** `aula_grade`  
**Caminho:** `/aula_grade/`

**URL:** https://github.com/lucasmiachon-blip/aulas/tree/aula_grade/aula_grade

---

## O que é este projeto

Apresentação HTML interativa sobre **metodologia GRADE aplicada à Diretriz Brasileira de Dislipidemia 2025**.

**Tecnologia atual:** HTML5 + CSS3 + JavaScript vanilla  
**Tecnologia futura:** PowerPoint (migração mantendo identidade visual)  
**Objetivo:** Funcionar offline, sem dependências externas

---

## Estrutura Atual

```
aula_grade/
├── README.md
├── CHANGELOG.md                    # v0.1.0
├── CONTEXT.md                      # Este arquivo
├── PROJECT_CONTEXT.md              # Para Claude Project
├── docs/
│   └── PALETA_CORES.md             # Guia completo navy/gold
├── slides/                         # (vazio, a criar)
└── assets/                         # (vazio, a criar)
    ├── css/
    ├── js/
    └── images/
```

---

## Estado do Projeto

### ✅ v0.1.0 (Atual)
- Estrutura de diretórios criada
- Documentação base (README, CHANGELOG)
- Paleta de cores definida e documentada
- CONTEXT e PROJECT_CONTEXT criados

### 🚧 v0.2.0 (Próximo)
- index.html + viewer.html
- CSS files (colors, typography, styles)
- JavaScript de navegação

### 📋 Roadmap
- v0.3.0: Slides iniciais (Ato I)
- v0.4.0: Interatividade
- v1.0.0: HTML completo (49 slides)
- v2.0.0: Migração PowerPoint

---

## Decisões de Design

### Paleta de Cores (CRÍTICO)
```css
Principal:
--navy-deep: #152432    (80% da apresentação)
--gold: #D4AF37         (15% - destaques)

Acentos (5%):
--blue: #2563EB         (certeza ALTA GRADE)
--green: #059669        (benefícios)
--red: #B91C1C          (riscos, rate down)
```

Ver `docs/PALETA_CORES.md` para detalhes completos.

### Tipografia
- **Títulos:** Georgia (serifa clássica)
- **Corpo:** Lato (sans-serif moderna)

### Arquitetura
- **Standalone:** Sem CDN, funciona offline
- **Sem frameworks:** Apenas HTML/CSS/JS puro
- **Responsivo:** Desktop prioritário, mobile compatível

---

## Diferença dos Outros Branches

### Branch `aula-GRADE` (PowerPoint direto)
- Criado primeiro
- Foco em PowerPoint/Canva desde o início
- Documentação sobre slides .pptx

### Branch `aula_grade` (este)
- HTML primeiro → PowerPoint depois
- Desenvolvimento web iterativo
- Paleta de cores idêntica

### Branch `aula_osteoporose`
- Projeto separado (GIOP)
- HTML standalone

**IMPORTANTE:** Trabalhar APENAS em `aula_grade` quando solicitado.

---

## Como Trabalhar Neste Projeto

### Adicionar Slide HTML
1. Criar arquivo em `/slides/` (ex: `00-capa.html`)
2. Usar variáveis CSS: `var(--navy-deep)`, `var(--gold)`
3. Seguir template de tipografia (Georgia + Lato)
4. Atualizar `index.html` com link

### Modificar Cores
Editar `/assets/css/colors.css` (variáveis CSS)

### Commits
```bash
git add arquivo.html
git commit -m "feat: adicionar slide capa com paleta navy/gold"
git push origin aula_grade
```

Prefixos: `feat:`, `fix:`, `style:`, `docs:`

---

## Contexto Clínico

**Tema:** Metodologia GRADE para Dislipidemia BR 2025

**Estrutura:** 49 slides planejados
1. Ato I: Gramática (0-8)
2. Caso CAC (9-16)
3. Caso Lp(a) (17-21)
4. Caso ApoB (22-29)
5. Caso Metas (30-32)
6. Caso PREVENT (33-34)
7. Síntese (35+)

**Público:** Médicos, residentes com conhecimento prévio

---

## Números-Chave (Conteúdo)

### ApoB
- UK Biobank: N=293.876 | 7,3% vs 4,0%
- Copenhagen: HR 1,49
- Certeza: MODERADA ⊕⊕⊕○

### Metas LDL
- CTT: −21% eventos/mmol/L
- FOURIER: N=27.564 | HR 0,85
- Certeza: ALTA ⊕⊕⊕⊕

### PREVENT
- Khan 2024: N=6.612.004 | c-stat 0,794
- Certeza: MODERADA ⊕⊕⊕○

---

## Versão Atual

**v0.1.0** (10/01/2025) — Estrutura base

**Próxima milestone:** v0.2.0 — HTML completo (index, viewer, CSS)

---

## Quando Claude Esquecer

1. Ler este arquivo (CONTEXT.md)
2. Ler PROJECT_CONTEXT.md no Claude Project
3. Verificar CHANGELOG.md para versão atual

**Perguntas rápidas:**
- Branch? → `aula_grade`
- Versão? → v0.1.0
- Tecnologia? → HTML (futuro PowerPoint)
- Cores? → Navy (#152432) + Gold (#D4AF37)
- Onde paleta? → `docs/PALETA_CORES.md`

---

**Última atualização:** 2025-01-10  
**Próxima revisão:** Após v0.2.0 (HTML completo)
