#!/usr/bin/env node
/* Pause the in-page O.G sweep mid-run and checkpoint its partial results.
 *
 * WHY (2026-07-29): Omar's internet was about to drop ~150/453 symbols into an
 * evening catch-up sweep. The sweep loop lives in the TradingView page and has
 * no stop switch; killing the Node poller alone leaves the page loop burning
 * through the remaining symbols with no data feed - garbage rows. This script:
 *   1. snapshots window.__og.results to a dated checkpoint file,
 *   2. halts the loop by patching the chart widget's setSymbol to throw
 *      (the loop's try/catch skips every remaining symbol in milliseconds),
 *   3. restores setSymbol so the chart works normally again,
 *   4. prints which symbols are DONE so the resume run can sweep the rest.
 *
 * Usage: node scripts/oneoff/pause_sweep.mjs YYYY-MM-DD
 * Writes: watchlists/og-sweep-partial-<date>-heikinashi.json
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { connect, evaluate, disconnect } from '../../src/connection.js';

const DATE = process.argv[2];
if (!DATE) { console.error('usage: pause_sweep.mjs YYYY-MM-DD'); process.exit(2); }
const REPO = path.dirname(path.dirname(path.dirname(fileURLToPath(import.meta.url))));
const CW = 'window.TradingViewApi._activeChartWidgetWV.value()';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

async function main() {
  await connect();
  const st = JSON.parse(await evaluate(
    `JSON.stringify({idx: window.__og && window.__og.idx, total: window.__og && window.__og.total,
                     got: window.__og && window.__og.results.length, done: window.__og && window.__og.done})`));
  console.log(`[pause] sweep state: ${st.got} read of ${st.total}, idx ${st.idx}, done=${st.done}`);
  if (!st || st.total == null) { console.error('[pause] no sweep found in page'); process.exit(1); }

  // Halt the loop FIRST so the snapshot is of a stopped world: patch setSymbol
  // to throw. The loop's per-symbol try/catch turns every remaining iteration
  // into an instant error entry; the loop reaches done=true within ~a second.
  if (!st.done) {
    await evaluate(`(function(){ var cw = ${CW};
      window.__ogPausedSetSymbol = true;
      cw.setSymbol = function(){ throw new Error('SWEEP-PAUSED-2026-07-29'); }; })()`);
    for (let i = 0; i < 40; i++) {
      await sleep(500);
      const d = await evaluate('window.__og.done');
      if (d) break;
    }
    // restore: the patch is an own-property shadowing the prototype method
    await evaluate(`(function(){ var cw = ${CW};
      delete cw.setSymbol; delete window.__ogPausedSetSymbol; })()`);
    const restored = await evaluate(`typeof ${CW}.setSymbol`);
    console.log(`[pause] loop halted; setSymbol restored (typeof: ${restored})`);
  }

  const raw = JSON.parse(await evaluate('JSON.stringify(window.__og.results)'));
  const good = raw.filter(r => r.ok);
  const out = path.join(REPO, 'watchlists', `og-sweep-partial-${DATE}-heikinashi.json`);
  fs.writeFileSync(out, JSON.stringify({
    date: DATE, paused_at: new Date().toISOString(),
    read_ok: good.map(r => r.req), rows: raw,
  }));
  await disconnect();
  console.log(`[pause] checkpoint: ${raw.length} rows (${good.length} ok) -> ${out}`);
}
main().catch(e => { console.error('[pause] ERROR:', e.message); process.exit(1); });
