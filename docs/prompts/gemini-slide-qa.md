# Gemini Slide QA — Prompt Template (Gate 4)

> v2.1 — o MENOS determinístico possível.
> Gemini tem fresh eyes. É especialista UI/UX, front-end, tipografia, cores.
> Não dizer o que procurar. Deixar o especialista trabalhar.
> Placeholder `${VAR}` por slide — preencher antes de enviar.

## Quando usar

Review visual de slide individual via Gemini (Gate 4 do QA pipeline).
Modelo: `gemini-3.1-pro` via MCP ou API REST.

## Variaveis (preencher por slide)

| Variavel | Exemplo | Fonte |
|----------|---------|-------|
| `${AULA}` | Meta-analise — Leitura critica para decisao clinica | CLAUDE.md da aula |
| `${PUBLICO}` | Residentes de clinica medica (basico-intermediario), Brasil | CLAUDE.md da aula |
| `${TELA}` | TV 75" 4K, sala de 40 lugares, plateia a 2-6m | Lucas define por evento |
| `${SLIDE_ID}` | s-hook | _manifest.js |
| `${SLIDE_POS}` | slide 2 de 18 | _manifest.js index |
| `${SLIDE_ANTERIOR}` | s-title — capa com 3 pilares | _manifest.js |
| `${SLIDE_SEGUINTE}` | s-contrato — 3 cards framework | _manifest.js |
| `${HTML_RAW}` | (conteudo completo) | slides/NN-slug.html |
| `${CSS_RAW}` | (CSS relevante do slide) | {aula}.css |
| `${JS_RAW}` | (state machine, se houver) | slide-registry.js |
| `${NOTES_RAW}` | (speaker notes) | aside.notes |

## Materiais multimodais

1. Screenshots PNG por estado/beat (1280x720)
2. Video .webm da animacao completa (se disponivel)
3. Raw HTML, CSS, JS, Notes inline

## Prompt

```
Voce é um especialista em UI/UX, front-end, tipografia e cor. Voce nunca viu este slide antes.

Este é UM slide de uma apresentação médica para ${PUBLICO}. Slide ${SLIDE_POS}. Vem depois de "${SLIDE_ANTERIOR}" e antes de "${SLIDE_SEGUINTE}".

O meio:
- É uma APRESENTAÇÃO, não uma página web. Canvas fixo 1280x720px, renderizado em ${TELA}.
- Este estágio do QA foca em LEGIBILIDADE — o slide precisa ser lido sem esforço por quem está sentado na última fileira.

Você recebe screenshots do slide (cada estado/beat se houver animação), o código-fonte completo (HTML + CSS + JS), e as speaker notes (o que o palestrante fala durante este slide).

${HTML_RAW}

${CSS_RAW}

${JS_RAW}

${NOTES_RAW}

Imagine que você é um residente sentado na plateia. Depois de ver este slide e ouvir o palestrante:
- Chamou sua atenção?
- Trouxe algo útil?
- Você conseguiu ler tudo sem esforço?

Agora com seus olhos de especialista UI/UX:
- O que funciona e por quê.
- O que não funciona e por quê.
- O que você faria diferente — propostas concretas. Pode ser qualquer coisa: tipografia, cor, layout, espaçamento, animação, conteúdo, texto. Se puder dar código, melhor. Se não, direção clara.

Seja direto. Não precisa seguir formato rígido. Diga o que importa.
```

## Parametros API

```js
generationConfig: {
  temperature: 0.9,       // criação bela, não aleatoriedade
  maxOutputTokens: 16384
}
```

## Principio

O valor do Gemini neste gate é ver o que nós (que olhamos para este slide há dias) não vemos mais.

Quanto MENOS estrutura no prompt, MAIS livre o especialista fica para apontar o que realmente importa. Rubricas numéricas, checklists obrigatórios e formatos rígidos canalizam a atenção para os nossos critérios — e perdem o que só fresh eyes captam.

O único viés que injetamos: **legibilidade**. O resto é expertise do Gemini.
