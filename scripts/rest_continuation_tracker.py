"""Rest-continuation cohort tracker (pre-registered 2026-08-01).

Nightly (chain step 4, non-fatal):
    python scripts/rest_continuation_tracker.py <YYYY-MM-DD>
  Tags every candidate in watchlists/universe-results-<date>.json as
  cohort member / non-member per the FROZEN rule in
  research/rest-continuation-preregistration.md and appends to
  research/rest-continuation-ledger.json. Idempotent per (date, sym).

Grading (Friday review):
    python scripts/rest_continuation_tracker.py --grade
  Fills outcomes for entries aged >= 15 sessions (best close within 15
  sessions vs tag-night close; win >= +15%) and prints cohort vs control.

Factor computations are the same code path as the 8/1 winner-factor study:
Wilder ADX/DI(14) and RVOL(50) from Yahoo-adjusted daily bars (NY-localized,
same fix as readiness_batch.py); readiness score comes from the nightly
readiness_batch stamp. Missing data on any factor = NOT a member (fails
closed), logged with nulls.
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import yfinance as yf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "research", "rest-continuation-ledger.json")

DI_MIN, ADX_MIN, READY_MAX, RVOL_MAX = 10.0, 25.0, 30, 1.2
WIN_PCT, WINDOW = 15.0, 15


def _load_ledger():
    if os.path.exists(LEDGER):
        return json.load(open(LEDGER))
    return {"preregistration": "research/rest-continuation-preregistration.md",
            "entries": []}


def _batch_history(syms, period="2y"):
    data = yf.download(syms, period=period, auto_adjust=True,
                       group_by="ticker", progress=False, threads=True)
    out = {}
    for s in syms:
        try:
            h = data[s].dropna(how="all")
            if h.empty:
                continue
            if h.index.tz is None:
                h = h.tz_localize("America/New_York")
            out[s] = h
        except Exception:
            pass
    return out


def adx_di(h, n=14):
    hi, lo, c = h.High, h.Low, h.Close
    up, dn = hi.diff(), -lo.diff()
    plus = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=h.index)
    minus = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=h.index)
    tr = np.maximum(hi - lo, np.maximum(abs(hi - c.shift(1)),
                                        abs(lo - c.shift(1))))
    atr = tr.ewm(alpha=1 / n, adjust=False).mean()
    pdi = 100 * plus.ewm(alpha=1 / n, adjust=False).mean() / atr
    mdi = 100 * minus.ewm(alpha=1 / n, adjust=False).mean() / atr
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi)
    adx = dx.ewm(alpha=1 / n, adjust=False).mean()
    return float(adx.iloc[-1]), float(pdi.iloc[-1] - mdi.iloc[-1])


def tag(date):
    res_path = os.path.join(REPO, "watchlists", f"universe-results-{date}.json")
    res = json.load(open(res_path))
    cands = {}
    for e in (res.get("hits") or []) + (res.get("gated_longs") or []):
        s = e.get("sym")
        if s and s not in cands:
            cands[s] = e
    led = _load_ledger()
    done = {(r["date"], r["sym"]) for r in led["entries"]}
    todo = [s for s in cands if (date, s) not in done]
    if not todo:
        print(f"rest-continuation: nothing new to tag for {date}")
        return
    hist = _batch_history(todo)
    first_syms = {r["sym"] for r in led["entries"]}
    n_new = n_mem = 0
    for s in todo:
        e = cands[s]
        ready = (e.get("readiness") or {}).get("score")
        row = {"date": date, "sym": s, "first_tag": s not in first_syms,
               "readiness": ready, "adx": None, "di": None, "rvol": None,
               "close": None, "member": False, "outcome": None}
        h = hist.get(s)
        try:
            hh = h.loc[:date] if h is not None else None
            if hh is not None and len(hh) >= 80 and \
                    hh.index[-1].strftime("%Y-%m-%d") == date:
                adx, di = adx_di(hh)
                rvol = float(hh.Volume.iloc[-1] / hh.Volume.tail(50).mean())
                row.update(adx=round(adx, 1), di=round(di, 1),
                           rvol=round(rvol, 2),
                           close=round(float(hh.Close.iloc[-1]), 4))
                row["member"] = bool(di >= DI_MIN and adx >= ADX_MIN
                                     and ready is not None
                                     and ready <= READY_MAX
                                     and rvol < RVOL_MAX)
        except Exception:
            pass
        led["entries"].append(row)
        n_new += 1
        n_mem += row["member"]
        first_syms.add(s)
    json.dump(led, open(LEDGER, "w"), indent=1)
    print(f"rest-continuation {date}: tagged {n_new} candidates, "
          f"{n_mem} cohort members -> {os.path.basename(LEDGER)}")


def grade():
    led = _load_ledger()
    pend = [r for r in led["entries"]
            if r["outcome"] is None and r["close"]]
    if pend:
        hist = _batch_history(sorted({r["sym"] for r in pend}), period="1y")
        for r in pend:
            h = hist.get(r["sym"])
            if h is None:
                continue
            post = h.loc[r["date"]:].iloc[1:]
            if len(post) < WINDOW:
                continue  # not aged yet
            best = float(post.Close.head(WINDOW).max() / r["close"] - 1) * 100
            r["outcome"] = {"best_pct": round(best, 1),
                            "win": best >= WIN_PCT,
                            "graded_after_sessions": WINDOW}
        json.dump(led, open(LEDGER, "w"), indent=1)

    firsts = [r for r in led["entries"] if r["first_tag"]]
    aged = [r for r in firsts if r["outcome"]]
    coh = [r for r in aged if r["member"]]
    ctl = [r for r in aged if not r["member"]]
    print(f"first-tags: {len(firsts)} total | aged 15 sessions: {len(aged)} "
          f"(cohort {len(coh)} / control {len(ctl)})")
    for name, grp in (("COHORT", coh), ("CONTROL", ctl)):
        if grp:
            w = sum(1 for r in grp if r["outcome"]["win"])
            print(f"  {name}: {w}/{len(grp)} = {w / len(grp):.1%} win "
                  f"(best>=+{WIN_PCT:.0f}% within {WINDOW} sessions)")
    if coh and ctl:
        cw = sum(1 for r in coh if r["outcome"]["win"]) / len(coh)
        xw = sum(1 for r in ctl if r["outcome"]["win"]) / len(ctl)
        print(f"  lift: {cw / xw:.2f}x" if xw else "  lift: control has 0 wins")
    print("Verdict rules (frozen): minimums 15 aged cohort members + 8 total "
          "winners; kill if lift < 1.5x at the 2026-09-25 review.")


if __name__ == "__main__":
    if "--grade" in sys.argv[1:]:
        grade()
    else:
        args = [a for a in sys.argv[1:] if not a.startswith("-")]
        if not args:
            sys.exit("usage: rest_continuation_tracker.py <YYYY-MM-DD> | --grade")
        tag(args[0])
