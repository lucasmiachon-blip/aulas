# Evidence DB — Meta-análise

> Dados quantitativos reais. Sem fonte tier 1 → [TBD].
> Lacunas de acesso declaradas explicitamente.

---

## Exemplo visual (Fases 1-2) — Musini et al. 2025

> Musini era candidato a âncora. Decisão final: **Valgimigli 2025 (Lancet)** é o artigo âncora (Fase 3).
> Musini fica como exemplo visual para forest plot e GRADE SoF table (quando full-text disponível).

### Identificação

| Campo | Valor |
|-------|-------|
| Autores | Musini VM, Tejani AM, Bassett K, Puil L, Thompson W, Wright JM |
| Título | Pharmacotherapy for hypertension in adults 60 years or older |
| Fonte | Cochrane Database Syst Rev. 2025 Oct 9;10(10):CD000028 |
| DOI | 10.1002/14651858.CD000028.pub4 |
| PMID | 41065416 ✅ |
| Publicação | 9 outubro 2025 |
| Tier | **1** (Cochrane) |
| Acesso | Abstract aberto. Full-text: acessível via Cochrane Library (acordo nacional CAPES/Wiley). PMC embargo até 2026-10-09 |

### Método

| Campo | Valor |
|-------|-------|
| Desenho | RS com MA de RCTs (pairwise) |
| Busca até | Junho 2024 |
| Bases | CENTRAL, MEDLINE, Embase, ICTRP, ClinicalTrials.gov |
| Elegibilidade | RCTs ≥1 ano, anti-HTN vs placebo/nada, ≥60 anos, PA >140/90 |
| RoB | Cochrane RoB 1, dois revisores |
| Modelo | Efeito fixo |
| Medida | RR com IC 95% |

### Amostra

| Campo | Valor |
|-------|-------|
| Estudos incluídos | 16 RCTs |
| Participantes | 26.795 |
| Contexto | Ambulatorial |
| Idade média | 73,8 anos |
| Tempo médio tx | 3,8 anos |
| PA média basal | 182/95 mmHg |

### Resultados — Desfechos primários

| Desfecho | RR | IC 95% | Certeza GRADE |
|----------|-----|--------|---------------|
| Mortalidade total | 0,91 | 0,85–0,97 | **Alta** |
| Morbimortalidade CV | 0,72 | 0,68–0,77 | Moderada |
| Eventos cerebrovasculares | 0,66 | 0,59–0,74 | Moderada |
| Eventos coronarianos | 0,78 | 0,69–0,88 | Moderada |
| Retirada por EA | 2,91 | 2,56–3,30 | Baixa |

### Notas para a aula

- PA média 182/95 → população com HAS moderada a grave; validade externa para HAS leve é questionável
- Maioria dos estudos avaliou tiazídico como 1ª linha → discussão de aplicabilidade contemporânea
- Certeza alta apenas para mortalidade total; moderada para CV; baixa para dano → ensino de GRADE por desfecho
- Cochrane classifica como **stable review** → gancho sobre ciclo de vida de RS

### Lacunas declaradas

- [ ] NNT / efeito absoluto: não calculável sem baseline risk do controle (necessário full-text)
- [ ] Forest plot: não disponível sem full-text ou PDF
- [ ] Análise de subgrupo: mencionada no abstract mas sem dados detalhados
- [ ] Detalhes de I² / tau²: não reportados no abstract

---

## Referências de apoio — por função

### Estrutura e relato

| Referência | Tier | Função na aula | Acesso |
|-----------|------|----------------|--------|
| PRISMA 2020 Statement (Page et al. BMJ 2021) | 1 | Transparência de relato | Aberto |
| PRISMA 2020 for Abstracts | 1 | Checklist de abstract (12 itens) — pre-reading | Aberto |

### Método — Cochrane Handbook

| Capítulo | Função na aula | Quem lê |
|----------|----------------|---------|
| Cap. 1 — definições | RS vs MA | Professor |
| Cap. 10 — Analysing data | Forest plot, pooling, fixed/random, I², Q, tau² | Professor (must), Residente (good to read) |
| Cap. 14 — SoF / GRADE | Certeza da evidência | Professor (must), Residente (introdução) |
| Cap. 15 — Interpreting results | Efeito absoluto, baseline risk, validade externa | Professor (must) |

### Didática de leitura

| Referência | Tier | Função | Acesso |
|-----------|------|--------|--------|
| Sedgwick P. BMJ 2015;351:h4028 — How to read a forest plot | 1 | Desmistificar forest plot — pre-reading | Aberto (BMJ educacional) |
| JAMA Users' Guides — how to use a systematic review | 1 | Ponte técnica → decisão clínica | Acesso institucional |

### Avaliação crítica (bastidor do professor)

| Referência | Tier | Função | Acesso |
|-----------|------|--------|--------|
| AMSTAR 2 (Shea et al. BMJ 2017) | 1 | Auditoria de qualidade da RS — NÃO é pre-reading | Aberto |
| RoB 2 (Sterne et al. BMJ 2019) | 1 | Linguagem correta para risco de viés | Aberto |

---

## Hook — Importância e crise de qualidade de SR/MA

### Volume epidêmico de publicações

| Dado | Valor | Fonte | PMID | DOI | Tier |
|------|-------|-------|------|-----|------|
| SRs publicadas por dia (2019) | **~80/dia** | Hoffmann et al. J Clin Epidemiol 2021;138:1-11 | 34091022 | 10.1016/j.jclinepi.2021.05.022 | 1 | ✅ **EM USO no hook card 1** |
| Aumento de SRs indexadas (2000→2019) | 1.432 → 29.073 (**20x**) | Hoffmann et al. 2021 | 34091022 | idem | 1 |
| Crescimento de SRs (1991→2014) | **+2.728%** (vs +153% total PubMed) | Ioannidis. Milbank Q 2016;94(3):485-514 | 27620683 | 10.1111/1468-0009.12210 | 1 |
| SRs/MAs indexadas em 2017 | 22.774 (48x vs 1995) | Niforatos et al. JAMA Intern Med 2019;179(11):1593-4 | 31355871 | 10.1001/jamainternmed.2019.3013 | 1 |
| SRs + RCTs por dia (2010) | 75 RCTs + 11 SRs/dia | Bastian et al. PLoS Med 2010;7(9):e1000326 | 20877712 | 10.1371/journal.pmed.1000326 | 1 |

### Qualidade criticamente baixa

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| SRs em câncer com qualidade criticamente baixa (AMSTAR-2) | **88,1%** (230/261) | Siemens et al. J Clin Epidemiol 2021;136:84-95 | 33741503 | 10.1016/j.jclinepi.2021.03.010 | 1 | ⚠ Específico de câncer avançado — não usar como dado geral |
| SRs que declaram AMSTAR-2: criticamente baixas (cross-field) | **81%** (35/43) | Bojcic et al. J Clin Epidemiol 2024;165:111210 | 37931822 ✅ | 10.1016/j.jclinepi.2023.10.026 | 1 | ✅ **EM USO no hook card 2** — cross-field, não específico de área |
| "A grande maioria é desnecessária, enganosa ou conflitada" | — | Ioannidis 2016 | 27620683 | idem | 1 | |
| MAs redundantes sobre antidepressivos (2007-2014) | **185** sobre o mesmo tema | Ioannidis 2016 | 27620683 | idem | 1 | |

### GRADE gap em MAs

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| SRs que avaliaram certeza da evidência | **33,8%** (346/1.023) | Siedler MR et al. Cochrane Evid Synth Methods 2025;3(2) | 40969451 ✅ | 10.1002/cesm.70014 | 1 | ✅ **EM USO no hook card 3** — 33,8% = SRs que AVALIARAM certeza (89,3% via GRADE). Dois terços omitem avaliação. 10 revistas alto impacto, Jan 2013–Jan 2024 |

### Guidelines e evidência de nível A

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Recomendações ACC/AHA com LoE A (=SR/MA) | **8,5%** (248/2930) | Fanaroff et al. JAMA 2019;321(11):1069-80 | 30874755 | 10.1001/jama.2019.1122 | 1 | Específico ACC/AHA cardiologia |
| Recomendações ESC com LoE A | **14,2%** (484/3399) | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações ESC com LoE C (opinião de expert) | **54,8%** | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações com evidência forte (LoE A equiv.) — cross-society | **10%** (768/7.582) | Qureshi et al. JGIM 2025 [online 22 dez] | 41428154 ✅ | 10.1007/s11606-025-10088-6 | 1 | ✅ **EM USO no hook** (substituiu Fanaroff 8,5%) — 23 sociedades EUA, 2019-2023, cross-specialty |
| Guidelines que usam métodos sistemáticos | **34%** (17/50) | Lunny et al. PLoS ONE 2021;16(4):e0250356 | 33886670 | 10.1371/journal.pone.0250356 | 1 | |

### Competência dos médicos

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Residentes: acerto em bioestatística | **41,4%** (IC 95%: 39,7–43,3%) | Windish DM et al. JAMA 2007;298(9):1010-22 | 17785646 ✅ | 10.1001/jama.298.9.1010 | 1 | ✅ **EM USO no hook** (swap 146→41%). n=277 residentes clín. médica, 11 programas |
| Residentes que acham importante saber bioestat | **95%** | Windish et al. 2007 | 17785646 ✅ | idem | 1 | vs 75% admitem não entender tudo |
| Residentes que interpretam Kaplan-Meier corretamente | **10,5%** | Windish et al. 2007 | 17785646 ✅ | idem | 1 | RR: 81,6% acertam. OR ajustado: 37,4% |
| Clínicos: baixa proficiência + alta confiança (n=898) | Ilusão de competência | Lakhlifi et al. Cogn Res Princ Implic 2023;8:23 | 37081292 | 10.1186/s41235-023-00474-1 | 1 | EM USO no hook (verdict) |
| Overconfidence → erros diagnósticos/terapêuticos | **36,5–77%** dos cenários | Saposnik G et al. BMC Med Inform Decis Mak 2016;16:138 | 27809908 ✅ | 10.1186/s12911-016-0377-1 | 2 | n=6.810 médicos, 20 estudos, 19 vieses cognitivos. 71,4% estudos: vieses → erros terapêuticos |
| Competências EBP mínimas (5-step model) | Consenso internacional | Sicily Statement. Dawes et al. BMC Med Educ 2005;5:1 | 15634359 | 10.1186/1472-6920-5-1 | 1 | |

### Integridade e confiabilidade de RCTs em SRs

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| RCTs com problemas de confiabilidade em Cochrane reviews | **25%** (24/95 RCTs em 50 SRs) | Wilkinson J et al. (INSPECT-SR). J Clin Epidemiol 2025;184:111824 | 40349737 ✅ | 10.1016/j.jclinepi.2025.111824 | 1 | ✅ **EM USO no hook notes**. 6% sérios. 22% MAs ficam com zero estudos após exclusão. RoB e GRADE não detectam |
| GRADE assume dados confiáveis | "Revisores devem verificar integridade dos estudos" | Brignardello-Petersen R, Guyatt GH. Am J Epidemiol 2025;194(6):1681-6 | 39218429 ✅ | 10.1093/aje/kwae332 | 1 | ✅ **EM USO no hook notes**. Guyatt (criador do GRADE) reconhece limitação |
| SRs observacionais usando dados brutos | **80,9%** | Paul J et al. J Clin Epidemiol 2025;181:111702 | 40414366 ✅ | 10.1016/j.jclinepi.2025.111702 | 1 | 500 SRs 2022. Risco de confusão residual não tratado |
| Problemas com SRs catalogados | **68 problemas** em 637 artigos | Uttley L et al. J Clin Epidemiol 2025;177:111575 | 39542225 ✅ | 10.1016/j.jclinepi.2024.111575 | 1 | Scoping review. Categorias: report, conduct, relevance, waste |

### Exemplo MA: controle glicêmico intensivo em UTI

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| MA pré-NICE-SUGAR: mortalidade | RR 0,93 (IC 0,85–1,03); hipoglicemia RR 5,13 | Wiener RS et al. JAMA 2008;300(8):933-44 | 18728267 ✅ | 10.1001/jama.300.8.933 | 1 | REMOVIDO do slide (rewrite sober). 29 RCTs, 8.432 pts. Ref para notes/futuro |
| NICE-SUGAR trial (reversão) | OR mortalidade 1,14 (IC 1,02–1,28) | NICE-SUGAR Study Investigators. NEJM 2009;360(13):1283-97 | 19318384 ✅ | 10.1056/NEJMoa0810625 | 1 | REMOVIDO do slide (rewrite sober). n=6.104, 42 centros. Ref para notes/futuro |
| MA pós-NICE-SUGAR: confirmação | RR 0,93 (IC 0,83–1,04); hipoglicemia RR 6,0 | Griesdale DEG et al. CMAJ 2009;180(8):821-7 | 19318387 ✅ | 10.1503/cmaj.091206 | 1 | REMOVIDO do slide (rewrite sober). 26 trials, 13.567 pts. Ref para notes/futuro |

### Pirâmide de evidência e hierarquia

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Nova pirâmide de evidência | Confiança no body of evidence, não hierarquia rígida | Murad MH et al. Evid Based Med 2016;21(4):125-7 | 27339128 ✅ | 10.1136/ebmed-2016-110401 | 1 | Redefine MA como "lupa, não oráculo" |

### MAs contraditas, retratadas e reversões médicas

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Trials retratados → MAs mudaram direção | **8,4%** (IC 95%: 6,8–10,1%) | Xu C et al. (VITALITY). BMJ 2025;389:e082068 | 40268307 ✅ | 10.1136/bmj-2024-082068 | 1 | REMOVIDO do slide (rewrite sober). Mantido como ref para notes/futuro |
| Trials retratados → MAs mudaram significância | **16,0%** (IC 95%: 14,2–17,9%) | Xu et al. (VITALITY) 2025 | 40268307 ✅ | idem | 1 | |
| Trials retratados → magnitude mudou >50% | **15,7%** (IC 95%: 13,5–17,9%) | Xu et al. (VITALITY) 2025 | 40268307 ✅ | idem | 1 | |
| Guidelines contaminadas por SRs com trials retratados | **68 SRs** → **157 guidelines** | Xu et al. (VITALITY) 2025 | 40268307 ✅ | idem | 1 | |
| MAs com <10 estudos: risco maior de mudar direção | OR 2,63 (1,29–5,38) vs ≥20 estudos | Xu et al. (VITALITY) 2025 | 40268307 ✅ | idem | 1 | |
| SRs em top-25 journals com retratados: desfecho primário mudou ≥10% | **42%** (27/64) | Possamai C et al. JAMA Intern Med 2025;185(6):702-9 | 40163084 ✅ | 10.1001/jamainternmed.2025.0256 | 1 | 61 SRs, 62 retratados. 74% retratações pós-publicação da SR |
| SRs em top-25 journals: desfecho primário mudou ≥50% | **19%** (12/64) | Possamai et al. 2025 | 40163084 ✅ | idem | 1 | |
| Práticas médicas revertidas em JAMA/Lancet/NEJM | **396** reversões em >3.000 RCTs | Herrera-Perez D et al. eLife 2019;8:e45183 | 31182188 ✅ | 10.7554/eLife.45183 | 1 | 92% em países de alta renda. Cardiovascular (20%) e medicamentos (33%) mais comuns |
| Estudos altamente citados contraditos | **16%** (7/45) + 16% efeito inicial mais forte | Ioannidis JPA. JAMA 2005;294(2):218-28 | 16014596 ✅ | 10.1001/jama.294.2.218 | 1 | Landmark. 49 estudos mais citados em medicina — 1/6 contradito, 1/6 efeito inflado |

---

## Checkpoint 1 — ACCORD trap (controle glicêmico e infarto)

> Dados REAIS do slide checkpoint-1. MA mostra benefício para IAM, mas o maior trial (ACCORD) aumentou mortalidade.
> Função: armadilha antes de ensinar forest plot — "olhar dentro do diamante".

### Ray 2009 — MA de controle glicêmico intensivo

| Campo | Valor |
|-------|-------|
| Autores | Ray KK, Seshasai SRK, Wijesuriya S, et al. |
| Título | Effect of intensive control of glucose on cardiovascular outcomes and death in patients with diabetes mellitus: a meta-analysis of randomised controlled trials |
| Fonte | Lancet 2009;373(9677):1765-72 |
| PMID | 19465231 ✅ |
| DOI | 10.1016/S0140-6736(09)60697-8 |
| Desenho | MA de 5 RCTs |
| Participantes | 33.040 |
| Tier | **1** (Lancet) |

### Resultados — Ray 2009

| Desfecho | Medida | IC 95% | Nota |
|----------|--------|--------|------|
| IAM não-fatal | OR 0,83 | 0,75–0,93 | Significativo — benefício |
| Mortalidade total | OR 1,02 | NS | Sem diferença |

### ACCORD 2008 — maior trial dentro da MA

| Campo | Valor |
|-------|-------|
| Autores | ACCORD Study Group |
| Título | Effects of intensive glucose lowering in type 2 diabetes |
| Fonte | N Engl J Med 2008;358(24):2545-59 |
| PMID | 18539917 ✅ |
| DOI | 10.1056/NEJMoa0802743 |
| Participantes | 10.251 (~31% da MA Ray 2009) |
| Tier | **1** (NEJM) |

### Resultados — ACCORD

| Desfecho | Medida | IC 95% | p | Nota |
|----------|--------|--------|---|------|
| Mortalidade total | HR 1,22 | 1,01–1,46 | 0,04 | Interrompido precocemente por excesso de mortalidade |

### Scite tallies (2026-03-21)

| Paper | Citing | Smart | Supporting | Contrasting | Mentioning |
|-------|--------|-------|------------|-------------|------------|
| ACCORD (PMID 18539917) | 7.335 | 2.399 | 64 | 15 | 2.320 |
| Ray 2009 (PMID 19465231) | 1.318 | 889 | 23 | 5 | 806 |

DOIs Scite (lowercase obrigatorio): `10.1056/nejmoa0802743`, `10.1016/s0140-6736(09)60697-8`

### Dados expandidos — ACCORD

| Dado | Valor | Nota |
|------|-------|------|
| NNH (mortalidade) | **95** (1 morte extra / 95 tratados / 3,5 anos) | Autores: "one death for every 95 patients treated for 3.5 years" |
| IAM nao-fatal | HR 0,76 (0,62-0,92) | Paradoxo: preveniu IAM E aumentou mortalidade |
| Hipoglicemia severa | 16,2% vs 5,1% (3x mais no intensivo) | Mas: HR morte pos-hipo STANDARD 2,93 vs INTENSIVO 1,79 |
| A1C atingida | Intensivo 6,4% vs Standard 7,5% | Paradoxo A1C: nao-respondedores = maior risco (Riddle 2010) |

### Paradoxo A1C (Riddle 2010, PMID 20427682)

No grupo intensivo, cada 1% de aumento na A1C media → HR 1,66 mortalidade (p<0,0001). No standard: HR 0,98 (NS). Interacao p=0,0007. Ajustando por A1C atingida, HR intensivo→standard SOBE de 1,22 para 1,82. Interpretacao: "insistencia cega mata" — nao-respondedores recebiam mais drogas sem beneficio.

### Follow-ups ACCORD

| Follow-up | Mortalidade | IAM nao-fatal | Fonte |
|-----------|-------------|---------------|-------|
| 3,5 anos (original) | HR 1,22 (1,01-1,46) | HR 0,76 (0,62-0,92) | NEJM 2008, PMID 18539917 |
| 5 anos | HR 1,19 (1,03-1,38) | HR 0,82 (0,70-0,96) | NEJM 2011, PMID 21366473 |
| 9 anos | Morte CV HR 1,20 (1,03-1,39) | — | Diabetes Care 2016, PMID 26822326 |
| VADT 15 anos (comparador) | HR 1,02 (0,88-1,18) = neutro | — | NEJM 2019, PMID 31167051 |

### Notas para a aula

- ACCORD era o maior trial (31% do N total) e foi interrompido por excesso de mortalidade
- A MA de Ray 2009 MASCARA o sinal do ACCORD ao poolar com os outros 4 trials
- Função didática: "olhar dentro do diamante" — a soma esconde a parte
- Usado como armadilha no checkpoint 1 (antes de ensinar forest plot)
- Outros trials na MA: UKPDS, ADVANCE, VADT, PROactive
- NNH 95 = dado clinicamente ressonante para arguicao
- Paradoxo A1C: material para responder "mas por que morreram mais?"
- 15 contrasting citations no Scite = comunidade nao aceitou passivamente
- Narrativa briefing completo: `research-accord-valgimigli.md`

---

## Referências metodológicas adicionais (verificadas 2026-03-14)

| Referência | PMID | DOI | Tier | Função |
|-----------|------|-----|------|--------|
| Murad et al. Rating the certainty in evidence in the absence of a single estimate of effect. JAMA 2014;312(2):171-9 | 25005654 ⚠️ [VERIFY] | 10.1001/jama.2014.5952 | 1 | GRADE tutorial canônico — rating sem single estimate. **PMID 25005654 resolve para "Users' Guides" (diferente artigo, mesmo vol/pag). Verificar PMID correto.** |
| Guyatt et al. GRADE: an emerging consensus on rating quality of evidence. BMJ 2008;336(7650):924-6 | 18436948 ✅ | 10.1136/bmj.39489.470347.AD | 1 | Série introdutória GRADE. **PMID corrigido: era 21195583 (GRADE Guidelines 2011, artigo diferente).** |
| Dettori et al. Understanding the forest plot. Global Spine J 2021;11(7):1137-9 | 33939533 ✅ | 10.1177/21925682211012058 | 1 | Didática forest plot (já usada no slide 07) |
| Higgins JPT, Lopez-Lopez JA. Reflections on the I-squared index for measuring inconsistency in meta-analysis. Res Synth Methods. Published online Dec 29, 2025 | [não indexado] | 10.1017/rsm.2025.10062 ✅ | 1 | I² creator cautions overuse. Usada no slide 10 notes. Epub ahead of print — re-checar PMID em abr/2026 |

---

## Artigo âncora — Valgimigli 2025 (Lancet clopidogrel vs aspirina)

| Campo | Valor |
|-------|-------|
| Autores | Valgimigli M, Choi KH, Giacoppo D, Gragnano F, et al. |
| Título | Clopidogrel versus aspirin for secondary prevention of coronary artery disease |
| Fonte | Lancet 2025;406(10508):1091-1102 |
| PMID | 40902613 ✅ |
| DOI | 10.1016/S0140-6736(25)01562-4 |
| Desenho | IPD meta-analysis |
| RCTs | 7 |
| Participantes | 28.982 (14.507 clopidogrel, 14.475 aspirina) |
| Follow-up mediano | 2,3 anos (IQR 1,1–4,0) |
| MACCE (5,5 anos) | HR 0,86 (0,77–0,96); p=0,0082 |
| Sangramento maior | HR 0,94 (0,74–1,21); NS |
| GRADE | Não explícito |
| PROSPERO | CRD42025645594 |
| Acesso | Abstract aberto (Lancet) |
| Nota | IPD (não pairwise clássica). HR (não RR). Tema universal |
| Scite | Não indexado (publicado ago 2025). Consensus: 5 citações |

### 7 RCTs incluídos

| Trial | País | N | Destaque |
|-------|------|---|----------|
| CAPRIE (1996) | Internacional | 19.185 | O avô — primeiro clopidogrel vs aspirina. Pop mista (AVC, IAM, DAP) |
| HOST-EXAM | Coreia | 5.530 | Pós-PCI, follow-up longo |
| STOPDAPT-2 | Japão | — | Curta DAPT → monoterapia |
| STOPDAPT-3 | Japão | — | Curta DAPT → monoterapia |
| SMART-CHOICE | Coreia | — | P2Y12 vs aspirina pós-PCI |
| ASCET | Noruega | — | DAC estável |
| CADET | — | — | Menor, confirmatório |

Generalização: dados orientais (Coreia, Japão) + ocidentais (Europa, CAPRIE). Idade média 66a, 22% mulheres.

### CYP2C19 — achado pré-especificado

Pacientes com variantes de perda de função do CYP2C19 (poor metabolizers) AINDA se beneficiaram do clopidogrel sobre aspirina. ACC editorial: "Even patients with impaired responsiveness to clopidogrel because of genetic or clinical factors still benefited from its use over aspirin." Relevante para s-aplicabilidade.

### Artigos relacionados

| Referência | PMID | Tipo |
|-----------|------|------|
| Valgimigli authors' reply (Lancet 2026) | 41763741 | Resposta a críticas |
| Giacoppo et al. (BMJ 2025) — MA confirmatória IPD | 40467090 | 16.117 pts, 5 RCTs pos-PCI. MACCE HR 0,77 (0,67-0,89). Confirmou clopidogrel sem aumento de sangramento |
| NICE TA210 | — | Guideline UK: aspirina 1ª linha pós-IAM (clopidogrel só AVC/DAP/multivascular). Gap vs evidência Valgimigli |

---

## Candidatos não selecionados (referência — DECIDIDO: Valgimigli S3)

> Decisão: Valgimigli 2025 (PMID 40902613). Candidatos abaixo mantidos como referência para futuras aulas ou troca de âncora.

| Cod | Artigo | Journal | PMID | Destaque didático |
|-----|--------|---------|------|-------------------|
| S1 | Musini 2025 — Anti-HTN ≥60a | Cochrane | 41065416 | GRADE alta/mod/baixa. Exemplo visual (Fases 1-2) |
| S2 | Zacharias 2023 — Rifaximin EH | Cochrane | 37467180 | Pacote completo: GRADE+NNT+I²+RoB. Hepatologia |
| A7 | Jeyaraj 2026 — ATB não-rifax EH | Cochrane | 41631546 | Mostra DANO (mortalidade ↑). GRADE baixa/muito baixa |
| F1 | Pitre 2025 — Corticoides PAC | ICM | 40323455 | GRADE variação ideal. Recomendado antes de Valgimigli |
| F2 | Kolkailah 2024 — VTE estendida | Cochrane | 39629741 | NNTB 204 vs NNTH 314. Trade-off exemplar |
| F3 | Carson 2025 — Transfusão | Cochrane | 41114449 | I²=97% ensina diversidade ≠ invalidez |
| G1 | Hanula 2023 — Oseltamivir | JAMA IM | 37306992 | "Quebrando dogma": sem benefício + dano GI |
| G2 | McIntyre 2024 — DOAC device-AF | Circulation | 37952187 | Espelhamento benefício ≈ dano |
| G3 | Greenwood 2024 — Sal CV | Ann Intern Med | 38588546 | Indirectness: p sig + GRADE baixo (7/8 trials asiáticos) |
| G4 | Abdul-Aziz 2024 — β-lactam sepse | JAMA | 38864162 | Muda prática. Bayesiano (CrI, não CI) — limitação |
| G5 | El-Taji 2024 — CV próstata | JAMA Oncol | 38842801 | Farmacovigilância via MA. Oncologia |

---

## Changelog

| Data | Mudança |
|------|---------|
| 2026-03-21b | v5.7 — 5 PMIDs corrigidos via PubMed MCP (ACCORD 5yr→21366473, VADT→31167051, Riddle→20427682, Bonds→20061358, Giacoppo→40467090). Giacoppo: 162.829→16.117 pts (era paper errado). Notion References DB: 9 papers criados. |
| 2026-03-21 | v5.6 — Scite tallies (ACCORD 7.335/2.399, Ray 1.318/889). NNH 95. Paradoxo A1C (Riddle 2010). Follow-ups 5yr/9yr/VADT-15yr. 7 RCTs nomeados. CYP2C19. Authors' reply + Giacoppo. research-accord-valgimigli.md criado. |
| 2026-03-20 | v5.5 — +Ray 2009 (PMID 19465231) e ACCORD 2008 (PMID 18539917) para checkpoint 1. Nova seção "Checkpoint 1 — ACCORD trap". |
| 2026-03-19 | v5.4 — PMID audit (reference-manager agent, 36 PMIDs): Guyatt BMJ 2008 PMID corrigido 21195583→18436948. Murad JAMA 2014 PMID 25005654 marcado [VERIFY] (resolve para artigo diferente). Brignardello-Petersen DOI corrigido kwae256→kwae332. |
| 2026-03-19 | v5.3 — Siedler PMID 40969451 verificado. Journal corrigido: Cochrane Evid Synth Methods (não J Clin Epidemiol). Framing corrigido: 33,8% = SRs que avaliaram certeza (não % com certeza moderada/alta). Higgins & Lopez-Lopez DOI verificado (10.1017/rsm.2025.10062), PMID não indexado (epub Dez 2025). |
| 2026-03-19 | v5.2 — Hook rewrite sober: VITALITY/NICE-SUGAR removidos do slide (mantidos como ref). Hoffmann "EM USO card 1", Bojcic "EM USO card 2". +Siedler 2025 (33.8% GRADE, "EM USO card 3"). Tags EM USO atualizadas. |
| 2026-03-19 | v5.1 — Hook rewrite VITALITY backbone: +8 refs. INSPECT-SR (Wilkinson 2025, PMID 40349737), Guyatt/Brignardello-Petersen 2025 (PMID 39218429), Paul 2025 (PMID 40414366), Uttley 2024 (PMID 39542225), Wiener MA 2008 (PMID 18728267), NICE-SUGAR 2009 (PMID 19318384), Griesdale MA 2009 (PMID 19318387), Murad 2016 pirâmide (PMID 27339128). Novas seções: integridade RCTs, exemplo MA UTI, pirâmide. Todos PMIDs ✅ |
| 2026-03-18 | v5.0 — 6 refs adicionadas: Windish JAMA 2007 (EM USO no hook, swap 146→41%), VITALITY BMJ 2025, Possamai JAMA Intern Med 2025, Herrera-Perez eLife 2019, Saposnik BMC 2016, Ioannidis JAMA 2005. Nova seção "MAs contraditas/retratadas". Todos PMIDs ✅ |
| 2026-03-17 | v4.3 — Candidatos S2/A7/F1-F3/G1-G5 colapsados em tabela-resumo (~200 linhas cortadas). Dados completos preservados em PMIDs |
| 2026-03-16j | v4.2 — Autores corrigidos via PubMed: G3 Yin→Greenwood H (PMID 38588546 ✅), G5 Bosco→El-Taji O (PMID 38842801 ✅). Todos 5 PMIDs candidatos agora verificados |
| 2026-03-16e | v4.1 — Hook dados atualizados: Siemens 88% → Bojcic 81% (cross-field); Fanaroff 8,5% → Qureshi 10% (23 sociedades). Tags CANDIDATO → EM USO. Pendente: sync Notion References DB |
| 2026-03-15d | v4.0 — 5 candidatos Gemini adicionados (PMIDs verificados, 2 corrigidos). Hanula/oseltamivir, McIntyre/DOAC-AF, Yin/sal, Abdul-Aziz/β-lactam, Bosco/próstata-CV. Lucas indeciso entre β-lactam e PAC; slides começam amanhã sem artigo definido |
| 2026-03-15c | v3.4 — 3 finalistas para âncora adicionados: Pitre/ICM 2025 (corticoides PAC, recomendado), Kolkailah/Cochrane 2024 (VTE), Carson/Cochrane 2025 (transfusão). Decisão: Cochrane = exemplos visuais; âncora preferencialmente não-Cochrane |
| 2026-03-15b | v3.3 — Musini PMID 41065416 ✅ verificado. Acesso atualizado: Cochrane Library via CAPES (acordo nacional) |
| 2026-03-15 | v3.2 — Zacharias PMID verificado (37467180 ✅). Higgins & Lopez-Lopez 2025 (I² reflections) adicionado. Header "Candidato a Âncora" (TBD) |
| 2026-03-14 | v3.1 — Jeyaraj/Cochrane 2026 (ATB não-rifaximin para EH, PMID 41631546 ✅). Mostra dano |
| 2026-03-14 | v3 — Refs metodológicas (Murad, Guyatt, Dettori). Candidatos âncora top 3 (Zacharias, Valgimigli). PMIDs verificados via PubMed MCP |
| 2026-03-13 | v2 — QA pass: dados verificados nos slides, word count trimado. Nenhuma alteração de dados |
| 2026-03-13 | v1 — adicionadas 12 referências tier 1 para hook (3 eixos: volume, qualidade, competência) |
| 2026-03-11 | v0 — dados extraídos do abstract Musini 2025 |
