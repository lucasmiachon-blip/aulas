# .claude/skills — Papel

**Superfície:** Claude Code (terminal), Claude.ai (web). Não conflita com .cursor — superfícies diferentes.

## Skills disponíveis (19 ativas + 2 archived)

| Skill | Papel | Quando ativar |
|-------|-------|--------------|
| `evidence` | Busca PubMed — RCT, meta-análise, guideline | "preciso de PMID para X" |
| `medical-researcher` | Orquestrador multi-MCP — 4 agentes paralelos, triangulação, rubrica de profundidade | "pesquisa profunda", "deep research", "avaliar profundidade" |
| `sync-evidence` | Persiste achados do researcher em evidence-db.md + Notion (opcional) | "sincronizar evidencias", "sync evidence", "salvar pesquisa" |
| `new-slide` | Cria HTML completo com template correto | "criar slide sobre X" |
| `review` | Auditoria multi-agent com confidence scoring (v0.4, parametrizado por aula) | "revise os slides" |
| `ralph-qa` | Loop autônomo lint→fix→build→fix até 0 FAILs | "qa loop", "rodar qa até passar" |
| `final-pass` | Avaliação final deck completo — coerência (A) + empolgação (B, 10 critérios) via Gemini | "final pass", "acabamento", "deck pronto?" |
| `docs-audit` | Auditoria de docs/*.md — redundância, links, verbosidade | "audite os docs" |
| `export` | PDF + screenshots via DeckTape | "exportar cirrose" |
| `context7` | Docs on-demand de GSAP/Reveal/Vite/OKLCH (lazy) | Ao codar com libs do projeto |
| `mem-search` | Busca semântica em HANDOFF/NOTES/lessons (lazy) | "o que decidimos sobre X?" |
| `new-skill` | Scaffold de nova skill (3 templates: simple, orchestrator, lazy) | "criar skill", "new skill" |
| `evolve` | Comitê de 4 agentes — pesquisa state-of-art, propõe patches para skills/docs/tools | "evoluir skills", "comitê", "evolve" |
| `repo-janitor` | Audita orphan files, broken MD links, dead HTML, temp files. READ-ONLY default | "limpar repo", "tem lixo?", "orphan files" |
| `resolve-conflict` | Guia passo-a-passo para resolver conflitos git. PT-BR, aprovacao obrigatoria | "resolver conflito", "merge conflict" |
| `gtd` | Getting Things Done simplificado — inbox, next actions, weekly review (lazy) | "gtd", "inbox", "o que tenho pendente?" |
| `retro` | Extrai lições da sessão atual em tasks/lessons.md | "retro", "extract lessons", final de sessão |
| `slide-punch` | Avalia encaixe narrativo de 1 slide — transicoes, gancho retorico, densidade | "slide solto", "nao se vende", "punch", "esse slide funciona?" |
| `audit-rules` | Audita .claude/rules/*.md — contradições, refs stale, gaps vs ERROR-LOG | "auditar rules", "rules stale?", "audit-rules" |

### Archived (`.claude/skills/archive/`)

| Skill | Motivo | Absorvido por |
|-------|--------|---------------|
| `assertion-evidence` | Coberto como dimensão de auditoria | `/review` v0.4+ |
| `medical-data` | Coberto como dimensão de auditoria | `/review` v0.4+ |

**Regra:** Cada skill tem um papel. Nenhum duplica função de outro.

## Pipeline — Sequência de uso

```
Pesquisa:   /evidence ──→ /medical-researcher ──→ /sync-evidence
                (rápida)      (profunda)           (persistir)

QA slide:   /review ──→ /ralph-qa ──→ commit
            (diagnóstico)  (fix loop)

Narrativa:  /slide-punch (1 slide solto/fraco)
            /final-pass  (deck inteiro, pós Gates 1-3)

QA deck:    /final-pass (Gates 1-3 já passaram, deck inteiro)

Suporte:    /evolve    (melhorar skills/docs)
            /docs-audit (auditar docs)
            /repo-janitor (limpar repo)
            /audit-rules (verificar rules)
```

**Regra de sequência:**
- `sync-evidence` só roda APÓS `medical-researcher` (precisa de achados)
- `final-pass` só roda APÓS Gates 1-3 (lint PASS + review PASS + ralph-qa PASS)
- `ralph-qa` pode rodar standalone, mas ideal após `/review` para ter diagnóstico

## Padrões arquiteturais utilizados

| Padrão | Origem | Skills que usam |
|--------|--------|----------------|
| Multi-agent paralelo + confidence scoring | code-review-agents (Anthropic) | `review`, `medical-researcher` |
| Lazy loading (frontmatter only no startup) | Context7 (Upstash) | `context7`, `mem-search` |
| 3-step token-efficient search | claude-mem (thedotmack) | `mem-search` |
| Comitê de votação (≥3/4 para aprovar patch) | Adversarial review pattern | `evolve` |
| Fan-out paralelo + consolidação + report | research-agent (Anthropic SDK demos) | `medical-researcher` |
| Rubrica de profundidade 8-dim + triangulação | Evidence-based medicine (GRADE) | `medical-researcher` |
| Plan-first + ask-if-unsure | manthanabc/paws + Olshansky | `resolve-conflict` |
| GTD 3-item focus limit | Raven GTD (mcpmarket) | `gtd` |

## Ralph Loop

Padrão de autonomia: Stop hook bloqueia Claude de sair, re-injeta o prompt, repete até `DONE`.
**Implementado em `ralph-qa`** para QA (domínio finito, critério objetivo).
Não usar para dev geral — escopo aberto → risco de loop infinito.

## Carregamento

Skills `context: lazy` → Claude lê só o YAML frontmatter no startup (~50 tokens).
Corpo completo carregado on-demand quando ativado → ~77% economia vs SessionStart hook.
