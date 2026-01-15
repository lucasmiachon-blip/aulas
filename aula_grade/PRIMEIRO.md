# 🎯 PRIMEIRO - Plano A para Visualização dos Slides

## 📍 SITUAÇÃO ATUAL

**Branch:** `refactor/v2.0.0`  
**Última versão:** `aula_grade/viewer_v2_0_0/`  
**Arquivo principal:** `viewer_v2_0_0/index.html`  
**Status:** ✅ Encoding UTF-8 correto, estrutura modular funcionando

---

## 🎬 PLANO A: Visualizar Slides e Ajustar em Tempo Real

Você tem **2 opções** para visualizar os slides e fazer ajustes:

### ✅ OPÇÃO 1: Usar Artifacts do Claude (Recomendado)

**Como funciona:**
1. Eu crio/atualizo o arquivo `viewer_v2_0_0/index.html`
2. Você pede: "mostre o viewer nos artifacts"
3. Eu envio o arquivo HTML completo como artifact
4. Você abre no navegador e vê as mudanças
5. Você me pede ajustes e eu atualizo
6. Repetir até ficar perfeito

**Vantagens:**
- ✅ Visualização imediata
- ✅ Não precisa servidor local
- ✅ Funciona offline
- ✅ Fácil de compartilhar

**Como pedir:**
```
"Mostre o viewer atualizado nos artifacts"
"Envie o index.html como artifact para eu ver"
"Crie um artifact com o viewer completo"
```

---

### ✅ OPÇÃO 2: Viewer em Tempo Real (Servidor Local)

**Como funciona:**
1. Você inicia um servidor HTTP local na pasta `viewer_v2_0_0/`
2. Abre `http://localhost:8000/index.html` no navegador
3. Eu faço mudanças no código
4. Você recarrega a página (F5) para ver mudanças
5. Ajustamos em tempo real

**Comandos para iniciar servidor:**

**Python:**
```bash
cd aula_grade/viewer_v2_0_0
python -m http.server 8000
# Acesse: http://localhost:8000/index.html
```

**Node.js:**
```bash
cd aula_grade/viewer_v2_0_0
npx http-server -p 8000
# Acesse: http://localhost:8000/index.html
```

**PowerShell (Windows):**
```powershell
cd aula_grade/viewer_v2_0_0
python -m http.server 8000
# Acesse: http://localhost:8000/index.html
```

**Vantagens:**
- ✅ Atualização em tempo real (F5)
- ✅ Hot reload se configurado
- ✅ Debug no navegador
- ✅ Testa funcionalidades interativas

---

## 📂 ESTRUTURA DO PROJETO (MANTIDA)

```
aula_grade/
├── PRIMEIRO.md              ← ESTE ARQUIVO
├── START_HERE.md            ← Guia rápido
├── CRITICAL_ENCODING_FIX.md ← Protocolo de encoding
└── viewer_v2_0_0/           ← ÚLTIMA VERSÃO (trabalhar aqui!)
    ├── index.html           ← HTML dos slides (1,464 linhas)
    ├── css/
    │   ├── base.css        ← Estilos (77 linhas)
    │   └── responsive-fix.css
    ├── js/
    │   └── navigation.js   ← Navegação (45 linhas)
    └── README.md           ← Documentação técnica
```

---

## 🔧 COMO TRABALHAR

### Para Editar Slides:
1. Editar: `viewer_v2_0_0/index.html`
2. Adicionar/modificar seções `<section class="slide">`
3. Usar classes CSS existentes (não criar inline)

### Para Editar Estilos:
1. Editar: `viewer_v2_0_0/css/base.css`
2. Modificar variáveis CSS (`:root`) para cores
3. Adicionar novos estilos se necessário

### Para Editar Navegação:
1. Editar: `viewer_v2_0_0/js/navigation.js`
2. Modificar funções de navegação
3. Adicionar novos controles se necessário

---

## 🚨 REGRAS CRÍTICAS

1. **Encoding:** Sempre UTF-8 sem BOM
2. **Versão:** Trabalhar APENAS em `viewer_v2_0_0/`
3. **Modular:** CSS em `css/`, JS em `js/`, HTML em `index.html`
4. **Testar:** Sempre verificar caracteres especiais após editar

---

## 📋 CHECKLIST ANTES DE PEDIR VISUALIZAÇÃO

- [ ] Arquivo salvo como UTF-8?
- [ ] Caracteres especiais corretos (é, ão, í, ú, ç)?
- [ ] Estrutura HTML válida?
- [ ] CSS e JS referenciados corretamente?
- [ ] Navegação funcionando?

---

## 🎯 PRÓXIMOS PASSOS

**Escolha uma opção:**
1. **"Mostre nos artifacts"** → Eu envio o HTML completo
2. **"Vou usar servidor local"** → Você inicia servidor, eu faço mudanças

---

**Última atualização:** 2026-01-14  
**Status:** ✅ Pronto para visualização
