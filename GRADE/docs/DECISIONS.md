# Changelog Editorial - Decisões de Refatoração

## 2026-01-16 - Refatoração Estrutural v2.0.0

### Motivação
Criar estrutura modular para permitir desenvolvimento independente de blocos sem quebrar conteúdo existente (especialmente Bloco 1 - CAC).

### Decisões Principais

#### 1. Arquivo de Código Legado
- **O que:** Movida pasta `/aula_grade/` para `GRADE/archive/legacy-root/aula_grade/`
- **Por quê:** Remover "projeto paralelo" antigo do caminho crítico. Manter apenas estrutura canônica `GRADE/deck/` e `OSTEOPOROSE/deck/` na raiz.
- **Impacto:** Zero - apenas reorganização. Arquivos legados preservados no archive.

#### 2. Estrutura Canônica de Paths
- **O que:** Definidos paths canônicos únicos:
  - `GRADE/deck/index.html`
  - `GRADE/deck/css/base.css`
  - `GRADE/deck/js/navigation.js`
  - `OSTEOPOROSE/deck/index.html`
- **Por quê:** Um único "produto" por aula. Eliminar duplicatas e confusão sobre qual arquivo usar.
- **Impacto:** Desenvolvedores e IA sabem exatamente qual arquivo editar.

#### 3. Scaffold Modular
- **O que:** Criadas pastas vazias: `GRADE/src/blocks/`, `GRADE/src/partials/`, `GRADE/src/build/`
- **Por quê:** Preparar estrutura para desenvolvimento futuro modular. Blocos não interferem uns nos outros.
- **Impacto:** Futuro - quando bloco 2 for desenvolvido, não precisará tocar em bloco 1.

#### 4. Proteções LOCK para Bloco 1 (CAC)
- **O que:** Adicionados comentários `<!-- LOCK_START: BLOCO_1_CAC -->` e `<!-- LOCK_END: BLOCO_1_CAC -->` envolvendo slides 9-13
- **Por quê:** Garantir que IA/claude não edite conteúdo clínico nem estética do Bloco 1 ao trabalhar em blocos futuros.
- **Impacto:** Proteção de conteúdo crítico. Ver `LOCK_RULES.md` para regras detalhadas.

#### 5. Navigation.js Sem Hardcode
- **O que:** Removido `if(index === 3)` e substituído por seleção via `data-anim="bars"`
- **Por quê:** Adicionar slides não deve quebrar animações. Lógica baseada em atributos é mais robusta.
- **Impacto:** Slides podem ser inseridos antes do slide interativo sem quebrar funcionalidade.

### Próximos Passos
- Desenvolvimento do Bloco 2 (Calculadoras) usando estrutura modular
- Sistema de build para combinar blocos (futuro)
- Documentação de padrões visuais por bloco
