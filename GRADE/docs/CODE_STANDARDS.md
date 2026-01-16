# Code Standards (MVP pragmático)

## Objetivo
Deck HTML que abre em qualquer máquina, sem build.

## Regras
- Preferir CSS e JS externos (evitar inline), MAS: não refatorar o que já funciona no MVP.
- Não adicionar dependências (React/Vue/etc).
- Uma única fonte de verdade para paleta e tipografia (CSS variables).
- Evitar duplicar lógica de navegação.
- Qualquer ajuste visual deve ser feito no CSS, não "espalhado" em 50 estilos inline.

## Qualidade mínima
- Sem 404 de assets
- Sem corte de conteúdo ("safe margins")
- Navegação por teclado funciona
