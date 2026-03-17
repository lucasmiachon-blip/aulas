# .claude/rules — Relação com .cursor/rules

> `.cursor/rules/` e `.claude/rules/` são **complementares, não redundantes**.

## Uso por superfície

| Superfície | Diretório | Papel |
|------------|-----------|-------|
| **Cursor** | `.cursor/rules/*.mdc` | Quick reference com frontmatter (globs, alwaysApply) |
| **Claude Code** | `.claude/rules/*.md` | Referência completa (clusters detalhados, princípios expandidos, workflows 5-tier) |
| **Claude.ai** | `.claude/rules/*.md` | Upload manual para Project Knowledge |

## Status por par

| .claude | .cursor | Quem é mais completo |
|---------|---------|---------------------|
| medical-data.md | medical-data.mdc | **.claude** (tabela Tier 1, checklist E21, WebSearch fallback) |
| slide-editing.md | slide-editing.mdc | **Ambos** (.cursor: tri-mode; .claude: E-codes, batch workflow) |
| design-principles.md | design-principles.mdc | **.claude** (27 princípios vs 11 — faltam Andragogia, F-pattern, Fill Ratio) |
| css-errors.md | css-errors.mdc | **.claude** (5 clusters detalhados, E30 regex, reincidências) |
| design-system.md | design-system.mdc + cirrose-design.mdc | **Split OK** (falta tabela WCAG no .cursor) |
| motion-qa.md | motion-qa.mdc | **.claude** (workflow 5 tiers, Gemini prompt, adequação por tipo) |
| deck-patterns.md | reveal-patterns.mdc | **.claude** (deck.js events, click-reveal, bg CSS) |
| reveal-legacy.md | — | .claude only (FROZEN — grade/osteoporose) |

## Regras sem par

| Arquivo | Existe em | Observação |
|---------|-----------|------------|
| core-constraints.mdc | .cursor only | Context window thresholds (70/85/95%) |
| plan-mode.mdc | .cursor only | Escalação por complexidade |
| notion-mcp.mdc | .cursor only | Workflow Notion + IDs |

## Regra

**Em caso de conflito:** conteúdo mais detalhado prevalece, independente do diretório.
