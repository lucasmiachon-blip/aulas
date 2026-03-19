# Meta-análise — Regras Específicas

Parent: ver CLAUDE.md na raiz.

## WT State (atualizar a cada sessao)

- **Branch:** feat/metanalise-mvp
- **Ultimo merge main:** 5406dd8 (2026-03-18) — absorve skills/agents (medical-researcher, final-pass v3, slide-punch, new-skill v2, sync-evidence)
- **Classe C pendente:** 0
- **Infra sync:** OK

## Worktree

- **Path:** `C:\Dev\Projetos\wt-metanalise`
- **Branch:** `feat/metanalise-mvp`
- **Upstream:** `origin/feat/metanalise-mvp`
- **Escopo:** apenas `aulas/metanalise/`
- **Proibido:** `shared/`, `docs/` raiz, `CLAUDE.md` raiz, outras aulas
- **Exceção documental:** `docs/metanalise-scope.md`, `docs/slide-pedagogy.md` (autorizados pelo usuário)
- **shared/ restrictions:** READ-ONLY. Deferir mudanças para sessão em main.
- **Pre-merge checklist:**
  - [ ] `git diff --name-only main...HEAD | grep shared/` retorna vazio
  - [ ] Build passa sem erros
  - [ ] `git status` limpo
- **Merge protocol:** No main: `git merge --no-ff feat/metanalise-mvp`

## Escopo

- 45–60 min, residentes clínica médica (básico-intermediário)
- Foco: LEITURA CRÍTICA de MA (não produção de RS)
- Modelo: pairwise clássico de RCTs
- Âncora: **Valgimigli 2025 — Clopidogrel vs Aspirina (Lancet, PMID 40902613)**. IPD-MA, 7 RCTs, 28.982 pts. Cochrane = exemplos visuais
- Conceitos avançados (NMA, IPD, bayesiana) = fora do escopo
- Forest plots = imagens cropadas de artigos reais (NUNCA SVG construído do zero)
- **Área do Lucas ≠ hepatologia** — artigo pode ser de qualquer área (ambulatório ou hospital)
- Acesso: CAPES/USP — não precisa ser open access

## Documentacao order

1. **WT-OPERATING.md** — maquina de estados, checklists de transicao, QA 5-stage, anti-drift
2. **HANDOFF.md** — estado operacional + tabela de estados por slide
3. **CLAUDE.md** (este arquivo) — regras especificas da aula

## Hierarquia de referencia

narrative.md → evidence-db.md → blueprint.md → slides/
reading-list.md (paralelo, informa pre-reading)
archetypes.md (6 layout patterns — skeleton, constraints, animation contract)

## Arquivos de trabalho

```
slides/*.html (18 arquivos)
slides/_manifest.js
slide-registry.js
metanalise.css
```

Sem archetypes.css. Build via `npm run build:metanalise`.
GSAP plugins: SplitText + Flip + ScrambleTextPlugin (registered in index.template.html).

## Estrutura narrativa (v1)

3 fases + 2 interações (ver narrative.md):
1. **Fase 1 — Criar importância** (slides 00-02): engajar antes de ensinar
2. **Interação 1** (slide 03): checkpoint de engajamento
3. **Fase 2 — Metodologia** (slides 04-11): conceitos genéricos, sem artigo
4. **Interação 2** (slide 12): checkpoint de consolidação
5. **Fase 3 — Aplicação** (slides 13-17): Valgimigli 2025 (Lancet, PMID 40902613)

**Regra:** nenhum slide antes da Fase 3 referencia artigo específico.

## Hard constraints (herda root + adiciona)

1. Assertion-evidence em todos os slides
2. Fases 1-2: dados genéricos ou Cochrane Handbook. Artigo específico só na Fase 3
3. Sem dados inventados. Sem fonte tier 1 → [TBD]. Dados de checkpoints = ilustrativos (sinalizar)
4. GRADE como linguagem clínica, não burocracia
5. Forest plot: cropado de artigo real quando disponível; placeholder até lá
6. Corpo do slide <= 30 palavras
7. Speaker notes em português
8. Uma MA não é melhor que os RCTs que a alimentam — isso permeia a aula

## Status

| Campo | Valor |
|-------|-------|
| Slides | 18/18 deck completo (F1+I1+F2+I2+F3) |
| Ancora | Valgimigli 2025 Lancet (PMID 40902613) |
| Gates 1-4 | 18/18 PASS |
| Scorecards 14-dim | 3/18 (F1): s-title DONE, s-hook Gate 3+4 PASS, s-contrato Gemini pendente |
| Docs | narrative v2.3, blueprint v1.8, evidence-db v5.1 |
| Main sync | 5406dd8 (2026-03-18) |

Detalhes QA por slide: HANDOFF.md. Pipeline: WT-OPERATING.md §4.
