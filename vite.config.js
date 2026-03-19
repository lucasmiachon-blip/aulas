import { defineConfig } from 'vite';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readdirSync, statSync } from 'node:fs';

const __dirname = fileURLToPath(new URL('.', import.meta.url));

// Auto-discover all HTML files in aulas/
// Convention: aulas/*/index*.html = lecture decks (Plan A + Plan B)
//             aulas/calibracao.html = projector calibration tool (intentionally here, ships with build)
// Frozen Reveal.js aulas excluded from entry discovery.
// They can still be served by URL in dev mode, but won't pollute the Vite dep cache.
const FROZEN_AULAS = ['grade', 'osteoporose'];

function discoverEntries() {
  const entries = {};
  const aulasDir = resolve(__dirname, 'aulas');

  // Top-level HTML — skip calibracao (depends on reveal.js, not installed in deck.js WTs)
  const SKIP_TOP_LEVEL = ['calibracao.html'];
  readdirSync(aulasDir).forEach(item => {
    const full = resolve(aulasDir, item);
    if (item.endsWith('.html') && !SKIP_TOP_LEVEL.includes(item)) {
      entries[item.replace('.html', '')] = full;
    } else if (statSync(full).isDirectory() && !FROZEN_AULAS.includes(item)) {
      // Subdir HTML (e.g., metanalise/index.html, cirrose/index.html)
      readdirSync(full).filter(f => f.endsWith('.html')).forEach(f => {
        const key = f === 'index.html'
          ? item
          : `${item}_${f.replace('.html', '').replace('index.', '')}`;
        entries[key] = resolve(full, f);
      });
    }
  });
  return entries;
}

export default defineConfig({
  root: '.',
  base: './',
  server: {
    port: 3000,
    open: '/aulas/metanalise/index.html',
    browser: 'google chrome'
  },
  build: {
    target: 'esnext',
    rollupOptions: {
      input: discoverEntries()
    }
  }
});
