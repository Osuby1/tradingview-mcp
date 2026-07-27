#!/usr/bin/env node
/* Deterministic CDP driver for the O.G Heikin-Ashi universe sweep.
 *
 * WHY THIS EXISTS: the nightly sweep used to run inside a single headless `claude -p`
 * that polled the 480-name chart loop for ~40 min. It failed 2026-07-21 (out of
 * credits) and 2026-07-24 (session ran out of budget mid-sweep). A headless LLM
 * turn-budget is the wrong tool for a long deterministic loop. This plain Node
 * process connects straight to CDP (reusing src/connection.js), installs the sweep
 * runner, sets Heikin Ashi, runs the sweep, polls to completion, and writes the raw
 * JSON. It cannot "run out of budget".
 *
 * Usage:  node scripts/og_sweep_cdp.mjs YYYY-MM-DD
 * Reads:  watchlists/og-sweep-universe-<date>-extended.json  (build_extended_universe.py first)
 * Writes: watchlists/og-sweep-raw-<date>-heikinashi.json
 * Exit:   0 = ok, 1 = failure (chart/style/sweep/timeout), 2 = usage error.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { connect, evaluate, disconnect, waitForChartTarget } from '../src/connection.js';

const DATE = process.argv[2];
if (!DATE || !/^\d{4}-\d{2}-\d{2}$/.test(DATE)) {
  console.error('usage: node scripts/og_sweep_cdp.mjs YYYY-MM-DD');
  process.exit(2);
}
const REPO = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const CHART = 'window.TradingViewApi._activeChartWidgetWV.value()';
const STYLE = `${CHART}._chartWidget.model().model().mainSeries().properties().style.value()`;
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const MAX_MS = 50 * 60 * 1000;   // hard cap so a hung chart can't run forever

function loadSymbols() {
  const f = path.join(REPO, 'watchlists', `og-sweep-universe-${DATE}-extended.json`);
  const d = JSON.parse(fs.readFileSync(f, 'utf8'));
  if (Array.isArray(d)) return d;
  for (const v of Object.values(d)) {
    if (Array.isArray(v) && v.length > 50 && v.every(x => typeof x === 'string')) return v;
  }
  throw new Error(`no symbol list found in ${f}`);
}

async function main() {
  console.log(`[cdp-sweep] ${DATE} - connecting to TradingView via CDP...`);
  // Wait for a REAL chart page before connecting. The Desktop build answers CDP
  // (and the .bat feed check) the moment the app is up, but its chart tab can be
  // seconds behind - and its file:// helper windows used to get picked instead,
  // which fails at setChartType with "_activeChartWidgetWV undefined". Waiting
  // here turns a race into a pause instead of a lost night. (2026-07-27)
  const tgt = await waitForChartTarget(3 * 60 * 1000);
  console.log(`[cdp-sweep] chart page found: ${tgt.url}`);
  await connect();

  // 1. install the sweep runner (idempotent - redefines the window fns)
  const runner = fs.readFileSync(path.join(REPO, 'scripts', 'og_sweep_runner.js'), 'utf8');
  await evaluate(runner);

  // 2. force Heikin Ashi (style 8) the proven way, then verify
  await evaluate(`${CHART}.setChartType(8)`);
  await sleep(2500);
  const style = await evaluate(STYLE);
  if (style !== 8) {
    console.error(`[cdp-sweep] FAILED: could not set Heikin Ashi (style=${style})`);
    process.exit(1);
  }
  console.log('[cdp-sweep] chart on Heikin Ashi (style 8)');

  // 3. start the sweep (runner refuses non-HA, so allowOtherStyle=false is correct)
  const syms = loadSymbols();
  const started = await evaluate(
    `window.__ogSweep(${JSON.stringify(syms)}, ${JSON.stringify('cdp-' + DATE)}, false)`);
  if (!/^started/.test(String(started))) {
    console.error(`[cdp-sweep] FAILED to start: ${started}`);
    process.exit(1);
  }
  console.log(`[cdp-sweep] ${started}`);

  // 4. poll to completion
  const t0 = Date.now();
  for (;;) {
    await sleep(15000);
    const o = JSON.parse(await evaluate(
      `JSON.stringify({done:window.__og.done, idx:window.__og.idx, total:window.__og.total, got:window.__og.results.length})`));
    console.log(`[cdp-sweep] ${o.idx}/${o.total} (${o.got} read)`);
    if (o.done) break;
    if (Date.now() - t0 > MAX_MS) {
      console.error('[cdp-sweep] FAILED: sweep timed out (>50 min)');
      process.exit(1);
    }
  }

  // 5. extract + write the raw sweep
  const raw = JSON.parse(await evaluate('JSON.stringify(window.__og.results)'));
  const okCount = raw.filter(r => r.ok).length;
  const style_ok = raw.every(r => r.style === 8);
  const out = path.join(REPO, 'watchlists', `og-sweep-raw-${DATE}-heikinashi.json`);
  fs.writeFileSync(out, JSON.stringify(raw));
  await disconnect();
  console.log(`[cdp-sweep] wrote ${out} | ${raw.length} rows, ${okCount} ok, all-HA=${style_ok}`);

  if (raw.length === 0 || okCount < raw.length * 0.8 || !style_ok) {
    console.error(`[cdp-sweep] FAILED verify: rows=${raw.length} ok=${okCount} all-HA=${style_ok}`);
    process.exit(1);
  }
  process.exit(0);
}

main().catch(e => { console.error('[cdp-sweep] ERROR:', e.message); process.exit(1); });
