"""Calibrate the BUY SCORE against forward returns. No massaging.

Requested by Omar 2026-07-22 - is the composite BUY SCORE (used to rank the
Fresh Buys tab) actually predictive, or is it a plausible-looking number that
predicts nothing? The Magical gate looked sensible for months and separated
21-day returns by 0.03 points across 1,725 signals. This subjects the BUY SCORE
to the same test.

Method (stated so it can be attacked):
  * Input: every historical Chandelier BUY flip across 60 followed names, with
    the full score feature set computed AS OF THE SIGNAL BAR (no lookahead) plus
    forward close-to-close returns at 5/10/21 sessions.
  * Score each signal with the SAME score_long() that ranks live - not a
    re-implementation.
  * Report Spearman rank correlation (score vs forward return), decile
    monotonicity, top-minus-bottom quintile spread, hit rates by score band,
    and the correlation of EACH component separately.

Honesty constraints wired in:
  * Close-to-close returns, no stops/costs/sizing. This tests only the
    DIRECTIONAL half of the score. The risk-quality and liquidity components
    (~35% of the weight) are about survival and sizing and CANNOT be credited by
    a raw-return test - reported separately, never blended into a flattering
    single number.
  * Freshness is ~constant here (every signal scored at age 0), so it carries no
    discriminating power in this design - stated, not hidden.
  * Sample is ~2024-2026, a mostly-strong tape, and 60 clean-resolving liquid
    names = survivorship. Both disclosed.

Usage:
    python scripts/calibrate_buy_score.py <rows.csv|.txt>
"""
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rank_candidates import score_long  # noqa: E402

COLS = ["sym", "date", "last", "stop", "zlsma", "atr", "adx", "pdi", "ndi",
        "regime", "pct200", "advol", "f5", "f10", "f21"]


def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    # unwrap {"result":"..."} envelope if present
    try:
        env = json.loads(raw)
        if isinstance(env, dict) and isinstance(env.get("result"), str):
            raw = env["result"]
        elif isinstance(env, list):
            raw = "\n".join(env)
    except json.JSONDecodeError:
        pass
    rows = []
    for ln in raw.splitlines():
        ln = ln.strip().strip('"').strip(",")
        if not ln or ln.startswith("sym,"):
            continue
        parts = ln.split(",")
        if len(parts) < 15:
            continue
        d = {}
        ok = True
        for k, v in zip(COLS, parts):
            if k in ("sym", "date", "regime"):
                d[k] = v
            else:
                try:
                    d[k] = float(v) if v not in ("", "null") else None
                except ValueError:
                    ok = False
                    break
        if ok:
            rows.append(d)
    return rows


def spearman(xs, ys):
    """Rank correlation, ties averaged. Returns None if degenerate."""
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    if n < 10:
        return None, n
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(vals):
            j = i
            while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    xr, yr = ranks([p[0] for p in pairs]), ranks([p[1] for p in pairs])
    mx, my = sum(xr) / n, sum(yr) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xr, yr))
    dx = sum((a - mx) ** 2 for a in xr) ** 0.5
    dy = sum((b - my) ** 2 for b in yr) ** 0.5
    if dx == 0 or dy == 0:
        return None, n
    return num / (dx * dy), n


def stat_block(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    n = len(vals)
    vals_s = sorted(vals)
    return {"n": n, "mean": round(sum(vals) / n, 2),
            "median": round(vals_s[n // 2], 2),
            "win": round(100 * sum(1 for v in vals if v > 0) / n, 1)}


def main():
    rows = load(sys.argv[1])
    horizon = sys.argv[2] if len(sys.argv) > 2 else "f21"

    # score every signal with the live scorer
    for r in rows:
        sc, comp, pros, cons = score_long({
            "last": r["last"], "long_stop": r["stop"], "zlsma": r["zlsma"],
            "atr": r["atr"], "adx": r["adx"], "plus_di": r["pdi"],
            "minus_di": r["ndi"], "regime": r["regime"], "pct_vs_200": r["pct200"],
            "avg_dollar_vol": r["advol"], "bars_back": 0,
        })
        r["score"] = sc
        r["comp"] = comp

    out = []
    out.append("# BUY SCORE calibration - hard facts")
    out.append("")
    nsym = len(set(r["sym"] for r in rows))
    out.append(f"**Signals:** {len(rows)} historical Chandelier BUY flips across "
               f"{nsym} names.  ")
    out.append(f"**Forward return:** close-to-close, no stops/costs.  ")
    out.append(f"**Scored with** the live `score_long()`.  ")
    out.append("")
    out.append("## Read this before the numbers")
    out.append("- Close-to-close return tests only the DIRECTIONAL half of the score. "
               "The risk-quality (stop in ATR) and liquidity components - about 35% of "
               "the weight - are about SURVIVAL and SIZING and a raw-return test cannot "
               "credit them. They are reported separately below, not blended.")
    out.append("- Freshness is constant (~every signal scored at age 0), so it carries "
               "ZERO discriminating power in this design.")
    out.append("- Sample skews to a strong tape and uses liquid survivors. Both inflate "
               "results. Treat these as an UPPER bound on real-world edge.")
    out.append("")

    for hz in ("f5", "f10", "f21"):
        rho, n = spearman([r["score"] for r in rows], [r[hz] for r in rows])
        rho_txt = f"{rho:+.3f}" if rho is not None else "n/a"
        out.append(f"- Spearman(score, {hz[1:]}d return) = **{rho_txt}**  (n={n})")
    out.append("")
    out.append("  Reference: 0 = no relationship. |0.1| weak, |0.2| modest, |0.3|+ "
               "genuinely useful for ranking. Negative = the score is BACKWARDS.")
    out.append("")

    # decile monotonicity on the chosen horizon
    graded = [r for r in rows if r[horizon] is not None]
    graded.sort(key=lambda r: r["score"])
    out.append(f"## Return by score decile ({horizon[1:]}-day)")
    out.append("")
    out.append("| Decile | Score range | n | mean % | median % | win % |")
    out.append("|---|---|---|---|---|---|")
    dq = max(1, len(graded) // 10)
    decile_means = []
    for i in range(10):
        chunk = graded[i * dq: (i + 1) * dq] if i < 9 else graded[i * dq:]
        if not chunk:
            continue
        s = stat_block([r[horizon] for r in chunk])
        lo, hi = chunk[0]["score"], chunk[-1]["score"]
        decile_means.append(s["mean"])
        out.append(f"| {i+1} {'(worst)' if i==0 else '(best)' if i==9 else ''} "
                   f"| {lo:.0f}-{hi:.0f} | {s['n']} | {s['mean']:+.2f} "
                   f"| {s['median']:+.2f} | {s['win']:.0f}% |")
    out.append("")

    # top vs bottom quintile
    graded.sort(key=lambda r: r["score"])
    q = max(1, len(graded) // 5)
    bot = stat_block([r[horizon] for r in graded[:q]])
    top = stat_block([r[horizon] for r in graded[-q:]])
    if top and bot:
        spread = top["mean"] - bot["mean"]
        out.append(f"## Top vs bottom quintile ({horizon[1:]}-day)")
        out.append("")
        out.append(f"- Bottom 20% by score: mean {bot['mean']:+.2f}%, win {bot['win']:.0f}% (n={bot['n']})")
        out.append(f"- Top 20% by score: mean {top['mean']:+.2f}%, win {top['win']:.0f}% (n={top['n']})")
        out.append(f"- **Spread (top - bottom): {spread:+.2f} pts.**")
        if abs(spread) < 1.0:
            out.append("- **The score separates almost nothing.**")
        elif spread < 0:
            out.append("- **The score is BACKWARDS - low scores beat high scores.**")
        out.append("")

    # monotonic?
    if decile_means:
        inc = sum(1 for a, b in zip(decile_means, decile_means[1:]) if b > a)
        out.append(f"Monotonicity: {inc}/9 decile steps go the right way "
                   f"(9/9 = perfectly monotonic, ~4-5 = coin-flip noise).")
        out.append("")

    # per-component correlation
    out.append(f"## Which components carry it ({horizon[1:]}-day)")
    out.append("")
    out.append("| Component | weight | Spearman vs return |")
    out.append("|---|---|---|")
    comp_keys = [("risk_quality", "risk quality (stop/ATR)", 30),
                 ("trend_strength", "trend (ADX/DI)", 25),
                 ("regime", "regime (vs 200d)", 20),
                 ("structure", "structure (vs ZLSMA)", 10),
                 ("freshness", "freshness", 10),
                 ("liquidity", "liquidity", 5)]
    for key, label, wt in comp_keys:
        rho, n = spearman([r["comp"].get(key) for r in rows], [r[horizon] for r in rows])
        rho_txt = f"{rho:+.3f}" if rho is not None else "flat/none"
        out.append(f"| {label} | {wt} | {rho_txt} |")
    out.append("")
    out.append("A component with near-zero or negative correlation is dead weight in the "
               "score, or actively wrong. This is where the score should be re-weighted.")

    path = "research/buy-score-calibration-2026-07-22.md"
    os.makedirs("research", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
