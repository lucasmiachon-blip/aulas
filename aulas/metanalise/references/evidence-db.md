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
| SRs publicadas por dia (2019) | **~80/dia** | Hoffmann et al. J Clin Epidemiol 2021;138:1-11 | 34091022 | 10.1016/j.jclinepi.2021.05.022 | 1 |
| Aumento de SRs indexadas (2000→2019) | 1.432 → 29.073 (**20x**) | Hoffmann et al. 2021 | 34091022 | idem | 1 |
| Crescimento de SRs (1991→2014) | **+2.728%** (vs +153% total PubMed) | Ioannidis. Milbank Q 2016;94(3):485-514 | 27620683 | 10.1111/1468-0009.12210 | 1 |
| SRs/MAs indexadas em 2017 | 22.774 (48x vs 1995) | Niforatos et al. JAMA Intern Med 2019;179(11):1593-4 | 31355871 | 10.1001/jamainternmed.2019.3013 | 1 |
| SRs + RCTs por dia (2010) | 75 RCTs + 11 SRs/dia | Bastian et al. PLoS Med 2010;7(9):e1000326 | 20877712 | 10.1371/journal.pmed.1000326 | 1 |

### Qualidade criticamente baixa

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| SRs em câncer com qualidade criticamente baixa (AMSTAR-2) | **88,1%** (230/261) | Siemens et al. J Clin Epidemiol 2021;136:84-95 | 33741503 | 10.1016/j.jclinepi.2021.03.010 | 1 | ⚠ Específico de câncer avançado — não usar como dado geral |
| SRs que declaram AMSTAR-2: criticamente baixas (cross-field) | **81%** (35/43) | Bojcic et al. J Clin Epidemiol 2024;165:111210 | 37931822 ✅ | 10.1016/j.jclinepi.2023.10.026 | 1 | ✅ **EM USO no hook** (substituiu Siemens 88%) — cross-field, não específico de área |
| "A grande maioria é desnecessária, enganosa ou conflitada" | — | Ioannidis 2016 | 27620683 | idem | 1 | |
| MAs redundantes sobre antidepressivos (2007-2014) | **185** sobre o mesmo tema | Ioannidis 2016 | 27620683 | idem | 1 | |

### Guidelines e evidência de nível A

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Recomendações ACC/AHA com LoE A (=SR/MA) | **8,5%** (248/2930) | Fanaroff et al. JAMA 2019;321(11):1069-80 | 30874755 | 10.1001/jama.2019.1122 | 1 | Específico ACC/AHA cardiologia |
| Recomendações ESC com LoE A | **14,2%** (484/3399) | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações ESC com LoE C (opinião de expert) | **54,8%** | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações com evidência forte (LoE A equiv.) — cross-society | **10%** (768/7.582) | Qureshi et al. JGIM 2025 [online 22 dez] | 41428154 ✅ | 10.1007/s11606-025-10088-6 | 1 | ✅ **EM USO no hook** (substituiu Fanaroff 8,5%) — 23 sociedades EUA, 2019-2023, cross-specialty |
| Guidelines que usam métodos sistemáticos | **34%** (17/50) | Lunny et al. PLoS ONE 2021;16(4):e0250356 | 33886670 | 10.1371/journal.pone.0250356 | 1 | |

### Competência dos médicos

| Dado | Valor | Fonte | PMID | DOI | Tier |
|------|-------|-------|------|-----|------|
| Clínicos: baixa proficiência + alta confiança (n=898) | Ilusão de competência | Lakhlifi et al. Cogn Res Princ Implic 2023;8:23 | 37081292 | 10.1186/s41235-023-00474-1 | 1 |
| Competências EBP mínimas (5-step model) | Consenso internacional | Sicily Statement. Dawes et al. BMC Med Educ 2005;5:1 | 15634359 | 10.1186/1472-6920-5-1 | 1 |

---

## Referências metodológicas adicionais (verificadas 2026-03-14)

| Referência | PMID | DOI | Tier | Função |
|-----------|------|-----|------|--------|
| Murad et al. Rating the certainty in evidence in the absence of a single estimate of effect. JAMA 2014;312(2):171-9 | 25005654 ✅ | 10.1001/jama.2014.5952 | 1 | GRADE tutorial canônico — rating sem single estimate |
| Guyatt et al. GRADE: an emerging consensus on rating quality of evidence. BMJ 2008;336(7650):924-6 | 21195583 ✅ | 10.1136/bmj.39489.470347.AD | 1 | Série introdutória GRADE |
| Dettori et al. Understanding the forest plot. Global Spine J 2021;11(7):1137-9 | 33939533 ✅ | 10.1177/21925682211012058 | 1 | Didática forest plot (já usada no slide 07) |
| Higgins & Lopez-Lopez. Reflections on the I² index for measuring inconsistency in meta-analysis. Res Synth Methods 2025 | pendente | — | 1 | I² creator cautions overuse. Usada no slide 10 notes |

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
