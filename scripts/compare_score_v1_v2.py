"""Test the re-weighted score_long_v2 HONESTLY against v1.

The v2 weights were chosen from the full 170-signal calibration, so any
full-sample re-test is CIRCULAR - it will flatter v2 by construction. This script
reports that in-sample number but leads with two held-out cuts, which are the
only ones that carry information:

  * TIME split: earlier 60% "informed" the weights (loosely - the direction was
    read off the whole sample), later 40% is the closest thing to out-of-sample.
  * SYMBOL split: odd vs even names, so a symbol's signals never straddle both
    sides.

Neither is perfectly clean (the weight DIRECTION was read off the full sample),
so even these are optimistic. State it, do not hide it.

Usage: python scripts/compare_score_v1_v2.py <signals.csv>
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calibrate_buy_score import load, spearman  # noqa: E402
from rank_candidates import score_long, score_long_v2  # noqa: E402


def score_all(rows):
    for r in rows:
        feat = {"last": r["last"], "long_stop": r["stop"], "zlsma": r["zlsma"],
                "atr": r["atr"], "adx": r["adx"], "plus_di": r["pdi"],
                "minus_di": r["ndi"], "regime": r["regime"],
                "pct_vs_200": r["pct200"], "avg_dollar_vol": r["advol"],
                "bars_back": 0}
        r["v1"] = score_long(feat)[0]
        r["v2"] = score_long_v2(feat)[0]


def rho_line(rows, label):
    parts = [label.ljust(22)]
    for hz in ("f5", "f10", "f21"):
        r1, _ = spearman([r["v1"] for r in rows], [r[hz] for r in rows])
        r2, n = spearman([r["v2"] for r in rows], [r[hz] for r in rows])
        parts.append(f"{hz[1:]}d v1={_f(r1)} v2={_f(r2)}")
    return "  ".join(parts) + f"  (n={n})"


def _f(x):
    return f"{x:+.3f}" if x is not None else " n/a "


def quintile_spread(rows, key, hz="f21"):
    g = [r for r in rows if r[hz] is not None]
    g.sort(key=lambda r: r[key])
    q = max(1, len(g) // 5)
    bot = sum(r[hz] for r in g[:q]) / q
    top = sum(r[hz] for r in g[-q:]) / q
    return top - bot


def main():
    rows = load(sys.argv[1])
    score_all(rows)

    out = []
    out.append("# BUY SCORE v2 (re-weighted) vs v1 - honest test")
    out.append("")
    out.append("v2 weights: trend 0.45, structure 0.35, regime 0.15, freshness 0.03, "
               "liquidity 0.02. Risk quality REMOVED from the sort.")
    out.append("")
    out.append("**The v2 weights were picked from this very sample, so the full-sample "
               "row below is CIRCULAR and optimistic. Read the held-out rows.**")
    out.append("")
    out.append("## Spearman(score, forward return)")
    out.append("```")
    out.append(rho_line(rows, "FULL (circular)"))

    # time split
    dated = sorted(rows, key=lambda r: r["date"])
    cut = int(len(dated) * 0.6)
    out.append(rho_line(dated[cut:], "TIME held-out (40%)"))

    # symbol split: even-indexed distinct symbols vs odd
    syms = sorted(set(r["sym"] for r in rows))
    odd = {s for i, s in enumerate(syms) if i % 2 == 1}
    out.append(rho_line([r for r in rows if r["sym"] in odd], "SYMBOL held-out (odd)"))
    out.append("```")
    out.append("")

    out.append("## Top-minus-bottom quintile, 21-day (pts)")
    out.append("```")
    for label, subset in (("FULL (circular)", rows),
                          ("TIME held-out (40%)", dated[cut:]),
                          ("SYMBOL held-out (odd)", [r for r in rows if r["sym"] in odd])):
        s1 = quintile_spread(subset, "v1")
        s2 = quintile_spread(subset, "v2")
        out.append(f"{label.ljust(22)} v1={s1:+.2f}   v2={s2:+.2f}   "
                   f"delta={s2-s1:+.2f}")
    out.append("```")
    out.append("")

    out.append("## Verdict")
    out.append("")
    # decide verdict from the held-out time 21d
    r1t, _ = spearman([r["v1"] for r in dated[cut:]], [r["f21"] for r in dated[cut:]])
    r2t, _ = spearman([r["v2"] for r in dated[cut:]], [r["f21"] for r in dated[cut:]])
    delta = (r2t or 0) - (r1t or 0)
    if r2t is not None and r2t >= 0.15 and delta > 0.05:
        out.append(f"On held-out time data, v2 rank-correlates {r2t:+.3f} at 21d vs v1 "
                   f"{r1t:+.3f} - a real improvement, though still only 'modest' and "
                   f"from one strong-tape window. Adopt v2 as the ranker but keep the "
                   f"UNCALIBRATED label until an out-of-period re-run confirms it.")
    elif r2t is not None and delta > 0.02:
        out.append(f"On held-out time data v2 ({r2t:+.3f} at 21d) edges v1 ({r1t:+.3f}) "
                   f"but both are still weak (<|0.15|). v2 is LESS WRONG, not "
                   f"calibrated. Use it as the ranker because it drops the "
                   f"return-negative risk-quality driver, but present it as a label, "
                   f"not a forecast.")
    else:
        out.append(f"On held-out time data v2 ({r2t:+.3f} at 21d) does NOT beat v1 "
                   f"({r1t:+.3f}) enough to claim an edge. The re-weight removes the "
                   f"return-negative risk-quality component (a real improvement in "
                   f"honesty) but does not buy predictive power. Do not sell v2 as "
                   f"calibrated.")
    out.append("")
    out.append("Caveats unchanged from the calibration: one ~4-month strong tape, 60 "
               "liquid survivors, close-to-close no costs, freshness untested, and the "
               "held-out cuts are only PARTIALLY clean (weight direction was read off "
               "the full sample). Run out-of-period before trusting any of this live.")

    path = "research/buy-score-v2-vs-v1-2026-07-22.md"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
