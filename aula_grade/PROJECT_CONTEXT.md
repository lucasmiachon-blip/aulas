# Projeto: Aula GRADE HTML → PowerPoint

## ⚠️ Adicione este arquivo ao seu Claude Project

Este arquivo fornece contexto permanente para Claude sobre o projeto de apresentação GRADE.

---

## Identificação do Projeto

**Nome:** Aula GRADE — Apresentação HTML → PowerPoint  
**Repositório:** lucasmiachon-blip/aulas  
**Branch:** `aula_grade` ← **TRABALHAR AQUI**  
**Tecnologia:** HTML5 + CSS3 + JS → futuro PowerPoint  
**Versão atual:** v0.1.0

---

## ⚠️ AVISO CRÍTICO - NÃO MEXER EM OUTROS BRANCHES

**NUNCA modificar, criar arquivos ou fazer commits no branch `aula_osteoporose`**

Esse branch é um projeto **SEPARADO** de osteoporose.  
**APENAS trabalhe em `aula_grade`** quando solicitado sobre GRADE/dislipidemia.

Se o usuário pedir algo sobre osteoporose, pergunte antes de fazer qualquer modificação.

---

## Objetivo

Criar apresentação sobre **metodologia GRADE aplicada à Diretriz Brasileira de Dislipidemia 2025**.

**Fases:**
1. **HTML (atual):** Prototipar e validar estrutura
2. **PowerPoint (futuro):** Migrar mantendo paleta navy/gold

**Por quê HTML primeiro?** Iteração rápida, testes, CSS reutilizável.

---

## Paleta de Cores (CRÍTICA!)

### Cores Principais
```css
--navy-deep: #152432    /* 80% da apresentação */
--gold: #D4AF37         /* 15% - destaques */
```

### Cores de Acento (5%)
```css
--blue: #2563EB         /* Certeza ALTA GRADE */
--green: #059669        /* Benefícios */
--red: #B91C1C          /* Riscos, rate down */
```

**Arquivo completo:** `docs/PALETA_CORES.md`

---

## Tipografia

- **Títulos:** Georgia (serifa clássica)
- **Corpo:** Lato (sans-serif moderna)

**Filosofia:** Sério mas elegante. MBE não é infantil nem entediante.

---

## Estrutura de Arquivos

```
aula_grade/
├── README.md
├── CHANGELOG.md                   # v0.1.0
├── CONTEXT.md                     # Para Claude
├── PROJECT_CONTEXT.md             # Este arquivo
├── docs/
│   ├── PALETA_CORES.md            # Guia completo
│   └── ESTRUTURA_VISUAL.md        # (a criar) Templates
├── slides/                        # HTML slides
├── assets/
│   ├── css/
│   │   ├── colors.css             # Variáveis CSS
│   │   ├── typography.css         # Fontes
│   │   └── styles.css             # Estilos gerais
│   ├── js/
│   │   └── navigation.js          # Setas ← →
│   └── images/
├── index.html                     # Navegação principal
└── viewer.html                    # Visualizador fullscreen
```

---

## Estado Atual (v0.1.0)

### ✅ Completo
- Estrutura de diretórios
- Documentação base (README, CHANGELOG)
- Paleta de cores definida e documentada
- CONTEXT e PROJECT_CONTEXT

### 🚧 Próximo (v0.2.0)
- index.html + viewer.html
- CSS files (colors, typography, styles)
- JavaScript de navegação

### 📋 Roadmap
- v0.3.0: Slides Ato I (capa, Montaigne, fundadores)
- v0.4.0: Interatividade (cards, pausas)
- v1.0.0: 49 slides HTML completos
- v2.0.0: Migração PowerPoint

---

## Comandos Git

### Ver branch atual
```bash
git branch
# Deve mostrar: * aula_grade
```

### Adicionar e commitar
```bash
git add .
git commit -m "feat: adicionar slide capa navy/gold"
git push origin aula_grade
```

### Ver arquivos modificados
```bash
git status
```

---

## Workflow de Trabalho

1. **Modificar arquivos HTML/CSS localmente**
2. **Testar no navegador** (abrir index.html)
3. **Adicionar ao Git:** `git add .`
4. **Commit:** `git commit -m "tipo: descrição"`
5. **Push:** `git push origin aula_grade`

**Prefixos:**
- `feat:` Nova funcionalidade (ex: novo slide)
- `fix:` Correção
- `style:` Mudança visual (CSS/cores)
- `docs:` Documentação

---

## Interatividade (Pedagogia)

### Sem Infantilização
- ❌ Mentimeter, gamificação, timers bobos
- ✅ Cards A/B/C (audience response profissional)
- ✅ Pausas estratégicas (10s silêncio)
- ✅ Escolha de caminhos (A/B/C - eles pensam)

### Voz do Paciente
Casos clínicos com perguntas QUE O PACIENTE FAZ:
- "Doutor, e se eu não tomar?"
- "Tem outro remédio?"
- "Vale a pena?"

Não é "médico ensinando". É "paciente perguntando, médico decide junto".

---

## Diferença dos Outros Branches

- **`aula-GRADE`** → PowerPoint direto, docs .pptx
- **`aula_grade`** → HTML → PowerPoint ← **TRABALHAR AQUI**
- **`aula_osteoporose`** → Projeto SEPARADO (osteoporose GIOP) **NÃO MEXER**

Quando trabalhar em GRADE/dislipidemia, usar `aula_grade`.

---

## Conteúdo Clínico

### Estrutura (49 slides planejados)

```
Ato I — Gramática (0-8)
├─ Capa
├─ "Que sais-je?" (Montaigne)
├─ Nossa travessia
├─ Fundadores (Guyatt)
└─ ...

Caso CAC (9-16)
Caso Lp(a) (17-21)
Caso ApoB (22-29)
Caso Metas (30-32)
Caso PREVENT (33-34)
Síntese (35+)
```

### Números-Chave
- **ApoB:** UK Biobank N=293.876 | 7,3% vs 4,0%
- **Metas:** CTT −21% eventos/mmol/L
- **PREVENT:** Khan 2024 N=6.612.004

---

## Contexto do Usuário (Lucas)

**Nível:**
- Git/GitHub: Iniciante
- HTML/CSS: Básico
- Programação: Começando

**Abordagem do Claude:**
- Explicações didáticas (analogias práticas)
- Comandos Git passo-a-passo
- Não validar excessivamente ("perfeito!")
- Ser crítico quando necessário
- Mostrar código comentado

---

## Princípios de Design

### Visual
- **Navy + Gold = Autoridade + Sofisticação**
- Não colorido demais (não é infantil)
- Não cinza demais (não é entediante)
- Equilíbrio: Sério mas elegante

### Técnico
- Sem frameworks (HTML/CSS/JS puro)
- Standalone (funciona offline)
- Sem CDN (todos recursos locais)
- Responsivo (desktop prioritário)

---

## Quando Claude Esquecer

Se Claude perder contexto:
1. Este arquivo deve estar no Claude Project
2. CONTEXT.md tem detalhes técnicos
3. CHANGELOG.md tem versão atual

**Pergunta rápida:** "Qual branch? Qual versão? Quais cores?"  
**Resposta:** `aula_grade`, v0.1.0, Navy #152432 + Gold #D4AF37

---

## Checklist Rápido

Antes de fazer qualquer mudança:
- [ ] Estou no branch `aula_grade`?
- [ ] Consultei `docs/PALETA_CORES.md` para cores?
- [ ] Seguindo tipografia Georgia + Lato?
- [ ] Commits com prefixo semântico?
- [ ] HTML standalone (sem CDN)?

---

**Última atualização:** 2025-01-10  
**Próxima revisão:** Após v0.2.0 (HTML completo)
