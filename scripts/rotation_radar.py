#!/usr/bin/env python3
"""Rotation Radar — daily sector/theme rotation-origination detector.

Detects group-level ignitions EARLY by measuring performance acceleration:
    accel = Perf.1M - (Perf.6M / 6)
i.e. how much the last month exceeds the group's own 6-month monthly run-rate.
This is the signature memory stocks (late '25), energy (Jan '26) and biotech
(June '26, XBI accel +19.5 caught 2026-07-09) all printed at their starts.

States:
  IGNITING  accel >= +8  and beating SPY on 1M and not collapsing this week
  WATCH     accel >= +4  (early candidates — one leg from igniting)
  ROLLING   accel <= -6  with a strong 6M base (old leadership decelerating)
  NEUTRAL   everything else

Run daily (EOD preferred, AM ok). Writes/diffs watchlists/rotation-radar-state.md.
NEW IGNITING entrant => run the Early Ignition single-name screen on that
group's names (holdings + list overlap) — see DRILLDOWN map below.

Data: TradingView scanner API (public, no auth, no chart tab needed).
"""
import json, os, re, sys, datetime, urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(REPO, "watchlists", "rotation-radar-state.md")

UNIVERSE = {  # ticker -> (label, drilldown hint)
    "AMEX:XLE": ("Energy", "XOM CVX COP OXY DVN + refiners"),
    "AMEX:XOP": ("Oil E&P", "E&P names"),
    "AMEX:OIH": ("Oil services", "BKR HAL SLB"),
    "AMEX:XLF": ("Financials", "GS BAC C BLK BX + insurance PGR ACGL CB ERIE"),
    "AMEX:KRE": ("Regional banks", "KRE holdings + HOPE FHB BCBP NTRS"),
    "AMEX:XLK": ("Tech broad", "megacap tech"),
    "NASDAQ:SMH": ("Semis", "NVDA AMD MU STX DELL AMAT ARM INTC + repair list"),
    "CBOE:IGV": ("Software", "NET CRWD PANW NOW SNOW"),
    "NASDAQ:SKYY": ("Cloud", "NET SNOW"),
    "AMEX:XBI": ("Biotech (eq-wt)", "XBI top-25 + TGTX SMMT ARQT — see ignition-biotech scan"),
    "NASDAQ:IBB": ("Biotech (cap-wt)", "VRTX REGN GILD AMGN"),
    "AMEX:XLV": ("Healthcare", "LLY ABBV JNJ AMGN BSX MDT WST ZTS"),
    "AMEX:XLI": ("Industrials", "GE URI UNP CAT DE EME FIX HWM MLI"),
    "CBOE:ITA": ("Defense/aero", "GD LHX LDOS HWM TDY AXON BWXT"),
    "AMEX:JETS": ("Airlines", "DAL UAL LUV"),
    "AMEX:XLU": ("Utilities", "DTE NEE CEG VST TLN"),
    "AMEX:XLP": ("Staples", "KO PEP PM CLX COST SFM"),
    "AMEX:XLY": ("Discretionary", "MCD SBUX NKE HD LOW CMG BROS SHAK"),
    "AMEX:XLB": ("Materials", "ALB FCX NUE DOW SHW BALL"),
    "AMEX:XME": ("Metals/mining", "FCX CENX MP BHP"),
    "AMEX:GDX": ("Gold miners", "NEM GOLD"),
    "AMEX:URA": ("Uranium", "CCJ OKLO SMR CEG"),
    "AMEX:KWEB": ("China internet", "BABA FUTU NIO"),
    "CBOE:ITB": ("Homebuilders", "DHI LEN"),
    "NASDAQ:BOTZ": ("Robotics", "SYM"),
    "AMEX:XRT": ("Retail", "TPR ANF GRMN"),
    "CBOE:ARKK": ("Spec growth", "HOOD COIN ROKU TDOC RXRX"),
    "NASDAQ:CIBR": ("Cybersecurity", "CRWD PANW"),
    "CBOE:IYT": ("Transports", "UNP ODFL JBHT XPO CAR"),
    "AMEX:SPY": ("SPY baseline", "-"),
}

def scan():
    body = json.dumps({"symbols": {"tickers": list(UNIVERSE.keys())},
                       "columns": ["name", "close", "change", "Perf.W", "Perf.1M", "Perf.3M", "Perf.6M", "Perf.YTD"]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/america/scan", data=body,
                                 headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]

def classify(accel, rel1m, w, m6):
    if accel >= 8 and rel1m > 0 and w > -2: return "IGNITING"
    if accel >= 4: return "WATCH"
    if accel <= -6 and m6 >= 10: return "ROLLING"
    return "NEUTRAL"

def load_prev():
    if not os.path.exists(STATE_FILE): return {}, None
    txt = open(STATE_FILE, encoding="utf-8").read()
    m = re.search(r"```json\n(.*?)\n```", txt, re.S)
    if not m: return {}, None
    d = json.loads(m.group(1))
    return d.get("states", {}), d.get("date")

def main():
    today = datetime.date.today().isoformat()
    data = scan()
    rows = []
    spy = None
    for r in data:
        tk = r["s"]
        n, c, ch, w, m1, m3, m6, ytd = [x if x is not None else 0 for x in r["d"]]
        if tk == "AMEX:SPY": spy = dict(m1=m1, m6=m6)
        rows.append(dict(tk=tk, label=UNIVERSE[tk][0], drill=UNIVERSE[tk][1], close=c, chg=ch,
                         w=w, m1=m1, m3=m3, m6=m6, ytd=ytd))
    for r in rows:
        r["accel"] = r["m1"] - r["m6"] / 6
        r["rel1m"] = r["m1"] - spy["m1"]
        r["state"] = classify(r["accel"], r["rel1m"], r["w"], r["m6"]) if r["tk"] != "AMEX:SPY" else "-"
    rows.sort(key=lambda r: -r["accel"])

    prev, prev_date = load_prev()
    deltas = []
    for r in rows:
        if r["tk"] == "AMEX:SPY": continue
        old = prev.get(r["tk"])
        if old and old != r["state"]:
            arrow = "🔥" if r["state"] == "IGNITING" else ("⚠" if r["state"] == "ROLLING" else "·")
            deltas.append(f"{arrow} **{r['label']} ({r['tk'].split(':')[1]})**: {old} → {r['state']} (accel {r['accel']:+.1f})")

    lines = [f"# Rotation Radar — {today}", "",
             f"accel = Perf.1M − Perf.6M/6 (excess vs own run-rate). Prev state: {prev_date or 'none (first run)'}.",
             "**NEW IGNITING ⇒ run the Early Ignition single-name screen on that group (drill column).**", ""]
    if deltas:
        lines += ["## ⚡ STATE CHANGES vs prior run"] + deltas + [""]
    else:
        lines += ["## State changes: none vs prior run", ""]
    lines += ["| Group | ETF | State | accel | 1W% | 1M% | 3M% | 6M% | rel1M | Drill-down |",
              "|-------|-----|-------|-------|-----|-----|-----|-----|-------|------------|"]
    for r in rows:
        lines.append(f"| {r['label']} | {r['tk'].split(':')[1]} | {r['state']} | {r['accel']:+.1f} | {r['w']:+.1f} | "
                     f"{r['m1']:+.1f} | {r['m3']:+.1f} | {r['m6']:+.1f} | {r['rel1m']:+.1f} | {r['drill']} |")
    lines += ["", "```json", json.dumps({"date": today, "states": {r["tk"]: r["state"] for r in rows if r["tk"] != "AMEX:SPY"}}, indent=1), "```", ""]

    out = "\n".join(lines)
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(out)

    # console summary for the brief
    ign = [r for r in rows if r["state"] == "IGNITING"]
    wat = [r for r in rows if r["state"] == "WATCH"]
    rol = [r for r in rows if r["state"] == "ROLLING"]
    print(f"Rotation Radar {today} (vs {prev_date or 'first run'})")
    if deltas:
        print("STATE CHANGES:"); [print(("  " + re.sub(r"\*\*", "", d)).encode("ascii","replace").decode()) for d in deltas]
    print(f"IGNITING: {', '.join(f'{r['label']} {r['accel']:+.1f}' for r in ign) or 'none'}")
    print(f"WATCH:    {', '.join(f'{r['label']} {r['accel']:+.1f}' for r in wat) or 'none'}")
    print(f"ROLLING:  {', '.join(f'{r['label']} {r['accel']:+.1f}' for r in rol) or 'none'}")
    print(f"State written: {STATE_FILE}")

if __name__ == "__main__":
    main()
