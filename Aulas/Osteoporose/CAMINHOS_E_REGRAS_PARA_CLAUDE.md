# 📍 CAMINHOS E REGRAS PARA CLAUDE

## 🎯 DOCUMENTOS COM REGRAS E CAMINHOS:

### **1. Como trabalhar com Git:**
📄 **`CLAUDE_COMO_TRABALHAR_GIT.md`**
- Caminho completo: `Aulas/Osteoporose/CLAUDE_COMO_TRABALHAR_GIT.md`
- Onde Auto está commitando (branch `main`)
- Como resolver conflitos (priorizar Claude)
- Estratégia completa de trabalho

### **2. Prompt rápido Git:**
📄 **`PROMPT_PARA_CLAUDE_GIT.md`**
- Caminho completo: `Aulas/Osteoporose/PROMPT_PARA_CLAUDE_GIT.md`
- Versão resumida das regras Git
- Comandos essenciais

### **3. Resumo completo do trabalho do Auto:**
📄 **`RESUMO_PARA_CLAUDE.md`**
- Caminho completo: `Aulas/Osteoporose/RESUMO_PARA_CLAUDE.md`
- Tudo que Auto fez no Slide 7
- Locais exatos no código (linhas)
- Como debugar

### **4. Mudanças para ensino:**
📄 **`MUDANCAS_PARA_CLAUDE.md`**
- Caminho completo: `Aulas/Osteoporose/MUDANCAS_PARA_CLAUDE.md`
- Mudanças detalhadas com explicações didáticas
- Conceitos para ensinar ao usuário

### **5. Workflow de colaboração:**
📄 **`WORKFLOW_AUTO_CLAUDE.md`**
- Caminho completo: `Aulas/Osteoporose/WORKFLOW_AUTO_CLAUDE.md`
- Sistema completo de colaboração
- Modalidades: ensino e escape

### **6. Como ler a documentação:**
📄 **`COMO_CLAUDE_DEVE_LER.md`**
- Caminho completo: `Aulas/Osteoporose/COMO_CLAUDE_DEVE_LER.md`
- Ordem de leitura recomendada
- Como debugar

---

## 📂 ESTRUTURA DE PASTAS:

```
Ignis_Animi/
└── Aulas/
    └── Osteoporose/
        ├── viewer_v2_35.html          (arquivo principal - v2.36)
        ├── CLAUDE_COMO_TRABALHAR_GIT.md
        ├── PROMPT_PARA_CLAUDE_GIT.md
        ├── RESUMO_PARA_CLAUDE.md
        ├── MUDANCAS_PARA_CLAUDE.md
        ├── WORKFLOW_AUTO_CLAUDE.md
        ├── COMO_CLAUDE_DEVE_LER.md
        ├── CHANGELOG_VIEWER.md
        ├── REGRA_VERSIONAMENTO.md
        └── CAMINHOS_E_REGRAS_PARA_CLAUDE.md (este arquivo)
```

---

## 🎯 REGRAS PRINCIPAIS:

### **Git:**
- Branch: `main`
- Local: `C:\Users\lucas\OneDrive\LM\Documentos\Ignis_Animi\Aulas\Osteoporose`
- Se conflitar: **remover mudanças do Auto, manter as do Claude**
- Prioridade: **Claude > Auto**

### **Versionamento:**
- Arquivo: `viewer_v2_35.html`
- Versão atual: **v2.36**
- Sempre atualizar versão ao fazer mudanças
- Ver `REGRA_VERSIONAMENTO.md`

### **Símbolos:**
- **NÃO usar símbolos especiais ou emojis**
- Substituir por letras/texto simples
- Exemplos:
  - `→` → `->`
  - `❌` → `[X]` ou `NAO`
  - `✅` → `[OK]` ou `SIM`
  - Acentos: usar sem acentos quando possível

---

## 🔍 COMO ENCONTRAR INFORMAÇÕES:

### **Se precisar saber sobre Git:**
1. Ler `CLAUDE_COMO_TRABALHAR_GIT.md`
2. Ou versão rápida: `PROMPT_PARA_CLAUDE_GIT.md`

### **Se precisar entender trabalho do Auto:**
1. Ler `RESUMO_PARA_CLAUDE.md` (visão geral)
2. Ler `MUDANCAS_PARA_CLAUDE.md` (detalhes)

### **Se precisar ensinar ao usuário:**
1. Ler `MUDANCAS_PARA_CLAUDE.md`
2. Usar seção "CONCEITOS PARA ENSINAR"

### **Se precisar debugar:**
1. Ler seção "DEBUG" em `RESUMO_PARA_CLAUDE.md`
2. Ver linhas específicas mencionadas

---

## 📋 CHECKLIST RÁPIDO:

Antes de trabalhar:

- [ ] Li `CLAUDE_COMO_TRABALHAR_GIT.md`?
- [ ] Entendi onde Auto está commitando?
- [ ] Sei como resolver conflitos?

Para entender trabalho do Auto:

- [ ] Li `RESUMO_PARA_CLAUDE.md`?
- [ ] Vi commits recentes: `git log --oneline -10`?

Para fazer mudanças:

- [ ] Sempre substituir símbolos por letras?
- [ ] Atualizar versão se mudar viewer?
- [ ] Priorizar minhas mudanças sobre Auto?

---

## 🚀 COMANDOS ÚTEIS:

```bash
# Ver status Git
git status

# Ver commits do Auto
git log --oneline -10

# Ver mudanças do Auto
git show HEAD

# Resolver conflito (priorizar Claude)
git checkout --theirs arquivo.html
git add arquivo.html
git commit -m "fix: [descrição] - priorizando Claude"
```

---

**Última atualização:** Janeiro 2025
**Versão:** v2.36
