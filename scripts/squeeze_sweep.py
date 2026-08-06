"""Market-wide short-interest sweep -> the squeeze tinder list.

DATA SOURCES (rebuilt 2026-08-06 after Omar's challenge "why is Yahoo still
being used when we have TradeStation and TradingView?"):
  - SHORT INTEREST: FINRA consolidated short interest API (free, no auth,
    BULK). This is the authoritative source of record - the same data Yahoo
    scrapes and republishes. Bi-weekly settlement. Gives short position,
    days-to-cover, AND the change vs prior period (shorts building vs
    covering - a signal the Yahoo path never provided).
  - FLOAT: TradingView scanner (float_shares_outstanding), one bulk call.
  - Yahoo/yfinance: NO LONGER USED. The old path made ~1,200 individual
    HTTP calls and got throttled on ~460 names on 8/5, which is exactly how
    IOVA (25.8% SI) was missing from the tinder list when it ignited +41%.

Neither TradeStation's Web API nor TradingView's scanner exposes short
interest (verified 8/6: all five TV short-interest columns return null), so
FINRA is the correct upstream - not a fallback.

Usage: python scripts/squeeze_sweep.py [--write]   (--write updates squeeze-watch.json tinder)
"""
import csv
import json
import sys
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent.parent
RUSSELL = Path(r"C:\Users\osuby\Documents\Equities_Scanner\russell_starter.csv")
CFG = REPO / "watchlists" / "squeeze-watch.json"
OUT = REPO / "watchlists" / "squeeze-sweep-results.json"
FINRA = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
TVSCAN = "https://scanner.tradingview.com/america/scan"
SI_BAR = 15.0          # % of float to make the tinder list
MIN_CAP = 500e6
MIN_VOL = 300_000


def universe():
    syms = set()
    if RUSSELL.exists():
        with open(RUSSELL) as f:
            for row in csv.reader(f):
                s = row[0].strip().upper()
                if s and s != "SYMBOL":
                    syms.add(s)
    wl = REPO / "watchlists" / "main-watchlist.md"
    if wl.exists():
        for line in wl.read_text(encoding="utf-8").splitlines():
            if line.startswith("AAPL,"):
                syms.update(t.strip() for t in line.split(",") if t.strip().isalpha())
    if CFG.exists():
        for t in json.loads(CFG.read_text(encoding="utf-8"))["tinder"]:
            syms.add(t["sym"].split(":")[1])
    return sorted(syms)


def finra_short_interest(symbols):
    """Bulk-fetch the latest short interest per symbol. Returns {sym: record}."""
    out = {}
    for i in range(0, len(symbols), 200):
        chunk = symbols[i:i + 200]
        body = {"limit": 5000,
                "compareFilters": [{"fieldName": "settlementDate",
                                    "fieldValue": "2026-06-01", "compareType": "GTE"}],
                "domainFilters": [{"fieldName": "symbolCode", "values": chunk}]}
        try:
            r = requests.post(FINRA, json=body, timeout=60,
                              headers={"Content-Type": "application/json", "Accept": "application/json"})
            r.raise_for_status()
            for rec in r.json():
                s = rec.get("symbolCode")
                prev = out.get(s)
                # keep the most recent settlement per symbol
                if not prev or (rec.get("settlementDate") or "") > (prev.get("settlementDate") or ""):
                    out[s] = rec
        except Exception as e:
            print(f"  FINRA chunk {i//200} failed: {e}", file=sys.stderr)
        print(f"  FINRA {min(i+200, len(symbols))}/{len(symbols)}", flush=True)
    return out


def tv_fundamentals(symbols):
    """Bulk float/cap/volume/price from the TV scanner. Returns {sym: dict}."""
    out = {}
    cols = ["name", "close", "float_shares_outstanding", "market_cap_basic",
            "average_volume_10d_calc", "price_52_week_high"]
    for i in range(0, len(symbols), 400):
        chunk = symbols[i:i + 400]
        tickers = [f"{ex}:{s}" for s in chunk for ex in ("NYSE", "NASDAQ", "AMEX")]
        try:
            r = requests.post(TVSCAN, json={"symbols": {"tickers": tickers}, "columns": cols}, timeout=60)
            r.raise_for_status()
            for row in r.json().get("data", []):
                d = row["d"]
                if d[0] not in out and d[2]:
                    out[d[0]] = {"full": row["s"], "close": d[1], "float": d[2],
                                 "cap": d[3], "avg_vol": d[4], "high52": d[5]}
        except Exception as e:
            print(f"  TV chunk {i//400} failed: {e}", file=sys.stderr)
    return out


def main():
    syms = universe()
    print(f"sweeping {len(syms)} symbols (FINRA short interest + TV float)...")
    si = finra_short_interest(syms)
    print(f"  FINRA returned {len(si)} symbols with short-interest records")
    fun = tv_fundamentals(syms)
    print(f"  TV returned {len(fun)} symbols with float data")

    rows = []
    for s, rec in si.items():
        f = fun.get(s)
        if not f or not f.get("float"):
            continue
        shares_short = rec.get("currentShortPositionQuantity") or 0
        si_pct = round(100.0 * shares_short / f["float"], 1)
        if si_pct < SI_BAR or (f.get("cap") or 0) < MIN_CAP or (f.get("avg_vol") or 0) < MIN_VOL:
            continue
        rows.append({
            "sym": f["full"], "si_pct_float": si_pct,
            "days_to_cover": rec.get("daysToCoverQuantity"),
            "si_change_pct": rec.get("changePercent"),      # NEW: building vs covering
            "float_m": round(f["float"] / 1e6, 1),
            "pct_of_52wk_high": round(100.0 * f["close"] / f["high52"], 1) if f.get("high52") else None,
            "si_asof": rec.get("settlementDate"),
        })
    rows.sort(key=lambda r: -r["si_pct_float"])
    OUT.write_text(json.dumps({"swept": len(syms), "hits": rows}, indent=1))

    print(f"\n{len(rows)} names at/above {SI_BAR}% SI (cap>=${MIN_CAP/1e6:.0f}M, vol>={MIN_VOL:,}):\n")
    print(f"{'SYM':<6}{'SI%':>6}{'DTC':>7}{'SIchg%':>8}{'Float(M)':>10}{'%52wkHi':>9}  as-of")
    for r in rows[:40]:
        print(f"{r['sym'].split(':')[1]:<6}{r['si_pct_float']:>6}{str(r['days_to_cover']):>7}"
              f"{str(r['si_change_pct']):>8}{r['float_m']:>10}{str(r['pct_of_52wk_high']):>9}  {r['si_asof']}")

    if "--write" in sys.argv and rows:
        cfg = json.loads(CFG.read_text(encoding="utf-8"))
        keep_notes = {t["sym"]: t.get("note") for t in cfg["tinder"] if t.get("note")}
        for r in rows:
            if r["sym"] in keep_notes:
                r["note"] = keep_notes[r["sym"]]
        cfg["tinder"] = rows
        cfg["short_interest_asof"] = (f"FINRA consolidated short interest, settlement "
                                      f"{rows[0].get('si_asof')} (bulk, authoritative; Yahoo retired 8/6)")
        CFG.write_text(json.dumps(cfg, indent=1))
        print(f"\nwrote {len(rows)} names to squeeze-watch.json tinder")
    return 0


if __name__ == "__main__":
    sys.exit(main())
