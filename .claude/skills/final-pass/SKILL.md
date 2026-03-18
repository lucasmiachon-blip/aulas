---
name: final-pass
description: |
  Avaliacao final do deck completo — coerencia cross-slide, ritmo narrativo, empolgacao, alternancia dark/light, densidade cognitiva. Inclui 10 criterios de excitement (resets de atencao, surprise numbers, breathe-to-think ratio, pause graduation, emotional valence). Rodar APENAS quando Gates 1-3 ja passaram. Ativar com "final pass", "acabamento", "deck pronto?", "avaliacao final", "polish", "narrativa empolgante?", "o deck engaja?".
version: 3.0.0
context: fork
agent: general-purpose
allowed-tools: Read, Edit, Bash, Grep, Glob, Agent
argument-hint: "[aula=auto-detect] [model=flash|pro] [mode=video|static|both] [max-iterations=3]"
---

# Final Pass v3 — Coerencia + Empolgacao

Deck: `$ARGUMENTS` (default: auto-detect, model: Pro 3.1, max: 3 iteracoes).

## Pre-requisito

**NAO rodar antes de Gates 1-3 passarem:** lint:slides (0 erros), /review, /ralph-qa (OPUS-PASS + GEMINI-PASS).

## Dois eixos de avaliacao

### Eixo A — Coerencia (ja existia)

| Dominio | O que checa |
|---------|-------------|
| A1 Coerencia cross-slide | Mesma cor/tipografia para mesmo conceito em todos slides |
| A2 Transicoes entre atos | Slide de transicao existe? Background muda? |
| A3 Abertura e fechamento | Hook impactante? CTA final concreto? (Primacy-recency) |
| A4 Apresentabilidade | "Voce apresentaria isso amanha num congresso?" |

### Eixo B — Empolgacao (NOVO v3)

> "Dados corretos que nao grudam = palestra esquecida em 48h."
> Fontes: Duarte (Resonate), Medina (Brain Rules 10-min rule), Kahneman (anchoring),
> Agarwal (testing effect), Meyer & Land (threshold concepts), Sweller (CLT)

| Criterio | O que checa | Como medir |
|----------|-------------|------------|
| **B1 Resets de atencao** | Pelo menos 1 reset a cada 8-12 slides (~10 min). Tipos: checkpoint, caso clinico twist, pergunta retorica, revelacao surpresa, mudanca de modo | Contar slides entre interaction points em _manifest.js. Flag se gap >12 |
| **B2 Surprise numbers** | Para hero numbers (NNT, mortalidade, HR), o baseline/esperado aparece ANTES do surpresa (via click-reveal ou slide anterior). O delta entre expectativa e realidade = empolgacao | Verificar data-reveal order + conteudo do slide anterior. Flag se hero number aparece sem contexto de contraste |
| **B3 Breathe-to-think ratio** | Pelo menos 1 em 4 slides e "breathe" (hero number, visual unico, beat emocional). O resto e "think" (dados, protocolo, evidencia) | Calcular fill ratio + element count via _manifest.js. Flag se ratio < 1:4 |
| **B4 Mode switches** | Pelo menos 2 trocas de modo por ato (dado→caso, caso→pergunta, pergunta→protocolo, protocolo→revelacao) | Analisar narrativeRole transitions em _manifest.js. Flag se <2 por ato |
| **B5 Pause graduation** | Speaker notes especificam duracao de pausa proporcional ao peso do conteudo: 3s (enfase), 5s (surprise number), 7s (mortalidade/dado impactante) | Grep por PAUSA nos notes. Flag se todas pausas = mesma duracao ou ausentes |
| **B6 Emotional valence arc** | Sequencia de valencia emocional NAO e monotona: neutro→tensao→alivio→tensao→esperanca. Max 4 slides consecutivos com mesma valencia | Mapear valencia por slide (neutro/tensao/esperanca/perigo/alivio). Flag se 4+ consecutivos iguais |
| **B7 Committed prediction** | Pelo menos 2 momentos no deck onde a audiencia e convidada a prever antes de ver a resposta (checkpoint, poll, "o que voce faria?") | Contar slides com interacao pre-reveal (checkpoints + polls). Flag se <2 |
| **B8 Reframing** | Pelo menos 3 slides com h2 que desafiam uma suposicao convencional ("X nao significa Y", "apesar de X, Y", "o mito de X") | Analisar linguagem de contraste no h2. Flag se <3 no deck |
| **B9 Densidade cognitiva por ato** | Act 1 = baixa-media (schema building), Act 2 = alta (decisoes clinicas), Act 3 = media-baixa (resolucao, esperanca) | Calcular elementos por slide por ato. Flag se curva nao segue padrao |
| **B10 Ritmo dark/light** | Alternancia dark/light segue arco Duarte. Transicoes de background marcam mudanca narrativa, nao decoracao | Verificar sequencia de backgrounds. Flag se >4 consecutivos mesma cor |

## Workflow

### Fase 1 — Structural (Opus, automatico)

Antes de enviar para Gemini, fazer checagem automatica lendo _manifest.js + speaker notes + HTML:

```
1. Ler _manifest.js → extrair: id, narrativeRole, tensionLevel, archetype
2. Para cada slide: ler <aside class="notes"> → extrair timing, PAUSA, perguntas
3. Calcular metricas B1-B10 automaticamente
4. Gerar "Pacing Map" do deck:

| # | Slide | Tempo | Densidade | Valencia | Modo | Reset? | Breathe? |
|---|-------|-------|-----------|----------|------|--------|----------|
| 1 | s-hook | 0:00 | baixa | tensao | caso | - | breathe |
| 2 | s-title | 0:30 | baixa | neutro | titulo | - | breathe |
| ... | ... | ... | ... | ... | ... | ... | ... |

5. Flaggar issues B1-B10 com confidence
```

### Fase 2 — Visual (Gemini)

1. **Gerar material:** Video .webm (default, 3-5s/slide via Playwright) e/ou screenshots estaticos
2. **Montar pacote:** Screenshots na ordem + Pacing Map + narrativeRole/tensionLevel + speaker notes
3. **Enviar para Gemini:** Via MCP (auto) ou API script ou manual

Prompt Gemini atualizado — avaliar os 2 eixos:

**Eixo A (coerencia):**
1. Coerencia visual (cor, tipografia, espacamento)
2. Alternancia dark/light como marcador narrativo
3. Transicoes entre atos
4. Animacoes e motion (timing, easing, adequacao)

**Eixo B (empolgacao):**
5. O deck mantem atencao? Onde voce perderia a audiencia?
6. Os surprise numbers funcionam? O reveal tem impacto?
7. Existe variacao de ritmo ou e monotono?
8. O arco emocional e coerente (tensao→resolucao→tensao→esperanca)?
9. Os checkpoints criam "committed prediction" antes de revelar?
10. O fechamento e acionavel ("o que fazer amanha")?

4. **Processar:** Issues confidence >= 80 → Opus fix. Ambiguos → [HUMAN-REVIEW]
5. **Re-avaliar:** Corrigir → re-screenshot → re-enviar. Max 3 iteracoes.

Output JSON: `{ scope, axis (A|B), criterion, slides_affected, severity, confidence, issue, fix, principle }`.

## Pacing Map (output da Fase 1)

Gerado automaticamente. Formato:

```
## Pacing Map — [Aula] ([N] slides, [MM:SS] estimado)

### Metricas globais
- Resets de atencao: [N] (target: >= ceil(slides/10))
- Breathe-to-think ratio: [X:Y] (target: >= 1:4)
- Mode switches por ato: A1=[N], A2=[N], A3=[N] (target: >=2 cada)
- Pause graduation: [3s: N, 5s: N, 7s: N] (target: variacao)
- Emotional valence: [sequencia resumida] (target: nao monotona)
- Committed predictions: [N] (target: >=2)
- Reframings: [N] (target: >=3)

### Timeline
[tabela completa: #, slide, tempo, densidade, valencia, modo, reset, breathe]

### Flags
- B1 FAIL: Gap de [N] slides sem reset entre s-XX e s-YY
- B5 WARN: Todas pausas = 3s, sem graduacao
- ...
```

## Criterios de PASS

**Eixo A:** Nenhum issue de coerencia com confidence >= 80.
**Eixo B:** Todos os 10 criterios B1-B10 satisfeitos. Tolerancia: max 2 WAR, zero FAIL.
**Deck PASS = A-PASS + B-PASS.**

## Custo

Pro 3.1: ~$0.26/pass, ~$0.77/3 passes. Flash 3: ~$0.07/pass. Budget: ate $100/projeto.

## Seguranca

- Max 3 iteracoes
- Gemini so sugere — Opus executa
- Issues < 80 confianca → ignorar. 3x sem melhora → [HUMAN-REVIEW]
- NUNCA modificar dados clinicos
- Criterios B (empolgacao) sao SUGESTIVOS, nao bloqueantes. Lucas tem a palavra final sobre ritmo e tom.
