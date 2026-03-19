# WT-OPERATING — Meta-análise (prompt operacional)

> Maquina de estados para sessoes de trabalho nesta worktree.
> Ler isto INTEIRO no inicio de TODA sessao. Sem excecoes.
> Criado: 2026-03-17. Coautoria: Lucas + Opus 4.6.

---

## 1. Inicio de Sessao (obrigatorio)

```bash
git log --oneline -5 && git status
cat aulas/metanalise/HANDOFF.md | head -40
```

Responder ANTES de qualquer trabalho:

1. **Qual slide esta em andamento?** (ver tabela de estados no HANDOFF)
2. **Qual estado ele esta?** (BACKLOG/DRAFT/CONTENT/SYNCED/LINT-PASS/QA/DONE)
3. **O que falta para avancar ao proximo estado?**
4. **Se tem slide em andamento → terminar ANTES de comecar outro.**

Se nenhum slide em andamento → propor o proximo do caminho critico ao usuario.

---

## 2. Maquina de Estados

```
BACKLOG → DRAFT → CONTENT → SYNCED → LINT-PASS → QA → DONE
```

| Estado | Significa | Criterio de saida |
|--------|-----------|-------------------|
| BACKLOG | Existe no manifest, sem HTML ou so esqueleto | Escrever conteudo completo |
| DRAFT | HTML existe, conteudo parcial ou [TBD] | Completar conteudo, verificar dados |
| CONTENT | Conteudo completo, dados verificados | Sincronizar 9 superficies (secao 7) |
| SYNCED | HTML + manifest + narrative + CSS alinhados | `npm run lint:slides` + `npm run lint:narrative-sync` PASS |
| LINT-PASS | Lints PASS | Submeter a QA (secao 4) |
| QA | Em revisao (5 sub-stages) | Todos sub-stages PASS |
| DONE | QA PASS + docs atualizados + commit | Nada — slide fechado |

### Regras de transicao

- **Transicoes so avancam.** Retrocesso = bug (registrar em ERROR-LOG).
- **Cada transicao tem checklist.** Nao pular etapas.
- **Um slide por vez.** Nao comecar outro ate fechar ou bloquear o atual.
- **Bloqueio** = precisa de Lucas, dado ausente, ou dependencia. Registrar em NOTES.md e mover para proximo.

---

## 3. Checklists de Transicao

### BACKLOG → DRAFT → CONTENT → SYNCED

Fases ja completadas (18/18 slides em LINT-PASS ou acima).
Checklists detalhados: ver `slide-editing.md` e `slide-identity.md` (9 superficies).

### SYNCED → LINT-PASS

- [ ] `npm run build:metanalise` PASS
- [ ] `npm run lint:slides` PASS
- [ ] `npm run lint:narrative-sync` PASS

### LINT-PASS → QA

Entrar no QA loop (secao 4). Nao ha checklist — e o loop inteiro.

### QA → DONE

- [ ] Todos sub-stages QA PASS (ou max iteracoes + NOTES.md)
- [ ] AUDIT-VISUAL.md scorecard atualizado (14 dims)
- [ ] HANDOFF.md estado = DONE
- [ ] CHANGELOG.md entry
- [ ] Commit: `fix(metanalise): s-{id} QA pass — {resumo}`

---

## 4. QA Sub-Loop (dentro do estado QA)

5 sub-stages, 5 checkpoints humanos. Agente NAO avanca sem OK do Lucas.

```
QA.0 CONTENT AUDIT
  → CHECKPOINT LUCAS

QA.1 CONSTRAINT CHECK
  → CHECKPOINT LUCAS

QA.2 VISUAL AUDIT (Opus)
  → CHECKPOINT LUCAS

QA.3 VISUAL AUDIT (Gemini multimodal)
  → CHECKPOINT LUCAS

QA.4 FIX + RE-AUDIT
  → DONE quando convergir (max 3 iteracoes)
```

### QA.0 — Content Audit

Verificar conteudo sem olhar visual:

- h2 e assercao clinica? Faz sentido para o publico?
- Dados numericos corretos? Fonte Tier 1?
- Narrativa: este slide cumpre seu `narrativeRole`?
- Tensao: `tensionLevel` bate com o conteudo?
- Para slides narrativeCritical: h2 foi aprovado por Lucas?

**Output:** lista de issues ou "PASS".
**→ CHECKPOINT:** apresentar ao Lucas, esperar OK.

### QA.1 — Constraint Check

Verificacoes automatizaveis (lint + HTML source):

| Check | Como | Obrigatorio |
|-------|------|-------------|
| h2 = assercao (nao rotulo) | Read HTML | Sim (exceto archetype title/hook) |
| Zero `<ul>/<ol>` no corpo | Grep HTML | Sim |
| `<aside class="notes">` com timing | Read HTML | Sim |
| `<section>` sem style display (E07) | Grep style= | Sim |
| Cores via var() — zero HEX hardcoded | Grep metanalise.css | Sim (exceto fallbacks) |
| PMIDs com [DATA] tag | Read notes | Sim |
| Headline match manifest↔HTML | lint:narrative-sync | Sim |
| Body word count <= 30 | Manual count | Sim |
| `.no-js`/`.stage-bad` failsafes | Grep metanalise.css | Sim |

**Output:** tabela check/resultado.
**→ CHECKPOINT:** apresentar ao Lucas, esperar OK.

### QA.2 — Visual Audit (Opus)

Capturar screenshots e analisar:

**Captura (Playwright) — DOIS formatos obrigatorios por estado:**

```bash
# Dev server deve estar ativo (npm run dev)
# Navegar ate o slide, esperar animacoes (2.5s), screenshot
# Se click-reveals: screenshot antes de cada click

# Output (AMBOS formatos para CADA estado):
# qa-screenshots/{slide-id}/
#   S0.png              ← 1280x720 — formato apresentacao (Plan C)
#   S0-fullscreen.png   ← 1920x1080 — inspecao detalhada
#   S1.png              ← apos click-reveal 1 (se existir)
#   S1-fullscreen.png   ← idem fullscreen
#   metrics.json        ← bounding boxes (opcional)
```

**Resolucoes obrigatorias:**
- **1280x720** — tamanho real da apresentacao (Plan C). Usar para avaliar legibilidade a distancia.
- **1920x1080** — fullscreen para inspecao de detalhes (tipografia, alinhamento, pixels).
- Ambos com viewport size real (sem deviceScaleFactor) para reproduzir o que o projetor mostra.

**Analise (Opus — leitura direta dos PNGs):**

Avaliar 14 dimensoes (escala 1-10):

| Cod | Dimensao | Fonte |
|-----|----------|-------|
| H | Hierarquia visual (Von Restorff) | Screenshot |
| T | Tipografia (escala, pesos, legibilidade) | Screenshot |
| E | Layout (fill ratio, gaps, alinhamento) | Screenshot + metrics |
| C | Cor e contraste (WCAG projecao >=7:1) | Screenshot + a11y check |
| V | Visuais (icones, graficos, decoracao) | Screenshot |
| K | Consistencia (tokens, patterns cross-slide) | Screenshot + design-system |
| S | Sofisticacao (sem AI markers, profissional) | Screenshot |
| M | Comunicacao (assercao + evidencia, clarity) | Screenshot + content |
| I | Interacoes (click-reveals, animacoes) | Screenshots por estado |
| D | Dados clinicos (PMIDs, accuracy) | HTML + notes |
| A | Acessibilidade (icones + cor, contraste) | Screenshot + a11y |
| L | Carga cognitiva (Cowan 4+-1, <=30 palavras) | Screenshot + count |
| P | Aprendiz adulto (expertise-reversal, Knowles) | Content + context |
| N | Arco narrativo (papel na fase, tensao) | Content + narrative.md |

Threshold: todas 14 dims >= 9.

**Output:** scorecard 14 dims com evidencias.
**→ CHECKPOINT:** apresentar ao Lucas, esperar OK.

### QA.3 — Visual Audit (Gemini multimodal)

Input para Gemini (TUDO junto):
1. Raw HTML do slide
2. Raw CSS (seletores relevantes do metanalise.css)
3. PNGs de cada estado (S0, S1... SN)
4. Video .webm da navegacao real

**Captura de video (Playwright):**

```js
// recordVideo: navegar ao slide, esperar, interagir, sair
// Slides sem animacao: video curto (entrada + estado final)
// Slides com click-reveals: video com cada click
// Slides com data-animate: video mostrando a animacao
// Salvar em qa-screenshots/{slide-id}/video.webm
```

**Prompt Gemini v6.0** (10 dimensoes, 5 personas, 10 lenses, radical ideas forcing):

Prompt canonico: `docs/prompts/gemini-slide-qa.md`

Principios do v6.0:
- 5 personas (director criativo, data-viz, andragogia, GSAP, a11y) com 10 lenses cada
- 10 dimensoes obrigatorias: legibilidade, beleza, animacao, narrativa, tipografia, dados, cor, layout, interacao, acessibilidade
- Constraint injection: sala pequena, ~15 pessoas, 1-4m, TV LED, iluminacao forte
- Radical ideas forcing + projected scorecard + temp 1.0
- Output: reasoning + propostas concretas com codigo quando possivel

**Output:** JSON do Gemini + interpretacao do agente.
**→ CHECKPOINT:** apresentar ao Lucas. Lucas aprova/rejeita sugestoes Gemini individualmente.

### QA.4 — Fix + Re-Audit

Aplicar fixes aprovados por Lucas:

1. Editar HTML/CSS conforme aprovado
2. `npm run build:metanalise`
3. Re-capturar PNGs + video do slide
4. Re-rodar QA.2 (Opus) nas dimensoes afetadas
5. Re-rodar QA.3 (Gemini) se fix foi significativo
6. Atualizar scorecard

**Max 3 iteracoes.** Se nao convergir:
- Registrar issues remanescentes em NOTES.md
- Marcar slide como DONE com ressalvas no AUDIT-VISUAL.md
- Mover para proximo slide

---

## 5. Anti-Drift

Regras completas: `.claude/rules/anti-drift.md` (auto-loaded).
Resumo operacional: check a cada 30 min ("mesmo slide?", "avancou estado?"), regra dos 3 commits, contraponto obrigatorio.

---

## 6. Final de Sessao (obrigatorio)

Antes de encerrar, SEMPRE:

1. **Qual slide?** Nome e ID.
2. **Qual estado ficou?** Estado na maquina.
3. **HANDOFF.md** com estado REAL (nao aspiracional).
4. **CHANGELOG.md** se slide mudou de estado.
5. **ERROR-LOG.md** se erro novo encontrado.
6. **NOTES.md** se decisao tomada.

**Teste:** outro agente amanha abre sessao, le HANDOFF.md, e sabe EXATAMENTE:
- Onde retomar
- O que falta
- O que NAO fazer (bloqueios, decisoes travadas)

---

## 7. Tabela de Propagacao

| Mudei... | Atualizar tambem... |
|----------|---------------------|
| h2 no HTML | `_manifest.js` headline, `narrative.md` |
| `<section id>` | TODAS 9 superficies (ver slide-identity.md) |
| CSS do slide | `AUDIT-VISUAL.md` se afeta score |
| Dados numericos | `evidence-db.md`, notes `[DATA]` tag |
| Posicao no deck | `_manifest.js` ordem, `narrative.md` |
| Click-reveals (add/remove) | `_manifest.js` clickReveals, `slide-registry.js` |
| customAnim | `_manifest.js` customAnim, `slide-registry.js` |
| Qualquer coisa no slide | `HANDOFF.md` estado do slide |

**Regra:** se voce editou um slide e NAO atualizou HANDOFF → sessao esta incompleta.

---

## 8. Conteudo que Vende

Antes de fechar CONTENT, o agente DEVE considerar (nao bloquear):

- **Atualizado?** Ultima guideline/trial relevante? Se >2 anos, verificar.
- **Gruda?** Tem numero ancora, regra de bolso, mnemonico?
- **Novo?** Angulo que a audiencia nao ouviu em outras aulas?
- **Expertise-reversal?** Residentes = basico-intermediario. Ir direto ao actionable, sem infantilizar.

Estas sao sugestoes, nao gates. O agente pode registrar em NOTES.md para Lucas decidir.

---

## 9. Tooling Reference

GSAP plugins, contraste, API keys → ver `CLAUDE.md` (aula) secao "Arquivos de trabalho".
Gemini: usar `gemini-3.1-pro` (unico modelo). Playwright: `npm run dev` ativo.

| Doc | Path | Papel |
|-----|------|-------|
| Rubrica 14-dim + scorecard | `.claude/agents/qa-engineer.md` | Template, rubricas por dim |
| Skill QA | `.claude/skills/ralph-qa/SKILL.md` | 2-loop Opus+Gemini |
| Scorecards registrados | `AUDIT-VISUAL.md` | Output por slide |

---

## 10. Estado dos Slides (referencia → HANDOFF.md)

A tabela canonica de estados vive em `HANDOFF.md`, secao "Estado dos Slides".
Este doc define a maquina; HANDOFF registra o estado de cada slide.

---

## Deprecated

> ~~QA-WORKFLOW.md~~ — arquivo removido. O loop de QA e definido por ESTE documento (secao 4).
