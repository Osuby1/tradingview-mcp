"""Pull a finished in-page O.G sweep (window.__og) straight to disk over CDP.

WHICH SWEEP SCRIPT DO I WANT?
  * Nightly / automated  -> scripts/og_sweep_cdp.mjs (does start + wait + pull
    in one deterministic Node process; this is what run_eod_chain.bat calls).
  * Manual or RECOVERY   -> og_sweep_start.py -> og_sweep_wait.py -> THIS FILE.
    The three-step lane exists because it can attach to a sweep ALREADY RUNNING
    in the page. If the automated driver dies mid-sweep, this pulls the results
    the page still holds instead of re-reading 490 symbols. That is how the
    2026-07-24 run was recovered.

Why this exists
---------------
A 492-name sweep is ~400 KB of JSON. Returning that through ui_evaluate means
paging it back through the agent's context in chunks - expensive, and every
chunk is a transcription risk. The sweep already lives in the browser; this
copies it to a file without anyone reading it.

    python scripts/og_sweep_pull.py watchlists/og-sweep-raw-2026-07-23-heikinashi.json

Exits non-zero if the sweep is missing, still running, or was read on any chart
style but Heikin Ashi (Omar's standing decision as of 2026-07-23). The style
check is duplicated here on purpose: og_sweep_runner.js refuses to START on the
wrong style, and this refuses to SAVE from the wrong style, so a sweep begun
before a style change can never quietly land in the repo.
"""
import asyncio
import json
import sys
import urllib.request

import websockets

CDP_HTTP = "http://localhost:9222/json/list"


async def evaluate(ws, expr, req_id):
    await ws.send(json.dumps({
        "id": req_id,
        "method": "Runtime.evaluate",
        "params": {"expression": expr, "returnByValue": True,
                   "awaitPromise": True},
    }))
    while True:
        msg = json.loads(await ws.recv())
        if msg.get("id") == req_id:
            if "error" in msg:
                raise RuntimeError(msg["error"])
            res = msg["result"]
            if res.get("exceptionDetails"):
                raise RuntimeError(res["exceptionDetails"])
            return res["result"].get("value")


async def main(out_path):
    targets = json.load(urllib.request.urlopen(CDP_HTTP, timeout=10))
    tv = [t for t in targets
          if "tradingview.com" in (t.get("url") or "") and t.get("webSocketDebuggerUrl")]
    if not tv:
        sys.exit("No TradingView target on :9222")

    async with websockets.connect(tv[0]["webSocketDebuggerUrl"],
                                  max_size=64 * 1024 * 1024,
                                  ping_interval=None) as ws:
        meta_raw = await evaluate(ws, (
            "window.__og ? JSON.stringify({done:window.__og.done,"
            "total:window.__og.total,got:window.__og.results.length,"
            "style:window.__og.style,style_name:window.__og.style_name,"
            "tag:window.__og.tag,errs:window.__og.errs.length}) : null"), 1)
        if not meta_raw:
            sys.exit("window.__og not present - sweep never started")
        m = json.loads(meta_raw)
        if not m["done"]:
            sys.exit("sweep still running (%d/%d)" % (m["got"], m["total"]))
        if m["style"] != 8:
            sys.exit("REFUSED: sweep ran on %s, not Heikin Ashi" % m["style_name"])

        payload = await evaluate(ws, "JSON.stringify(window.__og.results)", 2)

    if not payload:
        sys.exit("empty payload")
    rows = json.loads(payload)
    if len(rows) != m["total"]:
        sys.exit("length mismatch: %d rows vs total %d" % (len(rows), m["total"]))
    wrong = [r for r in rows if r.get("style") != 8]
    if wrong:
        sys.exit("REFUSED: %d rows not read on Heikin Ashi" % len(wrong))

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1)

    ok = [r for r in rows if r.get("ok")]
    bars = {}
    for r in rows:
        bars[r.get("bar_date")] = bars.get(r.get("bar_date"), 0) + 1
    print("wrote %d rows -> %s" % (len(rows), out_path))
    print("  tag=%s style=%s ok=%d not_ok=%d errs=%d"
          % (m["tag"], m["style_name"], len(ok), len(rows) - len(ok), m["errs"]))
    print("  bar dates: %s" % json.dumps(bars))
    if len(ok) != len(rows):
        print("  NOT OK: %s" % ", ".join(
            "%s:%s" % (r.get("req"), r.get("why")) for r in rows if not r.get("ok")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: og_sweep_pull.py <outfile.json>")
    asyncio.run(main(sys.argv[1]))
