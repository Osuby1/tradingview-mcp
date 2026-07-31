"""
Momentum-flag-into-earnings study — executes the PRE-REGISTERED protocol in
research/momentum-flag-into-earnings-preregistration.md EXACTLY as written.
Thresholds are LOCKED. Registered 2026-07-30; run 2026-07-31.

Pre-registered cohort conditions (all four, at the close of the last session
BEFORE the report, daily bars, no lookahead):
  1. 6-month (126-session) total return beats SPY's by >= 40 points.
  2. Close within 12% of 52-week high AND a 3-10% pullback from that high
     within the prior 10 sessions.
  3. Final pre-earnings session closed UP >= 1.5% on volume >= 1.1x its
     50-day average.
  4. Close above a rising 200-day SMA.

Pre-registered verdict bars (LOCKED):
  - < 40 qualifying events  -> auto "insufficient data", blackout stands.
  - Asymmetry bar: median close-to-close > +1.0% AND win rate >= 55% AND
    10th percentile shallower than -8% AND beats Benchmark 1 median. ALL FOUR.
  - Options bar: synthetic delta-0.35 capped-premium ticket shows positive
    expectancy after -100% losers across >= 40 events.

Implementation choices NOT specified by the prereg (documented, made before
seeing results):
  - "Rising 200d SMA" = SMA200 at D0 > SMA200 20 sessions earlier.
  - Pullback depth = 1 - min(close over the 10 sessions before D0) / 52wk high
    (52wk high = trailing 252-session max of daily highs as of D0).
  - 50d avg volume = mean of the 50 sessions BEFORE D0 (D0 excluded).
  - BMO/AMC: earnings timestamp hour < 12 ET = before-open (D0 = prior
    trading day, D1 = report day); else after-close (D0 = report day,
    D1 = next trading day).
  - Adjusted prices (splits+dividends) throughout = total-return proxy.
  - Synthetic option exit IV = max(RV20, RV60) un-bumped (the 1.25 factor is
    the pre-earnings bump per the prereg; it crushes off after the print).
    r = 4%. Nearest monthly (3rd-Friday) expiry >= 5 calendar days after D0.
  - Reaction session must fall within 5 calendar days of the reported
    earnings date, else the event is dropped as unmappable (logged).
"""
import json, math, os, random, sys, time, traceback
from datetime import date, datetime, timedelta
from statistics import NormalDist

import numpy as np
import pandas as pd
import yfinance as yf

ND = NormalDist()
TODAY = pd.Timestamp("2026-07-31")
EVENT_START = pd.Timestamp("2024-07-31")   # 8 quarters back
EVENT_END = pd.Timestamp("2026-07-29")     # D1 must exist by 7/30 close
PRICE_START = "2023-05-01"
UNIVERSE_CSV = os.path.expanduser("~/Documents/Equities_Scanner/russell_starter.csv")
SCRATCH = r"C:\Users\osuby\AppData\Local\Temp\claude\C--Users-osuby-tradingview-mcp\a5f96f84-eb32-45ca-9054-b50adbf87839\scratchpad"
CACHE_PRICES = os.path.join(SCRATCH, "mf_prices.pkl")
CACHE_EARN = os.path.join(SCRATCH, "mf_earnings.json")
OUT_MD = r"C:\Users\osuby\tradingview-mcp\research\momentum-flag-earnings-study-results.md"
OUT_JSON = r"C:\Users\osuby\tradingview-mcp\research\momentum-flag-earnings-study-results.json"
R_RATE = 0.04
random.seed(42)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ---------------------------------------------------------------- universe
def load_universe():
    df = pd.read_csv(UNIVERSE_CSV)
    syms = [str(s).strip().upper().replace(".", "-") for s in df["symbol"].dropna()]
    return sorted(set(syms))

# ---------------------------------------------------------------- prices
def download_prices(tickers):
    if os.path.exists(CACHE_PRICES):
        log("price cache hit")
        return pd.read_pickle(CACHE_PRICES)
    frames = {"Open": [], "High": [], "Close": [], "Volume": []}
    failed = []
    chunks = [tickers[i:i+100] for i in range(0, len(tickers), 100)]
    for ci, chunk in enumerate(chunks):
        for attempt in (1, 2):
            try:
                raw = yf.download(chunk, start=PRICE_START, auto_adjust=True,
                                  group_by="column", progress=False, threads=True)
                break
            except Exception as e:
                log(f"chunk {ci} attempt {attempt} failed: {e}")
                if attempt == 2:
                    raw = None
                time.sleep(10)
        if raw is None or raw.empty:
            failed.extend(chunk)
            continue
        for f in frames:
            sub = raw[f] if isinstance(raw.columns, pd.MultiIndex) else raw[[f]].rename(columns={f: chunk[0]})
            frames[f].append(sub)
        log(f"prices chunk {ci+1}/{len(chunks)} done")
    out = {}
    for f in frames:
        big = pd.concat(frames[f], axis=1)
        big = big.loc[:, ~big.columns.duplicated()]
        big.index = pd.DatetimeIndex(big.index).tz_localize(None).normalize()
        out[f] = big.sort_index()
    # drop tickers with no close data at all
    dead = [c for c in out["Close"].columns if out["Close"][c].dropna().empty]
    obj = {"frames": out, "no_data": sorted(set(dead + failed))}
    pd.to_pickle(obj, CACHE_PRICES)
    return obj

# ---------------------------------------------------------------- earnings
def fetch_earnings(tickers):
    cache = {}
    if os.path.exists(CACHE_EARN):
        cache = json.load(open(CACHE_EARN))
    failures = []
    todo = [t for t in tickers if t not in cache]
    for i, t in enumerate(todo):
        got = None
        for attempt in (1, 2):
            try:
                ed = yf.Ticker(t).get_earnings_dates(limit=24)
                if ed is None or ed.empty:
                    got = []
                else:
                    idx = ed.index
                    rows = []
                    for ts in idx:
                        ts = pd.Timestamp(ts)
                        if ts.tzinfo is not None:
                            ts = ts.tz_convert("America/New_York")
                        rows.append([ts.strftime("%Y-%m-%d"), int(ts.hour)])
                    got = rows
                break
            except Exception as e:
                if attempt == 2:
                    failures.append({"ticker": t, "error": str(e)[:200]})
                else:
                    time.sleep(5)
        if got is not None:
            cache[t] = got
        if (i + 1) % 25 == 0:
            json.dump(cache, open(CACHE_EARN, "w"))
            log(f"earnings {i+1}/{len(todo)} (fails so far: {len(failures)})")
        time.sleep(0.15)
    json.dump(cache, open(CACHE_EARN, "w"))
    return cache, failures

# ---------------------------------------------------------------- BS math
def bs_call(S, K, T, sig, r=R_RATE):
    if T <= 0 or sig <= 0:
        return max(S - K, 0.0)
    d1 = (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))
    d2 = d1 - sig * math.sqrt(T)
    return S * ND.cdf(d1) - K * math.exp(-r * T) * ND.cdf(d2)

def bs_delta(S, K, T, sig, r=R_RATE):
    if T <= 0 or sig <= 0:
        return 1.0 if S > K else 0.0
    d1 = (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))
    return ND.cdf(d1)

def strike_for_delta(S, T, sig, target=0.35, r=R_RATE):
    d1 = ND.inv_cdf(target)
    K = S * math.exp(-(d1 * sig * math.sqrt(T) - (r + sig * sig / 2) * T))
    inc = 0.5 if S < 25 else 1.0 if S < 100 else 2.5 if S < 200 else 5.0
    return max(inc, round(K / inc) * inc)

def third_friday(y, m):
    d = date(y, m, 15)
    while d.weekday() != 4:
        d += timedelta(days=1)
    return d

def next_monthly_expiry(d0):
    d = d0.date()
    for k in range(4):
        m = d.month + k
        y = d.year + (m - 1) // 12
        m = (m - 1) % 12 + 1
        tf = third_friday(y, m)
        if (tf - d).days >= 5:
            return pd.Timestamp(tf)
    return None

# ---------------------------------------------------------------- events
def map_event(dates_idx, edate, hour):
    """Return (D0, D1) trading days around an earnings report, or None."""
    E = pd.Timestamp(edate)
    bmo = hour < 12
    if bmo:
        pos = dates_idx.searchsorted(E, side="left")   # D1 = first day >= E
    else:
        pos = dates_idx.searchsorted(E, side="right")  # D1 = first day > E
    if pos <= 0 or pos >= len(dates_idx):
        return None
    d1, d0 = dates_idx[pos], dates_idx[pos - 1]
    if abs((d1 - E).days) > 5 or abs((E - d0).days) > 5:
        return None
    return d0, d1

def main():
    universe = load_universe()
    log(f"universe: {len(universe)} tickers")
    pobj = download_prices(universe + ["SPY"])
    C, O, H, V = (pobj["frames"][k] for k in ("Close", "Open", "High", "Volume"))
    price_fail = pobj["no_data"]
    log(f"prices: {C.shape[1]} cols, {C.shape[0]} days; no-data: {len(price_fail)}")

    spy = C["SPY"].dropna()
    spy_r126 = spy / spy.shift(126) - 1

    # ---- pre-filter: any day in event window with 6mo outperformance >= 40pts
    win_mask = (C.index >= EVENT_START - pd.Timedelta(days=7)) & (C.index <= EVENT_END)
    prefilter = []
    for t in universe:
        if t not in C.columns:
            continue
        s = C[t]
        rel = (s / s.shift(126) - 1) - spy_r126
        if rel[win_mask].max() >= 0.40:
            prefilter.append(t)
    log(f"pre-filter (6mo outperf >=40pts at any point in window): {len(prefilter)} names")

    # ---- benchmark-2 random sample tickers (from FULL universe, seed 42)
    b2_sample = random.sample([t for t in universe if t in C.columns], 80)
    earn_targets = sorted(set(prefilter) | set(b2_sample))
    log(f"fetching earnings dates for {len(earn_targets)} tickers")
    earn, earn_failures = fetch_earnings(earn_targets)
    log(f"earnings fetched; failures: {len(earn_failures)}")

    def reactions(t, d0, d1):
        c, o = C[t], O[t]
        idx = c.index
        p1 = idx.get_loc(d1)
        c2c = c[d1] / c[d0] - 1
        gap = o[d1] / c[d0] - 1
        o2o = (o.iloc[p1 + 1] / o[d1] - 1) if p1 + 1 < len(idx) and not np.isnan(o.iloc[p1 + 1]) else np.nan
        return c2c, gap, o2o

    def all_events(t):
        """All mappable earnings events in window for ticker t."""
        out = []
        if t not in earn or t not in C.columns:
            return out
        s = C[t].dropna()
        if len(s) < 300:
            return out
        seen = set()
        for edate, hour in earn[t]:
            E = pd.Timestamp(edate)
            if E < EVENT_START or E > EVENT_END:
                continue
            m = map_event(s.index, E, hour)
            if m is None or m[0] in seen:
                continue
            seen.add(m[0])
            out.append((E, hour, m[0], m[1]))
        return out

    # ---- test the four locked conditions per event
    cohort, funnel = [], {"events_checked": 0, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "all4": 0}
    bench1_pool_tickers = set()
    dropped_unmappable = 0

    for t in prefilter:
        if t not in C.columns:
            continue
        c, h, v = C[t].dropna(), H[t], V[t]
        idx = c.index
        rel6 = (c / c.shift(126) - 1) - spy_r126.reindex(idx)
        h52 = H[t].reindex(idx).rolling(252).max()
        sma200 = c.rolling(200).mean()
        vol50 = V[t].reindex(idx).rolling(50).mean().shift(1)
        dayret = c / c.shift(1) - 1
        for (E, hour, d0, d1) in all_events(t):
            if d0 not in idx:
                dropped_unmappable += 1
                continue
            p0 = idx.get_loc(d0)
            if p0 < 260:
                continue
            funnel["events_checked"] += 1
            c1 = bool(rel6[d0] >= 0.40) if not np.isnan(rel6[d0]) else False
            hh = h52[d0]
            near_high = (not np.isnan(hh)) and c[d0] >= 0.88 * hh
            lows10 = c.iloc[p0 - 10:p0]
            depth = 1 - lows10.min() / hh if (not np.isnan(hh) and len(lows10) == 10) else np.nan
            c2 = bool(near_high and not np.isnan(depth) and 0.03 <= depth <= 0.10)
            volo = (not np.isnan(vol50[d0])) and (not np.isnan(v[d0])) and v[d0] >= 1.1 * vol50[d0]
            c3 = bool(dayret[d0] >= 0.015 and volo)
            sm_now, sm_prev = sma200[d0], sma200.iloc[p0 - 20]
            c4 = bool((not np.isnan(sm_now)) and (not np.isnan(sm_prev))
                      and c[d0] > sm_now and sm_now > sm_prev)
            for k, val in zip(("c1", "c2", "c3", "c4"), (c1, c2, c3, c4)):
                funnel[k] += int(val)
            if not (c1 and c2 and c3 and c4):
                continue
            funnel["all4"] += 1
            c2c, gap, o2o = reactions(t, d0, d1)
            if np.isnan(c2c):
                continue
            bench1_pool_tickers.add(t)

            # ---- synthetic delta-0.35 call ticket
            logret = np.log(c / c.shift(1))
            rv20 = logret.iloc[p0 - 19:p0 + 1].std() * math.sqrt(252)
            rv60 = logret.iloc[p0 - 59:p0 + 1].std() * math.sqrt(252)
            base_iv = max(rv20, rv60)
            iv_in = base_iv * 1.25
            expiry = next_monthly_expiry(d0)
            opt = None
            if expiry is not None and base_iv > 0:
                S0, S1 = c[d0], c[d1]
                T0 = (expiry - d0).days / 365.0
                K = strike_for_delta(S0, T0, iv_in)
                prem = bs_call(S0, K, T0, iv_in)
                if prem > 0.01:
                    T1 = max((expiry - d1).days / 365.0, 1 / 365.0)
                    exitv = max(bs_call(S1, K, T1, base_iv), max(S1 - K, 0.0))
                    opt = {"expiry": str(expiry.date()), "K": K,
                           "delta_in": round(bs_delta(S0, K, T0, iv_in), 3),
                           "iv_in": round(iv_in, 3), "prem_in": round(prem, 3),
                           "exit_val": round(exitv, 3),
                           "ret_pct": round((exitv / prem - 1) * 100, 1)}
            cohort.append({
                "ticker": t, "earnings_date": str(E.date()),
                "timing": "BMO" if hour < 12 else "AMC",
                "d0": str(d0.date()), "d1": str(d1.date()),
                "c2c_pct": round(c2c * 100, 2), "gap_pct": round(gap * 100, 2),
                "o2o_pct": round(o2o * 100, 2) if not np.isnan(o2o) else None,
                "rel6m_pts": round(rel6[d0] * 100, 1),
                "pullback_pct": round(depth * 100, 1),
                "preday_ret_pct": round(dayret[d0] * 100, 2),
                "option": opt})

    log(f"cohort: {len(cohort)} qualifying events; funnel {funnel}")

    # ---- Benchmark 1: same stocks, ALL their earnings events in window
    b1 = []
    for t in sorted(bench1_pool_tickers):
        for (E, hour, d0, d1) in all_events(t):
            c2c, gap, o2o = reactions(t, d0, d1)
            if not np.isnan(c2c):
                b1.append(c2c * 100)

    # ---- Benchmark 2: random-sample base rate (labeled)
    b2 = []
    for t in b2_sample:
        for (E, hour, d0, d1) in all_events(t):
            c2c, gap, o2o = reactions(t, d0, d1)
            if not np.isnan(c2c):
                b2.append(c2c * 100)

    def stats(vals):
        if not vals:
            return None
        a = np.array(vals, dtype=float)
        return {"n": int(len(a)), "median": round(float(np.median(a)), 2),
                "mean": round(float(np.mean(a)), 2),
                "win_rate": round(float((a > 0).mean() * 100, ), 1),
                "p10": round(float(np.percentile(a, 10)), 2),
                "p90": round(float(np.percentile(a, 90)), 2)}

    c2c_vals = [e["c2c_pct"] for e in cohort]
    gap_vals = [e["gap_pct"] for e in cohort]
    o2o_vals = [e["o2o_pct"] for e in cohort if e["o2o_pct"] is not None]
    opt_rets = [e["option"]["ret_pct"] for e in cohort if e["option"]]
    s_c2c, s_gap, s_o2o = stats(c2c_vals), stats(gap_vals), stats(o2o_vals)
    s_b1, s_b2 = stats(b1), stats(b2)
    s_opt = stats(opt_rets)

    n = len(cohort)
    insufficient = n < 40
    asym = None
    if not insufficient and s_c2c and s_b1:
        bars = {
            "median_gt_1pct": s_c2c["median"] > 1.0,
            "win_rate_ge_55": s_c2c["win_rate"] >= 55.0,
            "p10_shallower_than_-8": s_c2c["p10"] > -8.0,
            "beats_bench1_median": s_c2c["median"] > s_b1["median"]}
        asym = {"bars": bars, "pass": all(bars.values())}
    opt_bar = None
    if s_opt:
        opt_bar = {"n": s_opt["n"], "mean_ret_pct": s_opt["mean"],
                   "pass": (s_opt["n"] >= 40 and s_opt["mean"] > 0)}

    if insufficient:
        verdict = "INSUFFICIENT DATA — fewer than 40 qualifying events; earnings blackout stands unchanged (auto-verdict per pre-registration)."
    elif asym and asym["pass"] and opt_bar and opt_bar["pass"]:
        verdict = "BOTH BARS PASS — design the paper-only earnings-ticket tactic per the pre-registered action mapping. Blackout on shares stands."
    else:
        verdict = "FAIL — the earnings blackout stands exactly as written; the PBF hypothetical is formally closed as a lucky coin flip."

    result = {
        "study": "momentum-flag-into-earnings",
        "prereg": "research/momentum-flag-into-earnings-preregistration.md",
        "run_at": datetime.now().isoformat(timespec="seconds"),
        "universe_file": UNIVERSE_CSV, "universe_n": len(universe),
        "price_no_data": price_fail,
        "event_window": [str(EVENT_START.date()), str(EVENT_END.date())],
        "lookback_quarters": 8,
        "prefilter_n": len(prefilter),
        "earnings_fetch_failures": earn_failures,
        "funnel": funnel, "dropped_unmappable": dropped_unmappable,
        "cohort_n": n,
        "stats": {"close_to_close": s_c2c, "gap_close_to_open": s_gap,
                  "open_to_open_D1_to_D2": s_o2o,
                  "benchmark1_same_stocks_unconditional": s_b1,
                  "benchmark2_random_sample_base_rate": s_b2,
                  "synthetic_option": s_opt},
        "verdicts": {"insufficient_data": insufficient,
                     "asymmetry_bar": asym, "options_bar": opt_bar,
                     "final": verdict},
        "events": cohort}
    json.dump(result, open(OUT_JSON, "w"), indent=1)
    log("JSON written")
    log(f"VERDICT: {verdict}")
    return result

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
