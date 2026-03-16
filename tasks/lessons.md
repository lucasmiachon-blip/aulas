# Lessons — Padrões Aprendidos

> Atualizado após correções e auditorias. Revisar no início de sessão.

---

## Sessão Flip + QA (2026-03-04)

### CSS selector: `#id.class` ≠ `#id .class`
- `#s-a1-damico.archetype-flow` = mesmo elemento com id E class → nunca casa (section tem id, div filho tem class)
- `#s-a1-damico .archetype-flow` = descendente → correto
- **Verificar sempre:** `document.querySelectorAll('seletor').length > 0` antes de assumir que uma rule aplica

### Archetype scope: reutilizar elementos de um archetype em outro
- `.archetype-pathway .pathway-track { display:flex }` → só funciona dentro de `archetype-pathway`
- Se reutilizar `.pathway-track` em `archetype-flow`, re-declarar `display:flex` no novo contexto
- Padrão: ao criar elementos de um archetype dentro de outro, sempre verificar se as regras de layout herdam corretamente

### Panel overlap: `min()` cap vence o panel-width
- `min(1120px, calc(100% - 140px - 1rem))` = 1120px (cap binding em viewport 1280px)
- Com `margin:0 auto`, conteúdo se estende sobre o panel
- Fix correto: `max-width: calc(100% - var(--panel-width) - 3rem)` + `margin: 0 0 0 2rem` quando panel visível

### overflow-y em slides: sempre hidden
- `overflow-y: auto` em eras = scrollbar no palco → inaceitável
- Slides são canvas fixo. Conteúdo que não cabe = problema de design, não de CSS
- Padrão: `.scores-era { overflow-y: hidden }`

### GSAP Flip + crossfade: capturar estado ANTES da transição
- `Flip.getState(formulaBlock)` DEVE ser chamado antes de `showEra(5)` (que faz opacity→0 no elemento)
- Passar `preFlipState` como parâmetro para a função de animação pós-transição
- Se `preFlipState = null` (era 4 não foi visitada antes), usar fallback `gsap.from`

## Auditoria Batches (2026-03)

### Rules: .cursor vs .claude

- `.cursor/rules/` e `.claude/rules/` sao **complementares, nao redundantes** (corrigido 04/mar)
- Em conflito, conteudo mais detalhado prevalece, independente do diretorio
- **design-system:** Mais verboso que cirrose-design; design-system = referência completa, cirrose-design = quick ref

### Paths CSS

- **NUNCA** documentar shared/css/archetypes.css ou shared/css/cirrose.css — não existem
- Realidade: base.css em shared/; archetypes.css e cirrose.css em aulas/cirrose/ (e grade, osteoporose)

### Notion ↔ Repo

- IDs canônicos: docs/SYNC-NOTION-REPO.md
- Conflito de versão: Composer/Claude Opus determina o mais atual → prevalece

### MD Audit

- Não manual. Skill docs-audit + subagent generalPurpose/qa-engineer
- Critérios: dev, designer, prompt eng, engenheiro de sistema, economia de tokens

### Skills .cursor vs .claude

- Sem conflito: cada superfície usa seu diretório (Cursor vs Claude Code vs Claude.ai)
- docs-audit espelhado: mesmo conteúdo, path no prompt adaptado
- assertion-evidence, medical-data: Claude only, complementam medical-slide (não duplicam)

### Skills

- medical-slide (Cursor) cobre assertion-evidence + verificação de dados
- assertion-evidence e medical-data (Claude) são subconjuntos — avaliar depreciação

### Context Window

- ≥70%: informar ao usuário
- ≥85%: recomendar subagent ou novo chat
- ≥95%: parar e recomendar novo chat
- **Sinais sem métrica:** respostas genéricas, esquecimento, repetição, confusão, pedidos já respondidos, lentidão → novo chat
- Regra em core-constraints.mdc; referência em docs/RULES.md, docs/SUBAGENTS.md

---

## Anti-patterns

- Documentar paths sem verificar existência no filesystem
- Duplicar regras entre .cursor e .claude sem decisão de fonte canônica
- Verbosidade em CLAUDE.md duplicando docs/

---

## Auditoria Profunda (2026-03-04)

### Rules .cursor vs .claude — NÃO são redundantes

- **CORRIGIDO:** README.md dizia ".cursor canônico" — na verdade são **complementares**
- `.claude` é mais completo em: medical-data (Tier 1 table), design-principles (27 vs 11), css-errors (5 clusters), motion-qa (5 tiers)
- `.cursor` é mais completo em: slide-editing (tri-mode), reveal-patterns (GSAP timeline)
- 3 rules .cursor sem equivalente .claude: core-constraints, plan-mode, notion-mcp
- Regra: em conflito, conteúdo mais detalhado prevalece

### Agents — Problemas Corrigidos

- **verifier:** model fast→sonnet (Haiku fraco demais para git diff + julgamento)
- **reference-checker → reference-manager:** Definido formato de handoff (report inline no NOTES.md)
- **slide-builder vs medical-slide:** NÃO são duplicatas — ambientes diferentes (Claude Code vs Cursor). Cross-references adicionadas
- **docs-audit .claude:** Clarificado como redirect para .cursor/skills/docs-audit/
- **assertion-evidence:** Descrição corrigida "Cria" → "Valida"

### design-principles.mdc — 15 princípios adicionados

- .cursor tinha 11, agora tem 26 (alinhado com .claude/27)
- Adicionados: Andragogia (3), Mayer extras (2), Kahneman, Duarte expandido (5), Tufte (4), Layout Patterns + Fill Ratio
- Faltava: F-pattern, Z-pattern, Fill Ratio, Expertise-Reversal, Testing Effect — todos críticos para design de slides médicos

---

*Append-only. Não remover lições antigas.*

---

## Sessão QA Metanalise (2026-03-15)

### Toda aula precisa de stage class no body

- `<body>` sem `class="stage-c"` (ou `stage-a`) → tokens `:root` default → cascata de inconsistências
- Cirrose funcionava porque `index.template.html` já tinha `class="stage-c"` hardcoded
- Metanalise renderizava white-bg acidental porque `index.html` não tinha stage class
- **Regra:** Ao criar nova aula, `<body class="stage-c">` é obrigatório. Sem isso, dark tokens (`--text-on-dark`, `--bg-navy`) mantêm valores escuros e o deck renderiza incorretamente em projeção light.

### deck.js ignora data-background-color

- `data-background-color` é convenção Reveal.js. O deck.js custom não processa esse atributo.
- Slides com `data-background-color="#162032"` ficam com fundo transparente → herdam bg do `#deck`.
- **Regra:** Em deck.js, usar stage classes + tokens CSS para controlar cores. `data-background-color` é documentação/legacy, não funcional.
- **Pendência (Classe B):** Implementar suporte a `data-background-color` em deck.js para stage-a/dark mode futuro.

### Safe-center pseudo-elements incompatíveis com flex:1 children

- `base.css` introduziu `::before, ::after { flex: 1 0 0px }` como spacers para safe-center (evitar clipping simétrico)
- Pattern funciona quando ALL content children têm tamanho fixo (sem `flex-grow`)
- Quando children têm `flex: 1` (compare-layout, pico-grid, etc), os spacers competem pelo espaço restante → conteúdo NÃO centra, h2 é empurrado para posições inconsistentes
- **Regra:** Safe-center com pseudo-elements requer `flex-shrink: 0` E ausência de `flex-grow` nos children de conteúdo. Se layout components usam `flex: 1`, usar `justify-content: center` direto (sem spacers).
- **Regra:** Após merge de main que modifica `.slide-inner`, medir h2 positions programaticamente em TODAS as aulas antes de prosseguir.

### justify-content: center + overflow = clipping simétrico

- `justify-content: center` em flex column com overflow distribui excesso simetricamente: metade para cima, metade para baixo
- Conteúdo que extravasa é cortado no TOPO (h2 desaparece) e no FUNDO
- **Fix pattern:** Remover `justify-content: center`, usar `margin-top: auto` no primeiro child real → centra quando cabe, colapsa a 0 quando overflows (conteúdo sempre começa do topo)
- **Regra:** Em layouts com conteúdo variável, NUNCA usar `justify-content: center` — usar margin-auto safe-center.

### Browser default p { margin: 1em } em flex layouts

- `<p>` dentro de flex layout com `gap` terá espaçamento DUPLICADO: `gap` + `margin: 1em` top + `margin: 1em` bottom
- Em checkpoint com 8 `<p>` = ~240px de margem invisível que inflava o layout
- **Regra:** Reset `p { margin: 0 }` dentro de qualquer flex layout que usa `gap`. Ou usar `<span>` se o parágrafo não precisa de block.

### CSS specificity: `#id` > `.class`

- `#deck h1 { color: var(--text-primary) }` (specificity 1-0-1) sempre ganha de `.slide-navy h1 { color: var(--text-on-dark) }` (0-1-1)
- Em stage-c isso não causa problema (ambos remapeiam para dark), mas em stage-a causaria
- **Pendência (Classe B):** Resolver specificity `.slide-navy` vs `#deck` em base.css para stage-a

---

## Sessão Infra (2026-03-12)

### Write tool preserva encoding do arquivo original

- `.gitattributes` estava em UTF-16 LE (BOM `FF FE`). O Write tool reescreveu o conteúdo mas **manteve UTF-16**.
- Fix: usar `printf` via Bash para forçar UTF-8: `printf '* text=auto eol=lf\n' > .gitattributes`
- **Regra:** Quando corrigir encoding, usar Bash `printf` — não confiar em Write/Edit para mudar encoding.

### Hook matcher: cobrir TODAS as tools que podem editar

- `"matcher": "Write"` deixava brecha: agent types com `Edit` ou `StrReplace` como tools separadas não eram interceptados pelo guard de evidence-db.
- **Regra:** Matcher de guards deve listar TODAS as tools de escrita: `"Write|Edit|StrReplace"`. Se uma tool não existe para um agent type, matcher nunca dispara (zero downside).

### Build artifacts (index.html) não devem ser tracked

- 4× `aulas/*/index.html` estavam tracked, gerando diffs de ~23k linhas em cada rebuild.
- **Regra:** Arquivo gerado por `npm run build:*` = `.gitignore`. Usar `git rm --cached` para destrackear sem deletar do disco.

---

## Propósito do Ecossistema (2026-03-07)

### Valores explícitos — nunca perder de vista

Lucas quer ser **um melhor** educador, pesquisador, médico e aprendiz — melhoria contínua, não perfeição.
Os agentes são **parceiros** que amplificam essas capacidades — não concorrentes, não ferramentas.

Objetivos encadeados:
1. Melhorar **AI/dev/ML fluency** → para usar melhor os agentes
2. Usar melhor os agentes → para ser melhor educador, pesquisador, médico
3. Aprendizado acumulado → pode contribuir de volta para criação de skills/agents/models

### O que isso muda na prática

- Retrabalho não é "custo" — é **tempo perdido de aprendizado**
- Handoff errado não é "ineficiência" — é **potencial desperdiçado**
- Cada slide bem feito = Lucas aprende algo sobre a doença + sobre como trabalhar com IA
- Documentação não é burocracia — é **memória do aprendizado compartilhada**

### Lição capturada

Framing inicial dos docs era "custo" e "eficiência". Correto é: **fluência e amplificação**.
Tokens não importam. Retrabalho é sinal de aprendizado — mas não pode paralisar. Avançar sempre.

### Skills frontmatter — campos mar 2026

- Novos campos disponíveis: `version`, `allowed-tools`, `argument-hint`, `user-invocable`, `disable-model-invocation`, `context`, `agent`
- `allowed-tools` evita aprovação manual por uso — sempre especificar em skills de auditoria (Read, Grep, Glob)
- **Bug crítico Issue #17283:** `context:fork` e `agent:` são ignorados quando skill invocado via Skill tool (API/SDK). Só funciona no CLI direto.
- `user-invocable: false` útil para skills de conhecimento de fundo (Claude auto-ativa, não aparece no menu `/`)
- `disable-model-invocation: true` para skills com side-effects sérios (deploy, push, send)

---

## Sessão Act 2 P0 + Narrative Rewrite (2026-03-08)

### NSBB: primary ≠ secondary prophylaxis — ERRO CONCEITUAL

- **PREDESCI** (PMID 30910320): testou NSBBs em pacientes com cACLD + CSPH **SEM descompensação prévia** → prevenção PRIMÁRIA
- Usar PREDESCI NNT 9 como hero number de slide PÓS-HDA = erro conceitual grave (mistura populações)
- Act 1 (s-a1-classify): PREDESCI como hero → correto (prevenção primária)
- Act 2 (A2-07 pós-HDA): NSBB = profilaxia SECUNDÁRIA → hero number deve vir de outro trial ou ser callback narrativo ao Act 1
- **Regra:** Sempre verificar a POPULAÇÃO do trial antes de usar como hero. Prevenção 1ª ≠ 2ª.

### MELD intermediários: dados narrativos vs clínicos

- Canônicos (CASE.md): ~10, 28, 12 — derivados de checkpoints clínicos reais
- Intermediários (12→14→17→18→28→24): são CONSTRUÇÕES NARRATIVAS para dar ritmo à cascata
- Moram em: narrative.md + _manifest.js panelStates. NUNCA em CASE.md.
- **Regra:** Dados narrativos plausíveis ≠ dados clínicos. Separar sempre. Documentar origem.

### PMIDs podem estar certos no evidence-db mas errados em medical-data.md

- ANSWER: evidence-db tinha 29861076 (correto), medical-data.md tinha 29793859 (errado)
- CONFIRM: medical-data.md tinha 34882432 (artigo de saúde transgênero!), correto = 33657294
- **Regra:** Ao fixar um PMID em qualquer arquivo, grep por ALL occurrences e corrigir em todos.

### Ioannou HCC: sobrevida pós-HCC ≠ incidência de HCC

- PMID 31374215: HR 0.29 é sobre morte PÓS-HCC em pacientes com SVR (não prevenção de HCC)
- PMID 31356807: este é o estudo sobre INCIDÊNCIA de HCC com/sem SVR
- **Regra:** Ao citar HR de HCC, explicitar: é sobre INCIDÊNCIA ou SOBREVIDA pós-diagnóstico?

### Operational records: atualizar no MESMO batch

- CHANGELOG, ERROR-LOG, lessons.md devem ser atualizados na MESMA sessão em que o trabalho foi feito
- Deixar para "depois" = invariavelmente esquece, próximo agente não tem contexto

---

## Sessão 09/mar — PMID audit + RAW_ACT3_V1

### NUNCA confiar em PMID gerado por modelo sem verificação

- **5/5 CANDIDATE PMIDs estavam ERRADOS.** Todos foram produzidos por ChatGPT 5.4 Pro e model-based search sem MCP.
- Tipos de erro: PMID de artigo completamente diferente (herbicida, belatacept, fluoxetine), off-by-4, journal errado.
- **Regra:** Todo PMID deve ser verificado via PubMed MCP ou WebSearch (pubmed.ncbi.nlm.nih.gov/{PMID}) antes de entrar em evidence-db ou slide.
- **Regra:** Marcar como `[CANDIDATE]` até verificado. Nunca promover a verificado sem check.
- **Regra:** Se PubMed MCP indisponível, WebSearch no domínio pubmed.ncbi.nlm.nih.gov é fallback aceitável.

### Hooks: usar `node -e`, nunca `python -c`

- Python não é dependência do projeto; Node >=20 é obrigatório.
- 4 hooks legados usavam `python -c` para JSON parsing — migrados para `node -e` em 12/mar.
- **Regra:** Todo novo hook DEVE usar `node -e` para parsing JSON. Padrão:
  ```bash
  VALUE=$(echo "$INPUT" | node -e "
  const d=JSON.parse(require('fs').readFileSync('/dev/stdin','utf8'));
  console.log(d.field||'');
  " 2>/dev/null)
  ```

### Act 3 anchor PMIDs: 2 não verificáveis

- PMID 41580090 (álcool abstinência) e PMID 39220088 (TIPS ≠ recompensação) não foram encontrados via WebSearch.
- Podem ser PMIDs recentes (2025/2026 não indexados) ou fabricados.
- Alternativa para álcool: PMID 37469291 (18,1% retrospectivo) — verificado.
- Alternativa para TIPS: conceito presente em Baveno VII (PMID 36646527/35120736) — verificado.

---

## Sessão 14/mar — Classe C guard + doc chain

### Classe C em main = violação silenciosa sem guard

- Act 3 skeletons foram commitados em `main` em vez de na WT `feat/cirrose-mvp` — violação do protocolo worktree.
- Sem mecanismo automatizado, o erro é inevitável (agente não verifica branch antes de commitar conteúdo).
- **Fix:** `scripts/pre-commit.sh` bloqueia slides, CSS, JS e references em `main`. Bypass: `ALLOW_MAIN_CONTENT=1`.
- **Regra:** Todo novo clone ou WT deve rodar `bash scripts/install-hooks.sh` uma vez.

### Cadeia documental: metanalise era invisível

- `aulas/metanalise/CLAUDE.md` existia mas não aparecia em XREF.md nem docs/README.md.
- Projeto marcado ATIVO no CLAUDE.md root mas sem referência cruzada nos docs de governança.
- **Regra:** Ao adicionar projeto ATIVO, registrar em: CLAUDE.md (projects), XREF.md (seção dedicada), docs/README.md (HANDOFFs).

---

## Sessão 16/mar — Pseudo-elements em base.css = contaminação cross-projeto

### NUNCA adicionar pseudo-elements com flex-grow em container base compartilhado

- `::before/::after { flex: 1 0 0px }` em `.slide-inner` (base.css) causou 2 bugs em 2 projetos:
  - **Cirrose:** archetypes têm `gap: 1rem` → pseudo-elements geram 2 gaps extras = 32px roubados por slide
  - **Metanalise:** filhos diretos com `flex: 1` competem com pseudo-elements → h2 empurrados 100-180px
- **Root cause:** pseudo-elements participam do layout flex como qualquer outro item. Combinados com `gap` ou `flex: 1` children, produzem efeitos colaterais invisíveis.
- **Regra:** `shared/css/base.css` deve conter apenas regras que funcionam com QUALQUER layout filho (grid, flex, custom). Mecanismos de centering/spacing que dependem de contexto flex → responsabilidade da aula, não da base.
- **`justify-content: flex-start` é suficiente** para o P0 (clipping sempre no bottom, h2 sempre visível). Centering estético = responsabilidade da WT.

## Sessão 16/mar — JS scaling + overflow diagnosis

### Canvas fixo + transform:scale = arquitetura correta para apresentações

- `scaleDeck()`: `Math.min(vw/1280, vh/720)` + `translate(-50%,-50%) scale(s)` em `#deck position:absolute`
- Responde a `resize` e `fullscreenchange`. Funciona em qualquer tela sem refactor de conteúdo.
- **Proibido:** `zoom` CSS (não dispara evento resize), `body { display:grid }` em cirrose.css (conflito com scaling global).
- **Regra:** Scaling é responsabilidade do `shared/js/deck.js`. CSS local NUNCA deve redefinir zoom/transform no body ou #deck.

### overflow=scrollHeight > clientHeight pode ser artefato GSAP

- Elementos com `opacity:0` (estado inicial GSAP) ocupam espaço de layout → scrollHeight inflado.
- Diagnóstico correto: `Array.from(el.querySelectorAll('*')).filter(c => parseFloat(getComputedStyle(c).opacity)===0 && c.offsetHeight>20)`
- **Regra:** Antes de "corrigir overflow", verificar se o overflow desaparece quando GSAP revela os elementos. Overflow em medição ≠ overflow visual.

### flex-wrap inline em HTML vence archetype CSS

- CSS inline no `<section>` tem especificidade máxima. Override em `cirrose.css` precisa de seletor mais específico (`#slide-viewport .screening-pathway`).
- **Regra:** Ao debugar layout, inspecionar regras inline via `document.styleSheets` + `rule.selectorText.includes('classe')`. Não assumir que `archetypes.css` é a única fonte.

### .slide-integrity: fingerprint contra rollback de conteúdo

- `build-html.ps1` gera SHA-256 por slide → `.slide-integrity`. Build seguinte compara e alerta.
- Pre-commit Guard 4: bloqueia se slides mudaram sem rebuild (`.slide-integrity` desatualizado).
- **Regra:** Após merge, sempre rodar `npm run build:cirrose` antes de commitar. O Guard 4 vai bloquear se esquecer.

### Agente em main editou worktree via path absoluto = VIOLAÇÃO

- Sessão no workspace `aulas-magnas` (main) escreveu diretamente em `C:\Dev\Projetos\wt-cirrose\` usando paths absolutos.
- Hooks (pre-commit, pre-push) só disparam no git commit/push — não impedem escrita direta em arquivos.
- **Regra:** Agente em main NUNCA pode escrever em `../wt-*`. Para editar worktree, abrir sessão Cursor naquele diretório.
- **Regra:** `scripts/pre-commit.sh` e `tasks/lessons.md` são Classe A/B — sempre commitar em main, nunca direto na WT.
