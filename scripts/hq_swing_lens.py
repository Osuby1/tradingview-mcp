"""Read a sweep through the HQ Swing v1 lens and compare it to the Chandelier.

Omar asked (2026-07-22) that HQ Swing v1 be part of the analysis, not just a veto
bolted onto the end. The two systems answer different questions:

  O.G Chandelier : "has this turned UP recently?"   (short-term flip)
  HQ Swing v1    : "is this in a real uptrend?"     (regime: 200SMA + ADX + DI)

They disagree in BOTH directions, which is exactly why both are needed:
  * GDX passed every Chandelier test and failed regime badly (-12.4% vs 200-day).
  * PANW/DE/KRE passed the whole regime filter and failed the Chandelier's ZLSMA.

Four buckets come out of this:

  BOTH        - fresh flip AND regime-qualified. The only real candidates.
  CHANDELIER  - fresh flip, regime fails. Bounces inside downtrends. The GDX trap.
  HQ SWING    - regime-qualified but no fresh flip. NOT trades today; this is the
                forward watchlist - when one of these flips, it flips with the
                trend behind it.
  NEITHER     - ignore.

Usage:
    python scripts/hq_swing_lens.py <raw_sweep.json|.txt> [--fresh-bars 5]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import ADX_MIN, evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402


def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    try:
        env = json.loads(raw)
        if isinstance(env, dict) and isinstance(env.get("result"), str):
            return json.loads(env["result"])
        if isinstance(env, list):
            return env
        if isinstance(env, dict) and isinstance(env.get("rows"), list):
            return env["rows"]
    except json.JSONDecodeError:
        pass
    s, e = raw.find("["), raw.rfind("]")
    return json.loads(raw[s:e + 1])


def hq_qualified(r):
    """HQ Swing v1's regime test, independent of any Chandelier state."""
    return (r.get("regime") == "PASS"
            and (r.get("adx") or 0) >= ADX_MIN
            and (r.get("plus_di") or 0) > (r.get("minus_di") or 0))


def main():
    rows = [r for r in load(sys.argv[1]) if r.get("ok")]
    fresh_bars = 5
    if "--fresh-bars" in sys.argv:
        fresh_bars = int(sys.argv[sys.argv.index("--fresh-bars") + 1])

    for r in rows:
        r["_fresh"] = (r.get("ce_mode") == "BUY"
                       and r.get("bars_back") is not None
                       and r["bars_back"] <= fresh_bars)
        r["_hq"] = hq_qualified(r)

    both = [r for r in rows if r["_fresh"] and r["_hq"]]
    chand_only = [r for r in rows if r["_fresh"] and not r["_hq"]]
    hq_only = [r for r in rows if r["_hq"] and not r["_fresh"]]

    out = []
    out.append("# HQ Swing v1 lens vs O.G Chandelier")
    out.append("")
    out.append(f"**Scanned:** {len(rows)} names read clean, candles.  ")
    out.append(f"**Fresh** = Chandelier BUY within {fresh_bars} sessions.  ")
    out.append(f"**HQ-qualified** = regime PASS + ADX >= {ADX_MIN:.0f} + buyers in control.")
    out.append("")
    out.append("| Bucket | Count | Meaning |")
    out.append("|---|---|---|")
    out.append(f"| BOTH agree | **{len(both)}** | Fresh flip WITH the trend behind it - the only real candidates |")
    out.append(f"| Chandelier only | {len(chand_only)} | Bounce inside a broken trend - the GDX trap |")
    out.append(f"| HQ Swing only | {len(hq_only)} | Healthy trend, no flip yet - FORWARD watchlist |")
    out.append("")

    # --- the candidates, fully gated -------------------------------------
    out.append("## BOTH - fresh flip and regime-qualified")
    out.append("")
    if both:
        out.append("| Sym | Flip | Bars | Price | Stop | Stop % | vs 200d | ADX | +DI/-DI | Gate verdict |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        for r in sorted(both, key=lambda x: x["bars_back"]):
            try:
                verdict, _, _ = evaluate(r, position_size=DEFAULT_POSITION)
            except MissingGateData:
                verdict = "BLOCKED: gate data missing"
            last, stop = r.get("last"), r.get("long_stop")
            sp = f"{(last-stop)/last*100:.1f}%" if (last and stop and last > stop) else "-"
            out.append(f"| {r['rname']} | {r.get('flip_date')} | {r['bars_back']} | {last} "
                       f"| {stop} | {sp} | {r.get('pct_vs_200')}% | {r.get('adx')} "
                       f"| {r.get('plus_di')}/{r.get('minus_di')} | {verdict} |")
    else:
        out.append("**(none)** - no name has both a fresh flip and a healthy trend.")
    out.append("")

    # --- the trap --------------------------------------------------------
    out.append("## Chandelier only - fresh flip, regime FAILS")
    out.append("")
    out.append("These look like buys on the indicator and are not. This is the bucket "
               "GDX was in.")
    out.append("")
    if chand_only:
        out.append("| Sym | Flip | Price | Regime | vs 200d | ADX | Why regime fails |")
        out.append("|---|---|---|---|---|---|---|")
        for r in sorted(chand_only, key=lambda x: (x.get("pct_vs_200") or 0)):
            why = []
            if r.get("regime") != "PASS":
                why.append(f"regime {r.get('regime')}")
            if (r.get("adx") or 0) < ADX_MIN:
                why.append(f"ADX {r.get('adx')} < {ADX_MIN:.0f}")
            if (r.get("plus_di") or 0) <= (r.get("minus_di") or 0):
                why.append("-DI >= +DI")
            out.append(f"| {r['rname']} | {r.get('flip_date')} | {r.get('last')} "
                       f"| {r.get('regime')} | {r.get('pct_vs_200')}% | {r.get('adx')} "
                       f"| {'; '.join(why)} |")
    out.append("")

    # --- forward watchlist ------------------------------------------------
    out.append("## HQ Swing only - healthy trend, waiting for a flip")
    out.append("")
    out.append("NOT trades today. These are the names to want a Chandelier flip in, "
               "because the trend is already behind them. Sorted by trend strength.")
    out.append("")
    if hq_only:
        out.append("| Sym | Price | vs 200d | ADX | +DI/-DI | CE state | Bars since flip |")
        out.append("|---|---|---|---|---|---|---|")
        for r in sorted(hq_only, key=lambda x: -(x.get("adx") or 0))[:30]:
            out.append(f"| {r['rname']} | {r.get('last')} | {r.get('pct_vs_200')}% "
                       f"| {r.get('adx')} | {r.get('plus_di')}/{r.get('minus_di')} "
                       f"| {r.get('ce_mode')} | {r.get('bars_back')} |")
        if len(hq_only) > 30:
            out.append(f"\n*(showing 30 of {len(hq_only)} by ADX)*")
    out.append("")

    path = "watchlists/hq-swing-lens-2026-07-22.md"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out[:40]))
    print(f"\n... wrote {path}")
    print(f"BOTH={len(both)} CHANDELIER-ONLY={len(chand_only)} HQ-ONLY={len(hq_only)}")


if __name__ == "__main__":
    main()
