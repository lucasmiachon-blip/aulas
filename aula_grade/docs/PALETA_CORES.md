# Paleta de Cores — Aula GRADE

Guia completo da paleta de cores do projeto. Usar em HTML/CSS agora e PowerPoint futuramente.

---

## Paleta Principal

### Navy Deep
```css
--navy-deep: #152432;
--navy-medium: #1E3A5F;
--navy-soft: #2A3D51;
```

**Uso:**
- Backgrounds principais
- Títulos de slides
- Textos de destaque
- Headers

**Peso visual:** 80% da apresentação

---

### Gold
```css
--gold: #D4AF37;
--gold-light: #f0c245;
--gold-dark: #C99D2E;
```

**Uso:**
- Call-to-action
- Números-chave (NNT, HR)
- Destaques importantes
- Linhas divisórias

**Peso visual:** 15% da apresentação

---

## Cores de Acento

### Blue (Certeza ALTA)
```css
--blue: #2563EB;
--blue-medium: #3B82F6;
--blue-light: #60A5FA;
```

**Uso:**
- Símbolos GRADE (⊕⊕⊕⊕)
- Links
- Dados positivos
- Evidência de alta qualidade

---

### Green (Benefícios)
```css
--green: #059669;
--green-bg: #D1FAE5;
```

**Uso:**
- Benefícios clínicos
- "Sim", aprovação
- Rate up (+1)
- Indicadores positivos

---

### Red (Riscos/Atenção)
```css
--red: #B91C1C;
--red-bg: #FEE2E2;
```

**Uso:**
- Riscos, efeitos adversos
- Rate down (−1)
- Atenção, alertas
- Rebaixamento GRADE

---

## Cores Neutras

### Background e Texto
```css
--bg: #F9F8F4;           /* Fundo slides (off-white quente) */
--text: #152432;          /* Texto principal (navy-deep) */
--text-secondary: #6B7280; /* Texto secundário (cinza) */
--border: #BeCDD8;        /* Bordas sutis */
```

---

## Hierarquia Cromática

### Regra 80-15-5

**80% Navy + Neutros (dominante):**
- Backgrounds
- Textos principais
- Estrutura geral

**15% Gold (destaque):**
- Títulos importantes
- Números-chave
- Call-to-action

**5% Acentos (sinalização):**
- Blue: certeza ALTA
- Green: benefícios
- Red: riscos

---

## Aplicações Práticas

### Slide de Título
```css
background: var(--navy-deep);
title-color: var(--gold);
subtitle-color: var(--bg);
```

### Slide de Conteúdo
```css
background: var(--bg);
title-color: var(--navy-deep);
text-color: var(--text);
highlight-color: var(--gold);
```

### Cards de Conceito
```css
background: white;
border-left: 4px solid var(--gold);
shadow: rgba(21, 36, 50, 0.08);
```

### Símbolos GRADE
```css
⊕⊕⊕⊕ → var(--blue)      /* ALTA */
⊕⊕⊕○ → var(--blue)      /* MODERADA */
⊕⊕○○ → var(--text-secondary) /* BAIXA */
```

---

## Combinações Recomendadas

### ✅ BOM
- Navy + Gold (contraste forte, elegante)
- Navy + White (leitura fácil)
- Gold + Navy-soft (destaque sutil)
- Blue + White (dados científicos)

### ❌ EVITAR
- Gold + Yellow (confunde)
- Red + Green (daltonismo)
- Navy-deep + Black (pouco contraste)
- Múltiplas cores saturadas juntas

---

## Acessibilidade

### Contraste WCAG AA (mínimo 4.5:1)

**✅ Aprovado:**
- Navy-deep (#152432) sobre White → 15.2:1
- Gold (#D4AF37) sobre Navy-deep → 4.8:1
- Blue (#2563EB) sobre White → 8.6:1

**⚠️ Atenção:**
- Gold sobre White → 3.2:1 (usar Gold-dark ou aumentar peso)

---

## Exportação para Outras Ferramentas

### PowerPoint
```
Navy Deep: RGB(21, 36, 50)
Gold: RGB(212, 175, 55)
Blue: RGB(37, 99, 235)
Green: RGB(5, 150, 105)
Red: RGB(185, 28, 28)
```

### Canva
Criar paleta customizada com HEX codes acima.

### Adobe (CMYK aproximado)
```
Navy Deep: C=100 M=77 Y=50 K=60
Gold: C=15 M=30 Y=80 K=10
```

---

## Variáveis CSS (Implementação)

### arquivo: `assets/css/colors.css`
```css
:root {
  /* Navy */
  --navy-deep: #152432;
  --navy-medium: #1E3A5F;
  --navy-soft: #2A3D51;
  
  /* Gold */
  --gold: #D4AF37;
  --gold-light: #f0c245;
  --gold-dark: #C99D2E;
  
  /* Blue */
  --blue: #2563EB;
  --blue-medium: #3B82F6;
  --blue-light: #60A5FA;
  
  /* Green */
  --green: #059669;
  --green-bg: #D1FAE5;
  
  /* Red */
  --red: #B91C1C;
  --red-bg: #FEE2E2;
  
  /* Neutrals */
  --bg: #F9F8F4;
  --text: #152432;
  --text-secondary: #6B7280;
  --border: #BeCDD8;
}
```

### Uso no CSS
```css
.slide-title {
  color: var(--gold);
  background: var(--navy-deep);
}

.highlight {
  border-left: 4px solid var(--gold);
}

.grade-high {
  color: var(--blue);
}
```

---

## Filosofia do Design

**Navy + Gold = Autoridade + Sofisticação**

MBE (Medicina Baseada em Evidências) não deve ser:
- Colorido demais (não é infantil)
- Cinza demais (não é entediante)

Equilíbrio: **Sério mas elegante**

---

## Testes de Impressão

### P&B (Grayscale)
- Navy → Cinza escuro (legível)
- Gold → Cinza médio (distinguível)
- Blue/Green/Red → Cinzas diferentes

### Projetor (Low contrast)
- Testar em projetor antigo
- Navy pode ficar muito escuro
- Usar Navy-medium em títulos se necessário

---

## Inspiração Visual

**Referências:**
- Financial Times (navy + salmon)
- The Economist (red + navy)
- Academic journals (sóbrio, limpo)

**NÃO inspirado em:**
- Startups tech (cores vibrantes)
- Infográficos jornalísticos (multicolorido)
- Material Design (muito Google)

---

**Versão:** 1.0  
**Última atualização:** 2025-01-10  
**Próxima revisão:** Após testes em apresentação real
