# Instruções para Continuação — Apresentação Osteoporose

## Status Atual (10/12/2024)

### Slides Finalizados ✅
1. **Classificação Prática de Risco** — 3 colunas (Alto / Muito Alto / Iminente)
2. **Quanto maior o risco basal, maior o ganho** — 2 gráficos + 2 data points NNT
3. **Risco iminente: a janela crítica** — Gráfico com janela dourada 0-2 anos
4. **Risco de refratura por sítio em 1 ano** — Barras horizontais (coluna/pelve destacadas)

---

## Design System Consolidado

### MODO 1: Pão Diário (80% dos slides — técnico/protocolo)

| Elemento | Especificação |
|----------|---------------|
| **Fundo** | Creme `#FAF8F5` |
| **Títulos** | Georgia Bold, 32-40pt, Azul Marinho `#1a365d` |
| **Corpo** | Lato, 12-14pt, Cinza `#4A5568` |
| **Fio de Ouro** | Borda dourada `#C9A227` em caixas de insight |
| **Destaque quente** | `#D4A574` (barras, highlights) |
| **Bordas de cartão** | Cinza gelo `#E0E0E0`, 0.75pt |
| **Números-chave** | Negrito, azul marinho, tamanho maior (16-18pt) |
| **Referências** | Itálico, 9pt, cinza sutil `#718096` |

### Princípios Visuais
- **Guerra às Caixas Sólidas** — Usar cartões brancos com borda fina, não fundos coloridos
- **Subtítulos enxutos** — 1-2 linhas, frase poderosa, destaque em negrito
- **Legendas de gráfico** — Itálico, acima ou dentro do gráfico
- **Data Points** — Caixas brancas com borda dourada, NNT em destaque grande
- **Hierarquia numérica** — Números em negrito sempre (7-10, 8-12, 2-3×, etc.)

---

## Padrões de Slide por Tipo

### Slide de Protocolo/Classificação
- 3 colunas (cartões brancos)
- Stripe colorido fino no topo (ouro/azul/vinho)
- Bullets com conectores lógicos em negrito (ou, e)
- Linha de síntese no rodapé

### Slide de Evidência/Gráfico
- Título + subtítulo enxuto
- Gráfico centralizado com destaque visual (janela, cor)
- 2 bullets informativos abaixo
- Frase de conexão clínica
- Referência pequena

### Slide de Dados Comparativos
- 2 gráficos lado a lado
- 2 Data Points (mesma largura dos gráficos)
- Borda dourada nos Data Points
- NNT grande e em negrito

---

## Próximos Slides a Criar

1. **Tratamento: visão geral das opções** — Antirreabsortivos vs Anabólicos
2. **Zoledronato: o pilar do tratamento** — Dados HORIZON
3. **Denosumabe: potência com ressalvas** — Rebound, sequenciamento
4. **Anabólicos: quando usar first** — Romosozumabe, Teriparatida
5. **Sequenciamento terapêutico** — Fluxograma visual
6. **Casos clínicos** — 2-3 vinhetas com classificação e conduta

---

## Código Reutilizável

### Estrutura Base de Slide (pptxgenjs)
```javascript
const PptxGenJS = require('pptxgenjs');
const pptx = new PptxGenJS();
pptx.defineLayout({ name: 'CUSTOM', width: 13.33, height: 7.5 });
pptx.layout = 'CUSTOM';

const COLORS = {
  CREAM_BG: 'FAF8F5',
  WHITE: 'FFFFFF',
  NAVY: '1a365d',
  GOLD: 'C9A227',
  GOLD_WARM: 'D4A574',
  GRAY_BORDER: 'E0E0E0',
  GRAY_TEXT: '4A5568',
  GRAY_SUBTLE: '718096',
  WINE: '7B2D42'
};

const FONTS = {
  TITLE: 'Georgia',
  BODY: 'Lato'
};
```

### Cartão com Borda Dourada
```javascript
slide.addShape('roundRect', {
  x: X, y: Y, w: WIDTH, h: HEIGHT,
  fill: { color: COLORS.WHITE },
  line: { color: COLORS.GOLD, width: 1 },
  rectRadius: 0.05
});
```

### Texto com Destaque em Negrito
```javascript
slide.addText([
  { text: 'Texto normal ', options: { fontSize: 12, fontFace: FONTS.BODY, color: COLORS.GRAY_TEXT } },
  { text: 'destaque', options: { fontSize: 12, fontFace: FONTS.BODY, bold: true, color: COLORS.NAVY } },
  { text: ' continuação.', options: { fontSize: 12, fontFace: FONTS.BODY, color: COLORS.GRAY_TEXT } }
], { x: 0.5, y: Y, w: 12.3, h: 0.3 });
```

---

## Observações Importantes

1. **Sempre usar `view` no SKILL.md** antes de criar apresentações
2. **Paleta Rilkeana**: Azul + Ouro apenas (sem roxo, sem teal)
3. **Números sempre em negrito** — é o que o olho precisa pescar
4. **Subtítulos curtos** — se passar de 2 linhas, cortar
5. **Referências discretas** — 9pt, itálico, cinza sutil, rodapé
6. **Testar no PowerPoint** — LibreOffice renderiza diferente

---

## Arquivos de Código Criados
- `/home/claude/create-slide-classificacao-v2.js`
- `/home/claude/create-slide-nnt-v2.js`
- `/home/claude/create-slide-risco-iminente.js`
- `/home/claude/create-slide-refratura-sitio.js`

---

*Última atualização: 10/12/2024*
