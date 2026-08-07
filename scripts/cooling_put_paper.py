#!/usr/bin/env python3
"""COOLING-ARRIVAL PUT PAPER TRACKER (per research/cooling-arrival-put-study-
preregistration.md, live from 2026-08-10). Nightly, in the EOD chain:
1. CLOSE/mark open paper puts: -50% premium stop or +5 sessions, whichever first.
2. OPEN new paper puts for TODAY's first-ever COOLING arrivals (next-open entry
   convention: recorded tonight, priced at tomorrow's open when it exists).
Synthetic Black-Scholes ATM puts, 35 DTE, IV = 1.2x realized-20, LABELED
SYNTHETIC. $500 notional premium per signal. Ledger: research/cooling-put-paper-ledger.json
Verdict after >=30 signals per the frozen bars. PAPER ONLY."""
import json, math, sys, datetime as dt
from pathlib import Path
import pandas as pd
REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "research" / "cooling-put-paper-ledger.json"
LOG = Path.home() / "Documents" / "Equities_Scanner" / "recommendations_log.csv"
START = "2026-08-10"

def N(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def bs_put(S, K, T, r, sig):
    if T <= 0: return max(K - S, 0)
    d1 = (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))
    return K * math.exp(-r * T) * N(-(d1 - sig * math.sqrt(T))) - S * N(-d1)

def rv20(sym, px):
    try:
        c = px[sym].dropna().Close.pct_change().tail(20)
        return float(c.std() * (252 ** 0.5))
    except Exception:
        return None

def main():
    today = dt.date.today().isoformat()
    led = json.loads(LEDGER.read_text()) if LEDGER.exists() else {"open": [], "closed": [], "signals_total": 0}
    d = pd.read_csv(LOG).dropna(subset=["date", "ticker", "tab"])
    d["tab"] = d.tab.astype(str).str.upper().str.strip()
    first_cool = d[d.tab == "COOLING"].groupby(d.ticker.str.upper()).date.min()
    new_syms = sorted(first_cool[first_cool.astype(str).str[:10] == today].index)
    syms = sorted(set(new_syms) | {p["sym"] for p in led["open"]})
    if not syms:
        print("[cool-put] nothing to do"); return 0
    import yfinance as yf
    px = yf.download(syms, period="3mo", progress=False, auto_adjust=True,
                     group_by="ticker", threads=True)
    # mark/close opens
    still = []
    for p in led["open"]:
        try:
            h = px[p["sym"]].dropna()
            spot = float(h.Close.iloc[-1])
        except Exception:
            still.append(p); continue
        if p.get("entry_prem") is None:                    # price the next-open entry
            iv = (rv20(p["sym"], px) or 0.5) * 1.2
            p["entry_spot"] = float(h.Open.iloc[-1]); p["iv"] = round(iv, 3)
            p["strike"] = round(p["entry_spot"], 2)
            p["entry_prem"] = round(bs_put(p["entry_spot"], p["strike"], 35/365, 0.04, iv), 3)
            p["qty"] = max(1, int(500 / max(p["entry_prem"] * 100, 1)))
        p["sessions"] = p.get("sessions", 0) + 1
        T = max((35 - p["sessions"]) / 365, 1e-4)
        mark = bs_put(spot, p["strike"], T, 0.04, p["iv"])
        pnl = round((mark - p["entry_prem"]) * 100 * p["qty"])
        if mark <= p["entry_prem"] * 0.5 or p["sessions"] >= 5:
            p.update(exit_date=today, exit_prem=round(mark, 3), pnl=pnl,
                     exit_why="-50% stop" if mark <= p["entry_prem"] * 0.5 else "5-session time exit")
            led["closed"].append(p)
        else:
            p["mark"] = round(mark, 3); p["upnl"] = pnl; still.append(p)
    led["open"] = still
    # open new signals (from START only)
    if today >= START:
        have = {p["sym"] for p in led["open"]} | {p["sym"] for p in led["closed"] if p.get("signal_date") == today}
        for s in new_syms:
            if s in have: continue
            led["open"].append({"sym": s, "signal_date": today, "entry_prem": None,
                                "note": "SYNTHETIC ATM put, priced at next session's open"})
            led["signals_total"] += 1
    closed_pnl = sum(p.get("pnl", 0) for p in led["closed"])
    wins = sum(1 for p in led["closed"] if p.get("pnl", 0) > 0)
    print(f"[cool-put] signals {led['signals_total']} | open {len(led['open'])} | "
          f"closed {len(led['closed'])} (P&L ${closed_pnl:+,}, wins {wins}) | verdict at >=30 signals")
    LEDGER.write_text(json.dumps(led, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
