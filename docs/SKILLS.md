# Skills — Melhores Práticas

> Baseado em: docs oficiais Anthropic Claude Code (mar 2026) + Cursor Docs. Última atualização: 2026-03-18.

---

## O que são Skills

Skills são pacotes de conhecimento e workflow que ensinam o agente a executar tarefas específicas. São portáveis, versionáveis e carregam recursos sob demanda.

**Locais:** `.cursor/skills/` (projeto) | `~/.cursor/skills/` (global)

---

## Estrutura

```
skill-name/
├── SKILL.md              # Obrigatório — instruções principais
├── reference.md          # Opcional — documentação detalhada
├── examples.md           # Opcional — exemplos de uso
├── scripts/              # Opcional — scripts executáveis
└── references/          # Opcional — docs adicionais
```

---

## SKILL.md — Frontmatter

```yaml
---
name: skill-name
description: O que faz e quando usar. Max 1024 chars.
version: 0.1.0
context: fork               # opcional — isola em subagent
agent: general-purpose      # opcional — só com context:fork
allowed-tools: Read, Grep   # opcional — sem aprovação por uso
argument-hint: "[arg]"      # opcional — hint no autocomplete
user-invocable: false       # opcional — esconde do menu /; Claude ainda auto-ativa
disable-model-invocation: true  # opcional — só invocação manual
---
```

| Campo | Obrigatório | Regras |
|------|-------------|--------|
| `name` | Sim | lowercase, hífens, max 64 chars |
| `description` | Sim | Terceira pessoa. Incluir WHAT + WHEN. Termos de trigger. Max 1024 chars. |
| `version` | Não | Semver (ex: `0.2.0`) para rastrear updates |
| `context` | Não | `fork` = isola em subagent com contexto separado |
| `agent` | Não | Tipo de subagent: `Explore`, `Plan`, `general-purpose` (só com `context:fork`) |
| `allowed-tools` | Não | Ferramentas sem aprovação: `Read, Grep, Glob`, `Bash(npm run *)` |
| `argument-hint` | Não | Hint no autocomplete: `[slide-file]`, `[query]` |
| `user-invocable` | Não | `false` = esconde do `/`; Claude ainda auto-ativa |
| `disable-model-invocation` | Não | `true` = só invocação manual (para workflows com side-effects) |

> **Bug conhecido (Issue #17283):** `context:fork` e `agent:` são ignorados quando skill é invocado via Skill tool (API/SDK). Funciona apenas no CLI direto.

---

## Melhores Práticas (Cursor Docs + create-skill)

1. **Descrição:** Terceira pessoa, específica, com termos de trigger
   - ✅ "Processa specs do Notion e gera HTML assertion-evidence. Use quando criar, implementar ou modificar slides médicos."
   - ❌ "Ajuda com slides"

2. **Concisão:** SKILL.md < 500 linhas. Detalhes em reference.md

3. **Progressive disclosure:** Essencial em SKILL.md; referências em arquivos separados

4. **When to Use:** Cenários concretos que disparam o skill

5. **Exemplos concretos:** Não abstratos

6. **Scripts:** Self-contained, mensagens de erro úteis

---

## Anti-patterns

- Paths Windows (`\`) — usar `/`
- Muitas opções sem default
- Informação sensível ao tempo (datas fixas)
- Nomes vagos: `helper`, `utils`, `tools`

---

## Skills do Projeto

### Claude Code (`.claude/skills/`) — 19 ativas

| Skill | version | context | allowed-tools | Papel |
|-------|---------|---------|---------------|-------|
| `evidence` | 0.2.0 | fork / general-purpose | Read, WebSearch | Busca evidências PubMed → citação AMA + dados slide |
| `medical-researcher` | 1.0.0 | fork / general-purpose | Read, Grep, Glob, Agent, WebSearch, WebFetch | Orquestrador multi-MCP: 4 agentes paralelos, triangulação, rubrica profundidade 8-dim |
| `sync-evidence` | 1.0.0 | fork / general-purpose | Read, Write, Grep, Glob, Agent | Ponte pesquisa→persistência: evidence-db.md + Notion (opcional, via reference-manager) |
| `review` | 0.4.0 | fork / Explore | Read, Grep, Glob | Audita slides: PASS/WARN/FAIL por dimensão (inclui assertion-evidence + medical-data) |
| `ralph-qa` | 6.0.1 | fork / qa-engineer | Read, Write, Bash | QA em 2 loops (Opus lint + Gemini visual) até PASS |
| `final-pass` | 3.0.0 | fork / general-purpose | Read, Edit, Bash, Grep, Glob, Agent | Avaliação final deck — coerência (A) + empolgação (B, 10 critérios) via Gemini |
| `new-slide` | — | — | — | Cria slide HTML completo com archetype correto |
| `export` | — | — | — | Exporta slides para PDF/compartilhamento |
| `docs-audit` | 0.2.0 | fork / general-purpose | Read, Grep, Glob | Audita docs/*.md: links, redundância, token economy |
| `context7` | — | — | Read, Grep, Glob | Injeta docs de libs no contexto (GSAP, Reveal, Vite, OKLCH) |
| `mem-search` | — | — | Read, Grep, Glob | Busca semântica na memória do projeto |
| `new-skill` | 2.0.0 | fork | Read, Write, Glob, Grep | Scaffold de nova skill (3 templates: simple, orchestrator, lazy) |
| `repo-janitor` | — | fork / general-purpose | Read, Grep, Glob, Bash | Audit orphan files, broken links, dead HTML (read-only) |
| `audit-rules` | — | — | Read, Grep, Glob | Audita rules para contradições, stale refs, gaps |
| `evolve` | — | fork / general-purpose | Read, Grep, Glob, WebSearch | Comitê de evolução — pesquisa + patches para skills/docs/tools |
| `gtd` | — | — | Read, Write | Getting Things Done file-based (inbox, next actions, weekly review) |
| `resolve-conflict` | — | — | Read, Grep | Guia PT-BR para merge conflicts |
| `slide-punch` | 1.0.0 | — | Read, Grep, Glob | Avalia encaixe narrativo de 1 slide — transições, gancho retórico, densidade vs respiro |
| `retro` | — | — | Read, Edit, Write, Grep, Glob | Extrai lições da sessão para tasks/lessons.md |

### Archived (`.claude/skills/archive/`)

| Skill | Absorvido por | Motivo |
|-------|---------------|--------|
| `assertion-evidence` v0.2.1 | `review` v0.4+ | Assertion-evidence é dimensão de auditoria dentro do review |
| `medical-data` v0.2.1 | `review` v0.4+ | Verificação de dados clínicos é dimensão de auditoria dentro do review |

### Cursor (`.cursor/skills/`)

| Skill | Papel |
|-------|-------|
| `slide-frontend-ux` | Frontend review UX de slides |

| Skill | Papel |
|-------|-------|
| `medical-slide` | Notion→HTML, tri-mode, execução completa |
| `visual-qa` | Playwright, a11y, screenshots |
| `docs-audit` | Canônico — Claude Code delega para `.cursor/skills/docs-audit/` |

## Papéis — Sem conflito

| Superfície | Skills | Papel |
|------------|--------|-------|
| **Cursor** | .cursor/skills/ | Execução: build, MCPs, subagents, Playwright |
| **Claude Code** | .claude/skills/ | Terminal: auditoria, validação, pesquisa (sem Cursor) |
| **Claude.ai** | .claude/skills/ | Web: specs, narrativa (upload manual) |

**Regra:** Cada superfície usa seu diretório. docs-audit espelhado: mesmo conteúdo, path adaptado. Nenhum skill duplica papel de outro.
