#!/usr/bin/env node
/* Retire (delete) TradingView alerts by id, safely.
 *
 * WHY: the standing protocol says "delete stale alerts on exits", and stale alerts
 * are not harmless clutter - they are actively dangerous. Found 2026-07-28: two
 * JNJ alerts from 7/14 (245 "dip-buy zone -> starter long", 243 "Chandelier stop
 * -> exit if long") sat active on the board while a NEW JNJ plan used 245.17 as its
 * STOP. Had JNJ fallen there, two alerts would have fired within pennies of each
 * other giving opposite instructions.
 *
 * SAFETY: this READS each alert first and prints its symbol, level and message, so
 * the thing being destroyed is seen before it is destroyed. --dry-run stops there.
 * Anything not found is reported and skipped rather than silently "succeeding".
 *
 * Usage:  node scripts/retire_alerts.mjs <id> [<id> ...] [--dry-run]
 * Exit:   0 = all requested ids gone, 1 = one or more failed/not found, 2 = usage.
 */
import { connect, evaluate, disconnect } from '../src/connection.js';

const args = process.argv.slice(2);
const DRY = args.includes('--dry-run');
const ids = args.filter(a => !a.startsWith('--')).map(Number);
if (!ids.length || ids.some(n => !Number.isFinite(n))) {
  console.error('usage: node scripts/retire_alerts.mjs <alert_id> [<alert_id> ...] [--dry-run]');
  process.exit(2);
}

function inspectOp(idList) {
  return `(function(){
    var x = new XMLHttpRequest();
    x.open('GET','https://pricealerts.tradingview.com/list_alerts', false);
    x.withCredentials = true;
    x.send();
    var all = (JSON.parse(x.responseText).r) || [];
    var want = ${JSON.stringify(idList)};
    var out = [];
    want.forEach(function(id){
      var hit = null;
      all.forEach(function(al){ if (al.alert_id === id) hit = al; });
      if (!hit) { out.push({id:id, found:false}); return; }
      var lvl = null;
      ((hit.condition||{}).series||[]).forEach(function(s){ if (s.type==='value') lvl = s.value; });
      out.push({id:id, found:true, symbol:hit.symbol, level:lvl, active:hit.active,
                message:(hit.message||'').slice(0,220), created:hit.create_time});
    });
    return JSON.stringify(out);
  })()`;
}

function deleteOp(idList) {
  return `(function(){
    var x = new XMLHttpRequest();
    x.open('POST','https://pricealerts.tradingview.com/delete_alerts', false);
    x.withCredentials = true;
    x.setRequestHeader('Content-Type','text/plain;charset=UTF-8');
    x.send(JSON.stringify({payload:{alert_ids:${JSON.stringify(idList)}}}));
    try { return x.responseText.slice(0,200); } catch(e){ return 'no response'; }
  })()`;
}

function verifyOp(idList) {
  return `(function(){
    var x = new XMLHttpRequest();
    x.open('GET','https://pricealerts.tradingview.com/list_alerts', false);
    x.withCredentials = true;
    x.send();
    var all = (JSON.parse(x.responseText).r) || [];
    var still = [];
    ${JSON.stringify(idList)}.forEach(function(id){
      all.forEach(function(al){ if (al.alert_id === id) still.push(id); });
    });
    return JSON.stringify(still);
  })()`;
}

async function main() {
  await connect();
  const found = JSON.parse(await evaluate(inspectOp(ids)));
  console.log('[retire] targets:');
  for (const f of found) {
    if (!f.found) { console.log(`  ${f.id}  *** NOT FOUND - already gone? ***`); continue; }
    const tk = (String(f.symbol).match(/"symbol":"([^"]+)"/) || [, f.symbol])[1];
    console.log(`  ${f.id}  ${tk} @ ${f.level}  active=${f.active}`);
    console.log(`        "${f.message}"`);
  }
  const live = found.filter(f => f.found).map(f => f.id);
  if (!live.length) { console.log('[retire] nothing to delete'); await disconnect(); return 1; }
  if (DRY) { console.log('[retire] --dry-run: nothing deleted'); await disconnect(); return 0; }

  console.log(`[retire] deleting ${live.length}...`);
  console.log('[retire] response: ' + await evaluate(deleteOp(live)));
  const still = JSON.parse(await evaluate(verifyOp(live)));
  await disconnect();
  if (still.length) { console.error('[retire] FAILED - still present: ' + still.join(', ')); return 1; }
  console.log('[retire] VERIFIED gone: ' + live.join(', '));
  return 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[retire] ' + e); process.exit(1); });
