#!/usr/bin/env node
/* Push squeeze-watch hits to Omar's phone via INSTANT-FIRE TradingView alerts.
 *
 * Reads watchlists/squeeze-hits.json (written by squeeze_watch_local.py).
 * For each hit: create a fire-once price-cross alert a hair below the live
 * price (crosses fire on the next tick - the "prefill equals current price
 * fires instantly" behavior, used deliberately). mobile_push:true delivers
 * to the phone through TV's proven channel. auto_deactivate keeps the board
 * clean; the alert is its own notification, not a standing level.
 *
 * Same REST-in-page pattern as ratchet_alerts.mjs (text/plain sync XHR,
 * {payload:...} envelope, ~1.5s spacing). Exit 0 = all pushed.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { connect, evaluate, disconnect } from '../src/connection.js';

const REPO = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const HITS = path.join(REPO, 'watchlists', 'squeeze-hits.json');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

function pageOp(hit) {
  // 'greater' with a level already far below the live price is TRUE on the
  // first evaluation -> the alert fires (and pushes) within seconds, then
  // auto-deactivates. The alert IS the notification.
  return `(function(){
    var h = ${JSON.stringify(hit)};
    var level = h.price ? h.price * 0.9 : 1;
    var p = { symbol: '={"symbol":"' + h.sym + '","adjustment":"splits","currency-id":"USD"}',
      resolution: '1',
      condition: {type:'greater', frequency:'on_first_fire',
                  series:[{type:'barset'},{type:'value', value: level}],
                  cross_interval: false, resolution:'1'},
      expiration: null, auto_deactivate: true,
      expiration_policy: {time: null, policy: 'never'},
      email: false, sms_over_email: false, mobile_push: true,
      message: h.msg, sound_file: null, sound_duration: 0, popup: true,
      web_hook: null, name: '', active: true, ignore_warnings: true };
    var x = new XMLHttpRequest();
    x.open('POST','https://pricealerts.tradingview.com/create_alert', false);
    x.withCredentials = true;
    x.setRequestHeader('Content-Type','text/plain;charset=UTF-8');
    x.send(JSON.stringify({payload: p}));
    try { var r = JSON.parse(x.responseText); return JSON.stringify({s: r.s, id: r.r && r.r.alert_id}); }
    catch(e){ return JSON.stringify({err: x.responseText.slice(0,120)}); }
  })()`;
}

async function main() {
  if (!fs.existsSync(HITS)) { console.log('[push] no hits file'); return 0; }
  const hits = JSON.parse(fs.readFileSync(HITS, 'utf8'));
  if (!hits.length) { fs.unlinkSync(HITS); return 0; }
  await connect();
  let fails = 0;
  for (const h of hits) {
    const res = await evaluate(pageOp(h));
    console.log(`[push] ${h.sym}: ${res}`);
    if (!String(res).includes('"s":"ok"')) fails++;
    await sleep(1500);
  }
  await disconnect();
  fs.unlinkSync(HITS);
  return fails ? 1 : 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[push] fatal:', e.message); process.exit(2); });
