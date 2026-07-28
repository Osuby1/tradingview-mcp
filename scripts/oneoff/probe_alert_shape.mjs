#!/usr/bin/env node
/* Read-only: print the raw shape of one price alert, so a NEW-symbol alert can be
 * built correctly. The clone-a-same-symbol-alert trick used by ratchet_alerts.mjs
 * cannot work for a symbol that has no alerts yet (JNJ/DGX, 2026-07-28).
 * Creates nothing, deletes nothing.
 */
import { connect, evaluate, disconnect } from '../../src/connection.js';

const op = `(function(){
  var x = new XMLHttpRequest();
  x.open('GET','https://pricealerts.tradingview.com/list_alerts', false);
  x.withCredentials = true;
  x.send();
  var all = (JSON.parse(x.responseText).r) || [];
  var hit = null;
  all.forEach(function(al){
    if (!hit && (al.symbol||'').indexOf(':SJM"') > -1 && al.condition
        && (al.condition.series||[]).some(function(s){ return s.type==='value'; })) hit = al;
  });
  if (!hit) return JSON.stringify({err:'no SJM price alert found'});
  return JSON.stringify({
    symbol_field_raw: hit.symbol,
    symbol_field_type: typeof hit.symbol,
    resolution: hit.resolution,
    condition: hit.condition,
    keys: Object.keys(hit)
  });
})()`;

await connect();
console.log(await evaluate(op));
await disconnect();
