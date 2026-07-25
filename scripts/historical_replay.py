"""Walk-forward historical replay of the scan. Pre-registered 2026-07-25.

Read research/historical-replay-preregistration.md FIRST. The method, the windows,
the success bar and the meaning of every outcome were committed to git BEFORE this
file existed. Nothing here may be tuned after seeing a result.

WHAT THIS DOES
--------------
Replays the exact live rules day by day over Jan-Jul 2026 across the whole
universe, using only data available on each decision date, and grades every
signal it would have produced - including all the ones that went nowhere.

It deliberately does NOT test "would we have caught the stocks that ran", because
selecting the sample on the outcome removes the denominator and the test then
cannot fail. The big movers are a DIAGNOSTIC, computed last, quarantined from the
verdict.

FIDELITY
--------
The gate stack is IMPORTED, never re-implemented. The indicator maths is a
port of scripts/og_sweep_runner.js (the live in-page sweep) and is validated
against a real recorded sweep before any replay is trusted:

    python scripts/historical_replay.py --validate

That compares this file's ATR / ADX / DI / SMA200 / dollar-volume against
watchlists/og-sweep-raw-2026-07-24-heikinashi.json, 494 names of ground truth,
and also settles empirically whether the live sweep's regime block reads RAW or
HEIKIN-ASHI bars - which the JS cannot tell us because it just asks the chart.

Usage:
    python scripts/historical_replay.py --validate      # prove the port first
    python scripts/historical_replay.py --run           # the pre-registered test
"""
import json
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- pre-registered constants. Changing any of these invalidates the test. ---
CE_LEN, CE_MULT = 1, 2.0        # Chandelier Exit inputs 1/2
ZL_LEN = 50                     # ZLSMA
FRESH_BARS = 5                  # "fresh" = flipped BUY within this many bars
HOLD = 21                       # trading days
COST_BP = 10                    # round-trip cost, basis points (reported, not primary)
PRIMARY = ("2026-01-02", "2026-06-30")     # out-of-sample
SECONDARY = ("2026-07-01", "2026-07-24")   # in-sample, no pass/fail weight
MIN_SAMPLE = 30
C1_MIN = 2.0                    # PASSED must beat SPY by >= this
C2_MIN = 2.0                    # PASSED must beat BLOCKED by >= this
HISTORY_START = "2024-06-01"    # enough runway for a 200-day SMA by Jan 2026

# Settled EMPIRICALLY by --validate against the 2026-07-24 live sweep, not assumed:
# regime/ADX/DI/ATR on Heikin-Ashi bars reproduce the live values to within 0.01%
# and match the regime string 99.6% of the time; on raw OHLC the ADX error is 18%
# and DI is 29%. The live sweep therefore computes the ENTIRE gate stack on
# Heikin-Ashi, not on real prices.
REGIME_ON_HA = True

# Excluded from the replay: on 2026-07-24 the live sweep resolved these bare
# tickers to FOREIGN listings of DIFFERENT COMPANIES (see the report). They are
# not the US names they claim to be, so replaying them would compare two
# different businesses.
BAD_SYMBOLS = {"BHP", "COCO", "DTE", "EQR", "SFL"}


# ----------------------------------------------------------------------------
# Indicators - ported from og_sweep_runner.js, matching its exact conventions.
# Every one is CAUSAL (uses only past/current bars), so computing the full series
# once and indexing by date gives identical values to recomputing on truncated
# data each day. That is what makes the replay affordable.
# ----------------------------------------------------------------------------
def heikin_ashi(df):
    ha = pd.DataFrame(index=df.index)
    ha["close"] = (df["Open"] + df["High"] + df["Low"] + df["Close"]) / 4
    op = np.empty(len(df))
    op[0] = (df["Open"].iloc[0] + df["Close"].iloc[0]) / 2
    hc = ha["close"].to_numpy()
    for i in range(1, len(df)):
        op[i] = (op[i - 1] + hc[i - 1]) / 2
    ha["open"] = op
    ha["high"] = np.maximum.reduce([df["High"].to_numpy(), op, hc])
    ha["low"] = np.minimum.reduce([df["Low"].to_numpy(), op, hc])
    return ha


def true_range(h, l, c):
    pc = c.shift(1)
    return pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)


def atr_live(h, l, c, per=14):
    """JS: simple mean of TR over the 14 COMPLETED bars, excluding the last bar."""
    return true_range(h, l, c).shift(1).rolling(per).mean()


def wilder_sum(arr, per):
    """JS `wil()`: a running SUM (not average): t = t - t/per + x."""
    out = np.full(len(arr), np.nan)
    if len(arr) < per:
        return out
    t = float(np.nansum(arr[:per]))
    out[per - 1] = t
    for i in range(per, len(arr)):
        t = t - t / per + arr[i]
        out[i] = t
    return out


def adx_di(h, l, c, per=14):
    """Wilder ADX/+DI/-DI, matching the JS exactly (which starts at bar index 1)."""
    hi, lo, cl = h.to_numpy(), l.to_numpy(), c.to_numpy()
    n = len(hi)
    up = hi[1:] - hi[:-1]
    dn = lo[:-1] - lo[1:]
    pdm = np.where((up > dn) & (up > 0), up, 0.0)
    ndm = np.where((dn > up) & (dn > 0), dn, 0.0)
    tr = np.maximum.reduce([hi[1:] - lo[1:], np.abs(hi[1:] - cl[:-1]), np.abs(lo[1:] - cl[:-1])])

    TR, PD, ND = wilder_sum(tr, per), wilder_sum(pdm, per), wilder_sum(ndm, per)
    with np.errstate(invalid="ignore", divide="ignore"):
        pp = 100 * PD / TR
        qq = 100 * ND / TR
        dx = 100 * np.abs(pp - qq) / (pp + qq)

    adx = np.full(len(dx), np.nan)
    valid = np.where(~np.isnan(dx))[0]
    if len(valid) >= per:
        s = valid[0]
        first = np.nanmean(dx[s:s + per])
        adx[s + per - 1] = first
        cur = first
        for i in range(s + per, len(dx)):
            cur = (cur * (per - 1) + dx[i]) / per
            adx[i] = cur

    def pad(a):
        return np.concatenate([[np.nan], a])
    idx = c.index
    return (pd.Series(pad(adx), index=idx), pd.Series(pad(pp), index=idx),
            pd.Series(pad(qq), index=idx))


def chandelier(ha):
    """Everget Chandelier Exit with ratchet. Returns (direction, long_stop)."""
    a = CE_MULT * true_range(ha["high"], ha["low"], ha["close"]).ewm(
        alpha=1 / CE_LEN, adjust=False).mean()
    hi = ha["high"].rolling(CE_LEN).max()
    lo = ha["low"].rolling(CE_LEN).min()
    lsb = (hi - a).to_numpy()
    ssb = (lo + a).to_numpy()
    c = ha["close"].to_numpy()
    n = len(c)
    ls, ss = lsb.copy(), ssb.copy()
    dirn = np.ones(n, dtype=int)
    for i in range(1, n):
        ls[i] = max(lsb[i], ls[i - 1]) if c[i - 1] > ls[i - 1] else lsb[i]
        ss[i] = min(ssb[i], ss[i - 1]) if c[i - 1] < ss[i - 1] else ssb[i]
        if c[i] > ss[i - 1]:
            dirn[i] = 1
        elif c[i] < ls[i - 1]:
            dirn[i] = -1
        else:
            dirn[i] = dirn[i - 1]
    return pd.Series(dirn, index=ha.index), pd.Series(ls, index=ha.index)


def linreg_endpoint(s, length):
    x = np.arange(length)
    xm = x.mean()
    denom = ((x - xm) ** 2).sum()

    def ep(w):
        b = ((x - xm) * (w - w.mean())).sum() / denom
        return w.mean() - b * xm + b * (length - 1)
    return s.rolling(length).apply(ep, raw=True)


def zlsma(close, length=ZL_LEN):
    l1 = linreg_endpoint(close, length)
    return 2 * l1 - linreg_endpoint(l1, length)


def build_features(df, regime_on_ha):
    """Every field the gate stack needs, as full causal series."""
    ha = heikin_ashi(df)
    dirn, lstop = chandelier(ha)
    src = ha if regime_on_ha else pd.DataFrame(
        {"high": df["High"], "low": df["Low"], "close": df["Close"]}, index=df.index)

    c = src["close"]
    sma200 = c.rolling(200).mean()
    sma50 = c.rolling(50).mean()
    adx, pdi, ndi = adx_di(src["high"], src["low"], c)
    px = src["close"]
    pct200 = (px / sma200 - 1) * 100
    rising = sma200 > sma200.shift(20)
    above50 = px > sma50

    regime = pd.Series(np.where(pct200 < -10, "DEEP-FAIL",
                       np.where(pct200 < 0, "REPAIR",
                       np.where(rising & above50, "PASS", "REPAIR"))), index=df.index)
    regime[sma200.isna() | sma200.shift(20).isna()] = None

    avg_vol = df["Volume"].shift(1).rolling(20).mean()
    return pd.DataFrame({
        "last": px, "raw_close": df["Close"], "high": df["High"], "low": df["Low"],
        "dirn": dirn, "long_stop": lstop, "zlsma": zlsma(ha["close"]),
        "atr": atr_live(src["high"], src["low"], c),
        "adx": adx, "plus_di": pdi, "minus_di": ndi,
        "regime": regime, "pct_vs_200": pct200,
        "avg_dollar_vol": avg_vol * px,
    })


# ----------------------------------------------------------------------------
def load_universe():
    p = os.path.join(REPO, "watchlists", "og-sweep-universe-2026-07-24-extended.json")
    d = json.load(open(p, encoding="utf-8"))
    if isinstance(d, list):
        return d
    for v in d.values():
        if isinstance(v, list) and len(v) > 50 and all(isinstance(x, str) for x in v):
            return v
    raise SystemExit("no symbol list found")


def download(syms, start=HISTORY_START, end="2026-07-25"):
    out, CH = {}, 120
    for i in range(0, len(syms), CH):
        part = syms[i:i + CH]
        d = yf.download(part, start=start, end=end, interval="1d", group_by="ticker",
                        auto_adjust=False, threads=True, progress=False)
        for s in part:
            try:
                df = d[s].dropna(subset=["Close"]) if len(part) > 1 else d.dropna(subset=["Close"])
                if df is not None and len(df) > 260:
                    df = df.copy()
                    df.index = pd.Index([str(x)[:10] for x in df.index])
                    out[s] = df
            except Exception:
                pass
        print(f"  downloaded {min(i+CH, len(syms))}/{len(syms)}", flush=True)
    return out


# ----------------------------------------------------------------------------
def validate():
    """Prove the port matches a real recorded sweep before trusting the replay."""
    raw = json.load(open(os.path.join(
        REPO, "watchlists", "og-sweep-raw-2026-07-24-heikinashi.json"), encoding="utf-8"))
    truth = {r["rname"]: r for r in raw if r.get("ok") and r.get("regime")}
    syms = sorted(truth)
    print(f"validating {len(syms)} names against the live 2026-07-24 sweep...")
    px = download(syms)

    res = {}
    for mode in (False, True):
        errs = {k: [] for k in ("last", "atr", "adx", "plus_di", "minus_di",
                                "sma200_pct", "avg_dollar_vol")}
        regime_match = 0
        n = 0
        for s in syms:
            df = px.get(s)
            if df is None or "2026-07-24" not in df.index:
                continue
            f = build_features(df, regime_on_ha=mode)
            row = f.loc["2026-07-24"]
            t = truth[s]
            if pd.isna(row["adx"]) or row["regime"] is None:
                continue
            n += 1

            def rel(a, b):
                return abs(a - b) / abs(b) * 100 if b else np.nan
            errs["last"].append(rel(float(row["last"]), t["last"]))
            errs["atr"].append(rel(float(row["atr"]), t["atr"]))
            errs["adx"].append(rel(float(row["adx"]), t["adx"]))
            errs["plus_di"].append(rel(float(row["plus_di"]), t["plus_di"]))
            errs["minus_di"].append(rel(float(row["minus_di"]), t["minus_di"]))
            errs["sma200_pct"].append(abs(float(row["pct_vs_200"]) - t["pct_vs_200"]))
            errs["avg_dollar_vol"].append(rel(float(row["avg_dollar_vol"]), t["avg_dollar_vol"]))
            regime_match += (row["regime"] == t["regime"])

        label = "HEIKIN-ASHI" if mode else "RAW OHLC"
        print(f"\n--- regime/ADX computed on {label} (n={n}) ---")
        for k, v in errs.items():
            v = [x for x in v if not np.isnan(x)]
            unit = "pt" if k == "sma200_pct" else "%"
            print(f"  {k:16s} median abs err {np.median(v):7.3f}{unit}   "
                  f"90th pct {np.percentile(v, 90):7.3f}{unit}")
        print(f"  regime string match: {regime_match}/{n} = {100*regime_match/n:.1f}%")
        res[label] = (np.median(errs["adx"]), regime_match / n)

    print("\n=== VERDICT ===")
    best = max(res, key=lambda k: res[k][1])
    print(f"The live sweep's regime block reads {best} bars "
          f"(regime match {100*res[best][1]:.1f}% vs "
          f"{100*res[min(res, key=lambda k: res[k][1])][1]:.1f}%).")
    print("Set REGIME_ON_HA accordingly before --run.")


def replay(px, universe):
    """Walk forward day by day. Entries and exits use REAL closes, never HA."""
    feats = {}
    for i, s in enumerate(universe):
        df = px.get(s)
        if df is None:
            continue
        try:
            feats[s] = build_features(df, REGIME_ON_HA)
        except Exception:
            pass
        if (i + 1) % 100 == 0:
            print(f"  features {i+1}/{len(universe)}", flush=True)

    spy = px.get("SPY")
    spy_close = spy["Close"] if spy is not None else None
    all_dates = sorted({d for f in feats.values() for d in f.index})
    dates = [d for d in all_dates if PRIMARY[0] <= d <= SECONDARY[1]]
    print(f"  replaying {len(dates)} trading days over {len(feats)} symbols", flush=True)

    signals = []
    for s, f in feats.items():
        idx = list(f.index)
        pos = {d: i for i, d in enumerate(idx)}
        dirn = f["dirn"].to_numpy()
        # bars since the last flip INTO long, computed causally
        since = np.full(len(dirn), 10 ** 6)
        run = 10 ** 6
        for i in range(len(dirn)):
            if dirn[i] == 1 and (i == 0 or dirn[i - 1] != 1):
                run = 0
            elif dirn[i] == 1:
                run += 1
            else:
                run = 10 ** 6
            since[i] = run

        raw_close = f["raw_close"].to_numpy()
        high = f["high"].to_numpy()
        low = f["low"].to_numpy()
        for d in dates:
            i = pos.get(d)
            if i is None or i + 1 >= len(idx):
                continue
            if not (0 <= since[i] <= FRESH_BARS):
                continue                       # not a fresh BUY signal
            row = f.iloc[i]
            gate_row = {
                "sym": s, "last": row["last"], "zlsma": row["zlsma"],
                "regime": row["regime"], "adx": row["adx"],
                "plus_di": row["plus_di"], "minus_di": row["minus_di"],
                "avg_dollar_vol": row["avg_dollar_vol"], "atr": row["atr"],
                "long_stop": row["long_stop"], "pct_vs_200": row["pct_vs_200"],
            }
            try:
                verdict, _, _ = evaluate(gate_row, position_size=DEFAULT_POSITION)
            except MissingGateData:
                continue                       # fails closed, as it does live
            cohort = "BLOCKED" if verdict.startswith("BLOCKED") else "PASSED"

            # --- grade on REAL prices, entry at the close of the signal day ---
            entry = float(raw_close[i])
            if not np.isfinite(entry) or entry <= 0:
                continue
            end = min(i + HOLD, len(idx) - 1)
            win = range(i + 1, end + 1)
            stop = float(row["long_stop"]) if np.isfinite(row["long_stop"]) else None
            # convert the HA-derived stop into a real-price stop by distance
            stop_pct = (row["last"] - row["long_stop"]) / row["last"] if stop else None
            real_stop = entry * (1 - stop_pct) if stop_pct and stop_pct > 0 else None
            target = entry * (1 + 2 * stop_pct) if stop_pct and stop_pct > 0 else None

            hit, exit_px, exit_i = None, float(raw_close[end]), end
            for j in win:
                if real_stop and low[j] <= real_stop:
                    hit, exit_px, exit_i = "STOP", real_stop, j
                    break
                if target and high[j] >= target:
                    hit, exit_px, exit_i = "TARGET", target, j
                    break

            managed = (exit_px / entry - 1) * 100
            pure = (float(raw_close[end]) / entry - 1) * 100
            spy_exc = None
            if spy_close is not None and d in spy_close.index:
                sidx = list(spy_close.index)
                sp = sidx.index(d)
                se = min(sp + HOLD, len(sidx) - 1)
                spy_ret = (float(spy_close.iloc[se]) / float(spy_close.iloc[sp]) - 1) * 100
                spy_exc = pure - spy_ret
            signals.append({
                "date": d, "sym": s, "cohort": cohort, "verdict": verdict,
                "regime": row["regime"], "entry": round(entry, 4),
                "managed_pct": round(managed, 3), "pure_pct": round(pure, 3),
                "spy_excess": round(spy_exc, 3) if spy_exc is not None else None,
                "hit": hit, "days_held": exit_i - i,
                "window": "primary" if d <= PRIMARY[1] else "secondary",
                "bars_since_flip": int(since[i]),
            })
    return signals


def _stats(rows, key="pure_pct"):
    if not rows:
        return None
    v = np.array([r[key] for r in rows], dtype=float)
    exc = [r["spy_excess"] for r in rows if r["spy_excess"] is not None]
    return {"n": len(v), "mean": float(np.mean(v)), "median": float(np.median(v)),
            "win": float(100 * (v > 0).mean()),
            "mean_excess": float(np.mean(exc)) if exc else None}


def run():
    universe = [s for s in load_universe() if s not in BAD_SYMBOLS]
    print(f"universe {len(universe)} (excluded {len(BAD_SYMBOLS)} mis-resolved symbols)")
    px = download(universe + ["SPY"])
    print(f"priced {len(px)} symbols")
    sigs = replay(px, universe)
    print(f"{len(sigs)} signals generated")
    json.dump({"generated": datetime.now().isoformat(timespec="seconds"),
               "preregistration": "research/historical-replay-preregistration.md",
               "signals": sigs},
              open(os.path.join(REPO, "research", "historical-replay-signals.json"), "w"),
              indent=1)
    return sigs


if __name__ == "__main__":
    if "--validate" in sys.argv:
        validate()
    elif "--run" in sys.argv:
        run()
    else:
        print("use --validate first, then --run (see the pre-registration)")
