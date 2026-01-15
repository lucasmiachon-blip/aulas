# 🚨 ESTADO CRÍTICO DO PROJETO - SESSÃO 2026-01-15

**URGÊNCIA:** Prazo de 1 dia | Modo híbrido com prioridade Claude

---

## 📊 SITUAÇÃO ATUAL

### ✅ O QUE ESTÁ PRONTO:
- **13 slides** completos (SLIDES 1-13)
- **CSS modular** completo (543 linhas, 14 seções)
- **Encoding UTF-8** corrigido e funcionando (CRLF)
- **GitHub** configurado e funcionando
- **Credenciais** salvas (GITHUB_CREDENTIALS.md)
- **Branch:** refactor/v2.0.0 (estado limpo, batch 3 revertido)

### ⏰ O QUE FALTA:
- **27 slides** (Slides 14-40)
- **Prazo:** 1 dia
- **Velocidade necessária:** 5-7 slides/hora

---

## 🎯 PRIORIDADES ABSOLUTAS

### **1. SLIDES 14-16 (IMEDIATO)**
Conteúdo já fornecido pelo usuário em 3 imagens:
- **Slide 14:** CAC para decidir sob incerteza (GRADE framework)
- **Slide 15:** O Motor do GRADE (metodologia)
- **Slide 16:** CAC = 0 (warranty period)

### **2. SLIDES 17-40 (PRÓXIMOS)**
Tópicos pendentes:
- PREVENT vs PCE (calculadoras)
- Risk stratification
- Aggressive LDL targets
- Bempedoic acid
- Outros 20 slides conforme diretriz SBC 2025

---

## 🔑 CREDENCIAIS GITHUB

**Token:** `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`  
**Repo:** https://github.com/lucasmiachon-blip/aulas  
**Branch:** refactor/v2.0.0  
**Path:** aula_grade/viewer_v2_0_0/

**Último commit:** 3932909d9ee (16:02 UTC - antes batch 3)

---

## 📐 PADRÕES ESTABELECIDOS

### **Design System (base.css):**
```css
--navy: #0B1320    /* Fundo escuro */
--gold: #DDB944    /* Destaques */
--bg: #F9F8F4      /* Fundo claro */
--teal: #1F766E    /* Científico */
```

### **Estrutura de cada slide:**
```html
<section class="slide">
    <div class="header">
        <p class="label-gold">CATEGORIA</p>
        <h2>Título do Slide</h2>
    </div>
    
    <div class="grid-3cols-asymmetric">
        <!-- conteúdo -->
    </div>
    
    <div class="reference">
        Autor et al. Journal 2024;vol(issue):pages
    </div>
</section>
```

### **Regras de ouro:**
1. ✅ SEMPRE UTF-8 com CRLF
2. ✅ ZERO inline styles (usar classes CSS)
3. ✅ Máximo 3 bullet points por card
4. ✅ Evidência tier-1 (NEJM, JACC, Circulation)
5. ✅ Entidades HTML (&eacute;, &aacute;, etc)
6. ✅ Símbolos premium (§, ›, —) não emojis

---

## 🚀 WORKFLOW RÁPIDO

### **Criar slides (Claude):**
1. Ler conteúdo/imagens
2. Criar HTML com classes CSS
3. Validar encoding UTF-8
4. Commitar via GitHub API
5. Informar URL do commit

### **Validar (Lucas):**
1. Abrir GitHub Pages
2. Ver slides no navegador
3. Dar feedback rápido ("OK" ou "ajustar X")

### **Iterar:**
- Se OK → Próximo lote (3-5 slides)
- Se ajuste → Claude corrige e recommita

---

## 📋 COMANDOS PARA PRÓXIMA SESSÃO

### **Iniciar trabalho:**
```
"Claude, continuar projeto GRADE. Criar slides 14-16."
```

### **Comandos rápidos:**
```
"PRÓXIMO LOTE" → Cria próximos 3-5 slides
"AJUSTAR SLIDE X" → Corrige slide específico
"COMMITAR TUDO" → Push para GitHub
"VER ESTADO" → Mostra progresso (X/40 slides)
```

---

## 🎓 PROTOCOLO GRADE (referência rápida)

### **Níveis de certeza:**
- ⊙⊙⊙⊙ ALTA (RCT sem limitações)
- ⊙⊙⊙◯ MODERADA (RCT com limitações OU obs forte)
- ⊙⊙◯◯ BAIXA (RCT sérias limitações OU obs)
- ⊙◯◯◯ MUITO BAIXA (opinião expert)

### **Força de recomendação:**
- **FORTE** (faça)
- **CONDICIONAL** (considere)

### **Fatores downgrade:**
1. Risco de viés
2. Inconsistência
3. Indireticidade (PICO)
4. Imprecisão
5. Viés de publicação

### **Fatores upgrade:**
1. Grande magnitude de efeito
2. Gradiente dose-resposta
3. Confundidor residual

---

## 📚 ARQUIVOS IMPORTANTES

### **No projeto (/mnt/project/):**
- `index.html` - HTML principal (1.466 linhas, 528 inline styles)
- `css/base.css` - Design system completo (543 linhas)
- `css/responsive-fix.css` - Media queries
- `js/navigation.js` - Sistema de navegação
- `GITHUB_CREDENTIALS.md` - Token e repo
- `README.md` - Documentação do projeto
- `PLANO_APRENDIZADO_REPETICAO.md` - Metodologia
- `PROTOCOLO_SLIDES_PREMIUM.md` - Padrões de qualidade
- `bmj2024*.pdf` - 8 artigos de referência

### **No GitHub:**
- https://github.com/lucasmiachon-blip/aulas/tree/refactor/v2.0.0
- https://lucasmiachon-blip.github.io/aulas/aula_grade/viewer_v2_0_0/

---

## 🎯 META PARA 1 DIA

**Objetivo:** 40 slides completos

**Estratégia:**
- **Manhã (6h):** Slides 14-25 (12 slides)
- **Tarde (6h):** Slides 26-37 (12 slides)
- **Noite (3h):** Slides 38-40 + ajustes finais (3 slides)

**Ritmo:** 1 slide a cada 25 minutos (incluindo commits)

---

## ⚡ AÇÃO IMEDIATA

**PRÓXIMO PASSO:** Criar slides 14-16 AGORA

**Conteúdo:**
1. Imagem 1 → Slide sobre CAC e GRADE
2. Imagem 2 → Slide sobre Motor do GRADE  
3. Imagem 3 → Slide sobre CAC = 0

**Após criar → Commitar → Validar → Próximo lote**

---

## 🔥 FILOSOFIA

**"É no atrito que se cresce"** - Dr. Lucas Miachon

- Velocidade > Perfeição inicial
- Iterar > Planejar demais
- Fazer > Pensar
- Commit frequente > Sessões longas

---

**Última atualização:** 2026-01-15 17:15 UTC  
**Status:** ⚡ MODO URGÊNCIA ATIVO  
**Próxima ação:** CRIAR SLIDES 14-16 IMEDIATAMENTE
