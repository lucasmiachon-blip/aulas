---
name: new-skill
description: |
  Scaffolds a new Claude Code skill from project conventions. Oferece 3 templates: simple (read-only), orchestrator (multi-agent), lazy (on-demand loading). Use when creating a new skill — "criar skill", "new skill", "scaffold skill [name]".
version: 2.0.0
context: fork
allowed-tools: Read, Write, Glob, Grep
argument-hint: "<skill-name> [description] [--template=simple|orchestrator|lazy]"
---

# new-skill — Scaffold de Skill

Cria uma nova skill seguindo as convenções do projeto: `$ARGUMENTS`

## Workflow

1. **Parse arguments:** extrair `<skill-name>`, `[description]`, `[--template]` de `$ARGUMENTS`
2. **Validate:** verificar que `.claude/skills/<skill-name>/` NÃO existe
3. **Prompt if missing:** se description não foi fornecida, perguntar ao usuário
4. **Choose template:** `--template=simple` (default), `orchestrator`, ou `lazy`
5. **Generate:** criar `.claude/skills/<skill-name>/SKILL.md` com template escolhido
6. **Report:** listar o que foi criado e próximos passos

## Templates

### Template A — Simple (default)

Para skills read-only ou com workflow linear simples.

```markdown
---
name: <skill-name>
description: <description — incluir trigger terms para o skill matcher>
version: 1.0.0
allowed-tools: Read, Grep, Glob
argument-hint: "[args]"
---

# <skill-name> — <Título>

<Descrição>: `$ARGUMENTS`

## Workflow

1. Step 1
2. Step 2
3. Step 3

## Output

<Formato esperado>

## Rules

- Regra 1
- Regra 2
```

### Template B — Orchestrator (multi-agent)

Para skills que lancam agentes paralelos, consolidam resultados e geram report estruturado. Padrão: fan-out + consolidação (Anthropic research-agent).

```markdown
---
name: <skill-name>
description: |
  <description multi-linha com trigger terms>
version: 1.0.0
context: fork
agent: general-purpose
allowed-tools: Read, Grep, Glob, Agent, WebSearch, WebFetch
argument-hint: "[query ou aula]"
---

# <skill-name> — <Título>

<Descrição>: `$ARGUMENTS`

## Step 0 — Detectar contexto

1. Auto-detectar aula: `git branch --show-current` → `feat/{aula}-*`
2. Ler `aulas/{aula}/CLAUDE.md` para contexto clínico

## Step 1 — Fan-out (agentes paralelos)

Lançar N agentes via Agent tool (subagent_type: general-purpose):

| Agente | Papel | Tools |
|--------|-------|-------|
| Agent 1 | <papel> | Read, WebSearch |
| Agent 2 | <papel> | Read, Grep |
| Agent N | <papel> | Read, WebFetch |

Cada agente retorna JSON estruturado.

## Step 2 — Consolidar

1. Coletar resultados dos N agentes
2. Triangular: mesmo achado de >=2 agentes = VERIFIED
3. Conflitos: flag para humano

## Step 3 — Report

Formato JSON ou Markdown estruturado com:
- TL;DR (3 linhas)
- Achados detalhados
- Flags e próximos passos

## Rules

- Max N agentes paralelos (ajustar conforme complexidade)
- NUNCA inventar dados — sem fonte = [TBD]
- Conflitos entre agentes = [HUMAN-REVIEW]
```

### Template C — Lazy (on-demand loading)

Para skills que devem carregar rapido no startup (frontmatter only ~50 tokens). Corpo carregado on-demand quando ativado.

```markdown
---
name: <skill-name>
description: <description com trigger terms>
version: 1.0.0
allowed-tools: Read, Grep, Glob
argument-hint: "[query]"
---

# <skill-name> — <Título>

<Descrição>: `$ARGUMENTS`

## Fonte de dados

Busca em: `<path ou recurso>` (carregado on-demand, não no startup).

## Workflow

1. Receber query do usuário
2. Carregar dados do fonte
3. Processar + filtrar
4. Retornar resultado formatado

## Rules

- Skill é lazy — corpo NÃO é lido no startup
- Manter SKILL.md < 100 linhas para economia de tokens
- Detalhes extensos em `reference.md` separado
```

## Escolha de template

| Cenário | Template | Exemplo no projeto |
|---------|----------|-------------------|
| Auditoria, validação, busca simples | Simple | `review`, `docs-audit`, `audit-rules` |
| Pesquisa multi-source, QA multi-agent | Orchestrator | `medical-researcher`, `evolve`, `ralph-qa` |
| Cache de docs, busca em memória | Lazy | `context7`, `mem-search` |

## Conventions (do projeto)

- **YAML frontmatter obrigatório:** name, description, version
- **description** deve conter trigger terms para o skill matcher encontrar a skill
- **context: fork** para skills que rodam em subagent (orchestrator sempre usa fork)
- **allowed-tools:** mínimo necessário. Nunca dar Write/Edit se a skill é read-only
- **`$ARGUMENTS`** placeholder no corpo — Claude injeta os args do usuário
- **agent:** campo opcional (só com `context:fork`) — `general-purpose`, `Explore`, `Plan`, `qa-engineer`
- **MCP-awareness:** se a skill precisa de MCPs, documentar quais e se tem fallback sem MCP
- **deprecated:** `deprecated: true` + nota no topo quando skill é absorvida por outra

## Post-creation Checklist

Após criar a skill, lembrar o usuário de:
- [ ] Preencher o conteúdo real do SKILL.md
- [ ] Testar invocando `/skill-name` ou trigger terms
- [ ] Adicionar entrada em `.claude/skills/README.md` (tabela + pipeline se aplicável)
- [ ] Adicionar entrada em `docs/SKILLS.md` se for skill permanente
- [ ] Adicionar em `docs/XREF.md` se referenciar/for referenciada por outros docs

## Rules

- **NUNCA sobrescrever skill existente** — avisar e abortar se diretório já existe
- **NUNCA criar skills fora de `.claude/skills/`** (deprecated vão para `.claude/skills/archive/`)
- Nomes em kebab-case: `my-skill`, não `mySkill` ou `my_skill`
- Description em uma linha (simple/lazy) ou multi-linha com `|` (orchestrator)
- Se o usuário não der description, perguntar — NUNCA inventar
