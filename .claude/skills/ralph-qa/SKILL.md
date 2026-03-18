---
name: ralph-qa
description: QA em dois loops separados por batch de 3 slides. Loop 1 (Opus 4.6): lint+constraints+estética (14 dimensões AUDIT-VISUAL.md) até PASS. Loop 2 (Gemini Flash/Pro via MCP): visual audit com video .webm das animações reais até PASS. Ativar quando usuário pedir "qa loop", "rodar qa até passar", "fix all lint", "qa autônomo", "qa batch".
version: 6.0.1
context: fork
agent: general-purpose
allowed-tools: Read, Edit, Bash, Grep, Glob, Agent
argument-hint: "[lecture?] [batch-size=3] [max-iterations=10]"
---

# Ralph-QA v6 — Opus Loop + Gemini Loop

Aula: `$ARGUMENTS` (default: auto-detectar via branch). Batch: 3 slides. Max iter/loop: 10.

## Arquitetura

```
Para cada batch de 3 slides:

  LOOP 1 — Opus 4.6 (codigo, constraints, estetica)
    → lint:slides → constraint check (h2, ul/ol, notes, E07, var(), fontes)
    → Playwright screenshots → Opus avalia 14 dim (AUDIT-VISUAL.md)
    → Fix cirurgico ate todas 14 dim >= 9 → "OPUS-PASS"

  LOOP 2 — Gemini 3.1 Pro (visual, animacoes, percepcao)
    → Screenshots/video .webm → Gemini audit → filtra confidence >= 80
    → Opus executa fix specs → Gemini re-audita → "GEMINI-PASS"

  git commit batch N → proximo batch
```

## Loop 1 — Opus

Criterio: todas 14 dimensoes AUDIT-VISUAL >= 9. Dims: H(hierarquia) T(tipografia) E(layout) C(cor) V(visuais) K(consistencia) S(sofisticacao) M(comunicacao) I(interacoes) D(dados) A(acessibilidade) L(carga cognitiva) P(aprendiz adulto) N(narrativa).

## Loop 2 — Gemini

Modelo: Pro 3.1 (default, ~$0.06/pass). Fallback: Flash 3, Flash-Lite 3.1.
Input: video .webm (default) ou screenshots estaticos.
Gemini **so sugere** — retorna JSON spec → Opus le o arquivo e executa fix.

Spec format por issue:
```json
{
  "slide": "08-a2-01.html",
  "line_hint": 23,
  "confidence": 91,
  "issue": "hero-number usa color hardcoded",
  "fix": "substituir por var(--danger)"
}
```

Prompt Gemini: aula medica, Reveal.js/deck.js Plan C 1280x720, design system OKLCH. Avaliar: hierarquia visual, flow narrativo (comparar estados S0→SN), legibilidade, daltonismo, densidade (<=30 palavras). Issues com confidence >= 80 apenas.

## Seguranca

- Max 10 iter **por loop**
- Fix > 30% do slide → PARAR + reportar
- NUNCA deletar `<aside class="notes">`
- NUNCA modificar dados clinicos — marcar `[TBD]`
- Issue < 80 confianca → ignorar
- Mesmo issue 3x no Loop 2 → PARAR (root cause humano)
