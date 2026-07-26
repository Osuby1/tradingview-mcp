#!/usr/bin/env node
/* Wire/raise the 20% trailing-ratchet alerts on TradingView.
 *
 * Consumes watchlists/ratchet-actions.json (written by ratchet_watch.py when a
 * position's 0.8-x-highest-close line rises above its stop, or above the alert
 * already wired). For each action: clone an existing alert on the same symbol
 * as the payload template (the stop alert is always there), set the new price
 * and message, create it fire-once, then delete the superseded ratchet alert.
 * Same proven REST-in-page pattern as the 7/25 manual rewire: text/plain sync
 * XHR, {payload:...} envelope, ~1.5s spacing.
 *
 * Updates open-book.json with the new alert id/level, deletes the actions file
 * on full success (keeps only the failed actions otherwise, so the next night
 * retries them without duplicating the ones that worked).
 *
 * Usage: node scripts/ratchet_alerts.mjs      (EOD chain step 4, after ratchet_watch)
 * Exit:  0 = ok / nothing to do, 1 = one or more actions failed.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { connect, evaluate, disconnect } from '../src/connection.js';

const REPO = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const ACTIONS = path.join(REPO, 'watchlists', 'ratchet-actions.json');
const BOOK = path.join(REPO, 'watchlists', 'open-book.json');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

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
  if (!fs.existsSync(ACTIONS)) { console.log('[ratchet] no actions file - nothing to do'); return 0; }
  const actions = JSON.parse(fs.readFileSync(ACTIONS, 'utf8'));
  if (!actions.length) { fs.unlinkSync(ACTIONS); return 0; }

  console.log(`[ratchet] ${actions.length} alert action(s) - connecting via CDP...`);
  await connect();
  const book = JSON.parse(fs.readFileSync(BOOK, 'utf8'));
  const failed = [];

  for (const a of actions) {
    let res;
    try { res = JSON.parse(await evaluate(pageOp(a))); }
    catch (e) { res = { err: String(e).slice(0, 150) }; }
    if (res && res.ok) {
      console.log(`[ratchet] ${a.sym}: alert at ${a.level} wired (id ${res.new_id}`
        + (a.delete_id ? `, old ${a.delete_id} delete=${res.deleted})` : ')'));
      const pos = book.positions.find(p => p.sym === a.sym);
      if (pos) pos.ratchet_alert = { id: res.new_id, level: a.level };
    } else {
      console.error(`[ratchet] ${a.sym}: FAILED - ${JSON.stringify(res)}`);
      failed.push(a);
    }
    await sleep(1500);
  }

  fs.writeFileSync(BOOK, JSON.stringify(book, null, 1));
  if (failed.length) fs.writeFileSync(ACTIONS, JSON.stringify(failed, null, 1));
  else fs.unlinkSync(ACTIONS);
  await disconnect();
  return failed.length ? 1 : 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[ratchet] ' + e); process.exit(1); });
