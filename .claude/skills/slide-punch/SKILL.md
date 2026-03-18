---
name: slide-punch
description: |
  Avalia se um slide individual se encaixa na narrativa e "se vende" — contexto (antes/depois), papel narrativo, gancho retorico, densidade vs respiro. Diagnostica slides que parecem soltos, fracos ou sem proposito claro. Ativar com "slide solto", "nao se vende", "slide fraco", "punch", "encaixe narrativo", "esse slide funciona?", "por que esse slide existe?".
version: 1.0.0
allowed-tools: Read, Grep, Glob
argument-hint: "<slide-id ou NN-slug.html> [aula=auto-detect]"
---

# Slide Punch — "Esse slide se vende?"

Slide: `$ARGUMENTS`

## Step 0 — Localizar

1. Auto-detectar aula: `git branch --show-current` → `feat/{aula}-*` ou pedir
2. Resolver slide: se `$ARGUMENTS` e ID (`s-a1-damico`), buscar em `_manifest.js`. Se filename (`02b-a1-damico.html`), buscar por arquivo.
3. Se nao encontrar → listar slides disponiveis e pedir ao usuario

## Step 1 — Ler contexto completo (5 arquivos)

| Arquivo | O que extrair |
|---------|---------------|
| `_manifest.js` | narrativeRole, tensionLevel, archetype, headline, actLabel do slide + 2 vizinhos (antes/depois) |
| `slides/{arquivo}.html` | h2 (assercao), corpo, aside notes |
| `references/narrative.md` | papel do slide no arco + tensao esperada |
| `aulas/{aula}/CLAUDE.md` | publico-alvo, tema |
| `references/evidence-db.md` | se o slide tem dados, verificar se estao no evidence-db |

## Step 2 — Diagnosticar (6 perguntas)

Responder CADA pergunta com PASS / WARN / FAIL + justificativa curta:

### P1. Por que esse slide existe?
- O slide tem um papel narrativo claro? (setup, evidencia, twist, checkpoint, resolucao, CTA)
- Se eu deletar esse slide, o deck perde algo? O que?
- FAIL se: "e informativo" (generico), "complementa" (vago), ou nao tem resposta clara

### P2. Transicao de entrada
- O slide ANTERIOR prepara para este? Existe ponte logica?
- O palestrante consegue fazer uma frase de transicao natural?
- FAIL se: salto tematico sem ponte, ou slide anterior nao tem relacao

### P3. Transicao de saida
- Este slide prepara para o PROXIMO? Existe gancho?
- FAIL se: slide seguinte muda de assunto sem que este feche o arco

### P4. Gancho retorico (o "punch")
- O h2 e uma assercao que PROVOCA (surpresa, contraste, decisao)?
- Ou e descritivo/informativo (rotulo, resumo, titulo generico)?
- Avaliar usando criterios: surprise number (B2), reframing (B8), committed prediction (B7)
- FAIL se h2 e rotulo generico ("Resultados", "Tratamento", "Diagnostico")

### P5. Densidade vs Respiro
- O slide e "think" (dados, evidencia, protocolo) ou "breathe" (hero, visual, beat emocional)?
- O tipo bate com os vizinhos? (evitar 4+ think consecutivos ou 3+ breathe consecutivos)
- Se think: tem dados suficientes para justificar 1 slide inteiro? Ou poderia ser absorvido pelo vizinho?
- Se breathe: o visual e impactante o suficiente para sustentar o slide sozinho?

### P6. Speaker notes alinham com visual
- As notes descrevem o que o visual mostra? (contiguidade temporal, Mayer)
- As notes tem PAUSA proporcional ao peso? (pause graduation, B5)
- As notes explicam POR QUE esse slide importa (nao so O QUE mostra)?

## Step 3 — Diagnostico

```
## Slide Punch — {slide-id}

| Pergunta | Veredicto | Nota |
|----------|-----------|------|
| P1 Por que existe | PASS/WARN/FAIL | ... |
| P2 Entrada | PASS/WARN/FAIL | ... |
| P3 Saida | PASS/WARN/FAIL | ... |
| P4 Gancho retorico | PASS/WARN/FAIL | ... |
| P5 Densidade/Respiro | PASS/WARN/FAIL | ... |
| P6 Notes alinham | PASS/WARN/FAIL | ... |

### Veredicto: {ENCAIXADO / SOLTO / FRACO}

- ENCAIXADO: 0 FAIL, max 1 WARN
- SOLTO: FAIL em P2 ou P3 (problema de transicao)
- FRACO: FAIL em P1 ou P4 (problema de proposito/retorica)

### Sugestoes (se SOLTO ou FRACO)
1. [sugestao concreta — NAO reescrever o slide, dar direcao]
2. [alternativa]
```

## Rules

- **Read-only.** Diagnostica, NAO edita. Sugestoes sao direcoes, nao codigo.
- **Contexto e tudo.** Sem ler vizinhos, nao ha como avaliar encaixe. Se _manifest nao tem vizinhos (primeiro/ultimo slide), ajustar criterios P2/P3.
- **NUNCA julgar conteudo clinico.** So estrutura narrativa, retorica e ritmo. Se dados estao errados, isso e dominio de `/review`.
- **Retorica NAO e deterministica.** Sugestoes sao opcoes, nao ordens. Lucas decide o tom final.
- **Publico importa.** Ler CLAUDE.md da aula — publico de congresso vs residencia muda completamente o "punch" esperado.
