# Lessons — Padrões Aprendidos

> Atualizado após correções e auditorias. Revisar no início de sessão.
> Organizado por escopo: universal → cirrose-only → metanalise-only.
> Patterns já codificados em rules indicam ref (ex: "→ E32").

---

## 1. Valores e Propósito (2026-03-07)

Lucas quer ser **um melhor** educador, pesquisador, médico e aprendiz — melhoria contínua, não perfeição.
Os agentes são **parceiros** que amplificam essas capacidades — não concorrentes, não ferramentas.

- Retrabalho não é "custo" — é **tempo perdido de aprendizado**
- Handoff errado não é "ineficiência" — é **potencial desperdiçado**
- Documentação não é burocracia — é **memória do aprendizado compartilhada**
- Framing correto: **fluência e amplificação**, não custo e eficiência

---

## 2. Universal — CSS & Layout

### Flexbox

| Pattern | Regra | Codificado em |
|---------|-------|---------------|
| `#id.class` ≠ `#id .class` | `.class` no mesmo elemento vs descendente | css-errors.md |
| Pseudo-elements com flex-grow em base compartilhada | PROIBIDO — participam do layout, criam side effects com gap/flex:1 | **E32** |
| `justify-content: center` + overflow | Clipping simétrico (h2 desaparece). Usar `margin-top: auto` | **E33** |
| `<p>` em flex com gap | Margin 1em default duplica espaçamento. Reset `p { margin: 0 }` | **E34** |
| Safe-center pseudo-elements + flex:1 children | Incompatíveis. Se children têm flex-grow → `justify-content: center` direto | **E32** derivado |
| `flex:1` igualitário em containers desiguais | PROIBIDO — 3x reincidência | **E26** |
| `space-between` com N≠M items | PROIBIDO | **E10** |

### Specificity

| Pattern | Regra |
|---------|-------|
| `#deck h1` (1-0-1) > `.slide-navy h1` (0-1-1) | Especificidade vence cascata. Pendência (Classe B): resolver para stage-a |
| `<p>` em `#deck` herda `max-width: 56ch` | Para full-width, sobrescrever com `max-width: none; width: 100%` |
| CSS inline no `<section>` | Especificidade máxima. Override precisa de seletor mais específico |

### deck.js

| Pattern | Regra | Codificado em |
|---------|-------|---------------|
| `data-background-color` ignorado por deck.js | Convenção Reveal.js. Usar CSS seletor `#id .slide-inner { background-color }` | deck-patterns.md, **ERRO-009** |
| `zoom` CSS com deck.js | PROIBIDO — double-scaling. deck.js escala via transform:scale | **ERRO-008** |
| Stage class obrigatória no `<body>` | Sem `class="stage-c"`, tokens default = renderização quebrada | **ERRO-001** |
| `.no-js` failsafe para `[data-animate]` | `opacity: 0` base + `.no-js { opacity: 1 }` | CLAUDE.md rule 12 |
| Scaling é responsabilidade do deck.js | CSS local NUNCA redefinir zoom/transform no body ou #deck | — |
| overflow-y em slides: sempre hidden | Canvas fixo. Conteúdo que não cabe = problema de design | — |

### stage-c remap

| Pattern | Regra |
|---------|-------|
| `--text-on-dark` em stage-c = texto ESCURO | Correto para slides light. Elemento com bg escuro em slide light DEVE usar cor explícita | **ERRO-009** derivado |
| Qualquer bg local escuro em slide light | Usar `oklch(95%)` ou HEX, NUNCA `var(--text-on-dark)` | — |

---

## 3. Universal — GSAP

| Pattern | Regra |
|---------|-------|
| `Flip.getState()` ANTES da transição | Capturar estado antes de opacity→0. Se null, fallback `gsap.from` |
| `SplitText type: 'chars'` causa word-break | SEMPRE usar `'words,chars'`. `&nbsp;` para espaços non-breaking |
| overflow=scrollHeight pode ser artefato GSAP | Elementos com `opacity:0` ocupam espaço. Verificar se overflow desaparece com reveal |
| `registerCustom` ANTES de `connect()` | wireAll → registerCustom → connect. Ordem importa |

---

## 4. Universal — Dados Médicos

| Pattern | Regra | Codificado em |
|---------|-------|---------------|
| NUNCA confiar em PMID gerado por LLM | 5/5 candidatos errados (GPT-5.4). Verificar via PubMed MCP | medical-data.md |
| PMID correto em um doc, errado em outro | Ao fixar PMID, grep ALL occurrences e corrigir em todos | medical-data.md |
| HR ≠ RR ≠ OR | Trial isolado = HR. Meta-análise = RR. NUNCA misturar | **E25** |
| Verificar POPULAÇÃO do trial | Prevenção 1ª ≠ 2ª. Trial de uma pop ≠ hero de outra | medical-data.md |
| Incidência ≠ sobrevida pós-diagnóstico | Ex: Ioannou HCC — PMID 31374215 (sobrevida) ≠ PMID 31356807 (incidência) | — |
| Dados narrativos ≠ dados clínicos | Intermediários plausíveis moram em narrative.md, NUNCA em evidence-db | — |

---

## 5. Universal — Docs & Workflow

### Propagação

| Pattern | Regra |
|---------|-------|
| Dados duplicados em N docs driftam | Ao atualizar dado, grep por valor antigo em TODOS os docs. Mesmo batch |
| evidence-db é fonte canônica de dados | Se evidence-db ≠ narrative → narrative está errado |
| Candidatos não-decididos acumulam verbosidade | Colapsar para tabela-resumo após decisão final. Mesma sessão |
| Trocar âncora = grep pelo nome antigo | Remover/atualizar refs obsoletas em todos os docs |
| Editar headline no HTML = atualizar _manifest.js | Superfície #1. lint:narrative-sync detecta drift |
| Operational records: atualizar no MESMO batch | CHANGELOG, ERROR-LOG, lessons.md: nunca "depois" |

### Checklist mental (4 perguntas antes de commit)

1. O h2/headline mudou? → `_manifest.js`
2. O ID mudou? → 9 superfícies completas (slide-identity.md)
3. Dados mudaram? → notes [DATA] tag + grep docs
4. Aula tem build script? → rodar antes de commit

### Infra

| Pattern | Regra |
|---------|-------|
| Write tool preserva encoding | Para forçar UTF-8, usar `printf` via Bash |
| Hook matcher: cobrir TODAS as tools de escrita | `"Write\|Edit\|StrReplace"`. Zero downside |
| Build artifacts (index.html) não tracked | `.gitignore`. `npm run build:*` regenera |
| Hooks: `node -e`, nunca `python -c` | Python não é dep. `node -e` com `/dev/stdin` |
| Agente em main escreveu em WT via path absoluto | VIOLAÇÃO. Hooks não impedem escrita direta |
| Classe C em main sem guard | Act 3 skeletons em main. Fix: pre-commit.sh bloqueia |
| Projeto ATIVO invisível nos docs | Registrar em CLAUDE.md, XREF.md, docs/README.md |
| Skills frontmatter: `allowed-tools` sempre especificar | Evita aprovação manual. Bug #17283: `context:fork` ignorado via Skill tool |

---

## 6. Universal — Anti-patterns

- Documentar paths sem verificar existência no filesystem
- Duplicar regras entre .cursor e .claude sem decisão de fonte canônica
- Verbosidade em CLAUDE.md duplicando docs/
- Diagnosticar "CSS specificity" sem verificar se dev server serve código certo
- `.cursor/rules/` e `.claude/rules/` são **complementares, não redundantes**. Em conflito, mais detalhado prevalece

---

## 7. Cirrose-only

### NSBB: primary ≠ secondary prophylaxis

- **PREDESCI** (PMID 30910320): prevenção PRIMÁRIA (cACLD + CSPH, sem descompensação)
- Usar PREDESCI NNT 9 em slide pós-HDA = erro conceitual (profilaxia SECUNDÁRIA)
- **Regra:** Verificar POPULAÇÃO do trial antes de usar como hero

### Archetypes

- Reutilizar elementos de um archetype em outro: re-declarar display/flex no novo contexto
- Panel overlap: `min()` cap vence panel-width. Fix: `max-width: calc(100% - var(--panel-width) - 3rem)`
- flex-wrap inline em HTML vence archetype CSS

### .slide-integrity: fingerprint contra rollback

- `build-html.ps1` gera SHA-256 por slide. Pre-commit Guard 4 bloqueia se desatualizado.
- Após merge, sempre `npm run build:{aula}` antes de commitar.

### PMIDs não verificáveis (Act 3)

- PMID 41580090 (álcool) e 39220088 (TIPS): não encontrados. Alternativas verificadas.

---

## 8. Metanalise-only

### Vite cache poisoning (ERRO-010)

- Tela preta: Vite cache com `reveal.js` de grade/osteoporose. Reveal.css colapsou sections.
- Fix: remover reveal.js de deps, excluir frozen aulas de discoverEntries.
- Regra: se tela preta, checar `.vite/deps/` ANTES de debugar CSS. `npx vite --force` ao trocar WTs.

### Tom alarmista rejeitado (s-hook)

- VITALITY/UTI geraram tom "escandaloso". Lucas rejeitou: sóbrio e clínico > alarmista.
- **Regra:** Framing clínico: "saber em quem confiar" > "a ciência está quebrada"

### Siedler 2025 — framing correto

- 33,8% = SRs que **avaliaram** certeza (89,3% via GRADE). NÃO "% com certeza moderada/alta".
- Framing mais poderoso: dois terços nem avaliam.
- PMID 40969451. Cochrane Evid Synth Methods 2025;3(2). Verificado 2026-03-19.

---

## 9. Auditoria Profunda (2026-03-04)

### Agents/Skills

- verifier: fast→sonnet. reference-checker→reference-manager
- slide-builder vs medical-slide: ambientes diferentes, não duplicatas
- assertion-evidence e medical-data: deprecated → cobertos por /review v0.4+
- design-principles.mdc: 26 princípios (alinhado com .claude/27)

### Referências operacionais

- IDs Notion canônicos: `.env.example` (variáveis `NOTION_*_ID`)
- Context window thresholds: `.cursor/rules/core-constraints.mdc`
- MD audit: skill docs-audit (não manual)
- Paths CSS: NUNCA documentar shared/css/archetypes.css (não existe)

---

*Append-only. Não remover lições — marcar como codificadas quando viram regra formal.*
