---
name: medical-researcher
description: |
  Orquestrador de pesquisa medica de alto nivel — busca multi-MCP (PubMed, Consensus, Scholar Gateway, CrossRef, Scite), avalia profundidade vs superficialidade do conteudo do slide, so usa fontes Tier 1 + autoridades + livros-referencia. Ativar com "pesquisa profunda", "deep research", "avaliar profundidade", "avaliar qualidade do slide", "buscar evidencia avancada", "researcher", "pesquisar a fundo", "quality assessment", "verificar dados do slide".
version: 1.0.0
context: fork
agent: general-purpose
allowed-tools: Read, Grep, Glob, Agent, WebSearch, WebFetch
argument-hint: "[topic OR slide-id] [aula=auto-detect]"
---

# Medical Researcher — Orquestrador Multi-MCP

Pesquisa profunda para: `$ARGUMENTS`

## Filosofia

Superficial = buzzwords sem numeros. Profundo = NNT com IC 95%, populacao, timeframe, citacao verificavel.
Este skill NAO e um buscador simples. E um comite de pesquisa que descobre, triangula, avalia e reporta.
Inspirado no research-agent da Anthropic (fan-out paralelo + consolidacao + report estruturado).

## Step 0 — Contexto

1. **Slide-id fornecido** (ex: `s-a1-damico`) → ler slide HTML + evidence-db da aula
2. **Topico livre** (ex: "hepatorenal syndrome") → pesquisar sem slide de referencia
3. **Detectar aula:** `git branch --show-current` → `feat/{aula}-*` ou exigir argumento
4. Ler `aulas/{aula}/CLAUDE.md` → publico-alvo, fontes Tier-1 especificas da aula
5. Ler `.claude/rules/medical-data.md` → regras de verificacao, tabela Tier-1

## Step 1 — Discovery (4 agentes paralelos)

Lancar 4 Agent em paralelo (subagent_type: general-purpose). Cada um busca de forma independente.
Instrucao compartilhada: "Retorne JSON estruturado. NUNCA invente PMID. Marque incerto como [CANDIDATE]."

### Agent G — Guideline Hunter

**Foco:** Guidelines vigentes (CPG) e consensos de sociedades medicas.
**Fontes primarias:** PubMed MCP (`practice guideline[pt]` OR `consensus development conference[pt]`), WebSearch em sites oficiais de sociedades.
**Sociedades-alvo (por campo):**

| Campo | Sociedades |
|-------|-----------|
| Hepatologia | EASL, AASLD, BAVENO, SBH |
| Cardiologia | ESC, AHA/ACC, SBC |
| Endocrinologia | AACE, ADA, SBEM |
| Gastro geral | AGA, ACG, SBAD |
| Oncologia | ASCO, ESMO, SBOC |

**Extrair por guideline:**
- Sociedade, ano, titulo, DOI/PMID
- Grau de recomendacao + nivel de evidencia (ex: "Strong, Moderate quality")
- Recomendacao especifica relevante ao topico
- Se supersedida: qual versao substituiu
- Mudancas vs versao anterior (se encontrada)

**Output esperado:**
```json
{
  "type": "guidelines",
  "results": [
    {
      "society": "EASL",
      "year": 2024,
      "title": "...",
      "doi": "...",
      "pmid": "...",
      "recommendation": "...",
      "grade": "Strong",
      "evidence_level": "Moderate",
      "supersedes": "EASL 2018",
      "key_changes": ["..."],
      "status": "VERIFIED"
    }
  ]
}
```

### Agent T — Trial Scout

**Foco:** RCTs landmark e recentes (ultimos 5 anos prioritarios).
**Fontes primarias:** PubMed MCP (`randomized controlled trial[pt]`, filtro n>100), Consensus MCP, WebSearch em NEJM/Lancet/JAMA/BMJ.
**Prioridade:** RCT multicentrico > RCT single-center > Quasi-experimental.

**Extrair por trial:**
- Acronimo (ex: PREDESCI, CONFIRM, ANSWER), PMID, DOI
- Design: RCT [multicentrico/single-center], [open-label/double-blind], [superiority/non-inferiority]
- n total (e por braco se disponivel)
- Populacao: criterios inclusao resumidos
- Intervencao vs comparador (droga, dose, regime)
- Primary endpoint + resultado: effect size (HR, RR, OR) com IC 95%
- NNT calculado quando possivel: `NNT = ceil(1/ARR)`, com IC derivado
- p-value
- Follow-up medio
- Mortalidade (se reportada): direcao + magnitude

**Output esperado:**
```json
{
  "type": "trials",
  "results": [
    {
      "acronym": "PREDESCI",
      "pmid": "30910320",
      "doi": "...",
      "journal": "Lancet",
      "year": 2019,
      "design": "RCT, multicenter, double-blind",
      "n": 201,
      "population": "Compensated cirrhosis with CSPH, no prior decompensation",
      "intervention": "Propranolol (titrated to HVPG response) vs placebo",
      "primary_endpoint": "First decompensation or death",
      "effect_size": "HR 0.51",
      "ci_95": "0.26-0.97",
      "nnt": "8",
      "nnt_ci": "4-142",
      "nnt_timeframe": "3 years (median follow-up 37 months)",
      "p_value": "0.041",
      "mortality": "No significant difference",
      "status": "VERIFIED"
    }
  ]
}
```

### Agent M — Meta-Analysis Finder

**Foco:** Meta-analises, revisoes sistematicas, Cochrane reviews.
**Fontes primarias:** PubMed MCP (`meta-analysis[pt]` OR `systematic review[pt]`), Scholar Gateway (semanticSearch), Consensus MCP.
**Prioridade:** Cochrane > Meta-analise com >=5 RCTs > Revisao sistematica qualitativa.

**Extrair por meta-analise:**
- PMID, DOI, titulo, journal, ano
- Tipo: Cochrane / meta-analise de RCTs / network meta-analysis / IPD meta-analysis
- k estudos incluidos, n pacientes total
- Pooled estimate: tipo (RR, OR, HR, MD, SMD) + valor + IC 95%
- Heterogeneidade: I-squared (%), Cochran Q p-value
- Risco de vies: ferramenta usada (Cochrane RoB, Newcastle-Ottawa, GRADE)
- GRADE assessment (se disponivel): certeza da evidencia
- Forest plot: disponivel no artigo? (flag para crop posterior — NUNCA construir SVG)
- Analise de sensibilidade: resultado robusto?

**Output esperado:**
```json
{
  "type": "meta_analyses",
  "results": [
    {
      "pmid": "...",
      "doi": "...",
      "title": "...",
      "journal": "...",
      "year": 2023,
      "type": "Meta-analysis of RCTs",
      "k_studies": 7,
      "n_patients": 1520,
      "pooled_estimate_type": "RR",
      "pooled_estimate": 0.65,
      "ci_95": "0.52-0.81",
      "i_squared": 28,
      "grade_certainty": "Moderate",
      "forest_plot_available": true,
      "sensitivity_robust": true,
      "status": "VERIFIED"
    }
  ]
}
```

### Agent A — Authority Verifier

**Foco:** Livros-referencia, experts, UpToDate, fontes brasileiras.
**Fontes primarias:** WebSearch (editoras medicas, UpToDate), Scholar Gateway (autores-chave).

**Livros-referencia por campo:**

| Campo | Livros canonicos |
|-------|-----------------|
| Hepatologia | Schiff's Diseases of the Liver, Sherlock's Diseases of the Liver, Zakim & Boyer |
| Gastroenterologia | Sleisenger & Fordtran, Yamada Textbook |
| Medicina Interna | Harrison's Principles, Goldman-Cecil |
| Cardiologia | Braunwald's Heart Disease |
| Farmacologia | Goodman & Gilman |

**Extrair:**
- Top 5 autores mais citados no topico (via Scholar Gateway: nome, h-index se disponivel, afiliacao)
- Referencia em livro canonico: edicao, capitulo, paginas, resumo do conteudo relevante
- UpToDate/DynaMed: grau de recomendacao, ultima atualizacao
- Fontes brasileiras especificas: SBC, SBH, SBHPA, protocolos PCDT/CONITEC

**Output esperado:**
```json
{
  "type": "authorities",
  "key_authors": [
    {"name": "Garcia-Tsao G", "h_index": "...", "affiliation": "Yale", "key_papers": 3}
  ],
  "textbooks": [
    {"book": "Schiff's Diseases of the Liver", "edition": "13th, 2024", "chapter": "Portal Hypertension", "pages": "450-490", "summary": "..."}
  ],
  "uptodate": {"recommendation": "...", "grade": "2B", "last_updated": "2025-11"},
  "brazilian_sources": [
    {"source": "PCDT Hepatite C 2024", "recommendation": "...", "url": "..."}
  ]
}
```

## Step 2 — Triangulacao & Verificacao

Apos os 4 agentes retornarem, o orquestrador consolida:

### 2.1 Cross-reference
- Mesmo dado numerico em >=2 fontes independentes → **VERIFIED**
- Dado em apenas 1 fonte → **UNCONFIRMED** (flag amarelo)
- Fontes discordam sobre mesmo dado → **CONFLICT** (flag vermelho, decisao humana)

### 2.2 PMID verification
- TODO PMID retornado deve ser verificado: PubMed MCP `get_article_metadata` ou WebSearch `pubmed.ncbi.nlm.nih.gov/{PMID}`
- PMID que retorna 404 ou artigo diferente → **INVALID** (remover do report)
- Status final: VERIFIED / CANDIDATE / INVALID

### 2.3 Currency check
- Guideline >5 anos sem atualizacao → **AGING** (flag)
- Trial com follow-up <2 anos → **SHORT-FOLLOW-UP** (flag)
- Meta-analise que nao inclui trials dos ultimos 3 anos → **OUTDATED** (flag)

### 2.4 Population match (se slide fornecido)
- Populacao do trial/meta ≠ populacao do slide → **MISMATCH** (flag critico)
  Ex: slide sobre prevencao primaria cita trial de prevencao secundaria
- Prevencao primaria ≠ secundaria (PREDESCI = 1a, pos-HDA = 2a)
- Cirrrose compensada ≠ descompensada
- Child A ≠ Child B ≠ Child C

### 2.5 HR ≠ RR check
- Trial isolado reporta HR → ok
- Meta-analise reporta RR/OR → ok
- Slide mistura HR de trial com RR de meta sem explicitar → **MIXED-METRICS** (flag)

## Step 3 — Avaliacao de Profundidade (se slide fornecido)

Ler o HTML do slide e avaliar em 8 dimensoes (1-10 cada):

| Dim | 1-3 SUPERFICIAL | 4-6 ADEQUADO | 7-10 PROFUNDO |
|-----|-----------------|--------------|---------------|
| **D1 Fonte** | Nenhuma ou "estudos mostram" | Guideline generica (EASL recomenda) | PMID especifico + ano + sociedade |
| **D2 Effect Size** | Ausente ou so p-value | HR/RR sem IC | HR/RR + IC 95% + NNT |
| **D3 Populacao** | "Pacientes com X" | n citado | n + criterios + multicentrico |
| **D4 Timeframe** | Ausente | "Ao longo do tempo" | "Em 5 anos" + follow-up medio |
| **D5 Comparador** | Ausente | "vs controle" | "vs [droga] [dose] [regime]" |
| **D6 Grading** | Ausente | "Recomendado" | GRADE nivel + forca + sociedade |
| **D7 Impacto Clinico** | "Melhora desfechos" | NNT sem CI | NNT (CI 95%) + traducao clinica |
| **D8 Atualidade** | >10 anos ou desconhecido | 5-10 anos, vigente | <5 anos ou guideline vigente |

**Score total:** media das 8 dimensoes.
- 1.0-3.0 → **SUPERFICIAL** (requer reescrita)
- 3.1-5.0 → **ADEQUADO COM GAPS** (melhorar dimensoes <4)
- 5.1-8.0 → **PROFUNDO** (ajustes pontuais)
- 8.1-10.0 → **EXEMPLAR** (manter)

## Step 4 — Relatorio Final

```
## Deep Research Report: [Topico]
Data: [YYYY-MM-DD] | Aula: [aula] | Slide: [id ou N/A]
Perfil MCP: [dev/research/full] | MCPs usados: [lista]

### TL;DR (3 linhas max)
[Achado principal + implicacao clinica + acao sugerida]

### Profundidade do Slide Atual (se aplicavel)
Score: [X.X]/10 — [SUPERFICIAL/ADEQUADO/PROFUNDO/EXEMPLAR]
| Dim | Score | Gap |
|-----|-------|-----|
| D1 Fonte | X | [o que falta] |
| ... | ... | ... |

### Guidelines Vigentes
1. **[Sociedade] [Ano]** — [Recomendacao] (Grau [X], Evidencia [Y])
   PMID: [verificado] | DOI: [link]
   Status: [Vigente/Supersedida por Z]
   Mudancas vs anterior: [lista]

### Trials Landmark
1. **[ACRONIMO]** (Autor et al., Journal Ano)
   PMID: [verificado] | n=[X] | [design]
   Populacao: [descricao] — [MATCH/MISMATCH com slide]
   Resultado: [effect size] (95% CI: [a]-[b]) | NNT: [Z] (CI: [c]-[d]) em [tempo]

### Meta-Analises
1. **[Titulo abreviado]** (Autor et al., Journal Ano)
   PMID: [verificado] | k=[N] estudos, n=[X] pacientes
   Pooled: [estimate] (95% CI: [a]-[b]) | I2=[Y]%
   GRADE: [certeza] | Forest plot: [sim/nao]

### Autoridades
- **Livro:** [Titulo] [edicao] — Cap. [X], p.[Y]
- **Expert:** [Nome] ([afiliacao]) — [N] publicacoes, h-index [Y]
- **UpToDate:** [recomendacao] (Grade [X], atualizado [data])
- **Brasil:** [fonte] — [recomendacao]

### Flags de Verificacao
- VERIFIED: [dado] confirmado por [N] fontes
- CONFLICT: [dado] — [Fonte A] diz X, [Fonte B] diz Y → decisao humana
- MISMATCH: Slide cita [pop A], trial estudou [pop B]
- AGING: [fonte] com [N] anos
- MIXED-METRICS: HR e RR misturados sem explicitar
- CANDIDATE: PMID [X] nao verificado

### Sugestoes de Melhoria (se slide fornecido)
1. **h2 sugerido:** "[Assertion atualizada com dado mais forte]"
2. **Adicionar:** [effect size com CI]
3. **Atualizar fonte:** [guideline X → Y]
4. **Corrigir populacao:** [especificar]
5. **NNT completo:** NNT [X] (IC 95%: [a]-[b]) em [tempo] | [populacao]

### Bloco evidence-db (pronto para copiar)
## [slide-id]
- **Source:** [Autor et al. Journal Ano;Vol:Pags]
- **PMID:** [X] | **DOI:** [Y]
- **Design:** [tipo] | **n:** [X]
- **Primary endpoint:** [descricao]
- **Result:** [effect size] (95% CI: [a]-[b])
- **NNT:** [X] (CI: [a]-[b]) em [tempo]
- **GRADE:** [certeza]
- **Verified:** [YYYY-MM-DD]
```

## Regras

### Hard constraints (do projeto — inviolaveis)
- NUNCA inventar dados — sem fonte verificada → `[TBD]`
- NUNCA usar PMID gerado por LLM sem verificacao via PubMed MCP ou WebSearch
- HR ≠ RR ≠ OR — especificar sempre qual metrica e de onde vem
- Trial isolado ≠ meta-analise — NUNCA misturar sem explicitar
- Pais-alvo = Brasil (default). Remover drogas nao disponiveis no BR.
- NNT DEVE ter IC 95% e timeframe. Sem isso → INCOMPLETO.

### Quality gates
- Toda citacao deve ter PMID ou DOI verificado antes de entrar no report
- Guideline deve ser versao vigente (checar se supersedida)
- Score de profundidade: TODAS as 8 dimensoes >=4 para ADEQUADO
- Se slide fornecido e score <3 em qualquer dimensao → FAIL obrigatorio naquela dimensao

### Hierarquia de fontes (prioridade decrescente)
1. Guidelines vigentes de sociedades medicas (EASL, AASLD, BAVENO, SBC, ESC, AGA, ACG)
2. Meta-analises Cochrane ou com >=5 RCTs
3. RCTs multicentricos >=200 pacientes
4. Livros-referencia do campo (edicao mais recente)
5. Expert consensus / Delphi
6. Series de caso grandes (n>500) — APENAS quando nao ha acima
7. Expert opinion individual — NUNCA como fonte primaria de dado numerico

### MCP awareness (degradacao graciosa)
Os agentes devem tentar MCPs na seguinte ordem e usar o que estiver disponivel:

| Prioridade | MCP | Tool prefix | Fallback |
|-----------|-----|-------------|----------|
| 1 | PubMed (claude.ai) | `mcp__claude_ai_PubMed__` | WebSearch pubmed.ncbi.nlm.nih.gov |
| 2 | Consensus (claude.ai) | `mcp__claude_ai_Consensus__` | WebSearch consensus.app |
| 3 | Scholar Gateway (claude.ai) | `mcp__claude_ai_Scholar_Gateway__` | WebSearch scholar.google.com |
| 4 | CrossRef (local) | `mcp__crossref__` | WebSearch doi.org |
| 5 | Scite (local) | `mcp__scite__` | Omitir analise de citacoes |
| 6 | ClinicalTrials (local) | `mcp__clinicaltrials__` | WebSearch clinicaltrials.gov |
| 7 | BioMCP (local) | `mcp__biomcp__` | WebSearch openFDA |

Se nenhum MCP academico disponivel → WebSearch como unica fonte. Reportar no cabecalho.

### Anti-patterns (rejeitar no report)
- "Estudos mostram que..." → Qual estudo? PMID?
- p < 0.05 sem effect size → Significancia ≠ relevancia clinica
- Guideline sem grau de recomendacao → INCOMPLETO
- NNT sem timeframe → INCOMPLETO
- Dados de trial aplicados a populacao diferente → FLAG MISMATCH
- Forest plot construido do zero → PROIBIDO (cropar de artigo real)
- Numero "redondo demais" sem fonte → provavelmente inventado

## Evolucao futura

Este skill pode evoluir para um custom agent (`.claude/agents/medical-researcher.md`) com:
- `mcpServers` scoped (pubmed, crossref, scholar, scite)
- `memory: project` (aprendizado persistente sobre fontes e padroes)
- `hooks` de validacao pre-tool (bloquear PMIDs nao verificados)
- Subagents dedicados: `guideline-hunter.md`, `trial-scout.md`, `meta-analyst.md`, `authority-verifier.md`

Por ora, o pattern skill + Agent tool e suficiente e consistente com o ecossistema do projeto.
