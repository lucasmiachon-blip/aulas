#!/usr/bin/env node
/**
 * QA Video — Grava .mp4 de cada slide com animações reais
 *
 * Playwright recordVideo captura o browser real:
 *   → GSAP rodando (countUp, stagger, drawPath)
 *   → Transições deck.js ou Reveal.js
 *   → Click-reveal progressivo
 *
 * Output: qa-screenshots/videos/{slide-id}.mp4
 *
 * Usage:
 *   npm run qa:video                                # cirrose (default)
 *   npm run qa:video -- --aula=metanalise           # metanalise (deck.js)
 *   npm run qa:video -- --slide=s-hook              # slide específico
 *   npm run qa:video -- --batch=0,5                 # slides 0 a 4
 *   npm run qa:video -- --url=http://localhost:3001/aulas/metanalise/index.html
 *
 * Workflow:
 *   1. Rodar: npm run qa:video
 *   2. Abrir qa-screenshots/videos/
 *   3. Upload do .mp4 para Gemini
 *   4. Gemini analisa animação real com contexto clínico
 *
 * Requer servidor: npm run dev  (ou npm run preview)
 */
import { chromium } from 'playwright';
import { mkdirSync, existsSync, renameSync, rmSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const ROOT = resolve(__dirname, '..');
const OUT_ROOT = join(ROOT, 'qa-screenshots', 'videos');
const TMP_DIR = join(ROOT, 'qa-screenshots', '.video-tmp');

const PORT = process.env.PORT || 3000;
const VIEWPORT = { width: 1280, height: 720 };

// Quanto tempo esperar entre cada ação (ms)
const TIMING = {
  afterNav: 800,        // após navegar para o slide
  afterTransition: 600, // após cada fragment/reveal
  endPause: 1000,       // pausa final antes de parar gravação
  maxRecording: 15000,  // timeout máximo por slide (15s, limit inlineData ~20MB)
};

const args = process.argv.slice(2);
const slideFilter = args.find(a => a.startsWith('--slide='))?.split('=')[1];
const batchArg = args.find(a => a.startsWith('--batch='))?.split('=')[1];
const aulaArg = args.find(a => a.startsWith('--aula='))?.split('=')[1] || 'cirrose';
const urlArg = args.find(a => a.startsWith('--url='))?.split('=')[1];

const BASE_URL = urlArg || `http://localhost:${PORT}/aulas/${aulaArg}/index.html`;
const FRAMEWORK = (aulaArg === 'grade' || aulaArg === 'osteoporose')
  ? 'reveal' : 'deck';

let batchRange = null;
if (batchArg) {
  const [from, to] = batchArg.split(',').map(Number);
  batchRange = { from, to };
}

// ── Framework-specific helpers ──

async function waitForReady(page) {
  if (FRAMEWORK === 'reveal') {
    await page.waitForFunction(
      () => typeof window.Reveal !== 'undefined' && window.Reveal.isReady?.(),
      { timeout: 15000 }
    );
  } else {
    // deck.js: wait for first section to be visible
    await page.waitForFunction(
      () => document.querySelector('section') !== null,
      { timeout: 15000 }
    );
    // Wait for engine.js to finish init (slide:entered fires on first slide)
    await page.waitForTimeout(800);
  }
}

async function getRevealCount(page) {
  if (FRAMEWORK === 'reveal') {
    return page.evaluate(() => {
      const slide = window.Reveal.getCurrentSlide();
      if (!slide) return 0;
      return slide.querySelectorAll('.fragment:not(.visible)').length;
    });
  } else {
    // deck.js: count unrevealed [data-reveal] elements in current slide
    return page.evaluate(() => {
      const current = document.querySelector('section.slide-active') || document.querySelector('section[aria-hidden="false"]');
      if (!current) return 0;
      return current.querySelectorAll('[data-reveal]:not(.revealed)').length;
    });
  }
}

async function goToSlide(page, slideIndex) {
  if (FRAMEWORK === 'reveal') {
    await page.evaluate((idx) => {
      window.Reveal.configure({ transition: 'none' });
      window.Reveal.slide(idx);
    }, slideIndex);
    await page.waitForTimeout(200);
    await page.evaluate(() => {
      window.Reveal.configure({ transition: 'fade' });
    });
  } else {
    // deck.js: pure ESM — no window.deck. Replicate goTo() via DOM.
    await page.evaluate((idx) => {
      const sections = document.querySelectorAll('#slide-viewport > section');
      const current = document.querySelector('section.slide-active');
      const target = sections[idx];
      if (!target) return;
      if (current) current.classList.remove('slide-active');
      target.classList.add('slide-active');
      document.dispatchEvent(new CustomEvent('slide:changed', {
        detail: { currentSlide: target, previousSlide: current, indexh: idx },
        bubbles: false
      }));
      setTimeout(() => {
        document.dispatchEvent(new CustomEvent('slide:entered', {
          detail: { currentSlide: target, indexh: idx },
          bubbles: false
        }));
      }, 600);
    }, slideIndex);
    // Wait for slide:entered event
    await page.waitForTimeout(800);
  }
}

async function getSlideMap(browser) {
  const ctx = await browser.newContext({ viewport: VIEWPORT });
  const page = await ctx.newPage();
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await waitForReady(page);

  let slideMap;
  if (FRAMEWORK === 'reveal') {
    slideMap = await page.evaluate(() =>
      window.Reveal.getSlides().map((el, i) => ({ index: i, id: el.id || null }))
    );
  } else {
    slideMap = await page.evaluate(() =>
      Array.from(document.querySelectorAll('section[id]')).map((el, i) => ({
        index: i,
        id: el.id || null
      }))
    );
  }

  await ctx.close();
  return slideMap;
}

// ── Recording ──

async function recordSlide(browser, slideIndex, slideId) {
  const tmpSlideDir = join(TMP_DIR, `slide-${slideIndex}`);
  mkdirSync(tmpSlideDir, { recursive: true });

  const context = await browser.newContext({
    viewport: VIEWPORT,
    recordVideo: {
      dir: tmpSlideDir,
      size: VIEWPORT,
    },
  });

  const page = await context.newPage();

  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await waitForReady(page);
  await goToSlide(page, slideIndex);
  await page.waitForTimeout(TIMING.afterNav);

  // Advance all reveals one by one (respecting max timeout)
  const recordStart = Date.now();
  let safetyCounter = 0;
  while (safetyCounter < 20) {
    if (Date.now() - recordStart > TIMING.maxRecording - TIMING.endPause) break;
    const remaining = await getRevealCount(page);
    if (remaining === 0) break;
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(TIMING.afterTransition);
    safetyCounter++;
  }

  // Final pause to show completed state
  const timeLeft = TIMING.maxRecording - (Date.now() - recordStart);
  await page.waitForTimeout(Math.min(TIMING.endPause, Math.max(200, timeLeft)));

  const videoPath = await page.video()?.path();
  await context.close();

  const finalName = `${slideId}.mp4`;
  const finalPath = join(OUT_ROOT, finalName);

  if (videoPath && existsSync(videoPath)) {
    renameSync(videoPath, finalPath);
  }

  return finalPath;
}

// ── Main ──

async function main() {
  try { rmSync(TMP_DIR, { recursive: true }); } catch {}
  mkdirSync(OUT_ROOT, { recursive: true });
  mkdirSync(TMP_DIR, { recursive: true });

  const browser = await chromium.launch({ headless: true });

  console.log(`QA Video → ${BASE_URL} (${FRAMEWORK})\n`);
  const slideMap = await getSlideMap(browser);

  let targets = slideMap;
  if (slideFilter) {
    targets = slideMap.filter(s => s.id === slideFilter);
    if (!targets.length) { console.error(`Slide "${slideFilter}" não encontrado.`); process.exit(1); }
  } else if (batchRange) {
    targets = slideMap.slice(batchRange.from, batchRange.to);
  }

  console.log(`Gravando ${targets.length} slide(s)...\n`);

  for (const { index, id } of targets) {
    const label = id || `slide-${String(index).padStart(2, '0')}`;
    process.stdout.write(`  [${String(index).padStart(2, '0')}] ${label} → gravando...`);
    await recordSlide(browser, index, label);
    process.stdout.write(` ✓ ${label}.mp4\n`);
  }

  await browser.close();
  try { rmSync(TMP_DIR, { recursive: true }); } catch {}

  console.log(`\n✓ Vídeos → qa-screenshots/videos/`);
  console.log(`\nPróximo passo:`);
  console.log(`  node scripts/gemini.mjs --slide {id} --file {html} --png {png} --mp4 {mp4} --json`);
}

main().catch(e => { console.error(e); process.exit(1); });
