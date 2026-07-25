"""Block until the in-page O.G sweep (window.__og) finishes, printing progress.

    python scripts/og_sweep_wait.py [max_minutes]

Companion to og_sweep_start.py / og_sweep_pull.py. Exits non-zero if the sweep
is missing or does not finish inside the time budget, so a batch step can tell
"finished" from "still grinding" without the agent polling by hand.
"""
import asyncio
import json
import sys
import time
import urllib.request

import websockets

CDP_HTTP = "http://localhost:9222/json/list"
META = ("window.__og ? JSON.stringify({done:window.__og.done,"
        "idx:window.__og.idx,total:window.__og.total,"
        "got:window.__og.results.length,errs:window.__og.errs.length,"
        "ok:window.__og.results.filter(function(r){return r.ok}).length}) : null")


async def evaluate(ws, expr, req_id):
    await ws.send(json.dumps({"id": req_id, "method": "Runtime.evaluate",
                              "params": {"expression": expr, "returnByValue": True}}))
    while True:
        msg = json.loads(await ws.recv())
        if msg.get("id") == req_id:
            return msg["result"]["result"].get("value")


async def main(max_minutes):
    targets = json.load(urllib.request.urlopen(CDP_HTTP, timeout=10))
    tv = [t for t in targets
          if "tradingview.com" in (t.get("url") or "") and t.get("webSocketDebuggerUrl")]
    if not tv:
        sys.exit("No TradingView target on :9222")

    deadline = time.time() + max_minutes * 60
    req = 0
    last_got, stalled_since = -1, time.time()
    async with websockets.connect(tv[0]["webSocketDebuggerUrl"],
                                  ping_interval=None) as ws:
        while True:
            req += 1
            raw = await evaluate(ws, META, req)
            if not raw:
                sys.exit("window.__og not present - sweep never started")
            m = json.loads(raw)
            if m["got"] != last_got:
                last_got, stalled_since = m["got"], time.time()
            print("%d/%d ok=%d errs=%d" % (m["got"], m["total"], m["ok"], m["errs"]),
                  flush=True)
            if m["done"]:
                print("DONE %d/%d ok=%d" % (m["got"], m["total"], m["ok"]))
                return
            if time.time() - stalled_since > 600:
                sys.exit("STALLED at %d/%d for 10 min" % (m["got"], m["total"]))
            if time.time() > deadline:
                sys.exit("TIMEOUT at %d/%d after %s min" % (m["got"], m["total"], max_minutes))
            await asyncio.sleep(45)


if __name__ == "__main__":
    asyncio.run(main(float(sys.argv[1]) if len(sys.argv) > 1 else 60))
