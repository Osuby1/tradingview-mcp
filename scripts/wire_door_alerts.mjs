#!/usr/bin/env node
/* Execute A-List door-alert actions on TradingView via CDP.
 *
 * Reads watchlists/door-actions.json: [{op:create|delete|audit, ...}]
 *  - create: fire-once price-cross alert AT the plan entry (a real door,
 *    not instant-fire) with the full plan in the message; writes alert_id
 *    back into the actions file for a_list.py to persist.
 *  - delete: remove a door whose name dropped off the A-List.
 *  - audit: report last_fire_time for a door (conversion tracking).
 * Same REST-in-page pattern as ratchet/squeeze pushers.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { connect, evaluate, disconnect } from '../src/connection.js';

const REPO = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const ACTIONS = path.join(REPO, 'watchlists', 'door-actions.json');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

function js(action) {
  return `(function(){
    var a = ${JSON.stringify(action)};
    function req(method, url, body){
      var x = new XMLHttpRequest();
      x.open(method, url, false);
      x.withCredentials = true;
      if (body) x.setRequestHeader('Content-Type','text/plain;charset=UTF-8');
      x.send(body ? JSON.stringify(body) : null);
      try { return JSON.parse(x.responseText); } catch(e){ return {err: x.responseText.slice(0,120)}; }
    }
    if (a.op === 'delete') {
      var d = req('POST','https://pricealerts.tradingview.com/delete_alerts', {payload:{alert_ids:[a.alert_id]}});
      return JSON.stringify({deleted: d.s === 'ok'});
    }
    if (a.op === 'audit') {
      var l = req('GET','https://pricealerts.tradingview.com/list_alerts');
      var arr = (l.r && l.r.alerts) || l.r || [];
      var hit = arr.filter(function(x){ return x.alert_id === a.alert_id; })[0];
      return JSON.stringify({fired: hit ? hit.last_fire_time : 'GONE'});
    }
    var p = { symbol: '={"symbol":"' + a.sym + '","adjustment":"splits","currency-id":"USD"}',
      resolution: '1',
      condition: {type:'cross', frequency:'on_first_fire',
                  series:[{type:'barset'},{type:'value', value: a.level}],
                  cross_interval: true, resolution:'1'},
      expiration: null, auto_deactivate: true,
      expiration_policy: {time: null, policy: 'never'},
      email: false, sms_over_email: false, mobile_push: true,
      message: a.msg, sound_file: null, sound_duration: 0, popup: true,
      web_hook: null, name: '', active: true, ignore_warnings: true };
    var r = req('POST','https://pricealerts.tradingview.com/create_alert', {payload: p});
    return JSON.stringify({s: r.s, id: r.r && r.r.alert_id});
  })()`;
}

async function main() {
  if (!fs.existsSync(ACTIONS)) { console.log('[doors] no actions'); return 0; }
  const actions = JSON.parse(fs.readFileSync(ACTIONS, 'utf8'));
  if (!actions.length) return 0;
  await connect();
  let fails = 0;
  for (const a of actions) {
    const res = JSON.parse(await evaluate(js(a)));
    if (a.op === 'create') {
      if (res.s === 'ok') { a.alert_id = res.id; console.log(`[doors] wired ${a.sym} @ ${a.level} -> ${res.id}`); }
      else { fails++; console.log(`[doors] FAILED ${a.sym}:`, JSON.stringify(res)); }
    } else if (a.op === 'delete') {
      console.log(`[doors] deleted ${a.sym} (${a.alert_id}): ${res.deleted}`);
    } else if (a.op === 'audit') {
      a.fired = res.fired && res.fired !== 'GONE' ? res.fired : null;
      if (a.fired) console.log(`[doors] ${a.sym} FIRED ${a.fired}`);
    }
    await sleep(1500);
  }
  fs.writeFileSync(ACTIONS, JSON.stringify(actions, null, 1));
  await disconnect();
  return fails ? 1 : 0;
}

main().then(c => process.exit(c)).catch(e => { console.error('[doors] fatal:', e.message); process.exit(2); });
