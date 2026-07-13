#!/usr/bin/env python3
"""Ignition Sweep — daily MARKET-WIDE single-name "before photo" detector.

Closes the gap between the Rotation Radar (which GROUP is igniting) and the
Early Ignition screen (which NAMES): this sweeps the ENTIRE liquid US market
daily, so names like APGE (Q-fired 6/23, before biotech was on any radar or
list) surface themselves instead of waiting to be looked for.

Pipeline:
 1. Scanner pre-filter (1 request): US common stocks, cap>$500M, avg vol>500k,
    price>$5, within 15% of 52wk high, 6M perf > -5% -> candidate list (~100-400)
 2. Precision pass (Yahoo daily bars): exact port of pine/early_ignition.pine
    - FIRED-Q / FIRED-S in the last 5 completed sessions
    - LOADED: stage-2 + RS-line 126d new high + ADX>20 + within 5% of the 60d
      base high — everything lit except the RVOL>3 ignition bar
 3. Diff vs prior run (watchlists/ignition-sweep-state.md): NEW fires/LOADED
    lead the report. Output feeds the EOD brief + Ignition Tracker + alerts.

Run daily post-close (EOD session). Runtime ~2-5 min (network-bound).
"""
import json, os, re, sys, time, datetime, urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(REPO, "watchlists", "ignition-sweep-state.md")

def fetch(url, body=None):
    req = urllib.request.Request(url, data=body,
        headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())

def prefilter():
    # NOTE: high_52_week_percent is NOT a valid scanner FILTER field (matches
    # nothing silently) — pull price_52_week_high as a COLUMN and filter here.
    body = json.dumps({
        "filter": [
            {"left": "market_cap_basic", "operation": "greater", "right": 500_000_000},
            {"left": "average_volume_10d_calc", "operation": "greater", "right": 500_000},
            {"left": "close", "operation": "greater", "right": 5},
            {"left": "Perf.6M", "operation": "greater", "right": -5},
            {"left": "type", "operation": "equal", "right": "stock"},
            {"left": "exchange", "operation": "in_range", "right": ["NASDAQ", "NYSE", "AMEX"]},
        ],
        "columns": ["name", "close", "price_52_week_high", "Perf.6M", "sector"],
        "sort": {"sortBy": "Perf.6M", "sortOrder": "desc"},
        "range": [0, 1400],
    }).encode()
    data = fetch("https://scanner.tradingview.com/america/scan", body)["data"]
    out = []
    for r in data:
        name, close, hi52, p6, sector = r["d"]
        if close and hi52 and close >= hi52 * 0.85:  # within 15% of 52wk high
            out.append((r["s"].split(":")[1], sector or "?"))
        if len(out) >= 400: break
    return out

def get_bars(sym):
    d = fetch(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=2y")["chart"]["result"][0]
    ts = d["timestamp"]; q = d["indicators"]["quote"][0]
    return [(t, h, l, c, v) for t, h, l, c, v in zip(ts, q["high"], q["low"], q["close"], q["volume"])
            if c is not None and h is not None]

def sma(a, n, i): return sum(a[i - n + 1:i + 1]) / n

def adx14_at(H, L, C, i):
    n = 14
    trs, pdms, ndms = [], [], []
    for k in range(max(1, i - 3 * n), i + 1):
        trs.append(max(H[k] - L[k], abs(H[k] - C[k - 1]), abs(L[k] - C[k - 1])))
        up, dn = H[k] - H[k - 1], L[k - 1] - L[k]
        pdms.append(up if (up > dn and up > 0) else 0.0)
        ndms.append(dn if (dn > up and dn > 0) else 0.0)
    if len(trs) < 2 * n: return 0
    str_, spdm, sndm = sum(trs[:n]), sum(pdms[:n]), sum(ndms[:n])
    dxs = []
    for k in range(n, len(trs)):
        str_ = str_ - str_ / n + trs[k]; spdm = spdm - spdm / n + pdms[k]; sndm = sndm - sndm / n + ndms[k]
        pdi, ndi = 100 * spdm / str_, 100 * sndm / str_
        dxs.append(100 * abs(pdi - ndi) / (pdi + ndi) if (pdi + ndi) else 0)
    if len(dxs) < n: return 0
    adx = sum(dxs[:n]) / n
    for dx in dxs[n:]: adx = (adx * (n - 1) + dx) / n
    return adx

def analyze(sym, spymap, today_day):
    bars = get_bars(sym)
    if bars and bars[-1][0] // 86400 >= today_day:
        bars = bars[:-1]  # drop today's partial bar
    if len(bars) < 300: return None
    T = [b[0] for b in bars]; H = [b[1] for b in bars]; L = [b[2] for b in bars]
    C = [b[3] for b in bars]; V = [b[4] for b in bars]

    def spy_at(d):
        for dd in (d, d - 1, d - 2, d - 3):
            if dd in spymap: return spymap[dd]
        return None

    def conditions(i):
        if i < 260: return None
        s200 = sma(C, 200, i); s200p = sma(C, 200, i - 20); s50 = sma(C, 50, i)
        va = sma(V, 50, i)
        rvol = V[i] / va if va > 0 else 0
        roc = (C[i] / C[i - 21] - 1) * 100
        ext = (C[i] - s50) / s50 * 100
        d_now, d_then = T[i] // 86400, T[i - 126] // 86400
        sn, st = spy_at(d_now), spy_at(d_then)
        rs_beat = sn and st and (C[i] / C[i - 126] - 1) > (sn / st - 1)
        rsl_hist = []
        for k in range(i - 125, i + 1):
            sc = spy_at(T[k] // 86400)
            if sc: rsl_hist.append(C[k] / sc)
        rs_nh = len(rsl_hist) > 100 and rsl_hist[-1] >= max(rsl_hist) * 0.9999
        hi60 = max(C[i - 60:i]); hi252 = max(H[i - 251:i + 1])
        base_break = C[i] > hi60
        new52 = C[i] >= hi252 * 0.99
        a = adx14_at(H, L, C, i)
        quality = C[i] > s200 and s200 > s200p and base_break and new52 and rvol > 3.0 and rs_beat and rs_nh and a > 20
        spec = roc > 50 and rvol > 5.0 and ext > 30 and C[i] > s50 and a > adx14_at(H, L, C, i - 5)
        return dict(q=quality, s=spec, rvol=rvol, adx=a, stage2=(C[i] > s200 and s200 > s200p),
                    rs_beat=bool(rs_beat), rs_nh=rs_nh, d60=(C[i] / hi60 - 1) * 100,
                    d52=(C[i] / (hi252 * 0.99) - 1) * 100)

    last = conditions(len(C) - 1)
    if last is None: return None
    fired_q, fired_s = None, None
    prev_q = prev_s = True  # require a fresh fire inside the window
    for i in range(len(C) - 6, len(C)):
        cd = conditions(i) if i >= 260 else None
        if not cd: prev_q = prev_s = False; continue
        if cd["q"] and not prev_q:
            fired_q = datetime.datetime.fromtimestamp(T[i], datetime.timezone.utc).strftime("%m-%d")
        if cd["s"] and not prev_s:
            fired_s = datetime.datetime.fromtimestamp(T[i], datetime.timezone.utc).strftime("%m-%d")
        prev_q, prev_s = cd["q"], cd["s"]
    loaded = (last["stage2"] and last["rs_beat"] and last["rs_nh"] and last["adx"] > 20
              and last["d60"] > -5 and last["d52"] > -6 and not fired_q)
    state = "FIRED-Q" if fired_q else ("FIRED-S" if fired_s else ("LOADED" if loaded else None))
    if not state: return None
    return dict(sym=sym, state=state, close=C[-1], fq=fired_q or "", fs=fired_s or "",
                d60=last["d60"], adx=last["adx"], rvol=last["rvol"])

def load_prev():
    if not os.path.exists(STATE_FILE): return {}, None
    m = re.search(r"```json\n(.*?)\n```", open(STATE_FILE, encoding="utf-8").read(), re.S)
    if not m: return {}, None
    d = json.loads(m.group(1))
    return d.get("states", {}), d.get("date")

def main():
    today = datetime.date.today().isoformat()
    today_day = int(datetime.datetime.now(datetime.timezone.utc).timestamp()) // 86400
    cands = prefilter()
    print(f"Pre-filter candidates: {len(cands)}", file=sys.stderr)
    spy_bars = get_bars("SPY")
    spymap = {b[0] // 86400: b[3] for b in spy_bars}

    hits, fails = [], 0
    for sym, sector in cands:
        try:
            r = analyze(sym, spymap, today_day)
            if r: r["sector"] = sector; hits.append(r)
        except Exception:
            fails += 1
        time.sleep(0.1)
    print(f"Hits: {len(hits)}, fetch fails: {fails}", file=sys.stderr)

    prev, prev_date = load_prev()
    order = {"FIRED-Q": 0, "FIRED-S": 1, "LOADED": 2}
    hits.sort(key=lambda r: (order[r["state"]], -r["adx"]))
    new = [h for h in hits if prev.get(h["sym"]) != h["state"]]

    lines = [f"# Ignition Sweep — {today} (market-wide, {len(cands)} pre-filtered)", "",
             f"Prev state: {prev_date or 'none (first run)'}. FIRED = early_ignition.pine signal in last 5 sessions; LOADED = all structure lit except the RVOL>3 bar.", ""]
    if new:
        lines += ["## 🔥 NEW since prior run"] + [
            f"- **{h['sym']}** {h['state']} @ {h['close']:.2f} ({h['sector']}) — d60 {h['d60']:+.1f}%, ADX {h['adx']:.0f}"
            + (f", Q-fired {h['fq']}" if h['fq'] else "") for h in new] + [""]
    else:
        lines += ["## No new fires/LOADED vs prior run", ""]
    lines += ["| Sym | State | Close | vs60dHi | ADX | fired | Sector |", "|-----|-------|-------|---------|-----|-------|--------|"]
    for h in hits:
        lines.append(f"| {h['sym']} | {h['state']} | {h['close']:.2f} | {h['d60']:+.1f}% | {h['adx']:.0f} | {h['fq'] or h['fs'] or ''} | {h['sector'][:20]} |")
    lines += ["", "```json", json.dumps({"date": today, "states": {h["sym"]: h["state"] for h in hits}}, indent=1), "```", ""]
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    open(STATE_FILE, "w", encoding="utf-8").write("\n".join(lines))

    print(f"Ignition Sweep {today} (vs {prev_date or 'first run'})")
    for h in hits:
        tag = "NEW " if prev.get(h["sym"]) != h["state"] else "    "
        print(f"{tag}{h['sym']:6s} {h['state']:8s} {h['close']:>9.2f}  d60={h['d60']:+.1f}%  ADX={h['adx']:.0f}  {h['sector'][:20]}")
    print(f"State written: {STATE_FILE}")

if __name__ == "__main__":
    main()
