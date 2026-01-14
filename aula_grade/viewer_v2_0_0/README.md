# GRADE Magna Viewer v2.0.0 - Modular Architecture

## 📁 Estrutura

```
viewer_v2_0_0/
├── index.html              (1,464 linhas - estrutura + conteúdo slides)
├── css/
│   └── base.css            (183 linhas - estilos completos)
├── js/
│   └── navigation.js       (65 linhas - sistema de navegação)
└── README.md               (este arquivo)
```

**Total: 1,712 linhas** (vs 1,563 linhas monolítico original)

## 🎯 Vantagens da Modularização

### 1. **Manutenção**
- Alterar cores → edite apenas `css/base.css`
- Ajustar navegação → edite apenas `js/navigation.js`
- Adicionar slides → edite apenas `index.html`

### 2. **Versionamento Git**
- Commits mais limpos e focados
- Diff mais legível (mudanças isoladas por arquivo)
- Merge conflicts reduzidos

### 3. **Performance**
- Browser pode cachear CSS/JS separadamente
- Recarregamento mais rápido em edições

### 4. **Escalabilidade**
- Fácil adicionar `css/components.css` para novos componentes
- Fácil adicionar `js/animations.js` para animações complexas
- Fácil criar `js/slides-data.json` para separar conteúdo

## 🔧 Como Usar

### Desenvolvimento Local
```bash
# Abrir no navegador (requer servidor HTTP local)
python3 -m http.server 8000
# Acesse: http://localhost:8000/index.html
```

### Edição de Estilos
```css
/* css/base.css */
:root {
    --navy: #0B1320;   /* Altere cores aqui */
    --gold: #DDB944;
    --bg: #F9F8F4;
    --teal: #1F766E;
}
```

### Adicionar Novo Slide
```html
<!-- index.html, antes de </div><!-- viewport --> -->
<section class="slide">
    <h2>Novo Título</h2>
    <div class="grid-main">
        <!-- Conteúdo do slide -->
    </div>
</section>
```

### Modificar Navegação
```javascript
// js/navigation.js
// Ex: Adicionar navegação por número
document.onkeydown = (e) => {
    if (e.key >= '1' && e.key <= '9') {
        show(parseInt(e.key) - 1);
    }
};
```

## 📊 Comparação v1.9.8 vs v2.0.0

| Aspecto | v1.9.8 (Monolítico) | v2.0.0 (Modular) |
|---------|---------------------|------------------|
| **Arquivos** | 1 arquivo (1,563 linhas) | 4 arquivos (1,712 linhas total) |
| **CSS** | Inline (86 linhas) | Externo (183 linhas) |
| **JS** | Inline (27 linhas) | Externo (65 linhas) |
| **HTML puro** | 1,450 linhas | 1,464 linhas |
| **Manutenção** | Difícil (tudo misturado) | Fácil (separado por concern) |
| **Git diff** | Verboso | Limpo |
| **Browser cache** | Não (tudo em 1 arquivo) | Sim (CSS/JS cacháveis) |

## 🚀 Próximas Melhorias (Roadmap v2.1)

### CSS Modularization
```
css/
├── base.css       (reset + viewport + typography)
├── components.css (cards, badges, buttons)
├── slides.css     (slide-specific styles)
└── animations.css (transitions, special effects)
```

### JS Modularization
```
js/
├── navigation.js  (controles + keyboard)
├── slides-data.js (conteúdo dos slides em JSON)
└── renderer.js    (monta slides dinamicamente)
```

### Data Separation (v2.2+)
```json
// slides-data.json
{
  "slides": [
    {
      "id": 1,
      "type": "cover",
      "title": "CORE GRADE",
      "subtitle": "A Coragem na Incerteza",
      "theme": "navy"
    },
    {
      "id": 2,
      "type": "content",
      "layout": "2-column",
      "content": { ... }
    }
  ]
}
```

## ⚠️ Notas Importantes

### Caminhos Relativos
- CSS: `href="css/base.css"` (relativo ao `index.html`)
- JS: `src="js/navigation.js"` (relativo ao `index.html`)

### Compatibilidade
- ✅ Chrome/Edge (Chromium) 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ⚠️ Requer servidor HTTP (não funciona em `file://`)

### Performance
- CSS carrega bloqueante (normal para apresentação)
- JS carrega no final (não bloqueia rendering)
- Total ~10KB (gzipped: ~3KB)

## 📝 Changelog desde v1.9.8

**v2.0.0 (2026-01-14)**
- ✨ FEAT: Extração completa de CSS inline → `css/base.css`
- ✨ FEAT: Extração completa de JS inline → `js/navigation.js`
- 📝 DOCS: Criação de README com guia de uso
- 🔧 REFACTOR: Estrutura de diretórios modular
- 🐛 FIX: Adicionado `preventDefault()` em keyboard nav (evita scroll)
- 🐛 FIX: Wrapped JS em IIFE para evitar poluição global

## 🤝 Desenvolvimento

### Adicionar Novo Componente CSS
1. Edite `css/base.css` ou crie novo arquivo CSS
2. Adicione `<link>` no `<head>` de `index.html`
3. Use classes nos slides

### Adicionar Nova Funcionalidade JS
1. Edite `js/navigation.js` ou crie novo arquivo JS
2. Adicione `<script>` antes de `</body>` em `index.html`
3. Use namespaces para evitar conflitos

## 📧 Contato

Projeto: CORE GRADE 2026 — SBC 2025 Dyslipidemia Guidelines  
Autor: Lucas Peres Miachon  
Versão: 2.0.0 (Modular Architecture)  
Data: Janeiro 2026
