#!/usr/bin/env python3
"""ROTATION DRILLDOWN (Omar standing order 8/7): a group newly IGNITING owes
CALL cards on its biggest movers; a group newly ROLLING owes PUT cards on its
biggest losers. Ranks each due group's names by move + direction-aware
readiness + liquidity; writes watchlists/rotation-drilldown-cards.json for the
next brief's mandatory protocol pass. Candidate filter reflects the 8/7
winner-traits scan (trend strength, control, prefer smaller liquid names).
Usage: python scripts/rotation_drilldown.py [--force TICKER DIRECTION]"""
import json, sys, datetime as dt
from pathlib import Path
import requests
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from rotation_radar import UNIVERSE

def scan_names(names, direction):
    cands = [f"{ex}:{n}" for n in names for ex in ("NASDAQ", "NYSE", "AMEX")]
    r = requests.post("https://scanner.tradingview.com/america/scan", json={
        "symbols": {"tickers": cands, "query": {"types": []}},
        "columns": ["name","close","change","Perf.W","ADX","ADX+DI","ADX-DI",
                    "average_volume_10d_calc","market_cap_basic","earnings_release_next_date"]},
        timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    rows = {}
    for e in r.json().get("data", []):
        v = e["d"]
        if v[1] is None or v[0] in rows: continue
        dv = (v[7] or 0) * v[1] / 1e6
        di = (v[5] or 0) - (v[6] or 0)
        ok_dir = di > 0 if direction == "CALL" else di < 0
        rows[v[0]] = {"sym": v[0], "close": v[1], "day": round(v[2] or 0, 1),
                      "week": round(v[3] or 0, 1), "adx": round(v[4] or 0),
                      "di_margin": round(di, 1), "dvol_m": round(dv),
                      "mcap_b": round((v[8] or 0) / 1e9, 1),
                      "next_earn": v[9], "direction_ok": ok_dir,
                      "liquid": dv >= 50}
    key = (lambda x: -x["week"]) if direction == "CALL" else (lambda x: x["week"])
    return sorted(rows.values(), key=key)

def main():
    today = dt.date.today().isoformat()
    due_p = REPO / "watchlists" / "radar-cards-due.json"
    if "--force" in sys.argv:
        i = sys.argv.index("--force")
        due = [{"group": sys.argv[i+1], "ticker": sys.argv[i+1],
                "direction": sys.argv[i+2].upper(), "accel": None}]
    elif due_p.exists():
        due = json.loads(due_p.read_text())
    else:
        print("[drilldown] no cards due"); return 0
    out = []
    for d in due:
        hint = UNIVERSE.get(d["ticker"], (d["group"], ""))[1]
        names = [w.strip().upper() for w in hint.replace("+", " ").split()
                 if w.isupper() and 1 < len(w) <= 5]
        if not names:
            print(f"[drilldown] {d['group']}: no member hints - vehicle card only"); continue
        ranked = scan_names(sorted(set(names)), d["direction"])
        top = [r for r in ranked if r["direction_ok"] and r["liquid"]][:3]
        out.append({"date": today, "group": d["group"], "vehicle": d["ticker"],
                    "direction": d["direction"], "accel": d.get("accel"),
                    "candidates": top, "all_ranked": ranked[:8],
                    "status": "PROTOCOL PENDING - card in next brief is MANDATORY"})
        print(f"[drilldown] {d['group']} ({d['direction']}): "
              + (", ".join(f"{t['sym']} wk{t['week']:+.0f}% ADX{t['adx']}" for t in top) or "no name passed direction+liquidity"))
    if out:
        (REPO / "watchlists" / "rotation-drilldown-cards.json").write_text(json.dumps(out, indent=1))
        print(f"[drilldown] wrote {len(out)} group card-set(s)")
    # 8/8 audit: consume the due-file so yesterday's promotions cannot re-owe
    # cards every night until the next state change overwrites them.
    if "--force" not in sys.argv and due_p.exists():
        due_p.rename(REPO / "watchlists" / f"radar-cards-due-done-{today}.json")
    return 0

if __name__ == "__main__":
    sys.exit(main())
