# Lessons — Padrões Aprendidos

> Atualizado após correções e auditorias. Revisar no início de sessão.

---

## Sessão Flip + QA (2026-03-04)

### CSS selector: `#id.class` ≠ `#id .class`
- `.class` no mesmo elemento vs descendente. Verificar: `querySelectorAll('seletor').length > 0`.
- Ver tambem: css-errors.md Cluster B.

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

### Skills
- Sem conflito entre superfícies (Cursor vs Claude Code vs Claude.ai). Ref: `docs/SKILLS.md`
- assertion-evidence e medical-data (Claude): deprecated → cobertos por /review v0.4+

### Context Window
- Thresholds 70/85/95%: `.cursor/rules/core-constraints.mdc`. Ref: `docs/SUBAGENTS.md`

---

## Anti-patterns

- Documentar paths sem verificar existência no filesystem
- Duplicar regras entre .cursor e .claude sem decisão de fonte canônica
- Verbosidade em CLAUDE.md duplicando docs/

---

## Auditoria Profunda (2026-03-04)

### Agents corrigidos
- verifier: fast→sonnet. reference-checker→reference-manager. assertion-evidence: "Cria"→"Valida"
- slide-builder vs medical-slide: ambientes diferentes (Claude Code vs Cursor), não duplicatas

### design-principles.mdc: 26 princípios (alinhado com .claude/27)
- Adicionados: Andragogia (3), Mayer (2), Kahneman, Duarte (5), Tufte (4), Layout/Fill Ratio

> Rules .cursor vs .claude: seção redundante removida — ver `.claude/rules/README.md`

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

- Gerado por `npm run build:*` = `.gitignore`. Feito em 2026-03-12.

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
- **Bug Issue #17283:** `context:fork` e `agent:` ignorados via Skill tool (API/SDK). Só funciona no CLI direto. Verificar se corrigido em versões posteriores.
- `user-invocable: false` útil para skills de conhecimento de fundo (Claude auto-ativa, não aparece no menu `/`)
- `disable-model-invocation: true` para skills com side-effects sérios (deploy, push, send)

---

## Sessão Act 2 P0 + Narrative Rewrite (2026-03-08)

### NSBB: primary ≠ secondary prophylaxis — ERRO CONCEITUAL

- **PREDESCI** (PMID 30910320): testou NSBBs em pacientes com cACLD + CSPH **SEM descompensação prévia** → prevenção PRIMÁRIA
- Usar PREDESCI NNT 9 como hero number de slide PÓS-HDA = erro conceitual grave (mistura populações)
- Act 1 (s-a1-classify): PREDESCI como hero → correto (prevenção primária)
- Act 2 (A2-07 pós-HDA): NSBB = profilaxia SECUNDÁRIA → hero number deve vir de outro trial ou ser callback narrativo ao Act 1
- **Regra:** Sempre verificar a POPULAÇÃO do trial antes de usar como hero. Prevenção 1ª ≠ 2ª. Ref: `medical-data.md` (População do Trial).

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

- CHANGELOG, ERROR-LOG, lessons.md: na MESMA sessao. Ver CLAUDE.md root "Workflow" step 6-7.

---

## Sessão 09/mar — PMID audit + RAW_ACT3_V1

### NUNCA confiar em PMID gerado por modelo sem verificação

- 5/5 CANDIDATE PMIDs estavam errados (ChatGPT/GPT-5.4). Sempre verificar via PubMed MCP ou WebSearch.
- Regra completa: `.claude/rules/medical-data.md` secao "Verificacao de PMIDs".

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

---

## Sessao 16/mar (j) — _manifest.js e a 9a superficie

### Editar headline no HTML sem atualizar _manifest.js = drift silencioso

- Hook slide: texto mudou de "80/dia" para "146/dia" no HTML (`01-hook.html`), speaker notes e body.
- `_manifest.js` headline ficou com "80 revisões..." — drift detectado pelo usuario no browser.
- **Root cause:** slide-identity.md lista 9 superficies. `_manifest.js` e a superficie #1. Agente atualizou superficies 2 (HTML body) e notes, mas esqueceu a #1.
- **Regra:** Toda mudanca em texto visivel de slide DEVE incluir `_manifest.js` headline no mesmo Edit batch. Nunca "depois".
- **Regra:** Antes de commitar mudanca em slides, rodar `npm run lint:narrative-sync` — detecta drift headline automaticamente.
- **Checklist mental (4 perguntas):** (1) O h2/headline mudou? → `_manifest.js`. (2) O ID mudou? → 9 superficies completas. (3) Dados mudaram? → notes [DATA] tag. (4) Aula tem build script? Se nao → **index.html manual e uma superficie extra**.

### index.html manual = superficie extra (RESOLVIDO para metanalise)

- ~~Metanalise nao tinha `build:metanalise` script~~ — **RESOLVIDO 2026-03:** `npm run build:metanalise` existe (build-html.ps1). Bug de chave duplicada em package.json corrigido.
- Vite serve `index.html`, NAO `slides/*.html`. Editar o standalone sem rodar build = usuario ve versao antiga.
- **Regra:** Toda aula com `_manifest.js` DEVE ter `npm run build:{aula}`. Rodar apos qualquer mudanca em slides.
- **Verificacao:** `npm run build:{aula}` antes de commitar. Guard 4 (post-merge) detecta drift.

---

## Sessao 17/mar — Doc sync: drift de dados entre docs

### Dados duplicados em N docs driftam silenciosamente

- O dado "80 SRs/dia" vivia em 4 docs: blueprint, narrative, evidence-db, reading-list.
- Quando o hook atualizou para "146/dia" (sessao 16/mar), apenas HTML + evidence-db foram atualizados. Blueprint e narrative ficaram com "80/dia".
- Drift só detectado na auditoria documental (sessao 17/mar) — 2 sessões depois.
- **Regra:** Ao atualizar dado numérico em slide, grep por TODOS os docs que mencionam o valor antigo: `grep -rn "80/dia\|80 revisões" aulas/{aula}/`. Atualizar no MESMO batch.
- **Regra:** evidence-db.md é fonte canônica de dados. Se evidence-db diz X mas narrative.md diz Y → narrative está errado. Nao o contrario.

### Candidatos não-decididos acumulam verbosidade

- 11 candidatos a artigo-âncora com 200+ linhas de dados detalhados permaneceram em evidence-db após decisão (Valgimigli).
- Após 3 sessões, ninguém mais consultava esses dados — mas ocupavam contexto.
- Fix: colapsar para tabela-resumo com PMIDs (1 linha cada, -189 linhas).
- **Regra:** Após decisão final sobre candidatos, colapsar os não-selecionados em tabela-resumo na mesma sessão. Dados completos ficam acessíveis via PMID.

### Referências cross-doc desatualizadas após troca de âncora

- reading-list.md item 4 referenciava Musini (antigo candidato). Âncora mudou para Valgimigli 2 sessões antes.
- **Regra:** Ao trocar artigo-âncora, grep por nome do antigo em TODOS os docs: `grep -rn "Musini\|antigo" aulas/{aula}/`. Atualizar ou remover referências obsoletas.

---

## Lessons adicionadas por auditoria (2026-03-17)

### deck.js bg escuro: CSS seletor, nao data-attribute

- `data-background-color` e convencao Reveal.js — deck.js NAO processa.
- Pattern correto: `#slide-id .slide-inner { background-color: #0d1a2d; }` no CSS da aula.
- Adicionar `.slide-navy` no `.slide-inner` para remap de tokens de texto.
- Ref: deck-patterns.md, slide-editing.md (ERRO-034).

### .no-js failsafe obrigatorio para [data-animate]

- CSS: `[data-animate] { opacity: 0; }` + `.no-js [data-animate] { opacity: 1; }`.
- Sem isso: GSAP offline/quebrado = slide em branco.
- Failsafe deve existir em `base.css` (shared) E pode ser reforçado em `{aula}.css`.
- Ref: CLAUDE.md rule 12, deck-patterns.md secao CSS Failsafe.

### Pseudo-elements com flex-grow: E32 canonizado

- `::before/::after { flex: 1 }` em containers base compartilhados PROIBIDO.
- Participam do layout flex → com gap ou flex:1 children, produzem efeitos colaterais.
- Codificado como E32 em css-errors.md. Lesson detalhada: sessao 16/mar neste arquivo.

---

## Sessão Diagnostico WT (2026-03-19)

### Vite cache poisoning entre worktrees (ERRO-010)

- Sintoma: tela preta no dev server, `section { display: none }`, DOM quase vazio.
- Root cause: `node_modules/.vite/deps/` continha `reveal__js.js` pre-bundled de grade/osteoporose entries. Vite serviu inline script de OUTRA worktree com `import Reveal`. Reveal.css colapsou todas as sections.
- Fix: (1) Remover `reveal.js` de dependencies. (2) Excluir frozen aulas de `discoverEntries()` no Vite config. (3) `npm install` invalida hash → cache limpo.
- Regra: Worktrees deck.js NUNCA devem ter `reveal.js` em dependencies. Se tela preta: checar `.vite/deps/` ANTES de debugar CSS. Rodar `npx vite --force` ao trocar entre WTs.

### "CSS bug" pode ser infra

- O CHANGELOG dizia "146 mono não renderiza (specificity CSS)". Diagnóstico errado.
- Computed styles mostraram JetBrains Mono 72px correto — o CSS SEMPRE esteve certo.
- A tela preta impedia validação visual → hipótese de CSS nunca foi testada.
- Regra: antes de diagnosticar "CSS specificity", verificar se o dev server está servindo o código certo.

### stage-c remap de --text-on-dark afeta elementos com bg local escuro

- `--text-on-dark` em stage-c é remapeado para `oklch(12%)` (texto ESCURO) — correto para slides light.
- Elemento com bg escuro DENTRO de slide light (ex: verdict pill com --danger bg) herda o remap → texto escuro sobre bg escuro = contraste 3.67:1.
- **Regra:** Qualquer elemento com background-color próprio escuro em slide light DEVE usar cor explícita (`oklch(95%)` ou HEX), NUNCA `var(--text-on-dark)`.
- Ref: NOTES.md 2026-03-19 (s-hook Gate 3 scorecard). ERRO-009 (mesmo root cause para slides inteiros).

### SplitText `type: 'chars'` causa word-break

- `SplitText({ type: 'chars' })` envolve cada caractere em `<span>` — browser faz word-break mid-word ("paci/entes").
- **Fix:** `type: 'words,chars'` — SplitText primeiro agrupa por palavra, depois por char. `&nbsp;` no HTML para espaços non-breaking.
- **Regra:** NUNCA usar `type: 'chars'` isolado. Sempre `'words,chars'` para manter word boundaries.

### Tom alarmista rejeitado pelo Lucas (s-hook)

- Dados VITALITY (1.330 retratados, guidelines contaminadas, UTI) geraram tom "escandaloso" no s-hook.
- Lucas rejeitou: apresentação sóbria e clínica > alarmista. Público = residentes, não jornalistas.
- **Regra:** Nunca usar dados de retratação/fraude para criar medo. Framing clínico: "saber em quem confiar" > "a ciência está quebrada".
