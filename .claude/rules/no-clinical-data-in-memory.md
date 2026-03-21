# No Clinical Data in Agent Memory

> Dados clínicos vivem em evidence-db.md. Agent memory é para instruções procedurais.

---

## Regra

**NUNCA salvar dados clínicos em `.claude/agent-memory/`.**

Dados clínicos incluem:
- PMIDs, DOIs
- Números de trials (HR, RR, OR, NNT, NNH, ARR, IC 95%, p-values)
- Contagens de pacientes, tamanhos amostrais
- Citações bibliográficas com dados numéricos
- Scite tallies, AMSTAR-2 scores, I²
- Qualquer dado verificável de paper

## Onde vive cada tipo de dado

| Tipo | Destino canônico | Como chega lá |
|------|-----------------|---------------|
| Dados clínicos verificados | `references/evidence-db.md` | Via `/sync-evidence` com aprovação do usuário |
| Quotes retóricas | `NOTES.md` da aula | Append manual |
| Instruções procedurais do agente | `.claude/agent-memory/` | Permitido |
| Achados de pesquisa (transitório) | Output do medical-researcher | Não persistir — migrar via `/sync-evidence` |

## Motivação

- Agent memory é gitignored — dados lá não têm versionamento nem review
- Stale risk: dados em memory divergem de evidence-db sem detecção
- guard-evidence-db.sh (BLOCK) protege evidence-db; memory não tem guard
- Single source of truth: evidence-db.md é a única fonte para dados em slides

## Para o agente medical-researcher

Ao concluir pesquisa:
1. Apresentar achados ao usuário
2. Usuário decide o que persistir
3. Persistir via `/sync-evidence` → evidence-db.md
4. **NÃO** salvar dados clínicos em memory como "cache" ou "referência rápida"

Permitido em memory:
- Notas sobre quais MCPs funcionam/não funcionam
- Preferências de busca (ex: "DOIs lowercase para Scite")
- Estado de pipelines procedurais
