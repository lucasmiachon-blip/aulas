---
name: gtd
description: Getting Things Done simplificado — inbox capture, next actions, weekly review. File-based (Markdown). Ativar com "gtd", "inbox", "next actions", "weekly review", "o que tenho pendente?", "capturar tarefa". Preparado para futura integracao com Obsidian.
version: 1.0.0
context: lazy
allowed-tools: Read, Write, Edit, Glob, Grep
argument-hint: "[capture|review|next|focus|done|inbox] [texto da tarefa]"
---

# GTD — Getting Things Done (Simplificado)

Comando: `$ARGUMENTS`

David Allen: "Sua mente e para ter ideias, nao para guarda-las."

---

## Estrutura de Arquivos

```
gtd/
├── inbox.md          ← Captura rapida
├── next-actions.md   ← Proximas acoes (max 3 em FOCO)
├── projects.md       ← Projetos ativos (>1 acao)
├── waiting-for.md    ← Esperando terceiros
├── someday-maybe.md  ← Ideias futuras
└── done.md           ← Conclusoes (append-only)
```

Markdown puro — compativel com Obsidian.

---

## Comandos

### `capture` / `inbox`
Adicionar item ao inbox.md: `- [ ] [texto] — capturado [YYYY-MM-DD]`

### `process`
Para cada item no inbox: acionavel? → <2min: fazer agora → delegavel: waiting-for → parte de projeto: projects.md → senao: next-actions.md. Nao acionavel: someday-maybe ou deletar.

### `next`
Mostrar next-actions.md. **Regra do 3:** max 3 itens em FOCO simultaneo.

```markdown
### FOCO (max 3)
- [ ] **[acao]** — projeto: [X] | contexto: @computador

### Backlog
- [ ] [acao] — projeto: [Y]
```

### `focus`
Mover itens entre FOCO e Backlog. Perguntar: "Qual e a coisa mais importante agora?"

### `done [item]`
1. Remover de next-actions/projects
2. Adicionar a done.md com data
3. Puxar proximo do backlog se FOCO <3

### `review` — Semanal (~15min)
1. Inbox zerado?
2. FOCO: os 3 ainda sao os mais importantes?
3. Projects: algum parado >7 dias?
4. Waiting-for: cobrar?
5. Someday-maybe: alguma virou prioridade?

Gerar resumo: concluido + foco proxima semana + bloqueios.

---

## Contextos

| Tag | Quando |
|-----|--------|
| `@computador` | Precisa de terminal/IDE |
| `@celular` | Pode fazer do celular |
| `@pesquisa` | Buscar evidencia/paper |
| `@decisao` | Decisao antes de agir |

---

## Formato de Item

```markdown
- [ ] **[verbo infinitivo] [objeto]** — projeto: [nome] | contexto: @[tag] | capturado: [data]
```

---

## Integracao com Projeto

- **HANDOFF.md → GTD:** P0/P1 → FOCO, P2 → backlog, futuros → someday-maybe
- **Tasks nativo (TaskCreate):** tracking de sessao (volatil). GTD = entre sessoes (persistente).
- **Anti-drift:** Se FOCO tem 3 itens e usuario pede algo fora → avisar e perguntar.
- **Bootstrap:** Popular inbox a partir de HANDOFF.md + lessons.md + NOTES.md + MEMORY.md.
