# HANDOFF — Meta-análise

> Estado operacional. Atualizar ao final de cada sessão.

---

## Estado atual

- **Fase:** QA slide-a-slide com **visual uplift** (beleza avançada + GSAP sofisticado). s-title DONE (Gemini). **s-hook content rewrite concluído (2026-03-19):** VITALITY backbone (1.330 trials retratados → 3.902 MAs → 20% mudam resultado → 157 guidelines), NICE-SUGAR como exemplo MA concreto (beat 2). ScrambleText atualizado (146→1.330, 41%→20%). QA.0-QA.2 INVALIDADOS (conteúdo mudou) — re-audit pendente. Prompt Gemini v4.0 pronto (docs/prompts/gemini-slide-qa.md — structured CoT, code grounding, few-shot, self-critique). Pre-work infra: SplitText + Flip + ScrambleTextPlugin importados, dark-bg CSS consolidado (6 slides), archetypes.md documentado (6 layout patterns).
- **HTML cleanup (2026-03-17d):** `data-background-color` removido de 18/18 slides (deck.js ignora). `slide-navy` removido de 16/18 slides light (mantido em CP1+CP2 que TEM bg navy via CSS override). ERRO-009 documentado.
- **QA pipeline:** ver [WT-OPERATING.md §4](WT-OPERATING.md#4-qa-sub-loop-dentro-do-estado-qa). Gates 1-4: 18/18 PASS. Scorecards formais 14-dim: 3/18 (F1). s-title QA.0-QA.4 PASS (Gemini approved). **s-hook QA.0-QA.2 INVALIDADOS** (content rewrite VITALITY), Gate 3 pendente (screenshots + Gemini). s-contrato Gemini pendente. Fase 3 (dynamic): 3 pendentes (hook, CP1, CP2). Fase 4 (Gemini): s-title done, demais pendentes.
- **Branch:** feat/metanalise-mvp (worktree wt-metanalise)
- **Slides no index.html:** 18 (00-title → 01-hook → 02-contrato → 03-checkpoint-1 → 04-rs-vs-ma → 05-pico → 06-abstract → 07-forest-plot → 08-benefit-harm → 09-grade → 10-heterogeneity → 11-fixed-random → 12-checkpoint-2 → 13-ancora → 14-aplicacao → 15-aplicabilidade → 16-absoluto → 17-takehome)
- **Slides planejados:** 18 (00-17) — ver blueprint.md v1.8
- **Docs fundacionais:** narrative.md (v2.3), evidence-db.md (v5.1 — 34+ refs, VITALITY backbone + NICE-SUGAR + INSPECT-SR + Guyatt 2025), blueprint.md (v1.8), reading-list.md (v0.4 — +3 pre-reading)
- **_manifest.js:** CRIADO — 18 slides, fases F1/I1/F2/I2/F3
- **slide-registry.js:** CRIADO — state machines para title (choreography), hook (3-beat: ScrambleText "1.330" + SplitText words → ScrambleText "20%" + hero label → blackout + SplitText chars verdict NICE-SUGAR), checkpoint-1 (2-beat: cenario + twist), checkpoint-2 (3-beat: cenario + reveal + punchline). SplitText + Flip + ScrambleTextPlugin disponíveis globalmente (registrados em index.template.html)
- **Orphan slides:** 0
- **Orphan CSS:** 0
- **Artigo âncora:** ✅ Valgimigli 2025, Clopidogrel vs Aspirina (Lancet, PMID 40902613). IPD-MA, 7 RCTs, 28.982 pts
- **lint:slides:** ✅ PASS (zero FAILs)
- **HEX navy:** #162032 mantido (decisao Lucas — consistencia cross-aula)
- **CSS overrides em metanalise.css vs base.css:** `justify-content: center` restaurado + pseudo-elements desativados (ERRO-005). Checkpoint safe-center pattern proprio (ERRO-006). CSS zoom REMOVIDO — deck.js scale() é o mecanismo correto (ERRO-008). Fixed px tokens mantidos para evitar vw double-scaling. Hook v5: grid assimétrico 2-col (Z-pattern), `.hook-vol-number` 96px mono "1.330", `.hook-vol-text` 22ch max-width, hero-label 30ch, verdict 40px brutalismo (`--danger`, border-radius:0), blackout beat 2. Dead CSS removido. **Dark-bg consolidado:** seletor compartilhado para 6 slides (`#s-checkpoint-1/2, #s-forest-plot, #s-heterogeneity, #s-ancora, #s-absoluto`) com `background-color: #162032` + 8 on-dark tokens restaurados. Novos slides dark = adicionar ID ao seletor.
- **Reveal.js:** REMOVIDO desta WT. `package.json` sem reveal, `vite.config.js` exclui frozen aulas (ERRO-010).
- **Backlog CSS:** ~40 refs `--on-dark` tokens em metanalise.css (funcional via stage-c remap, naming misleading em slides light). Nao bloqueia QA — registrado para cleanup futuro.

## Estado dos Slides (maquina de estados — WT-OPERATING.md)

> Estados: BACKLOG → DRAFT → CONTENT → SYNCED → LINT-PASS → QA → DONE
> Verificar 1 a 1 antes de registrar. Nao assumir.

### F1 — Criar importancia (3 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 1 | s-title | QA | QA.0-QA.4 PASS. Gemini approved (beauty 9, legibility 10). Choreography + masking. |
| 2 | s-hook | QA | **v5 VITALITY rewrite**: 3-beat (1.330 retratados → 20% mudam → NICE-SUGAR). ScrambleText + SplitText. QA.0-QA.2 invalidados, Gate 3 pendente. |
| 3 | s-contrato | QA | Scorecard 14-dim PASS (Opus). Gemini pendente. |

### I1 — Checkpoint engajamento (1 slide)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 4 | s-checkpoint-1 | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### F2 — Metodologia (8 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 5 | s-rs-vs-ma | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 6 | s-pico | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 7 | s-abstract | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 8 | s-forest-plot | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 9 | s-benefit-harm | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 10 | s-grade | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 11 | s-heterogeneity | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 12 | s-fixed-random | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### I2 — Checkpoint consolidacao (1 slide)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 13 | s-checkpoint-2 | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### F3 — Aplicacao Valgimigli (5 slides)

| # | Slide | Estado | Notas |
|---|-------|--------|-------|
| 14 | s-ancora | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 15 | s-aplicacao | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 16 | s-aplicabilidade | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 17 | s-absoluto | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |
| 18 | s-takehome | LINT-PASS | Gates 1-4 PASS. Scorecard 14-dim pendente. |

### Resumo

- **QA (3):** s-title (DONE Gemini), s-hook (content rewrite, re-QA pendente), s-contrato (Gemini pendente)
- **LINT-PASS (15):** restantes — scorecard 14-dim pendente
- **DONE (0):** nenhum slide completou QA full (Opus + Gemini) — s-title aguarda re-confirmação formal

---

## Histórico

Trabalho completado e decisões tomadas: ver [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)

## Caminho crítico — próximas sessões

### Sessão N+1 (imediata) — QA slide-a-slide com visual uplift
1. **Pre-work DONE:** SplitText + Flip + ScrambleTextPlugin importados, dark-bg consolidado (6 slides), prompt Gemini v4.0 pronto, archetypes.md documentado.
2. **Pipeline normal** (WT-OPERATING.md §4): proximo slide na fila → QA.0-QA.4 → DONE → proximo.
   - Criterios visuais elevados: beleza avançada + GSAP sofisticado (SplitText, Flip, ScrambleText, custom choreographies)
   - Gemini prompt v4.0 (structured CoT 5-step, code-grounded GSAP API, few-shot exemplar, self-critique, token budget 1500-3000)
   - Contexto sala: pequena, ~15 pessoas, 1-4m, iluminacao forte, TV LED — legibilidade constraint #1
3. **Dark-bg reference** (sugestao, decide-se por slide):
   - Ja dark: s-checkpoint-1, s-checkpoint-2
   - Propostos dark: s-forest-plot, s-heterogeneity, s-ancora, s-absoluto (CSS pronto)
   - Light: demais (s-rs-vs-ma, s-pico, s-abstract, s-benefit-harm, s-grade, s-fixed-random, s-aplicacao, s-aplicabilidade, s-takehome)
4. **Ordem:** s-hook (Gate 3: screenshots + Gemini) → s-contrato (Gemini pendente) → s-checkpoint-1 → F2 em sequencia

### Sessão N+2
- Fase 4 (Gemini deck-level — este sim em batches)
- Build de producao (`npm run build:metanalise`)
- Merge para main

### Opcional — Merge cirrose→main
- Plano pronto (ver conversa anterior). Elimina WT cirrose permanentemente.
- Sequência: push cirrose → merge --no-ff em main (ALLOW_MAIN_CONTENT=1) → remover WT → atualizar hooks → push

## Bloqueios conhecidos

| Bloqueio | Impacto | Workaround |
|----------|---------|------------|
| Cochrane exemplos visuais | Forest plots e GRADE tables reais precisam de screenshots/crops | Acessar via CAPES e cropar quando iniciar QA visual |

## Pendências para main (Classe B — não editar na WT)

- **lint-slides.js false positive:** `scripts/lint-slides.js:110` — `data-animate="countUp"` sem `data-target` não pula `<script>` blocks. 2 false positives no index.html built.
- **qa-engineer.md:** ref a `mcp__claude_ai_perplexity` diverge do nome real. Verificar e corrigir em main.
- **ralph-qa SKILL.md:** ref a `perplexity_reason` pode não bater com MCP name real. Idem.
- **XREF.md:** entries metanalise adicionadas (autorização Lucas 2026-03-17)

## Não fazer ainda

- Não tocar em Cirrose
- Não expandir para NMA, IPD, bayesiana
- Não fazer build de producao antes de QA visual completo

> Sessoes anteriores (2026-03-14 a 2026-03-18): [HANDOFF-ARCHIVE.md](HANDOFF-ARCHIVE.md)
