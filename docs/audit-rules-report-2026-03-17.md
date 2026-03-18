# audit-rules Report — 2026-03-17

## FAIL (corrigir)

- **slide-editing.md**: Ref stale — cita `ERRO-033` e `ERRO-034` que não existem em ERROR-LOG.md (cirrose ou root). Essas regras operacionais foram derivadas de lessons (deck.js stopPropagation, data-background-color) mas nunca foram registradas como ERRO-NNN. Ação: registrar ERRO-033/034 em cirrose ERROR-LOG ou remover referências e documentar fonte como lessons.

## WARN (revisar)

- **design-principles.mdc vs design-principles.md**: lessons.md (16/mar) diz que .cursor tinha 11 princípios e foi alinhado para 26 com .claude (27). design-principles.md tem 27 princípios + Layout Patterns. Verificar se design-principles.mdc está atualizado.
- **slide-editing.md**: `references/decision-protocol.md` — path é relativo à aula. Existe em `aulas/cirrose/references/` mas a rule não especifica contexto. Outras aulas (metanalise, grade) podem não ter. Considerar path genérico ou documentar que é cirrose-specific.
- **ERRO-022 (HIGH, pendente)**: slide s-a1-vote — interação nunca testada. Nenhuma rule cobre explicitamente "QA de interação antes de commitar". css-errors E02 (preview antes de pronto) é próximo mas não específico para interação JS.
- **Bloat check**: .claude/rules/README.md declara pares complementares. design-principles: .claude tem 27 vs .cursor "11" (lessons diz 26 após correção). design-system + cirrose-design: split OK. Nenhuma duplicação substancial problemática detectada.

## INFO

- **design-system.md**: Cita `aulas/calibracao.html` — existe. `shared/assets/fonts/README.md` — existe.
- **Cross-refs entre rules**: Todos os links `[rule](rule.md)` em .claude/rules/ apontam para arquivos existentes (design-system, css-errors, slide-editing, deck-patterns, reveal-legacy, medical-data, motion-qa, slide-identity).
- **ERRO-033/034**: Regras operacionais em slide-editing referenciam códigos não registrados. Provável origem: lessons (16/mar deck.js). Decisão: registrar como ERRO ou usar "Fonte: lessons" em vez de ERRO-NNN.
- **GSAP version**: CLAUDE.md root diz GSAP 3.14. aulas/cirrose/CLAUDE.md diz 3.12. Inconsistência menor — cirrose pode estar desatualizado no doc.
- **Paths CSS**: lessons.md diz "NUNCA documentar shared/css/archetypes.css ou shared/css/cirrose.css — não existem". Nenhuma rule em .claude/rules/ documenta esses paths. OK.

## Summary

| Métrica | Valor |
|---------|-------|
| Rules auditadas | 10 (.claude/rules/*.md) |
| FAIL | 1 |
| WARN | 4 |
| INFO | 5 |
| Lessons cobertas por rules | ~85% (maioria tem regra correspondente; gaps: stage class body, ERRO-022 interação) |
| Erros CRITICAL+HIGH cobertos | 17/18 (ERRO-022 pendente sem rule específica) |

## Recomendações

1. **Prioridade alta:** Registrar ERRO-033 (stopPropagation) e ERRO-034 (data-background-color deck.js) em aulas/cirrose/ERROR-LOG.md, ou ajustar slide-editing.md para citar fonte como "lessons" em vez de ERRO-NNN.
2. **Prioridade média:** Adicionar rule ou checklist item para "interação JS deve ter ao menos 1 screenshot de cada estado antes de commitar" (cobre ERRO-022).
3. **Prioridade baixa:** Alinhar versão GSAP em aulas/cirrose/CLAUDE.md (3.12 → 3.14 se for o caso).
