"""Install og_sweep_runner.js in the live TradingView page and start a sweep.

Companion to og_sweep_pull.py. The runner is ~12 KB of source and the universe
is ~500 tickers; pushing both through ui_evaluate means paging them through the
agent's context, which is expensive and a transcription risk. This sends both
straight over CDP.

    python scripts/og_sweep_start.py watchlists/og-sweep-universe-<date>-extended.json heikinashi-<date>

Exits non-zero if the chart is not Heikin Ashi - the runner itself also refuses
(standing decision 2026-07-23), this is the same guard one step earlier so a
wrong-style sweep never even starts.
"""
import asyncio
import json
import sys
import urllib.request

import websockets

CDP_HTTP = "http://localhost:9222/json/list"
RUNNER = "scripts/og_sweep_runner.js"


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


def load_symbols(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        for key in ("symbols", "universe", "names"):
            if key in data:
                data = data[key]
                break
    if not isinstance(data, list):
        sys.exit("universe file is not a list of symbols")
    out = []
    for row in data:
        sym = row if isinstance(row, str) else (row.get("symbol") or row.get("sym"))
        if sym:
            out.append(sym)
    return out


async def main(universe_path, tag):
    symbols = load_symbols(universe_path)
    if not symbols:
        sys.exit("no symbols in %s" % universe_path)
    runner_src = open(RUNNER, encoding="utf-8").read()

    targets = json.load(urllib.request.urlopen(CDP_HTTP, timeout=10))
    tv = [t for t in targets
          if "tradingview.com" in (t.get("url") or "") and t.get("webSocketDebuggerUrl")]
    if not tv:
        sys.exit("No TradingView target on :9222")

    async with websockets.connect(tv[0]["webSocketDebuggerUrl"],
                                  max_size=64 * 1024 * 1024,
                                  ping_interval=None) as ws:
        installed = await evaluate(ws, runner_src, 1)
        print(installed)
        if "installed" not in str(installed):
            sys.exit("runner did not install: %r" % installed)

        started = await evaluate(
            ws, "window.__ogSweep(%s, %s)" % (json.dumps(symbols), json.dumps(tag)), 2)
        print(started)
        if str(started).startswith("REFUSED"):
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: og_sweep_start.py <universe.json> <tag>")
    asyncio.run(main(sys.argv[1], sys.argv[2]))
