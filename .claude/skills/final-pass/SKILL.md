---
name: final-pass
description: Avaliacao final do deck completo via Gemini — coerencia cross-slide, ritmo narrativo, alternancia dark/light, densidade cognitiva. Rodar APENAS quando Gates 1-3 ja passaram. Ativar com "final pass", "acabamento", "deck pronto?", "avaliacao final", "polish".
version: 2.0.1
context: fork
agent: general-purpose
allowed-tools: Read, Edit, Bash, Grep, Glob, Agent
argument-hint: "[aula=auto-detect] [model=flash|pro] [mode=video|static|both] [max-iterations=3]"
---

# Final Pass — Avaliacao de Deck Completo

Deck: `$ARGUMENTS` (default: auto-detect, model: Pro 3.1, max: 3 iteracoes).

## Pre-requisito

**NAO rodar antes de Gates 1-3 passarem:** lint:slides (0 erros), /review, /ralph-qa (OPUS-PASS + GEMINI-PASS).

## O que avalia (dominios que Gates 1-3 NAO cobrem)

| Dominio | O que checa |
|---------|-------------|
| Coerencia cross-slide | Mesma cor/tipografia para mesmo conceito em todos slides |
| Ritmo narrativo | Alternancia dark/light segue arco Duarte? Checkpoints no lugar? |
| Densidade cognitiva | Act 1 leve → Act 2 pesado → Act 3 resolucao (Sweller) |
| Transicoes entre atos | Slide de transicao existe? Background muda? |
| Abertura e fechamento | Hook impactante? CTA final concreto? (Primacy-recency) |
| Apresentabilidade | "Voce apresentaria isso amanha?" |

## Workflow

1. **Gerar material:** Video .webm (default, 3-5s/slide via Playwright) e/ou screenshots estaticos
2. **Montar pacote:** Screenshots na ordem do _manifest.js + narrativeRole/tensionLevel + speaker notes
3. **Enviar para Gemini:** Via MCP (auto) ou API script ou manual (user cola no web)
4. **Processar:** Issues confidence >= 80 → Opus fix cirurgico. Ambiguos → [HUMAN-REVIEW]
5. **Re-avaliar:** Se issues, corrigir → re-screenshot → re-enviar. Max 3 iteracoes.

## Prompt Gemini (resumo)

Aula medica, publico/tema de CLAUDE.md da aula. Deck completo na ordem de apresentacao. Avaliar:
1. Coerencia visual (cor, tipografia, espacamento)
2. Ritmo narrativo (tensao/resolucao Duarte sparkline)
3. Alternancia dark/light
4. Densidade cognitiva por ato
5. Transicoes entre atos
6. Animacoes e motion (timing, easing, adequacao)
7. Apresentabilidade geral

Output JSON: `{ scope, slides_affected, severity, confidence, issue, fix, principle }`. PASS se nenhum issue >= 80.

## Custo

Pro 3.1: ~$0.26/pass, ~$0.77/3 passes. Flash 3: ~$0.07/pass. Budget: ate $100/projeto.

## Seguranca

- Max 3 iteracoes
- Gemini so sugere — Opus executa
- Issues < 80 confianca → ignorar. 3x sem melhora → [HUMAN-REVIEW]
- NUNCA modificar dados clinicos
