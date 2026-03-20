/**
 * _manifest.js — Meta-análise
 * Source of truth para ordem dos slides, fases narrativas e interações.
 *
 * DERIVADO DE: references/blueprint.md + references/narrative.md
 * Validação: npm run lint:narrative-sync metanalise
 *
 * Coautoria: Lucas (decisão clínica) · Opus 4.6 (código + governance)
 * Atualizado: 2026-03-19 — Deck completo (18 slides)
 */

export const slides = [
  // ── Fase 1: Criar importância ──
  { id: 's-title',        file: '00-title.html',        phase: 'F1', archetype: 'title',      headline: 'Meta-análise — Leitura crítica para decisão clínica',                                                                timing: null, clickReveals: 0, customAnim: 's-title',        narrativeRole: null,         tensionLevel: 0, narrativeCritical: false },
  { id: 's-hook',         file: '01-hook.html',         phase: 'F1', archetype: 'cards',       headline: 'Por que isso importa',                                    timing: 60,   clickReveals: 0, customAnim: 's-hook',             narrativeRole: 'hook',       tensionLevel: 2, narrativeCritical: true },
  { id: 's-contrato',     file: '02-contrato.html',     phase: 'F1', archetype: 'cards',      headline: '3 perguntas que você faz a toda meta-análise',                                            timing: 45,   clickReveals: 0, customAnim: 's-contrato',             narrativeRole: 'setup',      tensionLevel: 1, narrativeCritical: false },

  // ── Interação 1: Checkpoint de engajamento ──
  { id: 's-checkpoint-1', file: '03-checkpoint-1.html', phase: 'I1', archetype: 'checkpoint', headline: 'Controle glicemico intensivo reduziu infarto — mas o maior trial da MA aumentou mortalidade',                       timing: 90,   clickReveals: 2, customAnim: 's-checkpoint-1', narrativeRole: 'checkpoint', tensionLevel: 3, narrativeCritical: true },

  // ── Fase 2: Metodologia ──
  { id: 's-rs-vs-ma',     file: '04-rs-vs-ma.html',     phase: 'F2', archetype: 'compare',    headline: 'RS é o método de busca e seleção; MA é o cálculo estatístico — e são separáveis',                                    timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'setup',      tensionLevel: 1, narrativeCritical: false },
  { id: 's-pico',         file: '04-pico.html',         phase: 'F2', archetype: 'cards',      headline: 'PICO define a validade externa: se a população ou o comparador não batem, o resultado não se aplica',                 timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'setup',      tensionLevel: 1, narrativeCritical: false },
  { id: 's-abstract',     file: '05-abstract.html',     phase: 'F2', archetype: 'flow',       headline: 'Abstract PRISMA entrega busca, elegibilidade, N de estudos e resultado — triagem em 2 min antes do PDF',              timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'setup',      tensionLevel: 1, narrativeCritical: false },
  { id: 's-forest-plot',  file: '06-forest-plot.html',  phase: 'F2', archetype: 'cards',      headline: 'Forest plot codifica efeito, precisão e peso de cada estudo em 5 elementos',                                         timing: 90,   clickReveals: 0, customAnim: null,             narrativeRole: 'setup',      tensionLevel: 2, narrativeCritical: false },
  { id: 's-benefit-harm', file: '07-benefit-harm.html', phase: 'F2', archetype: 'compare',    headline: 'Benefício e dano podem ter certeza GRADE diferente na mesma MA — avaliar ambos separadamente',                        timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 2, narrativeCritical: false },
  { id: 's-grade',        file: '08-grade.html',        phase: 'F2', archetype: 'cards',      headline: 'Certeza GRADE expressa confiança no efeito estimado — avalia por desfecho, não por artigo',                           timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 2, narrativeCritical: false },
  { id: 's-heterogeneity',file: '09-heterogeneity.html',phase: 'F2', archetype: 'hero-stat',  headline: 'I² alto não invalida a MA — importa se a heterogeneidade é explicável e clinicamente relevante',                      timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 2, narrativeCritical: false },
  { id: 's-fixed-random', file: '10-fixed-random.html', phase: 'F2', archetype: 'compare',    headline: 'Random-effects alarga o IC quando há heterogeneidade — resultado significativo em fixed-effect pode desaparecer',      timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 1, narrativeCritical: false },

  // ── Interação 2: Checkpoint de consolidação ──
  { id: 's-checkpoint-2', file: '12-checkpoint-2.html', phase: 'I2', archetype: 'checkpoint', headline: 'RR 0,75 (IC 0,60–0,93), I²=72%, GRADE baixa — o diamante favorece. Você muda?',                                     timing: 120,  clickReveals: 3, customAnim: 's-checkpoint-2', narrativeRole: 'checkpoint', tensionLevel: 4, narrativeCritical: true },

  // ── Fase 3: Aplicação (Valgimigli 2025) ──
  { id: 's-ancora',       file: '13-ancora.html',       phase: 'F3', archetype: 'hero-stat',  headline: 'Clopidogrel reduziu eventos CV vs aspirina — 7 RCTs e 28.982 pacientes com dados individuais',                       timing: 90,   clickReveals: 0, customAnim: null,             narrativeRole: 'setup',      tensionLevel: 2, narrativeCritical: false },
  { id: 's-aplicacao',    file: '14-aplicacao.html',    phase: 'F3', archetype: 'compare',    headline: 'MACCE caiu 14% com clopidogrel, sem aumento de sangramento — mas certeza GRADE não foi avaliada',                     timing: 90,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 3, narrativeCritical: false },
  { id: 's-aplicabilidade',file:'15-aplicabilidade.html',phase:'F3', archetype: 'cards',      headline: 'Prevenção secundária de DAC, seguimento 2,3a — antes de adotar, verifique se seu paciente se encaixa',                timing: 90,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 2, narrativeCritical: false },
  { id: 's-absoluto',     file: '16-absoluto.html',     phase: 'F3', archetype: 'hero-stat',  headline: 'Mesmo RR pode significar NNT 25 ou NNT 250 — sem risco basal, efeito relativo não informa decisão',                  timing: 90,   clickReveals: 0, customAnim: null,             narrativeRole: 'payoff',     tensionLevel: 3, narrativeCritical: false },
  { id: 's-takehome',     file: '17-takehome.html',     phase: 'F3', archetype: 'recap',      headline: 'Três perguntas que você faz a toda MA antes de mudar sua conduta',                                                   timing: 60,   clickReveals: 0, customAnim: null,             narrativeRole: 'resolve',    tensionLevel: 1, narrativeCritical: true },
];
