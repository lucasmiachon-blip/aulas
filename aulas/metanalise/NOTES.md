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
- O que muda: criterios visuais elevados + GSAP sofisticado + prompt Gemini v6.0
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

### Prompt Gemini v6.0 (docs/prompts/gemini-slide-qa.md)
- Substitui v3.0. 10 dimensoes, 5 personas, 10 lenses, radical ideas forcing, projected scorecard, temp 1.0.
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

### Gate 3 + QA.4 (mesma sessão)
- 6 screenshots Playwright (3 beats × 2 resoluções)
- Contrast table: todos beat 0/1 >= 9.05:1 AAA. Source-tag 5.32:1 AA (known).
- **Bug encontrado:** verdict usava `var(--text-on-dark)` que stage-c remapeia para oklch(12%) — dark text on dark-red bg = 3.67:1. Fix: explicit `oklch(95%)` + darker red `oklch(38% 0.17 25)` = 7.78:1 AAA.
- **Bug encontrado:** SplitText `type: 'chars'` criava spans individuais por char — browser fazia word-break mid-word "paci/entes". Fix: `type: 'words,chars'` + `&nbsp;` no HTML.
- Regra aprendida: **qualquer elemento com bg próprio escuro em slide light DEVE usar cor explícita, não var(--text-on-dark)** — stage-c remap não distingue "slide escuro" de "elemento escuro em slide claro".
- 14-dim scorecard: avg 8.6/10. Lucas aprovou resultado: "melhorou muito".

## 2026-03-19 — Governance hardening round 2

### Scope
- MEMORY.md: 5 fixes (orphan ref, missing entry, branch state, descriptions)
- .gitignore: +`.claude/agent-memory/` (HANDOFF pendencia resolvida)
- HANDOFF.md: "s-contrato (Gemini pendente)" → DONE
- CLAUDE.md (aula): scorecards status atualizado (F1 DONE)
- blueprint.md: s-hook assertion atualizada (VITALITY→sober), s-contrato status DONE, version bump v1.9
- lessons.md: +3 licoes (stage-c remap, SplitText word-break, tom sober)
- feedback_metanalise_narrative_order.md: ancora atualizada (Musini→Valgimigli)
- feedback_gemini_model.md: criado (file missing, so index)

### Gemini model discrepancy
- WT-OPERATING.md §9 diz "gemini-3.1-pro" (unico modelo)
- AUDIT-VISUAL.md registra "gemini-2.5-pro" nas chamadas reais
- Possivel causa: MCP @fre4x/gemini usa model default != especificado
- **Acao:** verificar configuracao do MCP na proxima chamada Gemini. Registros historicos em AUDIT-VISUAL NAO devem ser alterados.

### Pendencias PMID
- Siedler 2025 (33.8% GRADE, EM USO hook card 3): PMID pendente
- Higgins & Lopez-Lopez 2025 (I² creator): PMID pendente
- Ambos aguardam verificacao por reference-manager agent

## 2026-03-19 — Batch 1 doc hardening: pendencias factuais

### PMIDs verificados
- **Siedler 2025:** PMID **40969451** verificado via PubMed MCP + Crossref. Journal correto: *Cochrane Evid Synth Methods* 2025;3(2). DOI: 10.1002/cesm.70014.
  - **CORREÇÃO DE DADOS:** 33,8% = proporção de SRs que *avaliaram* certeza da evidência (89,3% destas via GRADE). NÃO é "% com certeza moderada/alta". Framing corrigido em blueprint.md e evidence-db.md. HTML do slide já tinha framing correto ("avaliaram certeza da evidência").
- **Higgins & Lopez-Lopez 2025:** DOI **10.1017/rsm.2025.10062** verificado via Crossref. Epub ahead of print (Dec 29, 2025). PMID **não indexado** — re-checar abr/2026. Autores confirmados (Julian PT Higgins = criador do I²).

### Gemini model discrepancy resolvida
- Prompt v6.0 dizia `gemini-3.1-pro` como modelo único. AUDIT-VISUAL registrava chamadas com `gemini-2.5-pro`.
- Causa: MCP `@fre4x/gemini` usa model default que pode diferir do especificado no prompt.
- Resolução: docs atualizados para recomendar especificar modelo explicitamente. Registros históricos preservados (refletem modelo real usado).
- Arquivos atualizados: WT-OPERATING.md §9, docs/prompts/gemini-slide-qa.md.

---

## 2026-03-19 — s-hook REWRITE (sober tone)

### Decisao Lucas
- Rejeitou tom alarmista/escandaloso: "1.330 retratados", "guidelines contaminadas", UTI, verdict vermelho.
- Novo framing: "Finding a SR is no longer the problem. Knowing which one to trust is." Sóbrio, clínico.
- h2 longo removido → curto "Por que isso importa". Section-tag redundante removido.
- Takeaway (frase editorial) removido do corpo → speaker notes.

### Impacto tecnico
- State machine (115 linhas JS) removida inteiramente. ScrambleText/SplitText nao mais usados.
- SplitText import removido de slide-registry.js (nenhum entry restante usa).
- CSS: -132 linhas (grid Z-pattern, beats, hero, verdict, fallbacks) / +30 linhas (metric cards).
- Archetype: hook → cards. clickReveals: 2 → 0. customAnim: 's-hook' → null.
- Scorecard anterior INVALIDADO. QA.0 pendente.

### Plugins GSAP
- SplitText, Flip, ScrambleTextPlugin permanecem REGISTRADOS em index.template.html (disponiveis para slides futuros).
- Atualmente usados: nenhum (s-title usa gsap.fromTo direto, nao SplitText).

## 2026-03-19 — Governance hardening R3: Notion sync + PMID audit

### Notion Slides DB sync (18/18)
- 5 novas opcoes Bloco Narrativo adicionadas via DDL: MA-F1, MA-I1, MA-F2, MA-I2, MA-F3
- Aula (relation) atualizada em todos os 18 slides → page `30adfe6859a881d2b1f6c81c59e3e12d`
- 2 duplicatas marcadas [DEP]: MA-F2-RSVSMA (`325dfe68...8cb6`), segundo MA-F2-BENHARM (`325dfe68...966e`)
- Pipeline Status atualizado: 3 QA-DONE (F1), 15 LINT-PASS

### PMID audit (reference-manager agent, 36 PMIDs)
- **28 OK**, 2 corrigidos, 1 DOI corrigido, 2 sem PMID (Siedler PMID ja verificado separadamente, Higgins epub), 1 flag dados (Qureshi 10% — verificar)
- **Guyatt BMJ 2008 GRADE:** PMID 21195583 → **18436948** (21195583 = GRADE Guidelines 2011, artigo diferente)
- **Murad JAMA 2014:** PMID 25005654 marcado **[VERIFY]** (resolve para "Users' Guides", nao "Rating certainty". PMID correto desconhecido)
- **Brignardello-Petersen DOI:** kwae256 → **kwae332**
- evidence-db.md atualizado para v5.4

### HANDOFF pendencias verificadas
- 3/5 eram falsas (qa-engineer.md, ralph-qa/SKILL.md, XREF.md — todos ja corretos)
- 2 reais confirmadas: lint-slides.js:110 (fix preparado para main), 4 scripts orphans (git rm preparado)

### Main-scope fixes preparados (NAO executar na WT)
- lint-slides.js:110: context-aware check (±3 linhas) elimina false positive em HTML built
- 4 orphan scripts: `git rm` confirmado pelo repo-janitor

### Gemini CLI migration (2026-03-20)
- Cloud MCP (@fre4x/gemini) substituido por CLI headless (scripts/gemini.mjs)
- qa-video.js adaptado para deck.js (--aula=metanalise)
- .audit/ criado para outputs JSON
- Zero refs MCP Gemini em .mcp.json ou profiles
- Registros historicos AUDIT-VISUAL preservados (gemini-2.5-pro = modelo real usado)

[2026-03-20 15:52] [medical-researcher:a4aec9e2] — concluído. Status: PASS

[2026-03-20 18:15] [medical-researcher:a5910edf] — concluído. Status: PASS

[2026-03-20 18:38] [BUILD] OK — npm run build:metanalise 2>&1

[2026-03-20 19:30] [unknown:a6fc834c] — concluído. Status: PARTIAL

[2026-03-20 19:52] [unknown:a1066330] — concluído. Status: PARTIAL

[2026-03-20 19:54] [medical-researcher:ae342915] — concluído. Status: PASS

## 2026-03-20 — s-checkpoint-1 ACCORD rewrite + arguição prep

### Decisões de conteúdo (Lucas aprovou)
- ACCORD como armadilha pedagógica: dados REAIS (Ray 2009 + ACCORD 2008), não ilustrativos
- Visual "liquidificador": diamante dissolve → trials aparecem → ACCORD em vermelho
- Escolha do ACCORD sobre CAST/Vioxx/rosiglitazona: custo cognitivo zero (todo residente conhece), estrutura perfeita ("dano dentro do diamante"), endocrinologia mas transcende especialidade

### Research deep dive — controle glicêmico intensivo
- **Achado principal:** NENHUMA MA de controle glicêmico (2009-2024) fez GRADE formal
  - Ray 2009: nenhum
  - Boussageon 2011: Jadad only
  - Hemmingsen 2013 Cochrane: TSA, sem SoF GRADE
  - Kunutsor 2024: não reportado
- Isso valida diretamente slides 09 (GRADE) e 14 (lacuna GRADE Valgimigli)
- Boussageon 2011 = crítica mais forte: NNT 117-150 vs NNH 15-52
- Scite tallies: 889 citações, 23 supporting, 5 contrasting (identidade das 5 requer auth)

### Arguição — material preparado
- Tese/antítese/síntese: confiança no diamante → ACCORD como crise → método como resposta
- 6 perguntas prováveis com respostas (desfechos diferentes, simplificação, por que não outro caso, visual simplificado, OR vs HR, dados reais vs googling)
- Ancoragem em Knowles (andragogia), Kahneman (anchoring/disponibilidade), Roediger (testing effect), Mayer (contiguidade), Kalyuga (expertise reversal)

### MCP setup
- Perplexity: configurado, API key não setada no ambiente. Perplexity Max ≠ API credits (verificar se plano inclui $5/mês grátis)
- Scite: adicionado ao `.mcp.json` (streamableHttp). OAuth via conta premium. Reiniciar Claude Code para ativar.
- Tallies endpoint funciona sem auth (usado para pegar contagem 889/23/5/806)

### Backlog MAs reais (NÃO implementar agora — plano aprovado)
- s-grade: Pitre 2023 (PMID 37076606) — corticoides PAC, GRADE diferente por subgrupo
- s-heterogeneity: antidepressivos para dor — PMID TBD
- Publication bias: Turner 2008 (PMID 18199864) — SSRIs, menção em notes
- Exemplares GRADE recentes: Lin 2025 (PMID 41147324, CINeMA NMA), Ghosal 2025 (PMID 41201574, formal SoF)

[2026-03-20 20:15] [BUILD] OK — npm run build:metanalise

[2026-03-20 20:18] [Explore:abe2c0bb] — concluído. Status: PARTIAL

[2026-03-20 21:28] [Explore:aec65f5c] — concluído. Status: PARTIAL

[2026-03-20 21:32] [Explore:a327ccbf] — concluído. Status: PASS

[2026-03-20 21:33] [Explore:a364f15c] — concluído. Status: PARTIAL

[2026-03-20 21:37] [Plan:a6a5734e] — concluído. Status: PASS

[2026-03-21 14:35] [general-purpose:a65ae895] — concluído. Status: PARTIAL

## 2026-03-21 — Sessão MCP research (ACCORD + Valgimigli enrichment)

### MCPs testados e configurados
- **Scite:** OAuth via `/mcp`. Premium. DOIs devem ser lowercase (mixed-case retorna 0).
- **Perplexity:** API key (stdio). Funcionando (search, ask, research, reason).
- **Consensus:** OAuth via `/mcp`. 200M+ papers.
- PubMed e Scholar Gateway: já funcionavam.

### Queries executadas
- Scite: ACCORD (DOI lowercase) → 7.335 citing, 2.399 smart, 64 supporting, 15 contrasting
- Scite: Ray 2009 → 1.318 citing, 889 smart, 23 supporting, 5 contrasting
- Scite: Valgimigli → não indexado (ago 2025)
- Perplexity: ACCORD mechanisms, A1C paradox, VADT comparison
- Consensus: Valgimigli 2025 (5 citações), Giacoppo BMJ 2025 (confirmação)

### Artefatos criados/atualizados
1. **`references/research-accord-valgimigli.md`** — briefing narrativo completo (Partes 1-3) + PDFs para NotebookLM
2. **`references/evidence-db.md`** v5.6 — Scite tallies, NNH 95, paradoxo A1C, follow-ups, 7 RCTs, CYP2C19, authors' reply, Giacoppo
3. **`slides/03-checkpoint-1.html`** — notes enriquecidas com contexto ACCORD para arguição
4. **`slides/13-ancora.html`** — notes com 7 RCTs nomeados, Scite status, Giacoppo
5. **`slides/14-aplicacao.html`** — notes com NICE gap, custo, lacuna GRADE
6. **`slides/15-aplicabilidade.html`** — notes com CYP2C19 e generalização geográfica

### Memories salvos
- `reference_scite_dois.md` — DOIs lowercase para Scite
- `feedback_research_narrative_form.md` — pesquisa como narrativa detalhada + download URLs

### Slides avançados: 0 (sessão de pesquisa/enriquecimento — suporte legítimo para QA)

### Notion sync 2026-03-21 (executado em sessão seguinte)
- **Slides DB:** 4 pages atualizadas (Speaker Notes EN): s-checkpoint-1, s-ancora, s-aplicacao, s-aplicabilidade
- **References DB:** 9 papers criados (todos verificados via PubMed MCP):
  - ACCORD 2008 (18539917), Ray 2009 (19465231), ACCORD 5yr (21366473), ACCORD 9yr (26822326), VADT 15yr (31167051), Riddle 2010 (20427682), Bonds 2010 (20061358), Giacoppo BMJ 2025 (40467090), Valgimigli reply (41763741)
- **5 PMIDs corrigidos** (LLM havia gerado errados na sessão anterior):
  - ACCORD 5yr: 21067804→21366473 (era CTT LDL cholesterol)
  - VADT 15yr: 31314966→31167051 (era HIV testing study)
  - Riddle 2010: 20103978→20427682 (era squalene fractionation)
  - Bonds 2010: 20044403→20061358 (era Varenicline/suicide)
  - Giacoppo BMJ: 41649579→40467090 (era Elbahloul Eur J Clin Pharmacol). Pts: 162.829→16.117
- Arquivos corrigidos: evidence-db.md, research-accord-valgimigli.md, 13-ancora.html, CHANGELOG.md
- evidence-db bump: v5.6→v5.7 (PMID corrections)

## 2026-03-21 — Sessão evolve + prep

### Evolve patches (aplicados em main)
- P1+P2: XREF.md — 2 hooks faltantes (teammate-idle-gate, task-completed-gate) + fix audit-trail matcher
- P6: lessons.md — warning Vite 8 (Rolldown, breaking changes)
- P3 RETIRADO: run-pubmed-mcp.js não é orphan (refs em .cursor/mcp.json + MCP-ENV-VARS.md)

### Prep para próxima sessão
- Perplexity API key configurada
- Scite OAuth configurado
- Buscas Scite (ACCORD, Valgimigli, Ray) deferidas — não bloqueiam QA visual

[2026-03-21 15:38] [medical-researcher:a4382197] — concluído. Status: PARTIAL

[2026-03-21 15:38] [medical-researcher:a822e95b] — concluído. Status: PASS

[2026-03-21 15:41] [medical-researcher:a8f9ef71] — concluído. Status: PASS

[2026-03-21 17:16] [unknown:ad22a6cc] — concluído. Status: PASS

[2026-03-21 17:24] [BUILD] OK — npm run build:metanalise 2>&1

[2026-03-21 17:39] [BUILD] OK — npm run build:metanalise 2>&1

[2026-03-21 17:43] [Explore:a83686d9] — concluído. Status: PASS

[2026-03-21 17:49] [unknown:a037d69e] — concluído. Status: PARTIAL

[2026-03-21 18:01] [unknown:a69ad7d9] — concluído. Status: PASS

[2026-03-21 18:02] [BUILD] OK — npm run build:metanalise
