# 🔥 ESTADO ATUAL DO PROJETO - SESSÃO 2026-01-15

**ÚLTIMA ATUALIZAÇÃO:** 2026-01-15 17:15 UTC  
**STATUS:** URGENTE - Prazo de 1 dia  
**PROGRESSO:** 13/40 slides (32.5%)

---

## 📊 SITUAÇÃO CRÍTICA

### ⏰ PRAZO REAL:
- **Total:** ~30 dias (até meados de fevereiro)
- **MVP:** 3-5 dias (mínimo 30 slides funcionando = 75%)
- **Últimos 2 dias:** Setup/aprendizado (encoding, Git, CSS modular)
- **AGORA:** MODO PRODUÇÃO - Claude faz, Lucas valida

### 🎯 META MVP (URGENTE):
- **Slides 14-30** (17 slides) = MVP completo
- **Prazo MVP:** 3 dias
- **Velocidade necessária:** 6 slides/dia
- **Estratégia:** Claude cria lotes de 3-5 slides, Lucas valida rápido

### ✅ O QUE ESTÁ PRONTO:
1. **Slides 1-13** funcionando (encoding UTF-8 correto)
2. **CSS modular completo** (base.css - 543 linhas, 14 seções)
3. **Estrutura de pastas** organizada (css/, js/)
4. **GitHub configurado** com token ativo
5. **Branch limpo** (refactor/v2.0.0 - batch 3 revertido)

### ❌ O QUE FALTA:
- **Slides 14-40** (27 slides)
- Conteúdo baseado em:
  - 3 imagens enviadas (CAC, Motor GRADE, CAC=0)
  - PDFs BMJ na pasta (8 arquivos)
  - Protocolo GRADE tier-1

---

## 🔐 CREDENCIAIS GITHUB

**Token:** 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  
**Repo:** https://github.com/lucasmiachon-blip/aulas  
**Branch:** refactor/v2.0.0  
**Path:** aula_grade/viewer_v2_0_0/

**Commit automático:** Claude tem acesso via API

---

## 📁 ESTRUTURA DO PROJETO

```
viewer_v2_0_0/
├── index.html              (1.466 linhas, 528 inline styles)
├── css/
│   ├── base.css           (543 linhas - MODULAR COMPLETO)
│   └── responsive-fix.css (23 linhas)
├── js/
│   └── navigation.js      (44 linhas)
├── README.md
├── GITHUB_CREDENTIALS.md  (no .gitignore)
└── bmj2024*.pdf (8 arquivos)
```

---

## 🎨 DESIGN SYSTEM (NÃO MUDAR!)

### Paleta Turner Premium:
```css
--navy: #0B1320    /* Fundo escuro */
--gold: #DDB944    /* Destaques */
--bg: #F9F8F4      /* Fundo claro */
--teal: #1F766E    /* Científico */
```

### Tipografia:
- **Títulos:** Georgia serif
- **Corpo:** Lato sans-serif

### Filosofia:
- "Paper premium minimalista"
- Sem emojis coloridos
- Símbolos tipográficos (§, ›, —)

---

## 📋 PROTOCOLO TIER-1 (OBRIGATÓRIO)

### Cada slide DEVE ter:
1. **1 definição clara** (máx 2 sentenças)
2. **1-3 regras de decisão** (práticas)
3. **Máximo 3 bullet points** (evitar sobrecarga cognitiva)
4. **Evidência GRADE explícita** (nível de certeza)
5. **Referência completa:** Autor, Journal, Ano, DOI
6. **Números exatos + IC 95%** quando aplicável

### Journals aceitos:
- NEJM, JACC, Circulation, BMJ, Lancet
- European Heart Journal
- ESC/AHA/ACC guidelines

### NÃO aceitar:
- Blogs, sites genéricos
- Opiniões sem dados
- Guidelines não tier-1

---

## 🔧 ENCODING (REGRA SAGRADA)

**SEMPRE UTF-8 com CRLF**

### Símbolos corretos:
```html
É → &Eacute;
Ç → &Ccedil;
Ã → &Atilde;
— → &mdash;
≠ → &ne;
≥ → &ge;
```

**NUNCA:** Raw UTF-8 characters (podem corromper)

---

## 📊 SLIDES EXISTENTES (1-13)

1. **CAPA** - "CORE GRADE - A Coragem na Incerteza"
2. **NAVEGAR É PRECISO** - Fernando Pessoa + stats ESC/ACC
3. **CAC SOB LENTE GRADE** - Comparação SBC/ESC/ACC
4. **CALIBRAGEM** - QR codes interativos
5. **O GRANDE DIVISOR** - Por onde começar vs Como interpretar
6. **O MOTOR DO GRADE** - Metodologia Guyatt
7A. **INDIRECTNESS** - PICO framework
7B. **DOSE-RESPONSE GRADIENT** - Upgrade factors
9. **CAC APLICAÇÃO GRADE** - Análise estruturada
10. **CAC = 0 PROGNÓSTICO** - Warranty period
11. **CAC MODIFICA NNT** - Estatinas por CAC
12. **ASPIRINA POR CAC** - NNT vs NNH
13. **PARADOXO CAC ZERO** - Low-attenuation plaque

---

## 📝 CONTEÚDO DOS PRÓXIMOS SLIDES (14-40)

### **BLOCO 3: PREVENT vs PCE vs QRISK** (Slides 14-16)
- Slide 14: Comparação PREVENT vs PCE
- Slide 15: QRISK3 vs Framingham
- Slide 16: Qual calculadora usar quando?

### **BLOCO 4: ESTRATIFICAÇÃO DE RISCO** (Slides 17-20)
- Slide 17: Risco baixo/intermediário/alto (definições)
- Slide 18: Fatores agravantes
- Slide 19: Reclassificação por CAC
- Slide 20: Árvore de decisão completa

### **BLOCO 5: METAS DE LDL** (Slides 21-25)
- Slide 21: LDL <70 vs <55 vs <40
- Slide 22: Evidências para metas agressivas
- Slide 23: IMPROVE-IT (ezetimibe)
- Slide 24: Evolocumab (FOURIER)
- Slide 25: Quando intensificar?

### **BLOCO 6: ÁCIDO BEMPEDOICO** (Slides 26-30)
- Slide 26: O que é? Mecanismo
- Slide 27: CLEAR Outcomes (trial)
- Slide 28: NNT vs estatina
- Slide 29: Papel em intolerância
- Slide 30: Algoritmo prático

### **BLOCO 7: CASOS CLÍNICOS** (Slides 31-35)
- Slide 31: Caso 1 - Risco intermediário + CAC=0
- Slide 32: Caso 2 - CAC alto + sintomas
- Slide 33: Caso 3 - Intolerância estatina
- Slide 34: Caso 4 - LDL refratário
- Slide 35: Caso 5 - Prevenção primária jovem

### **BLOCO 8: SÍNTESE** (Slides 36-40)
- Slide 36: Fluxograma completo
- Slide 37: Erros comuns
- Slide 38: Checklist GRADE
- Slide 39: Referências tier-1
- Slide 40: Encerramento + QR feedback

---

## 🚀 WORKFLOW PARA PRÓXIMA SESSÃO

### **Comando para Claude:**
```
"Continua do Slide 14. Cria lote de 3 slides (14-16) sobre PREVENT.
Use CSS modular, encoding UTF-8, commit direto no GitHub."
```

### **Checklist por lote:**
1. ☐ Criar HTML com classes CSS (zero inline)
2. ☐ Validar encoding UTF-8
3. ☐ Verificar referências tier-1
4. ☐ Commit no GitHub via API
5. ☐ Documentar no changelog

### **Velocidade esperada:**
- 3 slides = 15-20 minutos
- 9 slides/hora (ritmo sustentável)
- 27 slides = ~3 horas de trabalho puro

---

## ⚠️ PROBLEMAS CONHECIDOS

### 1. **Encoding pode quebrar se:**
- Usar Python sem `encoding='utf-8'`
- Copiar/colar de fontes externas
- Editar sem BOM handling

**Solução:** Sempre usar `str_replace` do Claude

### 2. **CSS inline ainda domina:**
- 528 inline styles no HTML atual
- Aceitar por enquanto (refatorar depois)
- Novos slides: apenas classes CSS

### 3. **GitHub API tem limites:**
- Arquivo muito grande = erro "File name too long"
- Solução: Usar arquivo temporário JSON

---

## 🔑 COMANDOS ÚTEIS

### Ver último commit:
```bash
curl -s -H "Authorization: token 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" \
  "https://api.github.com/repos/lucasmiachon-blip/aulas/commits?sha=refactor/v2.0.0&per_page=1"
```

### Reverter commit (se necessário):
```bash
curl -X PATCH \
  -H "Authorization: token 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" \
  -d '{"sha": "COMMIT_SHA_BOM", "force": true}' \
  "https://api.github.com/repos/lucasmiachon-blip/aulas/git/refs/heads/refactor/v2.0.0"
```

---

## 📚 DOCUMENTOS ESSENCIAIS

1. **README.md** - Overview do projeto
2. **GITHUB_CREDENTIALS.md** - Token e acesso
3. **INICIO_RAPIDO.md** - Comandos rápidos
4. **PLANO_APRENDIZADO_REPETICAO.md** - Metodologia Lucas
5. **PROTOCOLO_SLIDES_PREMIUM.md** - Padrões de qualidade
6. **ESTE ARQUIVO** - Estado atual

---

## 💪 FILOSOFIA DO LUCAS

**"É no atrito que se cresce"**

- Aprender fazendo
- Repetição intencional
- Documentar decisões
- Commits semânticos
- Zero inline CSS (meta futura)

---

## 🎯 META IMEDIATA

**HOJE (próximas 3-4 horas):**
- [ ] Slides 14-16 (PREVENT)
- [ ] Slides 17-20 (Estratificação)
- [ ] Slides 21-25 (Metas LDL)

**AMANHÃ:**
- [ ] Slides 26-30 (Bempedoico)
- [ ] Slides 31-35 (Casos clínicos)
- [ ] Slides 36-40 (Síntese)

**Total:** 27 slides em 2 sessões intensas

---

**SE ESTA SESSÃO CAIR:**
1. Abrir este arquivo
2. Verificar último commit no GitHub
3. Dizer ao Claude: "Continua do Slide X, usa ESTADO_ATUAL.md"
4. Claude retoma do ponto exato

**NÃO PERDER TEMPO! EXECUTAR AGORA! 🚀**
