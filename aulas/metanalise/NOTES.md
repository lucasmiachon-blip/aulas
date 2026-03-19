# NOTES — Meta-análise

> Decisões entre agentes e observações de sessão. Append-only.
> Referenciado por WT-OPERATING.md (bloqueios, decisões pendentes).

---

## 2026-03-17 — Verificação documental

### Pendências s-hook resolvidas
- evidence-db.md: Bojcic/Qureshi → EM USO (v4.1, linhas 126/137)
- narrative.md: 146/dia, Bojcic 81%, Qureshi 10% (linha 51)
- Notion References DB: Bojcic e Qureshi com "EM USO" confirmado via Notion search (timestamp 2026-03-16T23:16)
- AUDIT-VISUAL.md atualizado — pendências operacionais fechadas

### Pendências para main resolvidas na WT (autorização Lucas)
- docs/XREF.md: 8 arquivos metanalise adicionados + canônico Estado Metanalise
- docs/README.md: WT-OPERATING.md adicionado à tabela Estado e handoff
- CLAUDE.md root: status metanalise atualizado (QA parcial → F1 QA PASS, F2-F3 LINT-PASS)
- tasks/lessons.md: 3 lições doc sync adicionadas (drift dados, verbosidade candidatos, refs cross-doc)

## 2026-03-18 — Refs cruzadas QA workflow

### Feito na WT
- WT-OPERATING.md §9: adicionada tabela "Documentos complementares" (qa-engineer.md, ralph-qa/SKILL.md, AUDIT-VISUAL.md)

### Pendências para próxima sessão main
- `.claude/agents/qa-engineer.md`: adicionar ref `WT-OPERATING.md §4` (state machine per-aula)
- `.claude/skills/ralph-qa/SKILL.md`: adicionar ref `WT-OPERATING.md` (source) + `qa-engineer.md` (rubric)
- `docs/XREF.md`: adicionar entradas para qa-engineer.md e ralph-qa/SKILL.md

### Merge main 2026-03-18
- 4 commits Classe A/B absorvidos (zero conflitos):
  - `d22acc4` medical-researcher skill + agent
  - `59f9f97` final-pass v3.0.0 (Eixo B excitement)
  - `7840e53` archive deprecated skills, new-skill v2
  - `2831807` slide-punch skill
- Merge commit: `5406dd8`
- Zero Classe C. Build OK. Lint PASS.

### Investigação viewport ultrawide
- Monitor dev: 2560x1600 @ 150% → viewport ~1707x1067 → scale 1.334 → centrado OK
- A 100% scaling: scale 2.0 → conteúdo grande, centrado, mas "faixa" embaixo (taskbar?)
- Projetor congresso: TBD — Lucas pega viewport amanhã
- deck.js (shared/) escala corretamente em todos os aspect ratios testados (16:9, 16:10, 21:9)
- Nenhum fix necessário em deck.js

## 2026-03-19 — Visual uplift pre-work

### Decisao: visual uplift dentro do pipeline existente
- Pipeline QA slide-a-slide (WT-OPERATING.md) NAO muda
- O que muda: criterios visuais elevados + GSAP sofisticado + prompt Gemini v3.0
- Contexto sala: pequena, ~15 pessoas, 1-4m, TV LED 55-75", iluminacao forte → legibilidade constraint #1

### Infra aplicada
- SplitText importado em `index.template.html` (disponivel para qualquer slide via slide-registry.js)
- Dark-bg CSS consolidado: seletor compartilhado 6 slides com token overrides. Para adicionar slide dark: acrescentar ID no seletor em metanalise.css (~linha 642)

### Dark-bg reference map (sugestao — decide-se por slide no pipeline)
| Slide | BG | Razao |
|-------|-----|-------|
| s-checkpoint-1 | DARK (ja) | Ritmo narrativo |
| s-checkpoint-2 | DARK (ja) | Ritmo narrativo |
| s-forest-plot | DARK (CSS pronto) | Ferramenta visual central, Von Restorff |
| s-heterogeneity | DARK (CSS pronto) | Hero I2 dramatico |
| s-ancora | DARK (CSS pronto) | Cinematic article reveal |
| s-absoluto | DARK (CSS pronto) | NNT conversion dramatica |
| demais | LIGHT | Modo aprendizado, cores semanticas em bg claro |

### Prompt Gemini v3.0 (docs/prompts/gemini-slide-qa.md)
- Substitui v2.1. 4 dimensoes com chain-of-thought forcado. Exploration mandate para GSAP avancado.
- Referenciado por WT-OPERATING.md §4 QA.3

## 2026-03-19 — s-hook content rewrite (VITALITY backbone)

### Motivação
- Dados anteriores (146 SRs/dia, 41% acerto, 396 reversões) eram válidos mas datados/genéricos
- Lucas pediu: "dados do VITALITY são mais interessantes", "exemplo deve ser de META-ANÁLISE, não de interpretação de HR"
- Deep research via medical-researcher: PubMed + Consensus + Scite + Perplexity. Filtro Tier-1.

### Decisões de conteúdo (Lucas aprovou)
- **Beat 0:** VITALITY (1.330 trials retratados → 3.902 MAs) + Bojcic (81% qualidade baixa). Número âncora: 1.330.
- **Beat 1:** Consequência sistêmica: 20% mudam resultado + 157 guidelines contaminadas. Hero: "20%".
- **Beat 2:** NICE-SUGAR como cadeia MA→guideline: Wiener 2008 (29 RCTs pre-NICE-SUGAR) → NICE-SUGAR 2009 (6.104 pts, mortalidade ↑) → Griesdale 2009 (26 trials, confirmou). Framing: MA problem, não trial problem.
- Speaker notes enriquecidas: INSPECT-SR (25% RCTs questionáveis em Cochrane), Possamai (42%/19% em top-25 journals), Guyatt quote ("GRADE assumes data trustworthy").
- TRH/WHI e rosiglitazona REMOVIDOS do corpo (eram trial-framed, não MA-framed). Herrera-Perez 396 removido (genérico demais).

### CSS ajustes
- vol-text 18ch→22ch, hero-label 20ch→30ch, verdict 48px→40px
- Nenhuma mudança estrutural no grid (Z-pattern mantido)

### QA status
- Scorecards QA.0-QA.2 invalidados (conteúdo mudou significativamente)
- Gate 3 (screenshots + Gemini) = próximo passo
