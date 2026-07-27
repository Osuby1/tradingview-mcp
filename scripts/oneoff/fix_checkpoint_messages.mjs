#!/usr/bin/env node
/* One-off: correct the four CHECKPOINT alert messages (2026-07-27).
 *
 * WHY: the checkpoint alerts were written 7/25, when the stops were still the
 * Chandelier levels (DVN 43.90 / HAS 84.30 / SJM 112.50 / MLI 60.30). On 7/26
 * the stops moved to 5%-below-entry (42.85 / 83.76 / 111.35 / 60.35) but the
 * checkpoint MESSAGE TEXT was never updated - so if one fired, the push would
 * quote a stop level that no longer exists. Prices/conditions were always
 * correct; this is a text-only correction.
 *
 * Also adds the ratchet ARMING level to each message (0.8 x high > stop, i.e.
 * ~+18.75% above entry given a 5% stop) so the note says when the trail starts
 * mattering instead of the vague "once well in profit".
 *
 * Method: identical to scripts/ratchet_alerts.mjs - clone an existing alert on
 * the same symbol as the payload template, set price + new message, create it
 * fire-once, delete the superseded one. Same sync-XHR text/plain REST pattern.
 *
 * Usage: node scripts/oneoff/fix_checkpoint_messages.mjs [--dry-run]
 * Exit:  0 = all four rewired, 1 = one or more failed.
 */
import { connect, evaluate, disconnect } from '../../src/connection.js';

const DRY = process.argv.includes('--dry-run');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const ACTIONS = [
  {
    sym: 'DVN', level: 47.5, delete_id: 5226932947,
    message: 'DVN 47.50 = CHECKPOINT only - do NOT sell. LONG 1000 @ 45.11. '
      + 'The old 2:1 target was RETIRED 7/25 (measured: targets cap the tail winners). '
      + 'Exits = stop 42.85 (5% below entry, set 7/26) / thesis break / 20% trail below '
      + 'the highest close, which only ARMS above 53.56. '
      + 'STILL TRIM/EXIT BEFORE 8/4 EARNINGS regardless of any price rule.',
  },
  {
    sym: 'HAS', level: 95.8, delete_id: 5226932954,
    message: 'HAS 95.80 = CHECKPOINT only - do NOT sell. LONG 500 @ 88.17. '
      + 'The old 2:1 target was RETIRED 7/25 (measured: targets cap the tail winners). '
      + 'Exits = stop 83.76 (5% below entry, set 7/26) / thesis break / 20% trail below '
      + 'the highest close, which only ARMS above 104.70. Earnings ~10/22 (far).',
  },
  {
    sym: 'SJM', level: 126.6, delete_id: 5226932961,
    message: 'SJM 126.60 = CHECKPOINT only - do NOT sell. LONG 400 @ 117.21. '
      + 'The old 2:1 target was RETIRED 7/25 (measured: targets cap the tail winners). '
      + 'Exits = stop 111.35 (5% below entry, set 7/26) / thesis break / 20% trail below '
      + 'the highest close, which only ARMS above 139.19. Earnings ~9/1 (far).',
  },
  {
    sym: 'MLI', level: 70.0, delete_id: 5226932966,
    message: 'MLI 70.00 = CHECKPOINT only - do NOT sell. LONG 900 @ 63.53. '
      + 'The old 2:1 target was RETIRED 7/25 (measured: targets cap the tail winners). '
      + 'Exits = stop 60.35 (5% below entry, set 7/26) / thesis break (bounce-flip entry: '
      + 'a failed 50-day reclaim IS the thesis break) / 20% trail below the highest close, '
      + 'which only ARMS above 75.44. Earnings ~10/27 (far).',
  },
];

function pageOp(action) {
  // Runs in TV page context. Sync XHR so the result comes back from evaluate().
  return `(function(){
    function post(url, body){
      var x = new XMLHttpRequest();
      x.open('POST', url, false);
      x.withCredentials = true;
      x.setRequestHeader('Content-Type','text/plain;charset=UTF-8');
      x.send(JSON.stringify(body));
      try { return JSON.parse(x.responseText); } catch(e){ return {parse_error: x.responseText.slice(0,150)}; }
    }
    var a = ${JSON.stringify(action)};
    var x = new XMLHttpRequest();
    x.open('GET','https://pricealerts.tradingview.com/list_alerts', false);
    x.withCredentials = true;
    x.send();
    var all = (JSON.parse(x.responseText).r) || [];
    var tmpl = null;
    all.forEach(function(al){
      if (!tmpl && (al.symbol||'').indexOf(':' + a.sym + '"') > -1 && al.condition
          && (al.condition.series||[]).some(function(s){ return s.type==='value'; })) tmpl = al;
    });
    if (!tmpl) return JSON.stringify({err: 'no template alert found for ' + a.sym});
    var cond = JSON.parse(JSON.stringify(tmpl.condition));
    cond.series = cond.series.map(function(s){
      if (s.type === 'value') s.value = a.level;
      return s;
    });
    var p = { symbol: tmpl.symbol, resolution: tmpl.resolution, condition: cond,
      expiration: null, auto_deactivate: true,
      expiration_policy: {time: null, policy: 'never'},
      email: false, sms_over_email: false, mobile_push: true,
      message: a.message, sound_file: null, sound_duration: 0, popup: true,
      web_hook: null, name: '', active: true, ignore_warnings: true };
    var made = post('https://pricealerts.tradingview.com/create_alert', {payload: p});
    if (!made || made.s !== 'ok') return JSON.stringify({err: 'create failed', resp: made});
    var newId = made.r && made.r.alert_id;
    var del = null;
    if (a.delete_id) del = post('https://pricealerts.tradingview.com/delete_alerts',
                                {payload: {alert_ids: [a.delete_id]}});
    return JSON.stringify({ok: true, new_id: newId, deleted: del ? del.s : 'n/a'});
  })()`;
}

async function main() {
  if (DRY) {
    for (const a of ACTIONS) console.log(`[dry] ${a.sym} @ ${a.level} replaces ${a.delete_id}\n      ${a.message}\n`);
    return 0;
  }
  console.log('[checkpoint-fix] connecting via CDP...');
  await connect();
  let failed = 0;
  for (const a of ACTIONS) {
    let res;
    try { res = JSON.parse(await evaluate(pageOp(a))); }
    catch (e) { res = { err: String(e).slice(0, 150) }; }
    if (res && res.ok) {
      console.log(`[checkpoint-fix] ${a.sym} ${a.level}: new id ${res.new_id}, old ${a.delete_id} delete=${res.deleted}`);
    } else {
      console.error(`[checkpoint-fix] ${a.sym}: FAILED - ${JSON.stringify(res)}`);
      failed++;
    }
    await sleep(1500);
  }
  await disconnect();
  return failed ? 1 : 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[checkpoint-fix] ' + e); process.exit(1); });
