# AUDIT-VISUAL — Meta-análise

> Scorecard por slide. 14 dimensões. Atualizado a cada QA pass.
> Pendente: audit final Gemini (Gate 4) para todas as dims.
> Pipeline: ver [QA-WORKFLOW.md](QA-WORKFLOW.md)

---

## Cobertura

| Fase | Slides | Scorecard formal | QA session |
|------|--------|-----------------|------------|
| F1 | s-title, s-hook, s-contrato | s-title e s-hook abaixo. s-contrato pendente decisao Lucas | 2026-03-16e |
| I1 | s-checkpoint-1 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F2 | s-rs-vs-ma → s-fixed-random (8) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |
| I2 | s-checkpoint-2 | Pendente (Fase 3 motion) | 2026-03-16j (constraint check PASS) |
| F3 | s-ancora → s-takehome (5) | Pendente scorecard formal | 2026-03-16j (constraint check PASS, QA slide-a-slide) |

**Nota:** Sessao 2026-03-16j fez QA slide-a-slide (h2 assertion, word count, refs, notes) para 17/18 slides — PASS.
Scorecards formais de 14 dimensoes existem apenas para s-title e s-hook (batch 1, sessao 2026-03-16e).
Demais slides passaram constraint check + review manual, mas sem scorecard 14-dim registrado.
Scorecards formais serao preenchidos durante ralph-qa batches 2-6 (proximas sessoes).

---

## s-title (00-title.html)

**Status:** PASS (QA slide-a-slide 2026-03-16e)
**Archetype:** title — dims E, M, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | h1 > subtitle > pillars > author — clara |
| T (tipografia) | 9 | Serif+sans, pesos adequados, uppercase 500 |
| E (layout fill) | 4 | ~30% — intencional para title |
| C (cor/contraste) | 8 | Tokens light-mode corretos (fix session 16e) |
| V (visuais) | 7 | Sem visual dominante — OK para title |
| K (consistência) | 9 | Padrão de capa |
| S (sofisticação) | 8 | Limpo, profissional |
| M (comunicação) | 5 | h1 = rótulo — correto para archetype |
| I (interações) | 6 | fadeUp + stagger presentes |
| D (dados) | N/A | Title — sem dados clínicos |
| A (acessibilidade) | 8 | aria-hidden nos dots, bom contraste |
| L (carga cognitiva) | 9 | Mínimo — título + 3 palavras |
| P (andragogia) | 6 | Sem decisão clínica — esperado |
| N (arco narrativo) | 8 | Abertura limpa, pilares antecipam estrutura |

**Fix aplicado:** tokens `--text-on-dark-*` → tokens light-mode (`--text-secondary`, `--text-primary`, `--text-muted`). Pilares peso 400→500.

**Pendências para audit Gemini (Gate 4):**
- Title divider (linha decorativa) — avaliar se é AI marker ou separação funcional
- Spacing vertical — grupo de conteúdo levemente acima do centro? Avaliar com Gemini
- Fill ratio 30% — confirmar que é adequado para projeção (muito vazio?)
- Tipografia do h1 (Instrument Serif) — confirmar legibilidade em projetor real

---

## s-hook (01-hook.html)

**Status:** PASS (QA slide-a-slide 2026-03-16e)
**Archetype:** hook — dims E, P intencionalmente baixas

| Dim | Score | Nota |
|-----|-------|------|
| H (hierarquia) | 9 | Pergunta > números (hero 81%) > verdict > source |
| T (tipografia) | 9 | Serif italic provocação, mono números, sans verdict |
| E (layout fill) | 5 | ~50% — intencional para hook (respiro dramático) |
| C (cor/contraste) | 9 | Tokens light-mode, verdict em --ui-accent |
| V (visuais) | 8 | 3 countUp hero numbers — impacto |
| K (consistência) | 9 | Padrão hook |
| S (sofisticação) | 9 | Limpo, dramático, source-tag no rodapé |
| M (comunicação) | 9 | Provocação → dados → punchline — arco completo |
| I (interações) | 9 | 2-beat state machine (beat0 auto, beat1 click) |
| D (dados) | 9 | 3 dados Tier 1 verificados + PMID (ERRO-003 corrigido) |
| A (acessibilidade) | 8 | Bom contraste, labels uppercase legíveis |
| L (carga cognitiva) | 9 | 3 dados + 1 verdict = dentro do 4±1 |
| P (andragogia) | 8 | Retrieval practice (pergunta antes de resposta) |
| N (arco narrativo) | 9 | Hook forte, cria tensão para Fase 1 |

**Fixes aplicados:**
- ERRO-003 corrigido: 88%→81% (Bojcic 2024), 8.5%→10% (Qureshi 2025)
- Especificidade `#deck p` corrigida (question text era 20px, agora --text-h2)
- Tokens: bulk fix --text-on-dark → --text-primary/secondary em TODO o CSS
- Labels encurtadas para fit horizontal
- Source-tag movida para .slide-inner (fora de .hook-question)
- Verdict em --ui-accent (cor sutil de ênfase)
- Source-tag centering fix: `#deck p.source-tag` com `max-width: none; width: 100%` (vence `.stage-c #deck p` de base.css)
- Texto beat-0: "publicadas hoje" → "por dia — só em 2019" (dado Hoffmann é de 2019, hoje >140/dia)
- Label "SRs por dia" → "SRs/dia em 2019" (contexto temporal)
- Speaker notes atualizadas (crescimento 80→146/dia entre 2019→2021)

**Pendências para audit Gemini (Gate 4):**
- Sufixo % nos números (81%, 10%) — avaliar se precisa de tratamento tipográfico (% menor)
- Distribuição vertical no fullscreen — validar em projetor real
- Beat 0 sozinho — avaliar impacto dramático do texto isolado antes do click
- Labels "CRITICAMENTE BAIXAS" e "GUIDELINES COM LOE FORTE" — legibilidade em projetor
- **Instrument Serif italic** na provocação (beat-0) — confirmar legibilidade em TV/projetor a 5m em sala iluminada. Se ilegível, fallback para DM Sans 600 italic
- "só em 2019" como qualificador — avaliar se enfraquece o impacto dramático ou se reforça (implica crescimento)

**Pendências operacionais:**
- Sync Notion References DB: Bojcic e Qureshi mudar de CANDIDATO → EM USO
- narrative.md atualizado (dados do hook)
- evidence-db.md atualizado (Bojcic/Qureshi: CANDIDATO → EM USO)
