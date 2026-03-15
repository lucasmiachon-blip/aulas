---
name: visual-qa
description: Use when testing, reviewing, or doing QA on slides. Runs visual checks with Playwright screenshots, accessibility verification with a11y, contrast checks, and reports issues found. See docs/SKILLS.md for best practices.
---

# Visual QA for Slides

> **Fonte canônica:** `.claude/agents/qa-engineer.md` — este arquivo é redirect + trigger guide.
> O agente `qa-engineer` cobre todas as dimensões abaixo + 14 dimensões com nota 0-10 (AUDIT-VISUAL.md).

## When to use

- User says "QA", "revise", "teste o slide", "verifique", "screenshot", "auditoria"
- Após implementar um batch de slides
- Antes de marcar qualquer slide como "ready" ou atualizar Notion status

## Como executar

**Para Cursor:** delegar para o subagent `qa-engineer` via Task tool:

```
Siga .claude/agents/qa-engineer.md. Auditar slide [ID].
URL local: http://localhost:3000/aulas/cirrose/
Viewport: 1280x720. Reportar com scorecard 14 dimensões (H,T,E,C,V,K,S,M,I,D,A,L,P,N).
```

**Para revisão rápida manual:**

| Check | Critério |
|-------|----------|
| Screenshot 1280×720 | Fill ratio 65-90%, sem overflow |
| a11y contraste | ≥ 4.5:1 body, ≥ 3:1 hero numbers |
| Interactions | `advance()` + `retreat()` testados |
| JS console | Zero erros |
| Plan B (sem JS) | Todo conteúdo visível com `.stage-bad` |

## 14 dimensões QA (AUDIT-VISUAL.md — referência rápida)

| Dim | Nome | Nota mín |
|-----|------|---------|
| H | Hierarquia Visual | 9/10 |
| T | Tipografia | 9/10 |
| E | Espaço & Layout | 9/10 |
| C | Cor & Contraste | 9/10 |
| V | Visuais & Figuras | 9/10 |
| K | Consistência | 9/10 |
| S | Sofisticação | 9/10 |
| M | Comunicação (Assertion-Evidence) | 9/10 |
| I | Interações | 9/10 |
| D | Dados clínicos | 9/10 |
| A | Acessibilidade | 9/10 |
| L | Carga cognitiva (Sweller CLT) | 9/10 |
| P | Aprendiz adulto (Knowles+Miller) | 9/10 |
| N | Arco narrativo (Duarte+Alley) | 9/10 |

## O que NÃO fazer

- Não alterar código durante QA — só reportar
- Não marcar como PASS se qualquer dimensão < 9
- Não pular Plan B (condições de projeção variam)
