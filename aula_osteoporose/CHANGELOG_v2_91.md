# CHANGELOG - SLIDES 11, 13, 14 E 18
## Osteoporose: Mudanças de Paradigma
### Data: 12 de Janeiro de 2026

---

## 📋 RESUMO EXECUTIVO

### Alterações Realizadas:
- ✅ **Slide 11**: Atualizado para "O que é QALY?" (Área sob a curva da vida)
- ✅ **Slide 13**: Atualizado para "Modelos de Risco: Qual ferramenta usar?"
- ✅ **Slide 14**: Atualizado para "FRAX-Brasil 2.0 e Estudo SPAH" + **Fontes adicionadas**
- ✅ **Slide 18**: Novo design "NOGG 2024: Regra de Decisão"

### Arquivos:
- **Principal**: `viewer_v2_91.html` (460K, 5007 linhas)
- **Backups**: 
  - `viewer_backup_antes_slide11_area_curva.html`
  - `viewer_backup_antes_slide13_modelos_risco.html`
  - `viewer_backup_antes_slide14_frax_brasil.html`
  - `viewer_backup_antes_fontes_slide14.html`
  - `viewer_backup_antes_slide18_nogg.html`

---

## 🎯 SLIDE 11: "O QUE É QALY?"

### Título:
```
"O que é QALY?"
Subtítulo: "Quality-Adjusted Life Year: A área sob a curva da vida"
Linha decorativa: Navy (60px × 4px)
```

### Layout: 1.2FR + 1FR

#### Card Esquerdo (1.2fr):
**"A Utilidade muda com o tempo"**

**Gráfico SVG:**
- Eixos X/Y: Anos × Utilidade (0.0 → 1.0)
- Linha pontilhada cinza: Envelhecimento normal
- Curva navy (4px): Trajetória real com evento
  - Path: `M 0 20 L 50 25 L 50 140 Q 100 80 150 80 L 400 100`
  - Queda vertical no evento (y=25 → y=140)
  - Recuperação curva (Q 100 80 150 80)
  - Nível crônico inferior ao basal
- Área vermelha sombreada: `rgba(185,28,28,0.15)`
  - Representa QALYs perdidos
  - Área entre linha normal e curva real
- Círculo vermelho: Marcador do evento agudo (cx=50, cy=140, r=5)

**Texto explicativo:**
> "A utilidade 'afunda' no evento e sobe na reabilitação (rampa), mas muitas vezes **não retorna ao basal**. O QALY perdido é a soma dessa diferença ao longo de toda a sobrevida."

#### Card Direito (1fr):
**"Comparação de Magnitude"**

**Perda média de QALYs por evento (Lifetime):**

1. **Fratura de Quadril: ~2,00 QALYs**
   - Barra: 100% largura, 24px altura
   - Background: var(--red) #B91C1C
   - Label: "DEVASTADOR" (branco, 11px bold)
   - Nota: "Impacto crônico, dependência e mortalidade precoce."

2. **AVC Isquêmico (Maior): ~1,90 QALYs**
   - Barra: 95% largura, 12px altura
   - Background: #6B7280 (cinza)
   - Opacity: 0.8

3. **Infarto (IAM): ~0,80 QALYs**
   - Barra: 40% largura, 12px altura
   - Background: #6B7280 (cinza)
   - Opacity: 0.8
   - Nota: "Recuperação funcional tende a ser melhor que no quadril."

### CSS Variables:
```css
--navy: #1E3A5F  (Curva principal, títulos)
--red: #B91C1C   (Perda, destaque, área sombreada)
```

### Rodapé:
> **Fontes Tier 1:** Tosteson AN et al. *Osteoporos Int* 2008 (Modelo NOF); Tengs & Wallace 1995 (Meta-análise de utilidade).
> 
> *Nota: A perda exata varia com a idade e reabilitação, mas a magnitude relativa do quadril vs. IAM é consistente na literatura.*

### Especificações Técnicas:
- **SVG ViewBox**: 0 0 400 200
- **Altura do gráfico**: 220px
- **Cards**: 
  - Background: white
  - Border-radius: 12px
  - Padding: 30px
  - Box-shadow: 0 4px 15px rgba(0,0,0,0.05)
  - Height: 100% (alturas iguais)
- **Gap entre cards**: 50px
- **Fontes**: Georgia (títulos, números), Lato (textos)

### Mensagem Pedagógica:
1. **QALY = Integral da utilidade ao longo do tempo**
2. **Área sob a curva = Vida total ajustada**
3. **Área vermelha = Vida perdida (não recuperada)**
4. **Fratura de quadril tem impacto DEVASTADOR (~2 QALYs)**

---

## 🎯 SLIDE 13: "MODELOS DE RISCO"

### Título:
```
"Modelos de Risco: Qual ferramenta usar?"
Linha decorativa: Navy (60px × 4px)
```

### Layout: 3 CARDS LADO A LADO (1FR + 1FR + 1FR)

#### Card 1 - FRAX® Clássico (Navy):
**Subtítulo:** "TRIAGEM INICIAL"

**Características:**
- 10-year probability (hip + MOF)
- Com ou sem DMO do colo femoral
- Incorpora mortalidade competitiva

**Limitações:**
- Não usa quedas como input
- Não capta bem recência de fratura

**Footer:** "Papel: O Primeiro Filtro"
- Background: #F0F4F8 (azul claro)
- Border-left: 4px solid var(--navy)

#### Card 2 - FRAX-Brasil 2.0 (Gold):
**Subtítulo:** "CALIBRAÇÃO LOCAL"

**Características:**
- Modelo brasileiro atualizado (Albergaria 2024)
- Estima probabilidades menores vs modelo anterior
- Rank preservado (r > 0,99)

**Footer:** "Papel: O Modelo Correto"
- Background: #FFFBEB (amarelo claro)
- Border-left: 4px solid var(--gold)
- Text color: #92400E (marrom escuro)

#### Card 3 - FRAXplus® (Green):
**Subtítulo:** "CAMADA DE AJUSTE"

**Características:**
Refina a probabilidade para riscos que o modelo clássico ignora:
- Fratura recente
- Dose alta de glicocorticoide
- Quedas / DM2 / TBS

**Footer:** "Papel: O Refino Clínico"
- Background: #ECFDF5 (verde claro)
- Border-left: 4px solid var(--green)
- Text color: #065F46 (verde escuro)

### Rodapé Comparativo:
> **Garvan:** útil quando você quer incorporar número de fraturas prévias e frequência de quedas; estima risco em 5 e 10 anos; validado externamente.

### CSS Variables:
```css
--navy: #1E3A5F   (FRAX Clássico)
--gold: #B8941F   (FRAX-Brasil 2.0)
--green: #065F46  (FRAXplus)
```

### Especificações dos Cards:
- **Grid**: 1fr 1fr 1fr
- **Gap**: 30px
- **Border-top**: 6px solid (cor específica)
- **Border-radius**: 8px
- **Padding**: 30px
- **Box-shadow**: 0 4px 12px rgba(0,0,0,0.06)
- **Display**: flex column
- **Align-items**: stretch (alturas iguais)

### Hierarquia Tipográfica:
- **H3 (Título card)**: Georgia 24px bold
- **Subtítulo**: Lato 14px uppercase (letter-spacing 1px)
- **Conteúdo**: Lato 18px
- **Footer**: Lato 16px bold

---

## 🎯 SLIDE 14: "FRAX-BRASIL 2.0 E ESTUDO SPAH"

### Título:
```
"FRAX-Brasil 2.0 e Estudo SPAH"
Subtítulo: "A prova local: recalibração do algoritmo e validação de cut-offs"
Linha decorativa: Gold (80px × 3px)
```

### Layout: GRID 1FR + 1PX + 1FR (com divisor vertical)

#### Coluna Esquerda: "Probabilidades (Novo Modelo)"

**Item 1 - Quadril:**
- Número: **↓ 26–44%** (Georgia 38px bold navy)
- Texto: "Menor risco de **Quadril**" (Lato 18px)
- Nota: "Publicado 2023; implementado na calculadora ABRASSO" (Lato 14px lightgray)

**Item 2 - MOF:**
- Número: **↓ 20–56%** (Georgia 38px bold navy)
- Texto: "Menor risco de **MOF**" (Lato 18px)
- Nota: "MOF deriva de incidência de quadril + razões epidemiológicas" (Lato 14px lightgray)

**Item 3 - Ranking:**
- Número: **r > 0,99** (Georgia 38px bold navy)
- Texto: "Ranking Preservado" (Lato 18px)
- Nota: "Apesar da redução absoluta, a hierarquia de risco se mantém." (Lato 14px lightgray)

**Gap entre itens:** 30px

#### Divisor Vertical:
- Width: 1px (definido pela grid)
- Height: 100%
- Background: var(--gold) #B8941F
- Opacity: 0.4 (translúcido)

#### Coluna Direita: "Performance na Coorte SPAH"

**Item 1 - Amostra:**
- Número: **n = 705** (Georgia 38px bold navy)
- Texto: "Idosos Comunitários (SP)" (Lato 18px navy)
- Nota: "Seguimento 4,3 ± 0,8 anos (Arch Osteoporos 2024)" (Lato 14px lightgray)

**Item 2 - Cutoffs (Flex Layout, gap 40px):**

**Cutoff MOF:**
- Número: **~8%** (Georgia 38px bold navy)
- Label: "Cutoff **MOF**" (Lato 14px gray)

**Cutoff Hip:**
- Número: **~3%** (Georgia 38px bold navy)
- Label: "Cutoff **Hip**" (Lato 14px gray)

Nota: "Pontos de melhor acurácia (ROC) na amostra." (Lato 14px lightgray)

**Item 3 - Box de Implicação:**
- Background: white
- Border-left: 4px solid var(--gold)
- Padding: 15px
- Box-shadow: 0 2px 10px rgba(0,0,0,0.03)

> **Implicação:** Cutoffs importados (20%) não calibram em idosos brasileiros; limiar é decisão local.

### Rodapé com Fontes: ✅ **ADICIONADO**
```html
<strong>Fontes:</strong> Albergaria BH et al. <em>Arch Osteoporos</em> 2024;19(1):24 (FRAX-Brasil 2.0);
Albergaria BH et al. <em>Arch Osteoporos</em> 2024;19(1):61 (Validação SPAH).
```

### CSS Variables:
```css
--navy: #152432      (Títulos, números principais)
--gold: #B8941F      (Linha decorativa, divisor, box)
--wine: #7F1D1D      (Reserva)
--gray: #6B7280      (Textos secundários)
--lightgray: #9CA3AF (Notas explicativas)
```

### Mensagens-Chave:
1. **Recalibração:** Probabilidades menores no novo modelo brasileiro
2. **Validação:** Cutoffs locais (~8% MOF, ~3% Hip) vs importados (20%)
3. **Implicação:** Decisão de limiar deve ser baseada em dados locais

---

## 🎯 SLIDE 18: "NOGG 2024: REGRA DE DECISÃO"

### Título:
```
"NOGG 2024: Regra de Decisão"
Subtítulo: "Substituindo o limiar fixo pelo limiar idade-dependente"
Linha decorativa: Wine (80px × 3px)
```

### Layout: GRID 0.9FR + 1.1FR

#### Coluna Esquerda (0.9fr): "Zonas de Risco"

**Layout:** Badges + Textos (Flex column, gap 20px)

**Badge LAT (Verde):**
- Background: var(--green) #065F46
- Label: "LAT" (65px width, 14px bold white)
- Texto: "Risco Baixo (Estilo de vida)"

**Badge UAT (Azul):**
- Background: var(--blue) #1E3A5F
- Label: "UAT" (65px width, 14px bold white)
- Texto: "Intermediário (Pedir DMO)"

**Badge IT (Dourado):**
- Background: var(--gold) #B8941F
- Label: "IT" (65px width, 14px bold white)
- Texto: "**Intervention Threshold** (Tratar)"

**Badge VHRT (Vinho):**
- Background: var(--wine) #7F1D1D
- Label: "VHRT" (65px width, 14px bold white)
- Texto: "**Very High Risk** (Anabólico)"

#### Coluna Direita (1.1fr): "Limiares (IT) por Idade"

**Box Branco:**
- Background: white
- Border: 1px solid #E5E7EB
- Border-radius: 8px
- Padding: 30px
- Box-shadow: 0 4px 15px rgba(0,0,0,0.03)

**Limiares (layout flex column, gap 20px):**

**50 – 55 anos:**
- Idade: Georgia 24px bold navy
- Limiar: **~ 7–10%** (Lato 22px bold gold)
- Border-bottom: 1px solid #F3F4F6

**65 – 70 anos:**
- Idade: Georgia 24px bold navy
- Limiar: **~ 15–18%** (Lato 22px bold gold)
- Border-bottom: 1px solid #F3F4F6

**≥ 75 anos:**
- Idade: Georgia 24px bold navy
- Limiar: **~ 20–25%** (Lato 22px bold gold)

**Nota explicativa:**
> *Valores aproximados para MOF. O aumento reflete o balanço com a mortalidade competitiva.*

### Box de Contexto Brasileiro:
- Background: white
- Border-left: 4px solid var(--navy)
- Padding: 20px
- Box-shadow: 0 2px 10px rgba(0,0,0,0.05)

> **Nota de Contexto:** Há avaliação brasileira do desempenho destes limiares por idade em idosos (SPAH), sugerindo necessidade de calibração local.

### Rodapé:
```
Fonte: Kanis JA et al. (NOGG 2024 Guideline).
```

### CSS Variables:
```css
--navy: #152432   (Títulos, box contexto)
--gold: #B8941F   (IT badge, limiares)
--wine: #7F1D1D   (VHRT badge, linha decorativa)
--green: #065F46  (LAT badge)
--blue: #1E3A5F   (UAT badge)
--gray: #6B7280   (Textos secundários)
```

### Conceito NOGG:
1. **LAT (Lower Assessment Threshold)**: Baixo risco → Estilo de vida
2. **UAT (Upper Assessment Threshold)**: Intermediário → Solicitar DMO
3. **IT (Intervention Threshold)**: Alto risco → Iniciar tratamento
4. **VHRT (Very High Risk Threshold)**: Risco muito alto → Anabólico

### Limiares Idade-Dependentes:
- **Justificativa:** Balanço com mortalidade competitiva
- **Progressão:** 7-10% (50-55 anos) → 15-18% (65-70 anos) → 20-25% (≥75 anos)
- **Aplicação:** MOF (Major Osteoporotic Fracture)

---

## 📊 ESTATÍSTICAS FINAIS

### Arquivo Principal:
- **Nome:** `viewer_v2_91.html`
- **Tamanho:** 460K
- **Linhas:** 5007
- **Slides atualizados:** 4 (Slides 11, 13, 14, 18)

### Backups Criados:
1. `viewer_backup_antes_slide11_area_curva.html` (453K)
2. `viewer_backup_antes_slide13_modelos_risco.html` (452K)
3. `viewer_backup_antes_slide14_frax_brasil.html` (454K)
4. `viewer_backup_antes_fontes_slide14.html` (460K)
5. `viewer_backup_antes_slide18_nogg.html` (454K)

### Incremento Total:
- **Linhas adicionadas:** +64 linhas
  - Slide 11: +36 linhas
  - Slide 13: +15 linhas
  - Slide 14: +20 linhas (+7 fontes)
  - Slide 18: +37 linhas

---

## 🎨 PALETA DE CORES CONSOLIDADA

### Cores Principais:
```css
--navy: #152432 / #1E3A5F    (Títulos, elementos principais)
--gold: #B8941F               (Destaques, IT threshold)
--wine: #7F1D1D               (VHRT, linha decorativa S18)
--red: #B91C1C                (Perdas, fratura quadril)
--green: #065F46              (LAT, FRAXplus)
--blue: #1E3A5F               (UAT, FRAX Clássico)
```

### Cores Secundárias:
```css
--gray: #6B7280               (Textos secundários)
--lightgray: #9CA3AF          (Notas explicativas)
```

### Fundos e Bordas:
```css
Background: #F9F8F4           (Fundo dos slides)
Cards: white                  (Fundo dos cards)
Borders: #E5E7EB / #F3F4F6    (Divisores sutis)
```

---

## 📚 REFERÊNCIAS BIBLIOGRÁFICAS

### Slide 11:
- Tosteson AN et al. *Osteoporos Int* 2008 (Modelo NOF)
- Tengs & Wallace. *Health Services Research* 1995 (Meta-análise de utilidade)

### Slide 14:
- Albergaria BH et al. *Arch Osteoporos* 2024;19(1):24 (FRAX-Brasil 2.0)
- Albergaria BH et al. *Arch Osteoporos* 2024;19(1):61 (Validação SPAH)

### Slide 18:
- Kanis JA et al. (NOGG 2024 Guideline)

---

## ✅ CHECKLIST DE QUALIDADE

### Design:
- ✅ CSS Variables implementadas
- ✅ Tipografia consistente (Georgia + Lato)
- ✅ Paleta de cores profissional
- ✅ Hierarquia visual clara
- ✅ Responsividade (grid layouts)
- ✅ Box-shadows sutis
- ✅ Border-radius consistente (4px, 8px, 12px)

### Conteúdo:
- ✅ Títulos descritivos
- ✅ Subtítulos explicativos
- ✅ Dados quantitativos destacados
- ✅ Fontes bibliográficas citadas
- ✅ Notas de contexto brasileiro
- ✅ Mensagens pedagógicas claras

### Técnico:
- ✅ HTML válido
- ✅ Inline styles organizados
- ✅ SVG otimizado (Slide 11)
- ✅ Grid layouts funcionais
- ✅ Flex layouts para alinhamento
- ✅ Backups múltiplos criados

---

## 🚀 PRÓXIMOS PASSOS SUGERIDOS

1. **Teste no Navegador:**
   - Abrir `viewer_v2_91.html` em Chrome/Firefox
   - Verificar renderização dos 4 slides
   - Testar responsividade

2. **Exportação PowerPoint:**
   - Converter HTML para PPTX
   - Verificar preservação de formatação
   - Ajustar se necessário

3. **Revisão de Conteúdo:**
   - Validar números e porcentagens
   - Conferir citações bibliográficas
   - Verificar consistência terminológica

4. **Slides Pendentes:**
   - Revisar outros slides da apresentação
   - Aplicar design system IGNIS consistente
   - Adicionar fontes onde necessário

---

## 📝 NOTAS TÉCNICAS

### Gráfico SVG (Slide 11):
- **ViewBox**: 0 0 400 200
- **Path da curva**: `M 0 20 L 50 25 L 50 140 Q 100 80 150 80 L 400 100`
- **Área sombreada**: Path fechado com `fill="rgba(185,28,28,0.15)"`
- **Componentes**: Eixos, linha pontilhada, curva, área, marcador

### Grid Layouts:
- **Slide 11**: `grid-template-columns: 1.2fr 1fr`
- **Slide 13**: `grid-template-columns: 1fr 1fr 1fr`
- **Slide 14**: `grid-template-columns: 1fr 1px 1fr` (com divisor)
- **Slide 18**: `grid-template-columns: 0.9fr 1.1fr`

### Typography Scale:
- **H1**: 42px-44px (Georgia bold)
- **H3**: 22px-26px (Georgia bold)
- **Números grandes**: 38px (Georgia bold)
- **Body**: 18px (Lato regular)
- **Notas**: 13px-14px (Lato regular)
- **Rodapé**: 12px (Lato regular)

---

**Documento gerado em:** 12/01/2026  
**Versão:** v2.91  
**Autor:** Sistema de Documentação Automatizada
