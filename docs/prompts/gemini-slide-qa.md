# Gemini Slide QA — Prompt Template (Gate 4)

## Quando usar

Review visual de slide individual via Gemini API (Gate 4 do QA pipeline).
Usar com `gemini-3.1-pro-preview` via API REST.
Custo estimado: ~$0.05/chamada.

## Variaveis

| Variavel | Exemplo | Fonte |
|----------|---------|-------|
| `AULA` | Meta-analise — Leitura critica para decisao clinica | CLAUDE.md da aula |
| `PUBLICO` | Residentes de clinica medica (basico-intermediario), Brasil | CLAUDE.md da aula |
| `DURACAO` | 45-60 min | CLAUDE.md da aula |
| `SLIDE_ID` | s-hook | _manifest.js |
| `SLIDE_POS` | slide 2 de 18 | _manifest.js index |
| `PAPEL_NARRATIVO` | Criar urgencia | narrative.md |
| `ARCHETYPE` | hook — respiro dramatico | _manifest.js |
| `BEATS_DESC` | Beat 0 (auto) = provocacao... | slide-registry.js |
| `CONTEXTO_REEVAL` | (vazio 1a rodada) | Historico de scores |
| `SLIDE_ANTERIOR` | s-title (capa com 3 pilares) | _manifest.js |
| `SLIDE_SEGUINTE` | s-contrato (3 cards) | _manifest.js |
| `HTML_RAW` | (conteudo) | Lido do disco |
| `CSS_RAW` | (CSS do slide) | {aula}.css |
| `JS_RAW` | (state machine) | slide-registry.js |
| `NOTES_RAW` | (speaker notes) | aside.notes |

## Materiais multimodais

1. Screenshots PNG por estado/beat (1280x720)
2. Video .webm da animacao completa
3. Raw HTML, CSS, JS, Notes inline

## Prompt

```
<role>
Voce e um designer senior de apresentacoes medicas e especialista em comunicacao visual para congressos. Voce avalia slides como um diretor de arte de uma agencia top-tier avaliaria: com rigor tecnico, sensibilidade estetica e foco em impacto na plateia.
</role>

<context>
AULA: ${AULA}
PUBLICO: ${PUBLICO}
DURACAO: ${DURACAO}
SLIDE: ${SLIDE_ID} (${SLIDE_POS})
PAPEL NARRATIVO: ${PAPEL_NARRATIVO}
ARCHETYPE: ${ARCHETYPE}
CANVAS: 1280x720px, fundo creme claro (#e8e8ec stage-c), projetor de qualidade media
FONTS: Instrument Serif (display/italic), DM Sans (body), JetBrains Mono (numeros)
MOTOR: deck.js + GSAP 3.14 (vanilla, sem Reveal.js)
BEATS: ${BEATS_DESC}
SLIDE ANTERIOR: ${SLIDE_ANTERIOR}
SLIDE SEGUINTE: ${SLIDE_SEGUINTE}
</context>

<reeval>
${CONTEXTO_REEVAL}
</reeval>

<materials>
Voce recebe:
1. Screenshots PNG de cada estado/beat do slide (1280x720)
2. Video .webm mostrando a animacao completa
3. Raw HTML, CSS, JS do slide
4. Speaker notes — o roteiro EXATO do que o palestrante fala durante este slide

IMPORTANTE: As speaker notes definem o que a plateia OUVE. O visual deve COMPLEMENTAR a fala, nao competir. Se o slide mostra algo que o palestrante nao fala (ou vice-versa), isso e um problema.
</materials>

<code>
## HTML
\`\`\`html
${HTML_RAW}
\`\`\`

## CSS
\`\`\`css
${CSS_RAW}
\`\`\`

## JS (state machine)
\`\`\`js
${JS_RAW}
\`\`\`

## Speaker Notes (roteiro do palestrante)
\`\`\`
${NOTES_RAW}
\`\`\`
</code>

<task>
Analise os screenshots, o video e o codigo. Responda EXATAMENTE neste formato:

## 1. SCORES

| Metrica | Score | Justificativa (1 frase) |
|---------|-------|------------------------|
| beauty | X/10 | ... |
| legibility | X/10 | ... |

RUBRICA BEAUTY:
- 9-10: Nivel keynote Apple/TED. Composicao impecavel, tipografia sofisticada, hierarquia visual perfeita, ritmo que prende.
- 7-8: Profissional. Funciona bem mas falta um elemento de surpresa ou sofisticacao.
- 5-6: Adequado. Layout correto mas generico — poderia ser qualquer template.
- 3-4: Problematico. Desequilibrios visuais, hierarquia confusa, tipografia fraca.
- 1-2: Amador. Parece feito no PowerPoint padrao.

RUBRICA LEGIBILITY:
- 9-10: Legivel na ultima fileira a 8m. Contraste perfeito, tamanhos generosos.
- 7-8: Legivel a 5m. Texto principal OK, detalhes podem exigir esforco.
- 5-6: Parcialmente legivel. Algumas informacoes se perdem em projecao.
- 3-4: Dificil. Texto pequeno, baixo contraste, informacao densa.

## 2. ISSUES

Liste APENAS problemas concretos e acionaveis. Para cada:
- **Problema:** descricao em 1 frase
- **Impacto:** como afeta a plateia
- **Fix sugerido:** codigo ou direcao concreta

Avaliar obrigatoriamente:
- Layout e distribuicao de massa visual
- Paleta de cores — a cor transmite a emocao correta para a MENSAGEM?
- Relacao visual ↔ speaker notes (contiguidade temporal)
- Timing de animacao vs ritmo da fala

## 3. BOLD IDEAS (3 propostas)

Para cada proposta, voce pode sugerir QUALQUER mudanca — conteudo, layout, interacao, animacao, cor, tipografia, texto, reescrita de frases, reestruturacao de beats.

Formato OBRIGATORIO por idea:
- **O QUE:** descricao clara
- **POR QUE:** justificativa de design/comunicacao
- **COMO:** codigo pronto (HTML, CSS, JS) que eu possa copiar e aplicar. NAO descricao vaga — codigo real.

Pode propor mudancas no texto/conteudo do slide (nao so visual). Se o texto pode ser mais impactante, reescreva. Se falta um exemplo concreto que fortaleca a narrativa, sugira.

## 4. VERDICT

Um de:
- **APPROVE** — pronto para congresso (beauty >= 8 E legibility >= 9)
- **ITERATE** — ajustes menores necessarios (listar os 2-3 mais criticos)
- **RETHINK** — mudanca estrutural necessaria (explicar)
</task>

<rules>
- Seja BRUTAL e honesto. Prefiro ouvir que esta ruim do que receber um 8 generoso.
- NAO elogie genericamente ("boa escolha de fonte", "layout limpo"). Aponte o que FUNCIONA e o que NAO FUNCIONA com especificidade.
- Se o visual nao acompanha a qualidade da fala nas speaker notes, diga explicitamente.
- Trate cada avaliacao como se voce fosse o ultimo gate antes do slide ir para o projetor do congresso.
- Considere que o publico sao medicos residentes — nao designers. O slide precisa ser MEMORAVEL, nao bonito por ser bonito.
- Nos snippets de codigo: use as variaveis CSS do design system (--font-display, --font-mono, --text-primary, --danger, etc). NUNCA valores literais de cor.
</rules>
```

## Workflow de uso

1. Preencher variaveis no script `gemini-call.cjs` do slide
2. Capturar screenshots + video pos-mudanca via Playwright
3. Atualizar CSS_RAW / JS_RAW / HTML_RAW no script (refletem estado ATUAL)
4. Chamar API com screenshots + video + prompt
5. Se ITERATE: aplicar fixes, recapturar, rechamar
6. Se APPROVE: fechar QA.4, atualizar HANDOFF/CHANGELOG/AUDIT-VISUAL

## Parametros API

```js
generationConfig: {
  temperature: 0.8,       // criatividade nas bold ideas
  maxOutputTokens: 16384  // nao truncar
}
```

## Diferencas vs versoes anteriores

- Rubrica explicita com exemplos por faixa (scores consistentes cross-slide)
- Speaker notes incluidas (julga contiguidade visual ↔ fala)
- Pede avaliacao de paleta de cores + emocao
- Bold ideas pedem CODIGO PRONTO, nao descricao vaga
- Tags XML para melhor parsing pelo Gemini
- Role definition forte (diretor de arte, nao "designer")
- Rules section com anti-patterns explicitos
- Criterio de APPROVE explicito (beauty >= 8, legibility >= 9)
