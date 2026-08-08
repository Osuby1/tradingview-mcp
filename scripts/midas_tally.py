#!/usr/bin/env python3
"""MIDAS SELECTOR running tally (Omar 8/7): grades the MIDAS (Winner Score v1)
shadow picks against the live selector's picks, cumulatively, from every
research/shadow-ws-<date>.json. Writes research/midas-tally.json for the
workbook's MIDAS SELECTOR PICKS tab. Measurement only - MIDAS stays shadow
until its promotion decision."""
import glob, json, statistics as st, sys, datetime as dt
from pathlib import Path
import yfinance as yf
REPO = Path(__file__).resolve().parent.parent

def main():
    days = []
    for f in sorted(glob.glob(str(REPO / "research" / "shadow-ws-*.json"))):
        try: days.append(json.loads(open(f, encoding="utf-8").read()))
        except Exception: pass
    if not days:
        print("[midas] no shadow days yet"); return 0
    refs = {}
    for d in days:
        for r in d["rankings"]:
            if r.get("ref_price"): refs[(d["date"], r["sym"])] = r["ref_price"]
    syms = sorted({s for _, s in refs})
    px = yf.download(syms, period="3mo", progress=False, auto_adjust=True,
                     group_by="ticker", threads=True)
    def now(s):
        try: return float(px[s].dropna().Close.iloc[-1])
        except Exception: return None
    out_days, m_all, l_all = [], [], []
    for d in days:
        m_rets, l_rets = [], []
        for cohort, bag in (("ws_top3", m_rets), ("live_top3", l_rets)):
            for s in d.get(cohort, []):
                ref = refs.get((d["date"], s)); cur = now(s)
                if ref and cur: bag.append((cur / ref - 1) * 100)
        if m_rets and l_rets:
            m, l = st.mean(m_rets), st.mean(l_rets)
            m_all += m_rets; l_all += l_rets
            out_days.append({"date": d["date"], "midas_picks": d["ws_top3"],
                             "live_picks": d["live_top3"],
                             "midas_ret_pct": round(m, 2), "live_ret_pct": round(l, 2),
                             "midas_ahead": m > l})
    tally = {"as_of": dt.date.today().isoformat(), "days_compared": len(out_days),
             "midas_mean_pct": round(st.mean(m_all), 2) if m_all else None,
             "live_mean_pct": round(st.mean(l_all), 2) if l_all else None,
             "midas_days_ahead": sum(1 for x in out_days if x["midas_ahead"]),
             "days": out_days,
             "note": "SHADOW ONLY - MIDAS ranks nothing live until the promotion decision (prereg c19b0a4)"}
    (REPO / "research" / "midas-tally.json").write_text(json.dumps(tally, indent=1))
    print(f"[midas] {len(out_days)} day(s): MIDAS mean {tally['midas_mean_pct']}% vs live {tally['live_mean_pct']}% | MIDAS ahead {tally['midas_days_ahead']}/{len(out_days)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
