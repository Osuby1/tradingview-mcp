#!/usr/bin/env node
/* Create TradingView price alerts on ANY symbol - including symbols that have no
 * alerts yet.
 *
 * WHY THIS EXISTS: the MCP `alert_create` tool is broken (see memory
 * alert-create-ui-workaround), and the working REST pattern in
 * scripts/ratchet_alerts.mjs clones an EXISTING alert on the same symbol as its
 * payload template. That is fine for maintaining alerts on the open book, but it
 * cannot wire a first alert on a new name - which is exactly what an entry-ladder
 * alert on a fresh scan candidate is. Hit on 2026-07-28 wiring JNJ/DGX entries.
 *
 * The symbol field is a string, not an object:
 *     ={"symbol":"BATS:JNJ","adjustment":"splits","currency-id":"USD"}
 * so it is built directly here rather than cloned.
 *
 * Usage:  node scripts/wire_alerts.mjs <specs.json> [--dry-run]
 * Spec:   [{ "sym": "BATS:JNJ", "level": 265.95, "message": "..." }, ...]
 *         optional per-spec: "delete_id" (supersede an old alert),
 *                            "exchange" (default BATS)
 * Exit:   0 = all wired, 1 = one or more failed, 2 = usage error.
 *
 * Every alert is created fire-once (auto_deactivate) with mobile push on, matching
 * the rest of the board. VERIFY AFTER RUNNING - this prints ids, it does not prove
 * the board is right; re-list and check.
 */
import fs from 'fs';
import { connect, evaluate, disconnect } from '../src/connection.js';

const args = process.argv.slice(2);
const DRY = args.includes('--dry-run');
const specPath = args.find(a => !a.startsWith('--'));
if (!specPath) {
  console.error('usage: node scripts/wire_alerts.mjs <specs.json> [--dry-run]');
  process.exit(2);
}
const specs = JSON.parse(fs.readFileSync(specPath, 'utf8'));
if (!Array.isArray(specs) || !specs.length) {
  console.error('spec file must be a non-empty array');
  process.exit(2);
}
for (const s of specs) {
  if (!s.sym || typeof s.level !== 'number' || !s.message) {
    console.error('each spec needs sym, numeric level, and message: ' + JSON.stringify(s));
    process.exit(2);
  }
}
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

function pageOp(spec) {
  const ticker = spec.sym.includes(':') ? spec.sym : `${spec.exchange || 'BATS'}:${spec.sym}`;
  const symbolField =
    `={"symbol":"${ticker}","adjustment":"splits","currency-id":"USD"}`;
  const payload = {
    symbol: symbolField,
    resolution: '1',
    condition: {
      type: 'cross', frequency: 'on_first_fire',
      series: [{ type: 'barset' }, { type: 'value', value: spec.level }],
      cross_interval: true, resolution: '1',
    },
    expiration: null,
    auto_deactivate: true,
    expiration_policy: { time: null, policy: 'never' },
    email: false, sms_over_email: false, mobile_push: true,
    message: spec.message,
    sound_file: null, sound_duration: 0, popup: true,
    web_hook: null, name: '', active: true, ignore_warnings: true,
  };
  return `(function(){
    function post(url, body){
      var x = new XMLHttpRequest();
      x.open('POST', url, false);
      x.withCredentials = true;
      x.setRequestHeader('Content-Type','text/plain;charset=UTF-8');
      x.send(JSON.stringify(body));
      try { return JSON.parse(x.responseText); } catch(e){ return {parse_error: x.responseText.slice(0,150)}; }
    }
    var made = post('https://pricealerts.tradingview.com/create_alert',
                    {payload: ${JSON.stringify(payload)}});
    if (!made || made.s !== 'ok') return JSON.stringify({err:'create failed', resp: made});
    var newId = made.r && made.r.alert_id;
    var del = null;
    ${spec.delete_id ? `del = post('https://pricealerts.tradingview.com/delete_alerts',
                                   {payload:{alert_ids:[${spec.delete_id}]}});` : ''}
    return JSON.stringify({ok:true, new_id:newId, deleted: del ? del.s : 'n/a'});
  })()`;
}

async function main() {
  if (DRY) {
    for (const s of specs) {
      const t = s.sym.includes(':') ? s.sym : `${s.exchange || 'BATS'}:${s.sym}`;
      console.log(`[dry] ${t} @ ${s.level}${s.delete_id ? ` (replaces ${s.delete_id})` : ''}`);
      console.log(`      ${s.message}\n`);
    }
    return 0;
  }
  console.log(`[wire-alerts] ${specs.length} alert(s) - connecting via CDP...`);
  await connect();
  let failed = 0;
  for (const s of specs) {
    let res;
    try { res = JSON.parse(await evaluate(pageOp(s))); }
    catch (e) { res = { err: String(e).slice(0, 150) }; }
    if (res && res.ok) {
      console.log(`[wire-alerts] ${s.sym} @ ${s.level}: id ${res.new_id}`
        + (s.delete_id ? ` (old ${s.delete_id} delete=${res.deleted})` : ''));
    } else {
      console.error(`[wire-alerts] ${s.sym} @ ${s.level}: FAILED - ${JSON.stringify(res)}`);
      failed++;
    }
    await sleep(1500);
  }
  await disconnect();
  return failed ? 1 : 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[wire-alerts] ' + e); process.exit(1); });
