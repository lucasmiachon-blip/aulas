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
| SRs que declaram AMSTAR-2: criticamente baixas (cross-field) | **81%** (35/43) | Bojcic et al. J Clin Epidemiol 2024;165:111210 | 37931822 ✅ | 10.1016/j.jclinepi.2023.10.026 | 1 | **CANDIDATO** para substituir Siemens no hook — não específico de área |
| "A grande maioria é desnecessária, enganosa ou conflitada" | — | Ioannidis 2016 | 27620683 | idem | 1 | |
| MAs redundantes sobre antidepressivos (2007-2014) | **185** sobre o mesmo tema | Ioannidis 2016 | 27620683 | idem | 1 | |

### Guidelines e evidência de nível A

| Dado | Valor | Fonte | PMID | DOI | Tier | Nota |
|------|-------|-------|------|-----|------|------|
| Recomendações ACC/AHA com LoE A (=SR/MA) | **8,5%** (248/2930) | Fanaroff et al. JAMA 2019;321(11):1069-80 | 30874755 | 10.1001/jama.2019.1122 | 1 | Específico ACC/AHA cardiologia |
| Recomendações ESC com LoE A | **14,2%** (484/3399) | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações ESC com LoE C (opinião de expert) | **54,8%** | Fanaroff et al. 2019 | 30874755 | idem | 1 | |
| Recomendações com evidência forte (LoE A equiv.) — cross-society | **10%** (768/7.582) | Qureshi et al. JGIM 2025 [online 22 dez] | 41428154 ✅ | 10.1007/s11606-025-10088-6 | 1 | **CANDIDATO** para substituir/complementar Fanaroff — 23 sociedades EUA, 2019-2023, cross-specialty |
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

## Candidatos a artigo âncora — dados resumidos

> Dados completos: ver blueprint.md v1.3 § Candidatos.
> Aqui apenas os top 3 com dados extraídos.

### S2 — Zacharias 2023 (Cochrane rifaximin para EH)

| Campo | Valor |
|-------|-------|
| Autores | Zacharias HD, Kamel F, Tan J, Kimer N, Gluud LL, Morgan MY |
| Título | Rifaximin for prevention and treatment of hepatic encephalopathy in people with cirrhosis |
| Fonte | Cochrane Database Syst Rev. 2023;7:CD011585 |
| PMID | 37467180 ✅ |
| RCTs | 41 |
| Participantes | 4.545 |
| Desfechos (rif+NAD vs NAD): mortalidade | RR 0,69 (0,55–0,86); NNT=22; I²=0%; certeza moderada |
| Desfechos (rif vs placebo): EH | RR 0,56 (0,42–0,77); NNT=5; I²=68%; certeza moderada |
| Desfechos (rif vs placebo): mortalidade | RR 0,83 (0,50–1,38); NS; I²=0%; certeza moderada |
| GRADE | ✅ Explícito por desfecho (muito baixa a moderada) |
| RoB | Cochrane RoB (11 trials alto risco para mortalidade) |
| Acesso | Abstract aberto (Cochrane) |
| Nota | Pacote completo para ensinar: GRADE, NNT, I², RoB, subgrupos. Hepatologia |

### S3 — Valgimigli 2025 (Lancet clopidogrel vs aspirina)

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

### A7 — Jeyaraj 2026 (Cochrane antibióticos não-rifaximin para EH)

| Campo | Valor |
|-------|-------|
| Autores | Jeyaraj R, Zacharias HD, Vadera S, Low ZY, Gluud LL, Morgan MY |
| Título | Aminoglycosides, vancomycin, and metronidazole for people with cirrhosis and hepatic encephalopathy |
| Fonte | Cochrane Database Syst Rev. 2026; CD012734.pub2 |
| DOI | 10.1002/14651858.CD012734.pub2 |
| PMID | 41631546 ✅ |
| RCTs | 24 |
| Participantes | 1.405 (1.418 eventos de EH) |
| Agentes | Neomicina (15), paromomicina (3), ribostamicina (1), vancomicina (2), metronidazol (3) |
| Mortalidade (aminoglicosídeo vs ativos) | RR 1,64 (1,03–2,62); 3 estudos, 166 pts |
| EA graves (aminoglicosídeo vs ativos) | RR 1,60 (1,03–2,47); 3 estudos, 166 pts |
| Mortalidade (aminoglicosídeo vs placebo) | RR 1,02 (0,62–1,69); NS |
| EH (aminoglicosídeo vs dissacarídeos) | RR 0,84 (0,67–1,05); NS |
| GRADE | ✅ Baixa a Muito Baixa em todas as comparações |
| Acesso | Abstract aberto (Cochrane) |
| Nota | Mostra DANO (aumento de mortalidade com aminoglicosídeos vs outros ativos). Perfeito para ensinar: Cochrane ≠ benefício garantido; GRADE baixa = não confiar; benefício-dano no mesmo artigo |

---

## Finalistas para âncora — Fase 3 (busca 2026-03-15)

> Critério: pairwise MA de RCTs, GRADE por desfecho com variação, benefício+dano, Tier 1, tema clínica médica geral.
> Cochrane reservado para exemplos visuais (Fases 1-2). Âncora preferencialmente não-Cochrane.

### F1 — Pitre 2025 — Corticoides em PAC (RECOMENDADO)

| Campo | Valor |
|-------|-------|
| Autores | Pitre T, Pauley E, Chaudhuri D, Saha R, ..., Annane D, Rochwerg B, Shankar-Hari M |
| Título | Corticosteroids for adult patients hospitalised with non-viral community-acquired pneumonia: a systematic review and meta-analysis |
| Fonte | Intensive Care Med. 2025 May;51(5):917-929 |
| DOI | 10.1007/s00134-025-07912-2 |
| PMID | 40323455 ✅ |
| PROSPERO | CRD42024521536 |
| RCTs | 30 |
| Participantes | 7.519 |
| Mortalidade curto prazo (28-30d) | RR 0,82 (0,74–0,91); certeza **moderada** |
| Mortalidade longo prazo (60-90d) | RR 0,89 (0,76–1,03); NS; certeza **baixa** |
| VM invasiva | RR 0,63 (0,48–0,82); certeza **alta** |
| Tempo UTI | MD −1,53d (0,31–2,75); certeza **baixa** |
| Tempo hospital | MD −2,30d (0,81–3,81); certeza **baixa** |
| Hiperglicemia (DANO) | RR 1,32 (1,12–1,56); certeza **moderada** |
| Infecções secundárias | RR 0,97 (0,85–1,11); NS; certeza **moderada** |
| GRADE | ✅ Explícito por desfecho: alta (1), moderada (3), baixa (3) |
| Acesso | Springer (acesso institucional CAPES) |
| Por que âncora | PAC universal, GRADE com variação ideal, benefício+dano claros, não-Cochrane (contraste), autores de referência (Rochwerg, Annane), guideline CCM 2024 já incorporou |

### F2 — Kolkailah 2024 — Profilaxia VTE estendida vs padrão

| Campo | Valor |
|-------|-------|
| Autores | Kolkailah AA, Abdelghaffar B, Elshafeey F, ..., Piazza G |
| Título | Standard- versus extended-duration anticoagulation for primary VTE prophylaxis in acutely ill medical patients |
| Fonte | Cochrane Database Syst Rev. 2024 Dec 4;12(12):CD014541 |
| PMID | 39629741 ✅ |
| RCTs | 7 |
| Participantes | 40.846 |
| TEV sintomático | RR 0,60 (0,46–0,78); NNTB 204; certeza **alta** |
| Sangramento maior (DANO) | RR 2,05 (1,51–2,79); NNTH 314; certeza **alta** |
| Mortalidade total | RR 0,97 (0,87–1,08); NS; certeza **alta** |
| TEV total | RR 0,75 (0,67–0,85); NNTB 107; certeza **alta** |
| Mortalidade por TEV | RR 0,78 (0,58–1,05); NS; certeza **moderada** |
| Sangramento fatal | RR 2,28 (0,84–6,22); NS; certeza **baixa** |
| GRADE | ✅ Explícito: alta (4), moderada (1), baixa (1) |
| RoB | RoB 2, todos baixo risco |
| Acesso | Cochrane Library (acordo CAPES) |
| Por que alternativa | Trade-off benefício/dano exemplar (NNTB vs NNTH), hospital medicine universal. Porém Cochrane (mesmo journal dos exemplos) |

### F3 — Carson 2025 — Limiares transfusionais (alternativa complexa)

| Campo | Valor |
|-------|-------|
| Autores | Carson JL, Stanworth SJ, Dennis JA, ..., Turgeon AF |
| Título | Transfusion thresholds and other strategies for guiding red blood cell transfusion |
| Fonte | Cochrane Database Syst Rev. 2025 (update) |
| PMID | 41114449 ✅ |
| RCTs | 61 (adultos) |
| Participantes | 27.639 |
| Mortalidade 30d | RR 1,01 (0,90–1,14); NS; certeza **alta** |
| Exposição a transfusão | RR 0,58 (0,52–0,65); certeza **alta**; I²=97% |
| IAM, AVC, TEV, infecção | NS; certeza **moderada–alta** |
| Subgrupo HDB | Mortalidade RR 0,63 (0,42–0,95) — favorece restritiva |
| Subgrupo neurocrítico | Desfecho neurológico pior com restritiva (RR 1,14) |
| GRADE | Alta a moderada por desfecho |
| Nota | I²=97% ensina "high I² ≠ MA inválida" (heterogeneidade por diversidade). Porém 61 trials = complexo para nível básico |

---

## Candidatos Gemini (busca 2026-03-15, PMIDs verificados)

> Fonte: busca assistida por Gemini com critérios da aula. PMIDs verificados manualmente via PubMed.
> ⚠️ Gemini errou 2 de 5 PMIDs. Valores abaixo são os corretos.

### G1 — Hanula 2023 — Oseltamivir em influenza ambulatorial

| Campo | Valor |
|-------|-------|
| Autores | Hanula R, Bortolussi-Courval É, Mendel A, Ward BJ, Lee TC, McDonald EG |
| Título | Evaluation of Oseltamivir Used to Prevent Hospitalization in Outpatients With Influenza |
| Fonte | JAMA Intern Med. 2023;183(10):1097-1104 |
| PMID | 37306992 ✅ |
| RCTs | 15 |
| Participantes | 6.166 (ITTi) |
| Hospitalização | RR 0,79 (0,48–1,29); NS |
| Hospitalização (alto risco) | RR 0,65 (0,33–1,28); NS |
| Náusea (DANO) | RR 1,43 (1,13–1,82) |
| Vômito (DANO) | RR 1,83 (1,28–2,63) |
| EA graves | RR 0,71 (0,46–1,08); NS |
| GRADE | ✅ Variação: baixa/moderada (eficácia), alta (dano GI) |
| Acesso | JAMA (acesso CAPES). Free PMC |
| Nota didática | "Quebrando dogma": Tamiflu não previne hospitalização mas causa dano GI. Choosing Wisely. Todo residente prescreve em plantão |

### G2 — McIntyre 2024 — DOAC em FA detectada por dispositivo

| Campo | Valor |
|-------|-------|
| Autores | McIntyre WF, Benz AP, Becher N, Healey JS, Granger CB, ..., Kirchhof P, Lopes RD |
| Título | Direct Oral Anticoagulants for Stroke Prevention in Patients With Device-Detected AF |
| Fonte | Circulation. 2024 Mar 26;149(13):981-988 |
| PMID | 37952187 ✅ (Gemini errou: 38205664) |
| PROSPERO | CRD42023463212 |
| RCTs | 2 (NOAH-AFNET 6 + ARTESiA) |
| Participantes | ~6.548 |
| AVC isquêmico | RR 0,68 (0,50–0,92); certeza **alta** |
| Composto CV | RR 0,85 (0,73–0,99); certeza **moderada** |
| Morte CV | RR 0,95 (0,76–1,17); NS; certeza **moderada** |
| Mortalidade total | RR 1,08 (0,96–1,21); NS; certeza **moderada** |
| Sangramento maior (DANO) | RR 1,62 (1,05–2,50); certeza **alta**; I²=61% |
| GRADE | ✅ Explícito: alta (2), moderada (3) |
| Acesso | Circulation (acesso CAPES) |
| Nota didática | Espelhamento: benefício AVC ≈ dano sangramento. Forest plot limpo (2 trials). Cenário atual (smartwatch/dispositivo). Apenas 2 RCTs = limitação para ensinar |

### G3 — Yin 2024 — Substituição de sal e desfechos CV

| Campo | Valor |
|-------|-------|
| Autores | Yin X, et al. |
| Título | Long-Term Effect of Salt Substitution for Cardiovascular Outcomes |
| Fonte | Ann Intern Med. 2024 Apr |
| PMID | 38588546 (verificação pendente — timeout) |
| RCTs | 16 |
| Participantes | 27.995 |
| Mortalidade total | RR 0,88 (0,82–0,93); certeza **baixa** |
| Mortalidade CV | RR 0,83; certeza **baixa** |
| EA graves / hipercalemia | RR 1,04 (0,87–1,25); NS; certeza **muito baixa** |
| GRADE | ✅ Variação: baixa a muito baixa |
| Nota didática | Melhor artigo para ensinar "indirectness" do GRADE: p significativo + N enorme + IC estreito, mas GRADE baixo porque 7/8 trials asiáticos (China/Taiwan). Validade externa |

### G4 — Abdul-Aziz 2024 — β-lactâmicos prolongados em sepse

| Campo | Valor |
|-------|-------|
| Autores | Abdul-Aziz MH, Hammond NE, Brett SJ, ..., Roberts JA |
| Título | Prolonged vs Intermittent Infusions of β-Lactam Antibiotics in Adults With Sepsis or Septic Shock |
| Fonte | JAMA. 2024 Aug 27;332(8):638-648 |
| PMID | 38864162 ✅ (Gemini errou: 38865173) |
| PROSPERO | CRD42023399434 |
| RCTs | 18 |
| Participantes | 9.108 |
| Mortalidade 90d | RR 0,86 (CrI 0,72–0,98); I²=21,5%; certeza **alta**; prob posterior 99,1% |
| Mortalidade UTI | RR 0,84 (CrI 0,70–0,97); certeza **alta** |
| Cura clínica | RR 1,16 (CrI 1,07–1,31); certeza **moderada** |
| GRADE | ✅ Alta (2), moderada (1) |
| Acesso | JAMA (acesso CAPES). Free PMC |
| ⚠️ Limitações | Framework **bayesiano** como análise primária (CrI, não CI). Sem desfecho de dano claro (EA ~1.0). GRADE com pouca variação (alta/alta/mod) |
| Nota didática | Muda prática imediatamente (infusão prolongada = padrão). Sepse = core residência. Mas: bayesiano pode confundir nível básico; ensino benefício-dano fica fraco |

### G5 — Bosco 2024 — Eventos CV com inibidores de receptor androgênico em câncer de próstata

| Campo | Valor |
|-------|-------|
| Autores | Bosco E (ou Sachdeva — verificar), et al. |
| Título | Cardiovascular Events and Androgen Receptor Signaling Inhibitors in Advanced Prostate Cancer |
| Fonte | JAMA Oncol. 2024 |
| PMID | 38842801 (verificação pendente) |
| RCTs | 24 |
| Participantes | 22.166 |
| Eventos CV grau ≥3 (DANO) | RR 2,10 (1,72–2,55) |
| HAS severa (DANO) | RR 2,25 |
| Morte CV (DANO) | RR 2,02 |
| GRADE | Framework de evidência aplicado à segurança |
| Nota didática | Ensina farmacovigilância: ler MA para comprovar iatrogenia. Porém: oncologia = menos cotidiano para clínica geral |

---

## Changelog

| Data | Mudança |
|------|---------|
| 2026-03-15d | v4.0 — 5 candidatos Gemini adicionados (PMIDs verificados, 2 corrigidos). Hanula/oseltamivir, McIntyre/DOAC-AF, Yin/sal, Abdul-Aziz/β-lactam, Bosco/próstata-CV. Lucas indeciso entre β-lactam e PAC; slides começam amanhã sem artigo definido |
| 2026-03-15c | v3.4 — 3 finalistas para âncora adicionados: Pitre/ICM 2025 (corticoides PAC, recomendado), Kolkailah/Cochrane 2024 (VTE), Carson/Cochrane 2025 (transfusão). Decisão: Cochrane = exemplos visuais; âncora preferencialmente não-Cochrane |
| 2026-03-15b | v3.3 — Musini PMID 41065416 ✅ verificado. Acesso atualizado: Cochrane Library via CAPES (acordo nacional) |
| 2026-03-15 | v3.2 — Zacharias PMID verificado (37467180 ✅). Higgins & Lopez-Lopez 2025 (I² reflections) adicionado. Header "Candidato a Âncora" (TBD) |
| 2026-03-14 | v3.1 — Jeyaraj/Cochrane 2026 (ATB não-rifaximin para EH, PMID 41631546 ✅). Mostra dano |
| 2026-03-14 | v3 — Refs metodológicas (Murad, Guyatt, Dettori). Candidatos âncora top 3 (Zacharias, Valgimigli). PMIDs verificados via PubMed MCP |
| 2026-03-13 | v2 — QA pass: dados verificados nos slides, word count trimado. Nenhuma alteração de dados |
| 2026-03-13 | v1 — adicionadas 12 referências tier 1 para hook (3 eixos: volume, qualidade, competência) |
| 2026-03-11 | v0 — dados extraídos do abstract Musini 2025 |
