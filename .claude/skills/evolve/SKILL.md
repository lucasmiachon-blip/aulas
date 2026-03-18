---
name: evolve
description: Comitê de evolução do ecossistema — pesquisa state-of-art, lê lições do projeto, e propõe patches cirúrgicos para skills/docs/tools. Ativar quando usuário pedir "evoluir skills", "melhorar agentes", "atualizar docs", "comitê de evolução", "evolve".
version: 1.0.1
context: fork
agent: general-purpose
allowed-tools: Read, Edit, Bash, Grep, Glob, Agent, WebSearch, WebFetch
argument-hint: "[target: skills|docs|tools|all] [topic?]"
---

# Evolve — Comite de Evolucao

4 subagentes paralelos pesquisam, comparam e votam em patches. Consenso >= 3/4 → patch entra.

## Fases

### Fase 1 — Intel (4 agentes paralelos, sem comunicacao)

| Agente | Le | Pergunta |
|--------|----|----------|
| **Archaeologist** | lessons.md, HANDOFF, NOTES, git log -30 | Erros recorrentes? Workarounds? Gaps? |
| **Researcher** | WebSearch state-of-art (Claude Code, GSAP, agents) | O que mudou? Novas capacidades? Anti-patterns? |
| **Auditor** | Todas skills, rules, docs, CLAUDE.md | Gaps? Redundancias? Versoes stale? Cross-refs quebradas? |
| **Tools Inspector** | tools/*.js, package.json, npm outdated/audit | Deps desatualizadas? Vulnerabilidades? Duplicacao? |

### Fase 2 — Deliberacao (Opus sintetiza)

Opus le 4 relatorios → convergencias (>=2 agentes) → ranqueia: impacto x seguranca / esforco → lista de patches com id, title, file, type, risk, score.

### Fase 3 — Votacao

Cada agente vota: SIM / SIM* (com condicao) / NAO / VETO.
- >= 3 SIM → APROVADO
- >= 2 NAO → REJEITADO
- 1 VETO → humano decide

### Fase 4 — Aplicacao

Apresentar diffs ao Lucas. Aplicar aprovados apos confirmacao. Commit.

## Seguranca

- NUNCA modificar `shared/` sem voto unanime (4/4)
- NUNCA deletar skills — deprecar com `deprecated: true`
- NUNCA alterar dados clinicos
- Max 10 patches/sessao
- Humano aprova ANTES do commit
