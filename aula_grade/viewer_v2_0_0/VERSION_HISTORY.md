# 📚 Histórico de Versões

## 🔄 Versões do Viewer

### v1.9.8 - Última Versão Viável (Monolítica)
**Localização:** `C:\Users\prece\Downloads\viewer_GRADE_MAGNA_v1_9_8 (2).html`

**Características:**
- ✅ Versão monolítica (tudo em um arquivo HTML)
- ✅ CSS inline (`<style>` dentro do HTML)
- ✅ JavaScript inline (`<script>` dentro do HTML)
- ✅ Encoding UTF-8 correto
- ✅ 13 slides completos
- ✅ Funcional e testada

**Status:** Última versão viável antes da modularização

---

### v2.0.0 - Versão Modular (Atual)
**Localização:** `aula_grade/viewer_v2_0_0/`

**Características:**
- ✅ Arquitetura modular
- ✅ CSS separado: `css/base.css` + `css/responsive-fix.css`
- ✅ JavaScript separado: `js/navigation.js`
- ✅ HTML limpo: `index.html`
- ✅ Encoding UTF-8 direto (sem entidades HTML)
- ✅ 13 slides completos
- ✅ Mesmo conteúdo da v1.9.8, apenas reorganizado

**Melhorias:**
- Manutenibilidade (código separado)
- Reutilização (CSS/JS podem ser compartilhados)
- Organização (estrutura clara)
- Encoding garantido (`.gitattributes` + `.editorconfig`)

---

## 📋 Comparação

| Aspecto | v1.9.8 (Monolítica) | v2.0.0 (Modular) |
|---------|---------------------|------------------|
| **Arquivos** | 1 arquivo HTML | 4 arquivos (HTML + CSS + JS + README) |
| **CSS** | Inline (`<style>`) | Externo (`css/base.css`) |
| **JS** | Inline (`<script>`) | Externo (`js/navigation.js`) |
| **Manutenção** | Difícil (tudo junto) | Fácil (separado) |
| **Reutilização** | Não | Sim |
| **Encoding** | UTF-8 | UTF-8 direto (sem entidades) |
| **Conteúdo** | 13 slides | 13 slides (mesmo conteúdo) |

---

## 🎯 Quando Usar Cada Versão

### Use v1.9.8 quando:
- Precisar de um arquivo único (portabilidade)
- Não precisar modificar código
- Quiser backup/referência

### Use v2.0.0 quando:
- For desenvolver/modificar
- Precisar de manutenção
- Quiser reutilizar CSS/JS
- Trabalhar em equipe

---

## 📂 Estrutura de Arquivos

### v1.9.8 (Monolítica):
```
Downloads/
└── viewer_GRADE_MAGNA_v1_9_8 (2).html  (305KB, tudo em um arquivo)
```

### v2.0.0 (Modular):
```
aula_grade/viewer_v2_0_0/
├── index.html          (HTML dos slides)
├── css/
│   ├── base.css        (Estilos principais)
│   └── responsive-fix.css (Ajustes responsivos)
├── js/
│   └── navigation.js   (Navegação)
└── README.md           (Documentação)
```

---

## ✅ Garantias

- **Conteúdo:** Ambas as versões têm exatamente o mesmo conteúdo (13 slides)
- **Funcionalidade:** Ambas funcionam perfeitamente
- **Encoding:** Ambas usam UTF-8 correto
- **Compatibilidade:** Ambas funcionam em navegadores modernos

---

**Última atualização:** 2026-01-15  
**Status:** v2.0.0 é a versão atual e recomendada para desenvolvimento
