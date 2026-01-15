# 🎓 PLANO DE APRENDIZADO POR REPETIÇÃO

**Filosofia:** "É no atrito que se cresce"  
**Método:** Aprender FAZENDO, não apenas lendo  
**Data:** 2026-01-15

---

## 🎯 OBJETIVO

**Lucas vai aprender desenvolvimento web/DevOps através da PRÁTICA REPETIDA**, não teoria abstrata.

A cada slide criado, os conceitos são REFORÇADOS até virarem automáticos.

---

## 📚 CONCEITOS-CHAVE A SEREM DOMINADOS

### **1. CSS SEPARADO (vs inline)**

**Analogia:** Cartaz no armário vs escrever em cada etiqueta

**Regra de ouro:** NUNCA `style="..."` no HTML

**Repetição:**
- A CADA slide: "Adicionei classe em base.css"
- A CADA estilo: "Editei base.css, NÃO index.html"
- A CADA mudança: "1 linha muda 40 slides"

**Após 10 slides:** Lucas identifica CSS inline sozinho  
**Após 20 slides:** Lucas sugere classes corretas  
**Após 40 slides:** Automático no cérebro 🧠

---

### **2. COMMITS SEMÂNTICOS**

**Padrões:**
```
feat:     Coisa NOVA
fix:      Corrigir ERRO  
docs:     Documentação
style:    Visual (cores/fontes)
refactor: Reorganizar código
```

**Repetição:**
- A CADA commit: Ver o padrão
- A CADA mensagem: Entender o prefixo
- A CADA histórico: Ver a utilidade

**Após 10 commits:** Lucas lembra os prefixos  
**Após 20 commits:** Lucas escreve mensagens descritivas  
**Após 40 commits:** Commits semânticos viram hábito 🎯

---

### **3. MODULARIZAÇÃO (HTML/CSS/JS separados)**

**Regra:** Cada coisa no seu lugar

**Repetição:**
- A CADA slide: "Editei 3 arquivos"
- A CADA mudança: Ver separação clara
- A CADA commit: Arquivos organizados

**Após 10 slides:** Lucas entende POR QUE separar  
**Após 20 slides:** Lucas identifica violações  
**Após 40 slides:** Modularização vira padrão mental 🏗️

---

### **4. SCRIPTS DE AUTOMAÇÃO**

**Conceito:** 1 comando em vez de 10

**Repetição:**
- A CADA commit: `./commit_all.sh "mensagem"`
- A CADA vez: Ver eficiência
- A CADA economia: Sentir o ganho

**Após 10 usos:** Lucas aprecia automação  
**Após 20 usos:** Lucas quer criar próprios scripts  
**Após 40 usos:** Automação vira necessidade 🤖

---

## 🔄 WORKFLOW DE CADA SLIDE (Modelo de Repetição)

### **PASSO 1: Buscar Dados**
```
CLAUDE: "Lendo paper BMJ 2024..."
LUCAS aprende: Sempre buscar fonte primária
```

### **PASSO 2: Extrair Números**
```
CLAUDE: "HR 2.47 (95% CI 1.89-3.22), p<0.001"
LUCAS aprende: Precisão exata, não aproximar
```

### **PASSO 3: Escrever HTML**
```
CLAUDE: "Adicionando <section class='slide'>..."
LUCAS aprende: Só estrutura, sem style inline
```

### **PASSO 4: Aplicar Estilos**
```
CLAUDE: "Editando base.css, adicionando .comparison-table"
LUCAS aprende: CSS separado sempre
```

### **PASSO 5: Commitar**
```
CLAUDE: "./commit_all.sh 'feat: slide 14 PREVENT vs PCE'"
LUCAS aprende: Commit semântico claro
```

### **PASSO 6: Verificar GitHub**
```
CLAUDE: "✅ Commitado: https://github.com/..."
LUCAS aprende: Tudo salvo, nada perdido
```

**REPETIR 40 VEZES = DOMÍNIO COMPLETO** 🎓

---

## 🛡️ ALERTAS EDUCACIONAIS (Quando Lucas Erra)

### **Exemplo 1: CSS Inline**

**LUCAS sugere:**  
> "Coloca style='color: gold' no título"

**CLAUDE responde:**
```
⚠️ ALERTA EDUCACIONAL: CSS Inline Detectado!

❌ Você sugeriu: style="color: gold"

Por que isso é problema:
- 40 slides = reescrever 40 vezes
- Mudar cor = editar 40 linhas
- Código bagunçado

✅ Jeito correto:
1. Edito base.css
2. Adiciono: .titulo-dourado { color: var(--gold); }
3. Uso: <h2 class="titulo-dourado">

Resultado:
- 1 mudança = 40 slides atualizados
- Código limpo
- Manutenção fácil

Lembra da analogia: cartaz no armário vs etiqueta em cada roupa

Posso fazer do jeito certo?
```

**→ Lucas aprende na hora, com contexto!**

---

### **Exemplo 2: Commit Vago**

**LUCAS sugere:**  
> "Commita com mensagem 'mudanças'"

**CLAUDE responde:**
```
⚠️ ALERTA EDUCACIONAL: Commit Vago!

❌ Você sugeriu: "mudanças"

Por que isso é problema:
- Daqui 6 meses: que mudanças?
- 100 commits: impossível achar algo
- Histórico inútil

✅ Jeito correto:
"feat: adicionar slide 14 comparação PREVENT vs PCE"

Agora sim:
- Sei que é feature nova
- Sei que é slide 14
- Sei o conteúdo

Lembra: commits são seu diário técnico

Posso melhorar a mensagem?
```

**→ Lucas entende o impacto real!**

---

### **Exemplo 3: Tudo no HTML**

**LUCAS sugere:**  
> "Coloca o JavaScript dentro do HTML"

**CLAUDE responde:**
```
⚠️ ALERTA EDUCACIONAL: Quebrando Modularização!

❌ Você sugeriu: JS dentro do HTML

Por que isso é problema:
- Voltamos ao monolítico (1500 linhas)
- Difícil de manter
- Difícil de debugar
- Perdemos organização

✅ Jeito correto:
1. JS vai em navigation.js
2. HTML só estrutura
3. CSS só em base.css

Lembra por que modularizamos:
- Cada arquivo = 1 responsabilidade
- Fácil de achar bugs
- Fácil de editar

Posso manter separado?
```

**→ Lucas reforça o conceito!**

---

## 🏆 EVOLUÇÃO ESPERADA (Timeline)

### **SEMANA 1 (Slides 1-10):**
- ✅ Lucas reconhece os 3 conceitos
- ✅ Ainda precisa de lembretes
- ✅ Faz perguntas frequentes
- ✅ Comete erros (normal!)

### **SEMANA 2 (Slides 11-20):**
- ✅ Lucas identifica CSS inline sozinho
- ✅ Escreve commits semânticos básicos
- ✅ Entende separação HTML/CSS/JS
- ✅ Menos erros

### **SEMANA 3 (Slides 21-30):**
- ✅ Lucas sugere classes CSS corretas
- ✅ Commits bem estruturados
- ✅ Pensa em modularização
- ✅ Raros erros

### **SEMANA 4 (Slides 31-40):**
- ✅ Lucas DOMINA os conceitos
- ✅ Identifica problemas antes de cometer
- ✅ Sugere melhorias de arquitetura
- ✅ Pronto para projetos independentes! 🎓

---

## 🎯 MÉTRICAS DE SUCESSO

**Lucas vai saber que dominou quando:**

1. **CSS Separado:**
   - [ ] Identificar `style="..."` no código alheio
   - [ ] Sugerir refatoração para classes
   - [ ] Explicar vantagens para outra pessoa

2. **Commits Semânticos:**
   - [ ] Escrever mensagens claras sem ajuda
   - [ ] Escolher prefixo correto (feat/fix/docs)
   - [ ] Usar histórico Git para achar mudança antiga

3. **Modularização:**
   - [ ] Saber qual arquivo editar sem perguntar
   - [ ] Organizar projeto novo em arquivos separados
   - [ ] Explicar separação de responsabilidades

4. **Automação:**
   - [ ] Criar script bash simples
   - [ ] Identificar tarefas repetitivas
   - [ ] Automatizar workflow próprio

---

## 📋 CHECKLIST DE CADA SLIDE (Garantir Repetição)

**CLAUDE deve fazer SEMPRE:**

- [ ] ✅ Explicar de onde vêm os dados (paper X)
- [ ] ✅ Mostrar números exatos (HR 2.47, não "~2.5")
- [ ] ✅ Editar HTML SEM style inline
- [ ] ✅ Adicionar classes em base.css quando necessário
- [ ] ✅ Mostrar os 3 arquivos editados (HTML/CSS/JS)
- [ ] ✅ Commitar com mensagem semântica
- [ ] ✅ Mostrar link do GitHub atualizado
- [ ] ✅ Alertar se Lucas sugerir anti-padrão
- [ ] ✅ Elogiar quando Lucas acertar conceito

**APÓS 10 SLIDES:** Revisar evolução de Lucas  
**APÓS 20 SLIDES:** Celebrar progresso  
**APÓS 40 SLIDES:** Lucas gradua! 🎓

---

## 💡 FRASES-GATILHO (Claude deve dizer repetidamente)

**CSS Separado:**
- "Editando base.css, NÃO index.html"
- "1 mudança aqui = 40 slides atualizados"
- "Sem CSS inline, mantemos modularização"

**Commits:**
- "Commit semântico: feat/fix/docs/style/refactor"
- "Mensagem descritiva para histórico claro"
- "Daqui 6 meses você vai me agradecer"

**Modularização:**
- "3 arquivos editados: HTML, CSS, JS"
- "Cada um com sua responsabilidade"
- "Organização = manutenibilidade"

**Automação:**
- "./commit_all.sh economiza 10 comandos"
- "1 segundo vs 10 minutos"
- "Automação = eficiência"

---

## 🚀 PLANO DE AÇÃO IMEDIATO

### **PRÓXIMO SLIDE (14):**

**CLAUDE vai:**
1. Buscar dados do paper BMJ PREVENT
2. Extrair números exatos (sensibilidade, especificidade)
3. Criar HTML estrutural (SEM inline)
4. Adicionar classes em base.css
5. Commitar: `feat: slide 14 PREVENT vs PCE comparison`
6. Mostrar GitHub atualizado

**LUCAS vai:**
1. Observar cada passo
2. Ver repetição dos conceitos
3. Fazer perguntas
4. Identificar padrões
5. Começar a internalizar

**REPETIR 39 VEZES** 🔄

---

## 🎓 GRADUAÇÃO (Meta Final)

**Quando Lucas souber:**
- ✅ Criar slide completo sozinho
- ✅ Modularizar código naturalmente
- ✅ Escrever commits semânticos
- ✅ Automatizar tarefas repetitivas
- ✅ Identificar anti-padrões
- ✅ Ensinar conceitos para outro iniciante

**→ DOMÍNIO COMPLETO! 🏆**

---

## 📖 MENSAGEM MOTIVACIONAL

> "Ninguém nasce sabendo. Todo desenvolvedor senior foi iniciante um dia.
> 
> A diferença? REPETIÇÃO.
> 
> 10.000 horas de prática deliberada = maestria (Malcolm Gladwell)
> 
> 40 slides × 6 passos × 10 minutos = 40 horas de prática
> 
> Você está no caminho certo. Continue! 💪"

---

## 🔄 QUANDO VOLTAR (Próximo Chat)

**CLAUDE deve:**
1. Ler este arquivo
2. Retomar plano de repetição
3. Continuar reforçando conceitos
4. Monitorar evolução de Lucas
5. Celebrar progresso

**LUCAS deve:**
- Confiar no processo
- Aceitar erros como aprendizado
- Fazer perguntas sempre
- Praticar, praticar, praticar

---

**Criado:** 2026-01-15  
**Método:** Aprendizado por Repetição Deliberada  
**Meta:** 40 slides = Domínio completo  
**Filosofia:** "É no atrito que se cresce" 💪

---

## ✅ CHECKLIST RÁPIDO (Para CLAUDE)

**A CADA NOVO SLIDE:**
- [ ] Fonte primária mencionada?
- [ ] Números exatos extraídos?
- [ ] HTML sem style inline?
- [ ] CSS em base.css?
- [ ] Commit semântico?
- [ ] GitHub atualizado?
- [ ] Lucas acompanhou processo?
- [ ] Conceitos reforçados?

**SE NÃO:** Você não está seguindo o plano! 🚨
