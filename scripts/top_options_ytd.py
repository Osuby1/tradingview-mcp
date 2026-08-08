#!/usr/bin/env python3
"""TOP OPTIONS CONTRACTS YTD (Omar 8/8): rank the most profitable listed option
contracts of 2026 by premium appreciation, with real daily bars.

METHOD: universe = top YTD stock movers both directions (TV scanner) + our
tracked movers. For each: calls above the January price on gainers, puts below
it on losers, across currently-listed expiries. TradeStation daily bars price
each contract from its first 2026 session; peak = highest daily close.

DECLARED LIMITS (printed on the sheet): (1) EXPIRED contracts are purged from
the feed - the true biggest winners (short-dated Feb-Jul expiries on the same
movers) cannot be priced; this is the SURVIVING-CONTRACT leaderboard. (2) Thin
contracts mark on sparse prints - volume floor applied. (3) 'Peak %' assumes an
exit at the best daily close - held-to-now % shown beside it."""
import sys, json, time, datetime as dt
from pathlib import Path
import requests
import yfinance as yf
sys.path.insert(0, "scripts")
from ts_api import get_access_token, API

REPO = Path(".")
# 8/8 fix: token fetched PER REQUEST (it expires ~20 min; a one-time fetch made
# every call in the back half of a long run silently return nothing).

def tv_movers():
    out = {}
    for order, n in (("desc", 110), ("asc", 55)):
        r = requests.post("https://scanner.tradingview.com/america/scan", json={
            "filter": [{"left": "market_cap_basic", "operation": "egreater", "right": 5e8},
                       {"left": "type", "operation": "equal", "right": "stock"},
                       {"left": "is_primary", "operation": "equal", "right": True},
                       {"left": "exchange", "operation": "in_range", "right": ["NYSE", "NASDAQ", "AMEX"]},
                       {"left": "average_volume_10d_calc", "operation": "egreater", "right": 400000}],
            "columns": ["name", "close", "Perf.YTD", "sector", "market_cap_basic"],
            "sort": {"sortBy": "Perf.YTD", "sortOrder": order}, "range": [0, n]},
            timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        for e in r.json().get("data", []):
            v = e["d"]
            if v[2] is None: continue
            out[v[0]] = {"close": v[1], "ytd": v[2], "sector": v[3] or "?", "mcap": v[4]}
    return out

def bars(sym):
    for attempt in range(3):
        try:
            r = requests.get(f"{API}/marketdata/barcharts/{sym}",
                             params={"interval": "1", "unit": "Daily",
                                     "firstdate": "2026-01-02T00:00:00Z", "lastdate": "2026-08-08T00:00:00Z"},
                             headers={"Authorization": f"Bearer {get_access_token()}"}, timeout=25)
            return r.json().get("Bars", [])
        except Exception:
            time.sleep(2 * (attempt + 1))
    return []

def main():
    movers = tv_movers()
    extra = ["HTZ","SOUN","IOVA","GDX","NEM","PLTR","HALO","OMDA","CRSR","DOCS","AMLX","GCT","CENX","INDI","WOLF","APP","TTD"]
    r = requests.post("https://scanner.tradingview.com/america/scan", json={
        "symbols": {"tickers": [f"{ex}:{s}" for s in extra for ex in ("NASDAQ","NYSE","AMEX")], "query": {"types": []}},
        "columns": ["name","close","Perf.YTD","sector","market_cap_basic"]}, timeout=30, headers={"User-Agent":"Mozilla/5.0"})
    for e in r.json().get("data", []):
        v = e["d"]
        if v[2] is not None and v[0] not in movers:
            movers[v[0]] = {"close": v[1], "ytd": v[2], "sector": v[3] or "?", "mcap": v[4]}
    print(f"underlyings: {len(movers)}")
    ckpt = Path("research/top-options-ytd-checkpoint.jsonl")
    done = set()
    results = []
    if ckpt.exists():
        for line in ckpt.read_text().splitlines():
            try:
                r_ = json.loads(line)
                done.add(r_["contract"]); results.append(r_)
            except Exception: pass
        print(f"resuming: {len(results)} qualified already checkpointed")
    tested_p = Path("research/top-options-ytd-tested.txt")
    tested_set = set(tested_p.read_text().splitlines()) if tested_p.exists() else set()
    tested = 0
    for i, (u, m) in enumerate(sorted(movers.items(), key=lambda x: -abs(x[1]["ytd"]))):
        jan_px = m["close"] / (1 + m["ytd"] / 100)
        side = "C" if m["ytd"] >= 0 else "P"
        try:
            tk = yf.Ticker(u); exps = [e for e in tk.options if e >= "2026-09-01"][:5]
        except Exception: continue
        cand = []
        for exp in exps:
            try:
                ch = tk.option_chain(exp)
                table = ch.calls if side == "C" else ch.puts
            except Exception: continue
            for _, row in table.iterrows():
                k = float(row.strike)
                if side == "C" and jan_px * 0.90 <= k <= jan_px * 2.2: cand.append((exp, k))
                if side == "P" and jan_px * 0.40 <= k <= jan_px * 1.05: cand.append((exp, k))
        # thin the candidates: max 5 per underlying, spread across expiries
        seen_exp = {}
        picked = []
        for exp, k in cand:
            if seen_exp.get(exp, 0) >= 3: continue
            seen_exp[exp] = seen_exp.get(exp, 0) + 1
            picked.append((exp, k))
            if len(picked) >= 8: break
        for exp, k in picked:
            tag = dt.datetime.strptime(exp, "%Y-%m-%d").strftime("%y%m%d")
            ks = str(int(k)) if k == int(k) else str(k)
            sym = f"{u} {tag}{side}{ks}"
            if sym in tested_set: continue
            b = bars(sym); tested += 1
            tested_set.add(sym)
            if tested % 25 == 0:
                tested_p.write_text(chr(10).join(sorted(tested_set)))
            if len(b) < 60: continue
            if b[0]["TimeStamp"][:10] > "2026-01-15": continue          # must be a true YTD contract
            first = float(b[0]["Close"])
            if first < 0.05: continue
            vol = sum(int(bb.get("TotalVolume", 0)) for bb in b)
            if vol < 50: continue
            closes = [(bb["TimeStamp"][:10], float(bb["Close"])) for bb in b]
            pk_date, pk = max(closes, key=lambda x: x[1])
            cur = closes[-1][1]
            rec = {"contract": sym, "underlying": u, "sector": m["sector"],
                            "type": "CALL" if side == "C" else "PUT", "expiry": exp, "strike": k,
                            "jan_price": first, "peak_price": pk, "peak_date": pk_date,
                            "now_price": cur, "peak_pct": round((pk/first - 1) * 100),
                            "now_pct": round((cur/first - 1) * 100),
                            "stock_ytd_pct": round(m["ytd"], 1), "opt_volume_ytd": vol}
            results.append(rec)
            with open(ckpt, "a") as fh: fh.write(json.dumps(rec) + chr(10))
            time.sleep(0.15)
        if i % 10 == 0:
            print(f"  ...{i} underlyings, {tested} tested this run, {len(results)} qualified total", flush=True)
            tested_p.write_text(chr(10).join(sorted(tested_set)))
    results.sort(key=lambda x: -x["peak_pct"])
    top = results[:100]
    json.dump(top, open("research/top-options-ytd-2026-pass2.json", "w"), indent=1)
    print(f"\ntested {tested} contracts -> {len(results)} qualified -> top 100 saved")
    for r_ in top[:15]:
        print(f"  {r_['contract']:<22} {r_['sector'][:18]:<18} peak {r_['peak_pct']:>6}%  now {r_['now_pct']:>6}%  stock YTD {r_['stock_ytd_pct']:>7}%")
    return 0

if __name__ == "__main__":
    sys.exit(main())
