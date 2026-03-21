# XREF — Referências Cruzadas

> Mapa canônico de dependências entre documentos do projeto.
> Atualizar ao criar, mover ou deletar qualquer .md.
> Gerado: 2026-03-07. Última revisão: 2026-03-18.

---

## Legenda

- **Canônico** = fonte da verdade para aquele assunto
- **→** = "referencia" ou "depende de"
- **←** = "é referenciado por"

---

## Hierarquia de Autoridade

```
CLAUDE.md (root)              ← fonte de verdade operacional (absorveu AGENTS.md)
├── .claude/rules/*.md        ← regras detalhadas (prevalecem sobre .cursor se mais completas)
├── .claude/hooks/*.sh        ← safety gates determinísticos (100% enforcement)
├── .claude/scripts/*.sh      ← worktree lifecycle (init, cleanup)
├── .claude/skills/*/SKILL.md ← skills invocáveis (20 ativas + 2 archived)
├── .cursor/rules/*.mdc       ← regras Cursor (quick-ref com globs)
├── docs/*.md                 ← referência expandida
└── aulas/*/HANDOFF.md        ← estado por aula
```

**Conflito:** conteúdo mais detalhado prevalece, independente do diretório.

---

## Mapa de Referências

### CLAUDE.md (root) — canônico operacional
| Referencia | Tipo |
|-----------|------|
| → docs/RULES.md | Extensão |
| → docs/SKILLS.md | Extensão |
| → docs/SUBAGENTS.md | Extensão |
| → aulas/cirrose/HANDOFF.md | Estado |
| → aulas/cirrose/HANDOFF-CLAUDE-AI.md | Estado |
| → aulas/metanalise/HANDOFF.md | Estado |
| → tasks/lessons.md | Self-improvement |

### .claude/rules/

| Arquivo | Referencia | Referenciado por |
|---------|-----------|-----------------|
| README.md | → todos .claude/rules/*.md, .cursor/rules/*.mdc | ← XREF.md (este arquivo) |
| anti-drift.md | (autônomo — protocolo de foco) | ← CLAUDE.md (workflow step 1) |
| css-errors.md | → design-system.md, medical-data.md | ← slide-editing.md |
| design-principles.md | → design-system.md | ← CLAUDE.md |
| deck-patterns.md | → slide-identity.md, design-system.md | ← slide-editing.md, motion-qa.md, CLAUDE.md |
| design-system.md | (autônomo) | ← css-errors.md, design-principles.md, slide-editing.md, deck-patterns.md |
| medical-data.md | (autônomo) | ← css-errors.md, slide-editing.md |
| motion-qa.md | → slide-editing.md, deck-patterns.md, reveal-legacy.md | ← CLAUDE.md |
| reveal-legacy.md | → deck-patterns.md | ← slide-editing.md, motion-qa.md (FROZEN — grade/osteoporose) |
| slide-editing.md | → css-errors.md, design-system.md, deck-patterns.md, reveal-legacy.md, medical-data.md | ← CLAUDE.md |
| no-clinical-data-in-memory.md | → medical-data.md, sync-evidence skill | ← guard-evidence-db.sh |
| slide-identity.md | → slide-editing.md, deck-patterns.md | ← CLAUDE.md, deck-patterns.md |

### docs/

| Arquivo | Referencia | Referenciado por |
|---------|-----------|-----------------|
| README.md | → todos docs/*.md | (índice) |
| XREF.md | (este arquivo) | ← README.md |
| ECOSYSTEM.md | → SKILLS.md, RULES.md, KPIs.md | ← docs/README.md |
| KPIs.md | (autônomo) | ← ECOSYSTEM.md, README.md |
| RULES.md | → SUBAGENTS.md, .cursor/rules/*.mdc | ← docs/README.md, ECOSYSTEM.md |
| SKILLS.md | → .cursor/skills/, .claude/skills/ | ← docs/README.md, ECOSYSTEM.md |
| SUBAGENTS.md | → .cursor/rules/core-constraints.mdc | ← docs/README.md, RULES.md |
| SYNC-NOTION-REPO.md | → .env.example (IDs Notion) | ← docs/README.md |
| blueprint-cirrose.md | (autônomo) | ← aulas/cirrose/HANDOFF.md |
| biblia-narrativa.md | (autônomo) | ← aulas/cirrose/HANDOFF.md |
| slide-pedagogy.md | (autônomo — teorias pedagógicas) | ← README.md |
| insights-html-cirrose-2026.md | (autônomo — análise Gemini HTML) | ← README.md |
| MCP-ACADEMICOS.md | → nlm-skill/SKILL.md (Q&A grounded) | ← docs/README.md, nlm-skill |
| MCP-ENV-VARS.md | (autônomo) | ← ECOSYSTEM.md |
| SETUP.md | (autônomo — setup inicial) | ← README.md |
| ZIP-LIMPO-PROTOCOLO.md | (autônomo) | ← README.md |
| metanalise-scope.md | (autônomo) | ← README.md |
| archive/pipeline/README.md | (pipeline humano — arquivado) | ← SUBAGENTS.md |

### docs/prompts/ e docs/external/

| Arquivo | Referencia | Referenciado por |
|---------|-----------|-----------------|
| prompts/weekly-updates.md | (prompt template) | ← README.md |
| prompts/research-best-practices.md | (prompt template) | ← README.md |
| prompts/gemini-deck-audit.md | (prompt template — Gemini) | ← README.md |
| prompts/gemini-paper-extraction.md | (prompt template — Gemini) | ← README.md |
| prompts/gemini-transcript-comparison.md | (prompt template — Gemini) | ← README.md |
| prompts/openai-backward-design.md | (prompt template — OpenAI) | ← README.md |
| prompts/openai-canvas-storyboard.md | (prompt template — OpenAI) | ← README.md |
| prompts/gemini-slide-qa.md | (prompt template — Gemini Gate 4 QA) | ← README.md |
| external/11-long-context-auditor.md | (tool spec — Gemini long-context) | ← README.md |

### .claude/agents/ (custom subagents)

| Arquivo | MCPs scoped | Papel |
|---------|------------|-------|
| qa-engineer.md | playwright, lighthouse, eslint, perplexity, ui-ux-pro, design-comparison, floto | QA perfection loop 14 dimensoes |
| reference-manager.md | pubmed, crossref, notion, scite | Valida PMIDs/DOIs, formata AMA, sync Notion |
| medical-researcher.md | pubmed, crossref, semantic-scholar, scite, biomcp | Pesquisa profunda multi-MCP + triangulacao + rubrica profundidade |
| notion-sync.md | notion | Sync Slides DB repo ↔ Notion |
| slide-builder.md | playwright | Build slides HTML |
| repo-janitor.md | — | Audit orphan files, broken links |
| verifier.md | — | Valida que trabalho declarado done realmente passa |

### .claude/hooks/ (safety gates — determinísticos)

| Arquivo | Wired em settings.json | Função |
|---------|----------------------|--------|
| audit-trail.sh | PostToolUse, PostToolUseFailure (*) | P0 traceability — JSONL log de toda tool call |
| build-monitor.sh | PostToolUse, PostToolUseFailure (Bash) | Detecta falhas de build |
| check-evidence-db.sh | PreToolUse (Write) | Valida dados clínicos antes de escrever |
| guard-evidence-db.sh | PreToolUse (Write) | BLOCK todas escritas em evidence-db.md (exit 2) |
| guard-shared.sh | PreToolUse (Write, Edit) | Bloqueia edição de shared/ em branches não-main |
| guard-destructive.sh | (dormant — coberto por deny permissions) | Backup: bloqueia comandos destrutivos |
| guard-merge.sh | PreToolUse (Bash) | Valida merge: --no-ff em main, bloqueia shared/ changes |
| guard-secrets.sh | PreToolUse (Bash) | WARN-only: escaneia staged files por padrões de secrets |
| warn-class-c.sh | PreToolUse (Bash) | WARN-only: lista arquivos Classe C ao fazer git merge main em WT |
| post-compact-reinject.sh | SessionStart (compact) | Reinjecta HANDOFF + git log após /compact |
| session-tracker.sh | SessionStart, SessionEnd | Lifecycle de sessão (3-terminal tracking) |
| subagent-stop-log.sh | SubagentStop | Loga conclusão de subagents |

### .claude/scripts/

| Arquivo | Função |
|---------|--------|
| worktree-init.sh | Cria WT com validação, logging, regras |
| worktree-cleanup.sh | Valida estado, confirma merge, remove WT |

### scripts/ (git hooks — versionados)

| Arquivo | Função | Wired via |
|---------|--------|-----------|
| pre-commit.sh | Guard 1 (Classe C em main) + Guard 2 (shared/ em WT) + Guard 3 (slide-count regression) + Guard 4 (slide-integrity build) + lint | .git/hooks/pre-commit (delegator) |
| pre-push.sh | done-gate --strict para aula detectada na branch | .git/hooks/pre-push (delegator) |
| post-merge.sh | Anti-rollback: slide count loss + content diff detection pós-merge | .git/hooks/post-merge (delegator) |
| install-hooks.sh | Instala pre-commit + pre-push + post-merge em .git/hooks/ | Manual: `bash scripts/install-hooks.sh` |
| ghost-canary.sh | Detecta ghost skills (dirs sem SKILL.md) | Manual |

### aulas/cirrose/

| Arquivo | Referencia | Referenciado por |
|---------|-----------|-----------------|
| CLAUDE.md | (regras + estado aula) | ← CLAUDE.md root (projects table) |
| HANDOFF.md | → blueprint-cirrose.md, biblia-narrativa.md | ← aulas/cirrose/CLAUDE.md |
| HANDOFF-CLAUDE-AI.md | → HANDOFF.md | ← aulas/cirrose/CLAUDE.md |
| AUDIT-VISUAL.md | (scorecards QA) | ← aulas/cirrose/CLAUDE.md |
| CHANGELOG.md | (append-only — histórico de batches) | ← aulas/cirrose/CLAUDE.md |
| ERROR-LOG.md | (append-only — erros → regras) | ← aulas/cirrose/CLAUDE.md |
| NOTES.md | (log de decisões entre agentes) | ← aulas/cirrose/CLAUDE.md |
### aulas/metanalise/

| Arquivo | Referencia | Referenciado por |
|---------|-----------|-----------------|
| CLAUDE.md | → CLAUDE.md (root), metanalise-scope.md | ← CLAUDE.md (projects table) |
| HANDOFF.md | → blueprint.md, narrative.md, evidence-db.md | ← docs/README.md |
| references/narrative.md | (canônico narrativa) | ← CLAUDE.md aula, blueprint.md |
| references/evidence-db.md | (canônico dados clínicos) | ← blueprint.md, slides/ |
| references/blueprint.md | → narrative.md, evidence-db.md | ← HANDOFF.md |
| slides/_manifest.js | (canônico ordem/metadata slides) | ← lint:narrative-sync, index.html |
| WT-OPERATING.md | → HANDOFF.md, slide-identity.md | ← CLAUDE.md aula (doc order) |
| CHANGELOG.md | (append-only — histórico de batches) | ← HANDOFF-ARCHIVE.md |
| ERROR-LOG.md | (append-only — erros → regras) | → CHANGELOG.md (ref header) |
| AUDIT-VISUAL.md | → WT-OPERATING.md §4 | ← WT-OPERATING.md §4 (QA loop) |
| NOTES.md | (log de decisões entre agentes) | ← WT-OPERATING.md |
| HANDOFF-ARCHIVE.md | (sessões arquivadas) | ← HANDOFF.md |
| references/archetypes.md | (6 layout patterns) | ← CLAUDE.md aula |
| references/reading-list.md | (pre-reading list) | ← CLAUDE.md aula, HANDOFF.md |

### Arquivados (docs/archive/)

| Arquivo | Motivo |
|---------|--------|
| AGENTS.md | Absorvido por CLAUDE.md (mar/2026) |
| REPO-DIAGNOSTIC.md | Superseded |
| DIAGNOSTIC-27fev.md | Superseded |
| HANDOFF-geral-2026-03-04.md | Estado distribuído por aula |
| HANDOFF_SYNC-CURSOR-2026-02-26.md | One-shot |
| cirrose-scope.md | Superseded por blueprint-cirrose.md |
| AUDIT-BATCHES.md | One-shot |
| research-skills-ecosystem-2026-03-11.md | Pesquisa ecosystem upgrade (referência, não operacional) |
| audit-rules-report-2026-03-17.md | Relatório audit rules (one-shot) |
| docs-audit-report-2026-03-17.md | Relatório docs audit (one-shot) |
| CHATGPT_HANDOFF_ACT2.md | One-shot planning Act 2 |
| NNT-IC95-REPORT.md | Relatório NNT verificação |
| aulas-magnas-system-v6.plan.md | System plan v6 |
| CURSOR.md | Superseded por CLAUDE.md (mar/2026) |

---

## Pares .claude ↔ .cursor

| .claude/rules/ | .cursor/rules/ | Mais completo |
|----------------|---------------|--------------|
| css-errors.md | css-errors.mdc | .claude |
| design-principles.md | design-principles.mdc | .claude (27 vs 11 princípios) |
| design-system.md | cirrose-design.mdc + design-system.mdc | Split OK |
| medical-data.md | medical-data.mdc | .claude |
| motion-qa.md | motion-qa.mdc | .claude |
| deck-patterns.md | reveal-patterns.mdc | .claude (deck.js specifics) |
| reveal-legacy.md | — | .claude only (FROZEN) |
| slide-editing.md | slide-editing.mdc | Ambos |
| slide-identity.md | slide-identity.mdc | .claude |

**Sem par em .claude:** core-constraints.mdc, plan-mode.mdc, notion-mcp.mdc (só .cursor).

---

## Canônicos por Assunto

| Assunto | Arquivo canônico | Fallback |
|---------|-----------------|----------|
| Anti-drift / foco de sessão | .claude/rules/anti-drift.md | — |
| Operacional (stack, regras, workflow) | CLAUDE.md | — |
| Tokens OKLCH | .claude/rules/design-system.md | base.css :root |
| Erros CSS | .claude/rules/css-errors.md | — |
| Dados médicos | .claude/rules/medical-data.md | — |
| Animações GSAP | .claude/rules/motion-qa.md | shared/js/engine.js |
| Deck.js patterns (ativo) | .claude/rules/deck-patterns.md | — |
| Reveal.js patterns (frozen) | .claude/rules/reveal-legacy.md | — |
| Assertion-Evidence | .claude/rules/slide-editing.md | design-principles.md §1 |
| Notion IDs | .env.example (variáveis `NOTION_*_ID`) | docs/SYNC-NOTION-REPO.md |
| MCP profiles | .mcp-profiles/*.json | .mcp.json (perfil ativo) |
| Estado Cirrose | aulas/cirrose/HANDOFF.md | — |
| Estado Metanalise | aulas/metanalise/HANDOFF.md | WT-OPERATING.md |
| Context window | docs/SUBAGENTS.md | .cursor/rules/core-constraints.mdc |
| Manifesto slides (cirrose) | aulas/cirrose/slides/_manifest.js | CLAUDE.md tabela |
| Manifesto slides (metanalise) | aulas/metanalise/slides/_manifest.js | CLAUDE.md tabela |
| Pipeline humano | docs/archive/pipeline/README.md | — |
| Pedagogia | docs/slide-pedagogy.md | .claude/rules/design-principles.md |
| KPIs multiagente | docs/KPIs.md | — |
| Benchmarks modelos | docs/ECOSYSTEM.md | — |
| Pesquisa médica profunda | .claude/skills/medical-researcher/SKILL.md | .claude/rules/medical-data.md, docs/MCP-ACADEMICOS.md |
| Q&A grounded em full-text | .claude/skills/nlm-skill/SKILL.md PAUSED (2026-03-22) | docs/MCP-ACADEMICOS.md |
| Safety gates (hooks) | .claude/settings.json + .claude/hooks/ | — |
| WT protocol | aulas/*/CLAUDE.md § Worktree | .claude/scripts/ |
| Audit trail | .claude/hooks/audit-trail.sh | ~/.claude/session-logs/ |

---

## Como Manter

1. **Novo doc:** adicionar aqui + em docs/README.md
2. **Mover/deletar:** atualizar referências aqui + grep por nome antigo
3. **Novo par .claude↔.cursor:** registrar na tabela de pares
4. **Auditoria periódica:** rodar skill `docs-audit` ou `audit-docs`
