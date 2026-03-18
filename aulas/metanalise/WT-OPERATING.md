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

### BACKLOG → DRAFT

- [ ] Arquivo HTML criado em `slides/NN-slug.html`
- [ ] `<section id="s-{slug}">` com ID correto
- [ ] `<div class="slide-inner">` wrapper
- [ ] `<h2>` com assercao (mesmo que provisoria)
- [ ] `<aside class="notes">` com timing placeholder
- [ ] Entrada em `_manifest.js` na posicao correta

### DRAFT → CONTENT

- [ ] h2 = assercao clinica verificavel (nao rotulo generico)
- [ ] Zero `<ul>`/`<ol>` no corpo do slide
- [ ] Todos dados numericos verificados (PMID ou [TBD] em notes)
- [ ] Corpo do slide <= 30 palavras
- [ ] Speaker notes com timing, [DATA] tags, fontes
- [ ] Conteudo atualizado (ultima guideline/trial?)
- [ ] Conteudo que gruda (numero ancora, regra de bolso?)

### CONTENT → SYNCED (critico — 9 superficies)

- [ ] `_manifest.js` headline = `<h2>` do HTML
- [ ] `_manifest.js` clickReveals = numero real de `[data-reveal]`
- [ ] `_manifest.js` customAnim = null ou ID correto
- [ ] `slide-registry.js` tem wiring se customAnim != null
- [ ] `metanalise.css` tem seletores `#slide-id` se necessario
- [ ] `narrative.md` tem linha para este slide na fase correta
- [ ] `evidence-db.md` tem referencias se slide tem dados
- [ ] `AUDIT-VISUAL.md` tem entrada (pode ser placeholder)
- [ ] `HANDOFF.md` registra estado SYNCED

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

**Captura (Playwright):**

```bash
# Dev server deve estar ativo (npm run dev)
# Navegar ate o slide, esperar animacoes (2.5s), screenshot
# Se click-reveals: screenshot antes de cada click

# Output:
# qa-screenshots/{slide-id}/
#   S0.png          ← estado apos entrada (animacoes completadas)
#   S1.png          ← apos click-reveal 1 (se existir)
#   S2.png          ← apos click-reveal 2 (se existir)
#   metrics.json    ← bounding boxes (opcional)
```

Resolucao: 1280x720 @2x (deviceScaleFactor: 2).

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

**Prompt Gemini (avaliacao livre, nao-deterministica):**

```
You are reviewing a single slide for a medical congress presentation
on meta-analysis critical reading.

Audience: medical residents (basic-intermediate), Brazilian congress.
Stack: deck.js, GSAP, OKLCH tokens.
Resolution: 1280x720, Plan C (good projector, light room).

I'm providing:
1. The raw HTML source
2. The CSS that styles this slide
3. Screenshots of each visual state (S0 = after entry, S1+ = after clicks)
4. A video recording of the slide in action (entry animation + interactions)

--- HTML ---
{raw HTML}

--- CSS ---
{relevant CSS}

[Screenshots and video attached]

Assess quality freely. Consider whatever matters:
- Would this look professional projected at a congress?
- Visual hierarchy from 5 meters away?
- Typography for projection (not screen)?
- Does anything look AI-generated rather than human-designed?
- Spacing, alignment, composition?
- Color, contrast, accessibility?
- How do the animations feel? Too fast? Too slow? Distracting?
- Does the progressive disclosure (click-reveals) make sense?
- Anything else you notice?

Be specific and honest. Point to exact elements/CSS properties.
Return JSON:
{
  "overall_impression": "...",
  "issues": [
    { "element": "...", "problem": "...", "suggestion": "...", "severity": "critical|high|medium|low" }
  ],
  "strengths": ["..."],
  "animation_notes": "...",
  "score_estimate": "1-10 overall"
}
```

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

## 5. Anti-Drift (embutido)

### Check a cada 30 minutos

O agente DEVE se perguntar:

1. "Estou no mesmo slide que comecei?"
2. "O slide que comecei ja avancou de estado?"
3. "Quantos slides avancaram nesta sessao?"

Se mudou de slide sem fechar o anterior → **PARAR, voltar, fechar ate SYNCED minimo.**

### Excecoes legitimas

- Bloqueio: precisa de dado do Lucas, PMID nao encontrado, dependencia de outro slide
- Lucas pediu explicitamente para mudar de foco
- Sessao mobile (sem dev server): docs e decisoes sao trabalho valido

### Regra dos 3 commits

Apos 3 commits consecutivos sem arquivo em `aulas/metanalise/slides/` ou `metanalise.css`:
- Pausar e perguntar: "3 commits sem tocar em slides. Continuar ou voltar ao produto?"

### Contraponto obrigatorio

Para toda decisao nao-trivial, o agente DEVE:
1. Apresentar o lado oposto — mesmo que concorde
2. Explicitar trade-offs
3. Dar recomendacao

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

### Playwright (screenshots + video)

```bash
# Dev server deve estar ativo
npm run dev

# Video via Playwright API
# recordVideo: { dir: 'qa-screenshots/{slide-id}/', size: { width: 1280, height: 720 } }
```

### Gemini MCP

Modelos disponiveis (Tier 1):

| Modelo | Uso recomendado |
|--------|-----------------|
| gemini-2.5-flash | Per-slide visual audit (rapido, barato) |
| gemini-2.5-pro | Analise profunda se flash insuficiente |
| gemini-3.1-pro-preview | Deck-level cross-slide (melhor visual reasoning) |

### API Keys

Keys no Windows User env vars. Se sessao nao herdar:
```bash
export GEMINI_API_KEY="$(powershell -Command "[System.Environment]::GetEnvironmentVariable('GEMINI_API_KEY', 'User')")"
```

### Contraste

- Texto primario (headlines, valores): >= 7:1 (AAA)
- Texto secundario (labels, refs): >= 6:1
- Large text hero: >= 4.5:1 (AA large)
- Testar com a11y-contrast MCP ou Playwright in-browser calc

---

## 10. Estado dos Slides (referencia → HANDOFF.md)

A tabela canonica de estados vive em `HANDOFF.md`, secao "Estado dos Slides".
Este doc define a maquina; HANDOFF registra o estado de cada slide.

---

## Deprecated

> **QA-WORKFLOW.md** contem detalhes historicos de tooling (Playwright, Gemini models, API keys, status tracker).
> O loop de QA agora e definido por ESTE documento (secao 4).
> QA-WORKFLOW.md mantido como referencia de tooling e execution logs anteriores.
