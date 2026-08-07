#!/usr/bin/env python3
"""GATE RE-CHECKER (Omar decision #6, 8/7): vetoes must expire.
GDX was vetoed 7/21 on regime and nobody re-looked for 3 weeks (+16%); PLTR was
ADX-blocked 8/4 and re-broke 8/7 (+$44/sh). Every recorded block gets re-tested
nightly against CURRENT data; anything now clear prints as UN-BLOCKED so it
re-enters the funnel loudly instead of never.
Registry: research/gate-blocks-registry.json - entries
  {sym, block, detail, added, resolved?}  block in: adx | regime | chain | date | ceiling
"""
import json, sys, datetime as dt
from pathlib import Path
import requests
REPO = Path(__file__).resolve().parent.parent
REG = REPO / "research" / "gate-blocks-registry.json"
sys.path.insert(0, str(REPO / "scripts"))
from gate_stack import ADX_MIN

def main():
    today = dt.date.today().isoformat()
    reg = json.loads(REG.read_text()) if REG.exists() else []
    live = [r for r in reg if not r.get("resolved")]
    if not live:
        print("[recheck] registry empty"); return 0
    syms = sorted({r["sym"] for r in live})
    cands = [f"{ex}:{s}" for s in syms for ex in ("NASDAQ","NYSE","AMEX")]
    rr = requests.post("https://scanner.tradingview.com/america/scan", json={
        "symbols": {"tickers": cands, "query": {"types": []}},
        "columns": ["name","close","ADX","SMA200","earnings_release_next_date","price_52_week_high"]},
        timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    data = {}
    for e in rr.json().get("data", []):
        v = e["d"]
        if v[1] is not None and v[0] not in data:
            data[v[0]] = {"close": v[1], "adx": v[2], "sma200": v[3], "next_earn": v[4], "h52": v[5]}
    unblocked, still = [], []
    for r in live:
        d = data.get(r["sym"]); ok, why = False, ""
        if not d: still.append(r); continue
        if r["block"] == "adx" and (d["adx"] or 0) >= ADX_MIN:
            ok, why = True, f"ADX now {d['adx']:.0f} >= {ADX_MIN:.0f}"
        elif r["block"] == "regime" and d["sma200"] and d["close"] > d["sma200"]:
            ok, why = True, f"back above the 200-day ({d['close']:.2f} > {d['sma200']:.2f})"
        elif r["block"] == "chain":
            try:
                from squeeze_watch_local import chain_gate
                ch = chain_gate(r["sym"], d["close"])
                if ch: ok, why = True, f"chain now tradeable: {ch['contract']} OI {ch['oi']} spread {ch['spread_pct']}%"
            except Exception as e: why = f"chain check failed: {e}"
        elif r["block"] == "date" and r.get("detail_date") and today >= r["detail_date"]:
            ok, why = True, f"date condition reached ({r['detail_date']})"
        elif r["block"] == "ceiling" and r.get("level") and d["close"] > float(r["level"]):
            ok, why = True, f"closed above the {r['level']} ceiling ({d['close']:.2f})"
        if ok:
            r["resolved"] = today; r["resolution"] = why
            unblocked.append(f"{r['sym']}: {why}  (blocked since {r['added']}: {r['detail']})")
        else:
            still.append(r)
    REG.write_text(json.dumps(reg, indent=1))
    print(f"[recheck] {len(live)} blocks tested - {len(unblocked)} UN-BLOCKED, {len(still)} standing")
    for u in unblocked: print("  UN-BLOCKED >> " + u)
    out = REPO / "reports" / f"gate-recheck-{today}.md"
    out.write_text("# Gate re-check " + today + "\n\n" +
        ("\n".join("- **UN-BLOCKED** " + u for u in unblocked) or "- nothing un-blocked") + "\n\n" +
        "\n".join(f"- standing: {r['sym']} ({r['block']}: {r['detail']})" for r in still) + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
