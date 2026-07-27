"""Fresh-Ignition "A" grade backtest. Pre-registered 2026-07-26.

Read research/fresh-ignition-preregistration.md FIRST. This replays the
origination scanner's OWN rules (stage2_leader_scanner_v3.py is the spec:
same config values, score weights, grade bands, flag/tab logic) daily over
2021-2025 across its own 1,200-name universe, then tests Omar's hypothesis:
buy Fresh Ignitions graded A, sell the day they move to the Cooling tab.

Weekly RSI/ROC use completed weeks (declared approximation). Capacity is
ranked cross-sectionally within the universe daily, as the scanner does.

Usage: python scripts/fresh_ignition_backtest.py
"""
import json
import os

import numpy as np
import pandas as pd
import yfinance as yf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNIVERSE = os.path.join(os.environ.get("USERPROFILE", ""), "Documents",
                        "Equities_Scanner", "russell_starter.csv")
START, END = "2021-01-01", "2025-12-31"
WARMUP, DATA_END = "2019-06-01", "2026-01-10"
COST_PT = 0.10
MAX_HOLD_R1 = 250
YEARS = ["2021", "2022", "2023", "2024", "2025"]

# -- scanner config, copied verbatim from stage2_leader_scanner_v3.CFG --------
SMA200_RISE_LB, HIGH_LB, NEAR_HIGH, RS_LB = 21, 252, 0.85, 60
BBW_TIGHT_MULT, BBW_CONTRACT_LB = 0.80, 5
RELVOL_MIN, RSI_W_MIN = 1.5, 50.0
RELVOL_PERSIST_MIN, RELVOL_PERSIST_K, IGNITE_LB, IGNITE_DRIFT = 1.3, 2, 5, 0.03
RSI_CHASE, EXT_OVER_50, RUN_60D_MAX, EXTENDED_CAP = 70.0, 0.25, 0.30, 49.0
PINNED_ATR_MAX, PB_SCORE_MIN, PB_RUN_MIN, PB_RSI_RESET, PB_ZONE_TOL = \
    0.006, 65.0, 0.25, 60.0, 0.02
W_TREND, W_LEAD, W_SQ, W_MOM, W_ACC, W_CAP = 15, 25, 10, 25, 10, 15

TAB = {"FRESH": 1, "BUYZONE": 2, "COOLING": 3, "COILED": 4, "OUT": 0}


def rsi(close, n=14):
    d = close.diff()
    ru = d.clip(lower=0.0).ewm(alpha=1 / n, adjust=False).mean()
    rd = (-d).clip(lower=0.0).ewm(alpha=1 / n, adjust=False).mean()
    return (100 - 100 / (1 + ru / rd.replace(0, np.nan))).fillna(50.0)


def true_range(h, l, c):
    pc = c.shift(1)
    return pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)


def adx_series(h, l, c, n=14):
    up, dn = h.diff(), -l.diff()
    pdm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=h.index)
    ndm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=h.index)
    a = true_range(h, l, c).ewm(alpha=1 / n, adjust=False).mean()
    pdi = 100 * pdm.ewm(alpha=1 / n, adjust=False).mean() / a.replace(0, np.nan)
    mdi = 100 * ndm.ewm(alpha=1 / n, adjust=False).mean() / a.replace(0, np.nan)
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return dx.ewm(alpha=1 / n, adjust=False).mean().fillna(0.0)


def clip01(s):
    return s.clip(0.0, 1.0)


def load_prices():
    syms = [s.strip().upper() for s in
            pd.read_csv(UNIVERSE).iloc[:, 0].dropna().astype(str)]
    syms = sorted(set(syms) | {"SPY"})
    print(f"downloading {len(syms)} symbols...", flush=True)
    out = {}
    for i in range(0, len(syms), 100):
        part = syms[i:i + 100]
        d = yf.download(part, start=WARMUP, end=DATA_END, interval="1d",
                        group_by="ticker", auto_adjust=True, threads=True,
                        progress=False)
        for s in part:
            try:
                df = d[s].dropna(subset=["Close"])
                if len(df) >= 260:
                    out[s] = df
            except Exception:
                pass
        print(f"  {min(i + 100, len(syms))}/{len(syms)}", flush=True)
    return out


def features(df, spy_close, cal):
    """Daily feature frame for one name, reindexed to the SPY calendar."""
    o, h, l, c, v = df["Open"], df["High"], df["Low"], df["Close"], df["Volume"]
    f = pd.DataFrame(index=df.index)
    sma20, sma50, sma200 = (c.rolling(k).mean() for k in (20, 50, 200))
    f["stage2"] = (c > sma200) & (sma50 > sma200) & (sma200 > sma200.shift(SMA200_RISE_LB))
    f["above200"] = c > sma200
    f["ext50"] = c / sma50 - 1
    f["rsi14"] = rsi(c)
    wk = c.resample("W-FRI").last().dropna()
    f["rsi_w"] = rsi(wk).reindex(df.index, method="ffill")
    f["roc_w"] = (wk / wk.shift(4) - 1).reindex(df.index, method="ffill")
    f["ret60"] = c / c.shift(60) - 1
    ax = adx_series(h, l, c)
    f["adx_ok"] = (ax > ax.shift(1)) | (ax > 20.0)
    rv = (v / v.rolling(20).mean()).replace([np.inf, -np.inf], np.nan)
    f["med3"] = rv.rolling(3).median()
    f["persist"] = ((rv >= RELVOL_PERSIST_MIN).rolling(5).sum() >= RELVOL_PERSIST_K) \
        | (f["med3"] >= RELVOL_MIN)
    surge = (rv >= RELVOL_MIN) & (c > c.shift(1))
    ign = pd.Series(False, index=df.index)
    for j in range(IGNITE_LB):
        ign = ign | (surge.shift(j).fillna(False) & (c >= c.shift(j) * (1 - IGNITE_DRIFT)))
    f["ignited"] = ign
    ob = (np.sign(c.diff()).fillna(0.0) * v).cumsum()
    f["accum"] = ob > ob.rolling(10).mean()
    hi52 = h.rolling(HIGH_LB, min_periods=200).max()
    f["prox"] = c / hi52
    rl = (c / spy_close.reindex(df.index).ffill()).dropna()
    f["rs_nh"] = (rl > rl.shift(1).rolling(RS_LB).max()).reindex(df.index).fillna(False)
    ma, sd = sma20, c.rolling(20).std(ddof=0)
    bw = ((ma + 2 * sd) - (ma - 2 * sd)) / ma
    f["squeeze"] = (bw < BBW_TIGHT_MULT * bw.rolling(20).mean()) | (bw < bw.shift(BBW_CONTRACT_LB))
    f["tight"] = bw < BBW_TIGHT_MULT * bw.rolling(20).mean()
    a14 = true_range(h, l, c).ewm(alpha=1 / 14, adjust=False).mean()
    f["atr_pct"] = a14 / c
    f["pb_hi"] = pd.concat([c.ewm(span=20, adjust=False).mean(), sma50], axis=1).max(axis=1)
    f["close"], f["open"], f["low"] = c, o, l
    return f.reindex(cal).astype(np.float32, errors="ignore")


def score_and_tab(f, cap_rank):
    trend = np.where(f["stage2"] > 0, 1.0, np.where(f["above200"] > 0, 0.5, 0.0))
    lead = clip01((f["prox"] - 0.80) / 0.20)
    lead = np.minimum(1.0, lead + np.where(f["rs_nh"] > 0, 0.15, 0.0))
    sq = np.where(f["tight"] > 0, 1.0, np.where(f["squeeze"] > 0, 0.6, 0.2))
    mom = (0.40 * clip01((f["med3"] - 1.0) / 2.0) + 0.30 * clip01(f["roc_w"] / 0.30)
           + 0.30 * clip01((f["rsi_w"] - 50.0) / 20.0))
    mom_gate = (f["ignited"] > 0) & (f["persist"] > 0) & (f["rsi_w"] > RSI_W_MIN) & (f["adx_ok"] > 0)
    mom = np.where(mom_gate, mom, mom * 0.5)
    accum = np.where(f["accum"] > 0, 1.0, 0.3)
    capv = 0.5 * cap_rank + 0.5 * clip01((f["atr_pct"] - 0.01) / 0.04)
    score = (W_TREND * trend + W_LEAD * lead + W_SQ * sq + W_MOM * mom
             + W_ACC * accum + W_CAP * capv)
    trend_gate = f["stage2"] > 0
    lead_gate = f["prox"] >= NEAR_HIGH
    score = np.where(trend_gate, score, np.minimum(score, 40.0))
    score = np.where(lead_gate, score, np.minimum(score, 45.0))
    precap = score.copy()
    extended = (f["rsi14"] > RSI_CHASE) | (f["ext50"] > EXT_OVER_50) | (f["ret60"] > RUN_60D_MAX)
    pinned = (f["atr_pct"] < PINNED_ATR_MAX) & (f["prox"] >= 0.90)
    pb_qual = trend_gate & lead_gate & ((precap >= PB_SCORE_MIN) | (f["ret60"] >= PB_RUN_MIN))
    leader = (~pinned) & (~extended) & trend_gate & lead_gate & mom_gate & (f["accum"] > 0)
    watch = (~pinned) & (~extended) & (~leader) & trend_gate & lead_gate & (f["squeeze"] > 0)
    score = np.where(pinned, np.minimum(score, 30.0), score)
    score = np.where((~pinned) & extended, np.minimum(score, EXTENDED_CAP), score)
    pb_ready = ((~pinned) & extended & pb_qual & (f["rsi14"] < PB_RSI_RESET)
                & (f["close"] <= f["pb_hi"] * (1 + PB_ZONE_TOL)))
    tab = np.select(
        [leader, (~pinned) & extended & pb_qual & pb_ready,
         (~pinned) & extended & pb_qual & (~pb_ready), watch],
        [TAB["FRESH"], TAB["BUYZONE"], TAB["COOLING"], TAB["COILED"]], TAB["OUT"])
    tab = np.where(np.isnan(f["close"].to_numpy(dtype=float)), TAB["OUT"], tab)
    return score, tab


def grade_of(score):
    return np.select([score >= 85, score >= 70, score >= 60, score >= 50],
                     [4, 3, 2, 1], 0)      # 4=A+ 3=A 2=B 1=C 0=SKIP


def main():
    px = load_prices()
    spy = px.pop("SPY")
    cal = spy.index
    spy_c = spy["Close"]
    print(f"{len(px)} names usable", flush=True)

    feats = {}
    for k, (s, df) in enumerate(px.items()):
        try:
            feats[s] = features(df, spy_c, cal)
        except Exception:
            pass
        if (k + 1) % 200 == 0:
            print(f"  features {k + 1}/{len(px)}", flush=True)
    atr_mat = pd.DataFrame({s: f["atr_pct"] for s, f in feats.items()})
    cap_rank = atr_mat.rank(axis=1, pct=True)

    spy_arr = spy_c.to_numpy(dtype=float)
    dates = [str(d)[:10] for d in cal]
    i0 = next(i for i, d in enumerate(dates) if d >= START)
    i1 = max(i for i, d in enumerate(dates) if d <= END)

    trades = {r: [] for r in ("R1", "R2", "R3", "R4")}
    cohort_fwd = {"COOLING": [], "COILED": [], "Aplus": [], "B": []}

    def fwd60(cl, i):
        e = min(i + 60, len(cl) - 1)
        if not (np.isfinite(cl[i]) and cl[i] > 0 and np.isfinite(cl[e])):
            return None
        r = (cl[e] / cl[i] - 1) * 100
        sp = (spy_arr[e] / spy_arr[i] - 1) * 100
        return r - sp

    for s, f in feats.items():
        score, tab = score_and_tab(f, cap_rank[s].to_numpy(dtype=float))
        g = grade_of(score)
        cl = f["close"].to_numpy(dtype=float)
        op = f["open"].to_numpy(dtype=float)
        lo = f["low"].to_numpy(dtype=float)
        fresh_a = (tab == TAB["FRESH"]) & (g == 3)
        prev = np.concatenate([[False], fresh_a[:-1]])
        entries_a = np.where(fresh_a & ~prev)[0]
        for cohort, mask in (("Aplus", (tab == TAB["FRESH"]) & (g == 4)),
                             ("B", (tab == TAB["FRESH"]) & (g == 2)),
                             ("COOLING", tab == TAB["COOLING"]),
                             ("COILED", tab == TAB["COILED"])):
            pm = np.concatenate([[False], mask[:-1]])
            for i in np.where(mask & ~pm)[0]:
                if i0 <= i <= i1:
                    x = fwd60(cl, i)
                    if x is not None:
                        cohort_fwd[cohort].append({"sym": s, "date": dates[i], "exc": x})

        last_exit = -1
        for i in entries_a:
            if not (i0 <= i <= i1) or i <= last_exit:
                continue
            entry = cl[i]
            if not (np.isfinite(entry) and entry > 0):
                continue
            end = min(i + MAX_HOLD_R1, len(cl) - 1)
            # R1: exit on first COOLING day; R2: first non-FRESH day
            e1 = e2 = end
            for j in range(i + 1, end + 1):
                if tab[j] == TAB["COOLING"] and e1 == end:
                    e1 = j
                if tab[j] != TAB["FRESH"] and e2 == end:
                    e2 = j
                if e1 < end and e2 < end:
                    break
            e3 = min(i + 60, len(cl) - 1)
            # R4: 5% stop (gap at open) -> 20% ratchet -> 120d
            stop, peak, e4, px4 = entry * 0.95, entry, min(i + 120, len(cl) - 1), None
            for j in range(i + 1, min(i + 120, len(cl) - 1) + 1):
                trail = 0.80 * peak
                if trail > stop:
                    if cl[j] < trail:
                        e4, px4 = j, cl[j]
                        break
                else:
                    if np.isfinite(op[j]) and op[j] <= stop:
                        e4, px4 = j, op[j]
                        break
                    if np.isfinite(lo[j]) and lo[j] <= stop:
                        e4, px4 = j, stop
                        break
                if np.isfinite(cl[j]):
                    peak = max(peak, cl[j])
            for rule, (ei, pxx) in (("R1", (e1, cl[e1])), ("R2", (e2, cl[e2])),
                                    ("R3", (e3, cl[e3])), ("R4", (e4, px4 if px4 else cl[e4]))):
                if not np.isfinite(pxx):
                    continue
                ret = (pxx / entry - 1) * 100 - COST_PT
                sp = (spy_arr[ei] / spy_arr[i] - 1) * 100
                trades[rule].append({"sym": s, "date": dates[i], "year": dates[i][:4],
                                     "ret": round(ret, 2), "exc": round(ret - sp, 2),
                                     "days": int(ei - i)})
            last_exit = e1

    def stats(rs):
        if not rs:
            return None
        e = np.array([r["exc"] for r in rs])
        r = np.array([r["ret"] for r in rs])
        return {"n": len(e), "mean_exc": round(float(e.mean()), 2),
                "median_exc": round(float(np.median(e)), 2),
                "hit_exc": round(float(100 * (e > 0).mean()), 1),
                "mean_ret": round(float(r.mean()), 2),
                "mean_days": round(float(np.mean([x["days"] for x in rs])), 1)}

    syms_sorted = sorted({t["sym"] for t in trades["R1"]})
    par = {s: k % 2 for k, s in enumerate(syms_sorted)}
    out = {"n_entries_A": len(trades["R1"]),
           "rules": {ru: stats(v) for ru, v in trades.items()},
           "by_year_R1": {y: stats([t for t in trades["R1"] if t["year"] == y]) for y in YEARS},
           "halves_R1": {h: stats([t for t in trades["R1"] if par[t["sym"]] == p])
                         for h, p in (("odd", 1), ("even", 0))},
           "cohorts_fwd60": {k: {"n": len(v),
                                 "mean_exc": round(float(np.mean([x["exc"] for x in v])), 2),
                                 "hit": round(float(100 * np.mean([x["exc"] > 0 for x in v])), 1)}
                             for k, v in cohort_fwd.items() if v}}
    json.dump({"summary": out, "trades_R1": trades["R1"]},
              open(os.path.join(REPO, "research", "fresh-ignition-backtest.json"), "w"), indent=1)

    print(f"\nA-grade FRESH IGNITION entries: {len(trades['R1'])}")
    for ru in ("R1", "R2", "R3", "R4"):
        print(f"  {ru}: {out['rules'][ru]}")
    print("by year R1:")
    for y in YEARS:
        print(f"  {y}: {out['by_year_R1'][y]}")
    print("halves R1:", out["halves_R1"])
    print("controls fwd60:", out["cohorts_fwd60"])
    print("wrote research/fresh-ignition-backtest.json")


if __name__ == "__main__":
    main()
