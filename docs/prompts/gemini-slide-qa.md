# Gemini Slide QA — Prompt Template (Gate 4)

> v2 — reescrito para ser o MENOS determinístico possível.
> Gemini tem fresh eyes e é especialista UI/UX/front-end/tipografia/cores.
> Não dizer o que procurar. Deixar o especialista trabalhar.

## Quando usar

Review visual de slide individual via Gemini API (Gate 4 do QA pipeline).
Usar com `gemini-3.1-pro` via MCP ou API REST.

## Variaveis

| Variavel | Exemplo | Fonte |
|----------|---------|-------|
| `AULA` | Meta-analise — Leitura critica para decisao clinica | CLAUDE.md da aula |
| `PUBLICO` | Residentes de clinica medica (basico-intermediario), Brasil | CLAUDE.md da aula |
| `SLIDE_ID` | s-hook | _manifest.js |
| `SLIDE_POS` | slide 2 de 18 | _manifest.js index |
| `PAPEL_NARRATIVO` | Criar urgencia | narrative.md |
| `SLIDE_ANTERIOR` | s-title (capa com 3 pilares) | _manifest.js |
| `SLIDE_SEGUINTE` | s-contrato (3 cards) | _manifest.js |
| `HTML_RAW` | (conteudo) | Lido do disco |
| `CSS_RAW` | (CSS do slide) | {aula}.css |
| `JS_RAW` | (state machine, se houver) | slide-registry.js |
| `NOTES_RAW` | (speaker notes) | aside.notes |

## Materiais multimodais

1. Screenshots PNG por estado/beat (1280x720)
2. Video .webm da animacao completa (se disponivel)
3. Raw HTML, CSS, JS inline

## Prompt

```
Voce é um especialista em UI/UX, front-end, tipografia e cor. Voce nunca viu este slide antes.

Este é UM slide de uma apresentação médica para ${PUBLICO}. São ${SLIDE_POS} slides no total. Este slide (${SLIDE_ID}) vem depois de "${SLIDE_ANTERIOR}" e antes de "${SLIDE_SEGUINTE}". Seu papel narrativo: ${PAPEL_NARRATIVO}.

Limitações do meio:
- É uma APRESENTAÇÃO projetada, não uma página web. Canvas fixo 1280x720px.
- Projetor de qualidade média em sala de congresso. Plateia a 3-8m da tela.
- Este estágio do QA é sobre LEGIBILIDADE em projeção.

Você recebe screenshots do slide (cada estado/beat), o código-fonte (HTML + CSS + JS), e as speaker notes (o que o palestrante fala durante este slide).

${HTML_RAW}

${CSS_RAW}

${JS_RAW}

${NOTES_RAW}

Olhe para este slide com seus olhos de especialista. Me diga:

1. O que você vê — sua reação honesta ao abrir este slide pela primeira vez.
2. O que funciona e por quê.
3. O que não funciona e por quê — especialmente qualquer coisa que prejudique legibilidade em projeção.
4. O que você faria diferente — propostas concretas. Pode ser qualquer coisa: tipografia, cor, layout, espaçamento, animação, conteúdo, texto. Se puder dar código, melhor. Se não, direção clara.

Seja direto. Não precisa ser gentil. Não precisa seguir formato rígido. Diga o que importa.
```

## Parametros API

```js
generationConfig: {
  temperature: 1.0,       // maximo de fresh eyes
  maxOutputTokens: 16384  // nao truncar
}
```

## Principio

O valor do Gemini neste gate é ver o que nós (que olhamos para este slide há dias) não vemos mais.

Quanto MENOS estrutura no prompt, MAIS livre o especialista fica para apontar o que realmente importa. Rubricas numéricas, checklists obrigatórios e formatos rígidos canalizam a atenção para os nossos critérios — e perdem o que só fresh eyes captam.

O único viés que injetamos: **legibilidade em projeção**. O resto é expertise do Gemini.
