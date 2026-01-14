# GRADE Magna Viewer v2.0.0 - Modular Architecture

## 📁 Estrutura

```
viewer_v2_0_0/
├── index.html              (1,464 linhas - estrutura + conteúdo slides)
├── css/
│   ├── base.css            (77 linhas - estilos completos)
│   └── responsive-fix.css   (CSS responsivo)
├── js/
│   └── navigation.js       (45 linhas - sistema de navegação)
└── README.md               (este arquivo)
```

**Total: ~1,586 linhas** (vs 1,564 linhas monolítico original)

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
| **Arquivos** | 1 arquivo (1,564 linhas) | 4 arquivos (~1,586 linhas total) |
| **CSS** | Inline (78 linhas) | Externo (77 linhas) |
| **JS** | Inline (26 linhas) | Externo (45 linhas, IIFE) |
| **HTML puro** | 1,460 linhas | 1,464 linhas |
| **Encoding** | Corrompido (caracteres especiais) | UTF-8 correto |
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

### Encoding UTF-8
- **CRÍTICO**: Arquivo deve ser salvo sempre em UTF-8 sem BOM
- Todos os caracteres especiais (é, ão, í, ú, ç, ê, ó, á, etc.) devem estar corretos
- Meta tag: `<meta charset="utf-8"/>` presente no HTML
- Se caracteres aparecerem como símbolos, verificar encoding do arquivo

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
- 🐛 FIX: **Correção crítica de encoding UTF-8** - todos os caracteres especiais (é, ão, í, ú, ç, etc.) agora corretos
- 🐛 FIX: Substituição de arquivo corrompido por versão limpa com encoding preservado

## 🤝 Desenvolvimento

### Adicionar Novo Componente CSS
1. Edite `css/base.css` ou crie novo arquivo CSS
2. Adicione `<link>` no `<head>` de `index.html`
3. Use classes nos slides

### Adicionar Nova Funcionalidade JS
1. Edite `js/navigation.js` ou crie novo arquivo JS
2. Adicione `<script>` antes de `</body>` em `index.html`
3. Use namespaces para evitar conflitos

## 🤖 Instruções para Claude AI

### Protocolo de Encoding (OBRIGATÓRIO)
**ANTES DE QUALQUER EDIÇÃO:**
1. ✅ Verificar que o arquivo está em UTF-8
2. ✅ Confirmar que caracteres especiais estão corretos (é, ão, í, ú, ç, etc.)
3. ✅ Se encontrar caracteres corrompidos (ex: "Ã©" em vez de "é"), NÃO editar até corrigir encoding
4. ✅ Sempre salvar em UTF-8 sem BOM após edições

### Estrutura Modular
- **HTML**: Apenas estrutura e conteúdo dos slides
- **CSS**: Tudo em `css/base.css` - NUNCA adicionar CSS inline
- **JS**: Tudo em `js/navigation.js` - NUNCA adicionar JS inline
- **Manter separação**: Cada arquivo tem sua responsabilidade

### Ao Adicionar/Modificar Slides
1. Editar apenas `index.html`
2. Usar classes CSS existentes (não criar estilos inline)
3. Manter estrutura semântica HTML
4. Verificar encoding após salvar

### Ao Modificar Estilos
1. Editar apenas `css/base.css`
2. Usar variáveis CSS (`:root`) para cores
3. Manter responsividade (unidades vw/vh)

### Ao Modificar Navegação
1. Editar apenas `js/navigation.js`
2. Manter código dentro do IIFE
3. Testar navegação por teclado (setas, espaço)

## 📧 Contato

Projeto: CORE GRADE 2026 — SBC 2025 Dyslipidemia Guidelines  
Autor: Lucas Peres Miachon  
Versão: 2.0.0 (Modular Architecture)  
Data: Janeiro 2026
