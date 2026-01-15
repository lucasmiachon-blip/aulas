# 🚀 PLANO MVP - CORE GRADE 2026

**Criado:** 2026-01-15 17:20 UTC  
**Objetivo:** 30 slides funcionando em 3-5 dias  
**Estratégia:** 95% Claude, 5% validação Lucas

---

## 📅 CRONOGRAMA MVP

### **DIA 1 (HOJE) - 6 slides**
⏰ **Meta:** Slides 14-19 (PREVENT + Estratificação)

**Sessão 1 (2h):**
- [ ] Slide 14: PREVENT vs PCE (comparação direta)
- [ ] Slide 15: QRISK3 características
- [ ] Slide 16: Qual calculadora usar quando?

**Sessão 2 (2h):**
- [ ] Slide 17: Risco baixo/intermediário/alto
- [ ] Slide 18: Fatores agravantes
- [ ] Slide 19: Reclassificação por CAC

**Entrega:** 19/40 slides (47.5%)

---

### **DIA 2 - 6 slides**
⏰ **Meta:** Slides 20-25 (Decisão + Metas LDL)

**Sessão 1 (2h):**
- [ ] Slide 20: Árvore de decisão completa
- [ ] Slide 21: Metas LDL (<70, <55, <40)
- [ ] Slide 22: Evidências metas agressivas

**Sessão 2 (2h):**
- [ ] Slide 23: IMPROVE-IT (ezetimibe)
- [ ] Slide 24: FOURIER (evolocumab)
- [ ] Slide 25: Quando intensificar?

**Entrega:** 25/40 slides (62.5%)

---

### **DIA 3 - 5 slides**
⏰ **Meta:** Slides 26-30 (Bempedoico completo)

**Sessão única (3h):**
- [ ] Slide 26: Ácido bempedoico - O que é?
- [ ] Slide 27: CLEAR Outcomes trial
- [ ] Slide 28: NNT vs estatina
- [ ] Slide 29: Papel em intolerância
- [ ] Slide 30: Algoritmo prático SUS

**Entrega:** 30/40 slides (75%) ✅ **MVP COMPLETO**

---

## 🎯 **MVP = 30 SLIDES (75%)**

**Conteúdo MVP cobre:**
- ✅ Introdução GRADE (1-5)
- ✅ Metodologia GRADE (6-9)
- ✅ CAC aplicado (10-13)
- ✅ Calculadoras de risco (14-16)
- ✅ Estratificação (17-20)
- ✅ Metas LDL (21-25)
- ✅ Bempedoico (26-30)

**Faltariam apenas:**
- ⏳ Casos clínicos (31-35)
- ⏳ Síntese final (36-40)

---

## 📋 DEPOIS DO MVP (Dias 4-30)

### **Fase 2: Refinamento (Dias 4-7)**
- Ajustes de design nos 30 slides
- Correções de conteúdo
- Testes de navegação
- Feedback inicial de colegas

### **Fase 3: Completar (Dias 8-14)**
- Slides 31-35 (Casos clínicos)
- Slides 36-40 (Síntese)
- Refinamento final

### **Fase 4: Polimento (Dias 15-30)**
- Refatorar CSS inline → classes
- Adicionar animações (se quiser)
- Otimizar performance
- Documentação final

---

## 🔧 WORKFLOW OTIMIZADO MVP

### **Para cada lote de 3 slides:**

**Claude faz (15 min):**
1. Cria HTML completo com CSS modular
2. Valida encoding UTF-8
3. Commit no GitHub
4. Documenta no changelog

**Lucas faz (5 min):**
1. Pull do GitHub
2. Abre no navegador
3. Valida visualmente
4. Se OK → próximo lote
5. Se problemas → lista ajustes

**Ciclo:** 20 min/lote = 9 slides/hora (teórico)  
**Real:** 6 slides/dia (sustentável com revisões)

---

## 📊 CONTEÚDO DETALHADO MVP

### **SLIDES 14-16: PREVENT vs PCE vs QRISK**

**Slide 14: PREVENT vs PCE**
```
Título: "Calculadoras de Risco: PREVENT vs PCE"

Content:
- PREVENT (2023): Inclui CKD, SDH, uACR
- PCE (2013): Idade, sexo, raça, lipídios, PA, DM, tabagismo
- Comparação: PREVENT mais preciso em CKD/DM
- Recomendação: PREVENT > PCE (AHA 2023)

Evidência: JAMA 2023;329(19):1674-83
```

**Slide 15: QRISK3**
```
Título: "QRISK3: Abordagem UK"

Content:
- Maior amostra (7.89M pacientes)
- Inclui: etnia, IMC, depressão, migrânea
- Validado: população UK
- Limitação: Não validado Brasil

Evidência: BMJ 2017;357:j2099
```

**Slide 16: Qual usar?**
```
Título: "Qual Calculadora Usar?"

Decisão:
1. Primeira linha: PREVENT (se disponível)
2. Alternativa: PCE (validado USA)
3. Não usar: Framingham (desatualizado)

Caveats:
- Todas subestimam em diabéticos
- CAC reclassifica 30-40%
- Decisão compartilhada sempre

Referência: Circulation 2023;148:1982-2001
```

### **SLIDES 17-19: ESTRATIFICAÇÃO**

**Slide 17: Definições**
```
Título: "Estratificação de Risco"

Risco Baixo: <5% em 10 anos
Risco Intermediário: 5-20% em 10 anos
Risco Alto: >20% em 10 anos

Decisões:
- Baixo: Estilo de vida
- Intermediário: CAC decisivo
- Alto: Estatina sempre

Evidência: Diretriz SBC 2025
```

**Slide 18: Fatores Agravantes**
```
Título: "Fatores que Elevam Risco"

Agravantes:
1. História familiar precoce (<55H, <65M)
2. LDL ≥160 mg/dL
3. CKD (TFG <60)
4. DM tipo 2 ≥10 anos
5. Tabagismo atual

Efeito: Reclassifica intermediário → alto

Referência: European Heart J 2021;42:3227
```

**Slide 19: CAC Reclassifica**
```
Título: "CAC Reclassifica 30-40%"

Dados MESA:
- CAC=0: Risco ↓50%
- CAC 1-99: Mantém risco
- CAC ≥100: Risco ↑2-3x
- CAC ≥400: Risco ↑5-7x

NNT muda:
- Sem CAC: NNT=100
- CAC >100: NNT=35

Evidência: JACC 2018;72:434-47
```

### **SLIDES 20-25: METAS LDL**

**Slide 20: Árvore Decisão**
```
Título: "Decisão Estruturada"

Fluxo:
1. Calcular risco (PREVENT)
2. Se intermediário → CAC
3. Estratificar: baixo/intermediário/alto
4. Definir meta LDL
5. Iniciar terapia
6. Monitorar + ajustar

Tool: Algoritmo visual com setas
```

**Slide 21: Metas LDL**
```
Título: "Metas LDL por Risco"

Risco Baixo: <130 mg/dL (sem estatina se <100)
Risco Intermediário: <100 mg/dL
Risco Alto: <70 mg/dL
Muito Alto: <55 mg/dL
Extremo: <40 mg/dL (opcional)

Evidência: ESC/EAS 2019
```

**Slide 22-25:** (Continua com trials...)

---

## 🎨 PADRÕES VISUAIS MVP

**Todos os slides MVP seguem:**
- Grid 2-3 colunas
- Cards brancos + navy
- Máximo 3 bullets por seção
- Referência completa rodapé
- Classes CSS modulares (zero inline)

**Typography:**
- H2: 3.2vw Georgia
- Body: 1.1vw Lato
- Labels: 0.9vw uppercase

**Colors:**
- Navy #0B1320 (headers)
- Gold #DDB944 (destaques)
- Teal #1F766E (dados)
- White #FFFFFF (cards)

---

## ⚡ COMANDO PARA INICIAR

**Lucas diz:**
```
"Claude, inicia MVP. Cria lote 1: Slides 14-16 (PREVENT).
CSS modular, UTF-8, commit GitHub. Vai!"
```

**Claude executa:**
1. Cria 3 slides HTML completos
2. Valida encoding
3. Commit no GitHub
4. Avisa "Lote 1 pronto, valida!"

**Lucas valida (2 min):**
- Abre GitHub Pages
- Confere visual
- Se OK: "Lote 2!"
- Se erro: "Ajusta X"

---

## 📝 TRACKING PROGRESS

### Checklist MVP:
```
[x] Slides 1-13 (base pronta)
[ ] Slides 14-16 (PREVENT) - DIA 1
[ ] Slides 17-19 (Estratificação) - DIA 1
[ ] Slides 20-22 (Decisão + Metas) - DIA 2
[ ] Slides 23-25 (Trials LDL) - DIA 2
[ ] Slides 26-30 (Bempedoico) - DIA 3

✅ MVP = 30/40 (75%)
```

---

## 🔥 REGRAS DO MVP

1. **Velocidade > Perfeição**
   - Conteúdo correto > Design impecável
   - Encoding UTF-8 > Refatoração CSS
   - Funcionando > Otimizado

2. **Validação mínima**
   - Abre no navegador
   - Lê o conteúdo
   - Se entendível → OK
   - Ajustes depois

3. **Zero bloqueio**
   - Não travar em detalhes
   - Não refatorar agora
   - Não otimizar antes de terminar

4. **Commit frequente**
   - Cada lote = 1 commit
   - Sempre pusha no GitHub
   - Histórico completo

---

## 🎯 SUCESSO DO MVP

**MVP é sucesso se:**
- ✅ 30 slides funcionando
- ✅ Conteúdo tier-1 correto
- ✅ Navegação fluida
- ✅ UTF-8 sem corrupção
- ✅ Apresentável para colegas

**Não precisa:**
- ❌ CSS 100% modular
- ❌ Animações fancy
- ❌ Performance otimizada
- ❌ Documentação completa

---

**APÓS MVP:** Refinamento com calma nos 20+ dias restantes.

**AGORA:** EXECUTAR! 🚀
