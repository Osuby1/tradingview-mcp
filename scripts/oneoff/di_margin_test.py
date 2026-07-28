"""Pre-registered test: does the buyer/seller margin (+DI - -DI) predict returns?

Hypothesis origin (2026-07-28): in the week-of-7/24 four-name batch, the two
names with dominant buying pressure (HAS, SJM) outran the name where buyers were
barely ahead (MLI, +4 margin). Omar asked whether that was knowable Friday.

Test design - registered BEFORE looking at the result:
  * Dataset: research/buy-score-calibration-2026-07-22-signals.csv - the frozen
    170-signal set from the 7/22 buy-score calibration. It PREDATES the trades
    that generated the hypothesis, so this is out-of-sample relative to the
    hypothesis source (though the same tape regime; see caveats in the output).
  * Metric: Spearman rank correlation of (pdi - ndi) vs forward returns at
    5, 10 and 21 days. Spearman, not Pearson, to match the 7/22 methodology.
  * Comparison baselines on the SAME rows: raw ADX, and the v2 trend sub-score.
  * Decision rule (stated in advance): the margin earns ranking weight ONLY if
    its 21-day Spearman beats raw ADX's AND clears +0.10. Otherwise it stays a
    display-only column.

Writes research/di-margin-test-2026-07-28.md + .json.
"""
import csv
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, "research", "buy-score-calibration-2026-07-22-signals.csv")


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def spearman(xs, ys):
    """Spearman rank correlation, average ranks for ties, no scipy needed."""
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    n = len(rx)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx) ** 0.5
    dy = sum((b - my) ** 2 for b in ry) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
    out = {"dataset": os.path.basename(SRC), "n_total": len(rows), "horizons": {}}
    for hz in ("f5", "f10", "f21"):
        sample = [(r, _f(r[hz])) for r in rows if _f(r[hz]) is not None
                  and _f(r["pdi"]) is not None and _f(r["ndi"]) is not None
                  and _f(r["adx"]) is not None]
        if len(sample) < 20:
            out["horizons"][hz] = {"n": len(sample), "note": "too few rows"}
            continue
        margin = [_f(r["pdi"]) - _f(r["ndi"]) for r, _ in sample]
        adx = [_f(r["adx"]) for r, _ in sample]
        fwd = [v for _, v in sample]
        # v2 trend sub-score on the same rows, for a like-for-like baseline
        def clamp(x):
            return max(0.0, min(1.0, x))
        trend = [clamp(0.6 * clamp((a - 15) / 25) + 0.4 * clamp(m / 20))
                 for a, m in zip(adx, margin)]
        # quartile means for readability
        order = sorted(range(len(margin)), key=lambda i: margin[i])
        q = len(order) // 4
        bot = sum(fwd[i] for i in order[:q]) / q
        top = sum(fwd[i] for i in order[-q:]) / q
        out["horizons"][hz] = {
            "n": len(sample),
            "spearman_di_margin": round(spearman(margin, fwd), 3),
            "spearman_adx": round(spearman(adx, fwd), 3),
            "spearman_v2_trend_sub": round(spearman(trend, fwd), 3),
            "bottom_quartile_mean_pct": round(bot, 2),
            "top_quartile_mean_pct": round(top, 2),
            "top_minus_bottom_pt": round(top - bot, 2),
        }

    h21 = out["horizons"].get("f21", {})
    di21, adx21 = h21.get("spearman_di_margin"), h21.get("spearman_adx")
    passed = (di21 is not None and adx21 is not None
              and di21 > adx21 and di21 >= 0.10)
    out["decision_rule"] = ("margin earns ranking weight only if 21d Spearman "
                            "beats raw ADX AND >= +0.10")
    out["verdict"] = ("PASS - margin earned ranking weight" if passed else
                      "FAIL - margin stays a DISPLAY-ONLY column")

    jpath = os.path.join(REPO, "research", "di-margin-test-2026-07-28.json")
    json.dump(out, open(jpath, "w"), indent=1)

    lines = [
        "# Buyer/seller margin (+DI - -DI) - pre-registered predictive test",
        "",
        f"Run 2026-07-28 on the frozen 7/22 calibration set ({out['n_total']} signals, "
        "April-June window). Hypothesis came from the week-of-7/24 four-name batch "
        "(HAS/SJM dominant-buyer names outran MLI's +4 margin), so the dataset is "
        "independent of the trades that raised the question.",
        "",
        "| Horizon | n | Spearman: DI margin | Spearman: raw ADX | Spearman: v2 trend sub | Top-25% mean | Bottom-25% mean |",
        "|---|---|---|---|---|---|---|",
    ]
    for hz, lab in (("f5", "5 days"), ("f10", "10 days"), ("f21", "21 days")):
        d = out["horizons"].get(hz, {})
        if "spearman_di_margin" not in d:
            continue
        lines.append(f"| {lab} | {d['n']} | {d['spearman_di_margin']:+.3f} "
                     f"| {d['spearman_adx']:+.3f} | {d['spearman_v2_trend_sub']:+.3f} "
                     f"| {d['top_quartile_mean_pct']:+.2f}% | {d['bottom_quartile_mean_pct']:+.2f}% |")
    lines += [
        "",
        f"**Decision rule (set before the run):** {out['decision_rule']}.",
        f"**Verdict: {out['verdict']}.**",
        "",
        "Caveats: one tape regime (spring 2026), unrealized 21-day horizons, and a "
        "modest sample. A pass here means 'worth weighting and re-testing', never "
        "'proven'. The Fresh Buys column ships either way - it is information, "
        "not a rule.",
    ]
    mpath = os.path.join(REPO, "research", "di-margin-test-2026-07-28.md")
    open(mpath, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(json.dumps(out, indent=1))
    print(f"wrote {mpath}")


if __name__ == "__main__":
    main()
