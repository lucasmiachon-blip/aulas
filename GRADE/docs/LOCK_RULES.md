# Regras de Proteção LOCK - Bloco 1 (CAC)

## Objetivo
Garantir que o conteúdo clínico e a estética do Bloco 1 (CAC) nunca sejam alterados acidentalmente durante desenvolvimento de blocos futuros.

## Localização do Bloco Protegido

O Bloco 1 (CAC) está delimitado pelos comentários:
```html
<!-- LOCK_START: BLOCO_1_CAC (NÃO EDITAR CONTEÚDO NEM ESTILO) -->
<!-- ... slides 9-13 (índices 8-12) ... -->
<!-- LOCK_END: BLOCO_1_CAC -->
```

**Slides protegidos:**
- Slide 9: CAC - Aplicação GRADE
- Slide 10: CAC = 0 - Prognóstico
- Slide 11: CAC Modifica Benefício da Estatina (NNT)
- Slide 12: Aspirina na Prevenção Primária - NNT vs NNH por CAC
- Slide 13: Paradoxo CAC Zero (Low-Attenuation Plaque)

## Regras para IA (Claude/GPT)

### ✅ PERMITIDO dentro de LOCK
- **Nenhuma edição de conteúdo clínico**
- **Nenhuma alteração de estilos/CSS inline**
- **Nenhuma modificação de estrutura HTML**

### ✅ PERMITIDO fora de LOCK
- Adicionar novos slides antes/depois do bloco
- Criar novos blocos (02_METAS, 03_BEMPEDOICO_SAMS, etc.)
- Editar slides introdutórios (1-8)
- Editar slides de outros blocos (14+)
- Corrigir paths quebrados (CSS/JS links)
- Atualizar metadados do HTML (title, charset)

### ❌ PROIBIDO
- Alterar texto médico dentro de `<!-- LOCK_START: BLOCO_1_CAC -->` até `<!-- LOCK_END: BLOCO_1_CAC -->`
- Modificar cores, fontes, espaçamentos dos slides 9-13
- Remover ou mover slides do Bloco 1
- Editar referências bibliográficas dos slides protegidos
- Alterar lógica de animação que afete apenas slides 9-13

## Exceções (Apenas com Aprovação Explícita)

Se for absolutamente necessário editar o Bloco 1:
1. **Solicitar aprovação explícita do mantenedor**
2. **Documentar motivo em `DECISIONS.md`**
3. **Criar backup antes da edição**
4. **Testar que nenhum outro bloco quebrou**

## Como Verificar se Está Dentro do LOCK

Antes de editar qualquer slide:
1. Procurar por `<!-- LOCK_START: BLOCO_1_CAC` no arquivo
2. Verificar se o slide que você quer editar está entre LOCK_START e LOCK_END
3. Se sim → **PARAR e perguntar ao usuário**
4. Se não → proceder com edição normalmente

## Exemplo de Uso

**Cenário:** Desenvolver Bloco 2 (Calculadoras)

**Ação permitida:**
- Adicionar slide 14, 15, 16... após `<!-- LOCK_END: BLOCO_1_CAC -->`
- Criar novo CSS para slides de calculadoras
- Não tocar nos slides 9-13

**Resultado:** Bloco 1 permanece intocado, Bloco 2 desenvolvido independentemente.
