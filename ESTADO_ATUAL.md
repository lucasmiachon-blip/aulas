# 📊 ESTADO ATUAL DO PROJETO - GRADE MAGNA VIEWER

**Data:** 2026-01-15 00:15 UTC  
**Versão:** v2.0.0 (Modular)  
**Branch GitHub:** `refactor/v2.0.0`  
**Status:** ✅ Estrutura limpa, 13 slides funcionais, pronto para expansão

---

## 📂 ESTRUTURA DE ARQUIVOS ATUAL

```
/mnt/project/
├── aula_grade/
│   └── viewer_v2_0_0/              ⭐ VERSÃO ATIVA
│       ├── index.html              (1464 linhas, 13 slides)
│       ├── README.md               (documentação completa)
│       ├── css/
│       │   ├── base.css            (2.6KB - paleta Turner)
│       │   └── responsive-fix.css  (3.8KB - responsividade)
│       └── js/
│           └── navigation.js       (1.4KB - navegação completa)
│
├── MEDICAL_SLIDE_PROTOCOL_v3_STREAMLINED.md  (568 linhas) ⭐ PROTOCOLO ATUAL
├── PLANO_APRENDIZADO_REPETICAO.md  ⭐ METODOLOGIA DE ENSINO
├── START_HERE.md                   (64 linhas - guia rápido)
├── WORKFLOW_CRIAR_COMMITAR.md      (guia de workflow)
├── GIT_COMMIT_INSTRUCTIONS.md      (instruções git)
├── Caminho_git_e_token.md          (token GitHub)
│
├── commit.sh                       ⭐ SCRIPT: commita 1 arquivo
├── commit_all.sh                   ⭐ SCRIPT: commita tudo
│
└── *.pdf (9 papers BMJ/ABC)        (papers de pesquisa)
```

---

## 🎯 13 SLIDES ATUAIS (Prontos)

| # | Título | Linha | Status |
|---|--------|-------|--------|
| 1 | CAPA: CORE GRADE | 17 | ✅ |
| 2 | NAVEGAR É PRECISO (Fernando Pessoa) | 27 | ✅ |
| 3 | CAC SOB LENTE GRADE | 93 | ✅ |
| 4 | CALIBRAGEM DA SALA (Interativo) | 229 | ✅ |
| 5 | O GRANDE DIVISOR | 285 | ✅ |
| 6 | O MOTOR DO GRADE | 348 | ✅ |
| 7A | INDIRECTNESS | 439 | ✅ |
| 7B | DOSE-RESPONSE GRADIENT | 537 | ✅ |
| 9 | CAC - APLICAÇÃO GRADE | 670 | ✅ |
| 10 | CAC = 0 - PROGNÓSTICO | 798 | ✅ |
| 11 | CAC MODIFICA BENEFÍCIO ESTATINA (NNT) | 911 | ✅ |
| 13 | PARADOXO CAC ZERO ⚠️ ordem | 1082 | ✅ |
| 12 | ASPIRINA PREVENÇÃO PRIMÁRIA ⚠️ ordem | 1247 | ✅ |

**Nota:** Slides 12 e 13 estão em ordem invertida no código (não afeta funcionalidade)

---

## 🧹 LIMPEZA REALIZADA (Hoje)

### ❌ DELETADOS (5 arquivos obsoletos):

1. `viewer_GRADE_MAGNA_v1_9_8__2_.html` (300KB - versão monolítica antiga)
2. `ESTADO_REAL_PROJETO.md` (desatualizado, branch errado)
3. `LEIA_QUANDO_VOLTAR.md` (desatualizado, branch errado)
4. `STATE_SLIDE_10.md` (encoding corrompido + desatualizado)
5. `COMPLETE_MEDICAL_SLIDE_PROTOCOL_v2.md` (5053 linhas - obsoleto)

### ✅ SUBSTITUÍDOS POR:

- `MEDICAL_SLIDE_PROTOCOL_v3_STREAMLINED.md` (568 linhas - protocolo atual)
- `START_HERE.md` (guia de orientação)
- `ESTADO_ATUAL.md` (este arquivo)

---

## 🎨 DESIGN SYSTEM (Paleta Turner)

```css
--navy: #0B1320     (backgrounds, títulos)
--gold: #DDB944     (destaques, números)
--bg: #F9F8F4       (fundo slides - ivory)
--teal: #1F766E     (clínico, certeza ALTA)
--blue: #2563EB     (links, interações)
--white: #FFFFFF    (cards, superfícies)
```

**Tipografia:**
- Georgia (títulos, citações)
- Lato (corpo, dados)

**Regra 80/15/5:**
- 80% Navy + Ivory (estrutura)
- 15% Gold (ênfase)
- 5% Teal/Blue (detalhes)

---

## 🚀 SCRIPTS DE COMMIT CONFIGURADOS

### **commit.sh** (commit individual)
```bash
./commit.sh "mensagem" "caminho/arquivo.html"
```

### **commit_all.sh** (commit completo)
```bash
./commit_all.sh "feat: adicionar slide 14 PREVENT"
```

**Commitam automaticamente para:**
- Branch: `refactor/v2.0.0`
- Repo: `lucasmiachon-blip/aulas`
- Path: `aula_grade/viewer_v2_0_0/`

---

## 📋 PROTOCOLO DE QUALIDADE (v3.0 Streamlined)

**Arquivo:** `MEDICAL_SLIDE_PROTOCOL_v3_STREAMLINED.md`  
**Linhas:** 568 (vs 5000 da versão antiga)

**Estrutura:**
- PART 1: Benchmark System (6 standards)
  - NEJM (rigor científico)
  - JACC (impacto clínico)
  - ESC (compliance regulatório)
  - Reynolds (signal vs noise)
  - Tufte (data-ink efficiency)
  - Duarte (impacto narrativo)
- PART 2: Design Essentials
- PART 3: Workflow (6 steps)
- PART 4: Cognitive Principles
- PART 5: Evidence-Based Framework (GRADE)
- Scoring Checklist

**Sistema de pontuação:** 6 benchmarks × 5 pontos = 30 max

---

## 🎯 PRÓXIMOS PASSOS (Sugeridos)

### **OPÇÃO A: Rodar Protocolo de Qualidade**
```
1. Aplicar protocolo no Slide 1 (teste)
2. Avaliar score (meta: >25/30)
3. Fazer ajustes necessários
4. Rodar em todos os 13 slides
5. Documentar scores
```

### **OPÇÃO B: Criar Slides Novos**
```
Slides planejados:
- Slide 14: PREVENT vs PCE vs QRISK (comparação modelos)
- Slide 15: Bempedoico + CLEAR Outcomes
- Slide 16: Metas LDL agressivas (<55, <70 mg/dL)
- Slide 17-20: Estratificação de risco
- Slide 21-25: Algoritmos SBC 2025
```

### **OPÇÃO C: Corrigir Ordem**
```
Inverter ordem dos slides 12 e 13 no código
(atualmente: 13 aparece antes do 12)
```

---

## 🔗 LINKS ÚTEIS

**GitHub:**
```
https://github.com/lucasmiachon-blip/aulas/tree/refactor/v2.0.0/aula_grade/viewer_v2_0_0
```

**Token:** Disponível em `Caminho_git_e_token.md` (não compartilhar)

---

## ⚙️ WORKFLOW DE TRABALHO ESTABELECIDO

### **Para criar novo slide:**

```
1. LUCAS pede: "Crie slide sobre [TEMA]"

2. CLAUDE faz:
   - Lê papers relevantes
   - Extrai dados tier-1
   - Cria HTML estrutural (sem style inline)
   - Adiciona classes CSS existentes
   - Se precisar estilo novo → edita base.css
   - Se precisar JS novo → edita navigation.js

3. LUCAS aprova código

4. CLAUDE salva arquivos separados:
   ✅ index.html (só estrutura)
   ✅ css/base.css (só estilos)
   ✅ js/navigation.js (só lógica)

5. CLAUDE commita:
   ./commit_all.sh "feat: slide [N] sobre [TEMA]"

6. GitHub atualizado ✅
```

### **NUNCA:**
- ❌ Adicionar `<style>` inline no HTML
- ❌ Adicionar `style="..."` nos elementos
- ❌ Adicionar `onClick="..."` inline
- ❌ Voltar ao padrão monolítico

---

## 📊 MÉTRICAS ATUAIS

- **Slides:** 13 (meta: ~40)
- **Linhas HTML:** 1464
- **Tamanho total:** ~310KB
- **Encoding:** UTF-8 ✅
- **Modularização:** 100% ✅

---

## ⚠️ ALERTAS AUTOMÁTICOS

**CLAUDE vai AVISAR quando:**
1. Arquivo HTML > 3000 linhas
2. Número de slides > 30
3. Código duplicado > 20%
4. Performance degradar

**AÍ:** Quebramos em módulos adicionais

---

## 🤝 COMPROMISSO DE QUALIDADE

**Mantido por:** Lucas Peres Miachon + Claude (Anthropic)  
**Padrão:** Tier-1 medical publications (NEJM, JACC, Lancet, BMJ)  
**Filosofia:** "Design for the tired resident in the back row at 5pm"  
**Encoding:** UTF-8 sem BOM (sempre)

---

## 🔄 QUANDO VOLTAR

**No próximo chat, diga:**

```
"Leia ESTADO_ATUAL.md e continue de onde paramos"
```

**OU:**

```
"Estamos no viewer v2.0.0, 13 slides prontos.
Próximo: [rodar protocolo / criar slide 14 / outro]"
```

---

**Última atualização:** 2026-01-15 00:15 UTC  
**Próxima ação sugerida:** Rodar protocolo de qualidade no Slide 1 (teste)

---

## 📌 NOTAS IMPORTANTES

1. **Encoding crítico:** Sempre UTF-8 sem BOM
2. **Modularização protegida:** HTML/CSS/JS sempre separados
3. **Commits frequentes:** Nunca perder trabalho
4. **Protocolo streamlined:** 568 linhas (não 5000)
5. **Scripts prontos:** `commit.sh` e `commit_all.sh` funcionais

---

**✅ TUDO PRONTO PARA CONTINUAR!**
