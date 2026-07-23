"""Pull the origination scanner's TRACKER history into the daily run.

Omar, 2026-07-22: we have been tracking recommendation performance in the
scanner's TRACKER tab / recommendations_log.csv since the origination scans began
- surface it in the daily workbook instead of only the fresh call ledger.

Source: Documents/Equities_Scanner/recommendations_log.csv - every A/B/C pick the
origination scanner has made, with entry price, stop, current price, cur_ret
(FRACTION, e.g. -0.0139 = -1.39%), best/worst excursion, stop_hit, days_held,
fwd5/fwd21 (filled only once a pick reaches those horizons), status.

This module reads it, snapshots a dated copy into research/ for reproducibility,
and produces a scorecard broken down by grade, tab, and score quartile - plus the
honest headline: are higher grades / scores actually outperforming?

Units caveat baked in: cur_ret/best_ret/worst_ret are FRACTIONS; multiply by 100.
Also: the logged cur_ret is the scanner's own tracked number and can differ from
cur_price/price-1 (it measures from a next-session entry reference) - we report the
scanner's number as the system's self-grade and note the caveat.
"""
import csv
import json
import os
import shutil
import statistics as st
import sys

SRC = os.path.expanduser("~/Documents/Equities_Scanner/recommendations_log.csv")


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _load(path):
    return list(csv.DictReader(open(path, encoding="utf-8", errors="replace")))


def _block(rows):
    cur = [_f(r["cur_ret"]) * 100 for r in rows if _f(r["cur_ret"]) is not None]
    if not cur:
        return None
    best = [_f(r["best_ret"]) * 100 for r in rows if _f(r["best_ret"]) is not None]
    worst = [_f(r["worst_ret"]) * 100 for r in rows if _f(r["worst_ret"]) is not None]
    dh = [_f(r["days_held"]) for r in rows if _f(r["days_held"]) is not None]
    sh = sum(1 for r in rows if str(r.get("stop_hit", "")).strip() in ("1", "1.0", "True"))
    mat = [_f(r["fwd21"]) * 100 for r in rows if _f(r["fwd21"]) is not None]
    return {
        "n": len(cur), "win_pct": round(100 * sum(1 for x in cur if x > 0) / len(cur)),
        "mean": round(st.mean(cur), 2), "median": round(st.median(cur), 2),
        "mfe": round(st.mean(best), 1) if best else None,
        "mae": round(st.mean(worst), 1) if worst else None,
        "avg_days": round(st.mean(dh)) if dh else None,
        "stop_hits": sh,
        "matured": len(mat),
        "matured_mean": round(st.mean(mat), 2) if mat else None,
    }


def build(date):
    if not os.path.exists(SRC):
        return {"error": f"{SRC} not found"}
    # snapshot for reproducibility
    snap = f"research/recommendations_log-{date}.csv"
    os.makedirs("research", exist_ok=True)
    shutil.copy2(SRC, snap)
    rows = _load(SRC)

    dates = sorted(r["date"] for r in rows)
    overall = _block(rows)

    by_grade = {g: _block([r for r in rows if r["grade"] == g])
                for g in ("A+", "A", "B", "C")}
    by_grade = {g: v for g, v in by_grade.items() if v}
    by_tab = {t: _block([r for r in rows if r["tab"] == t])
              for t in sorted(set(r["tab"] for r in rows))}
    by_tab = {t: v for t, v in by_tab.items() if v}

    # does score predict? top vs bottom quartile by score_precap
    scored = sorted((_f(r["score_precap"]), _f(r["cur_ret"]) * 100)
                    for r in rows if _f(r["score_precap"]) and _f(r["cur_ret"]) is not None)
    qspread = None
    if len(scored) >= 8:
        q = len(scored) // 4
        bot = st.mean([x[1] for x in scored[:q]])
        top = st.mean([x[1] for x in scored[-q:]])
        qspread = {"bottom_q_mean": round(bot, 2), "top_q_mean": round(top, 2),
                   "spread": round(top - bot, 2)}

    return {"date": date, "source": os.path.basename(SRC), "snapshot": snap,
            "date_range": [dates[0], dates[-1]] if dates else None,
            "total": len(rows), "overall": overall,
            "by_grade": by_grade, "by_tab": by_tab, "score_quartile": qspread}


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else "latest"
    rec = build(date)
    if rec.get("error"):
        raise SystemExit(rec["error"])

    o = rec["overall"]
    lines = []
    lines.append(f"# Origination TRACKER - track record")
    lines.append("")
    lines.append(f"Source {rec['source']}, {rec['total']} picks, "
                 f"{rec['date_range'][0]} to {rec['date_range'][1]}. Returns are "
                 f"UNREALIZED (matured={o['matured']} of {rec['total']} at fwd21).")
    lines.append("")
    lines.append(f"**ALL {o['n']} picks: {o['win_pct']}% green, mean {o['mean']:+.2f}%, "
                 f"median {o['median']:+.2f}%, avg {o['avg_days']} days held, "
                 f"{o['stop_hits']} stop-hits.**")
    lines.append("")
    lines.append("## By grade - is a higher grade worth more?")
    lines.append("| Grade | n | win% | mean | median | MFE | MAE |")
    lines.append("|---|---|---|---|---|---|---|")
    for g, v in rec["by_grade"].items():
        lines.append(f"| {g} | {v['n']} | {v['win_pct']}% | {v['mean']:+.2f}% "
                     f"| {v['median']:+.2f}% | +{v['mfe']}% | {v['mae']}% |")
    lines.append("")
    lines.append("## By tab")
    lines.append("| Tab | n | win% | mean | median |")
    lines.append("|---|---|---|---|---|")
    for t, v in rec["by_tab"].items():
        lines.append(f"| {t} | {v['n']} | {v['win_pct']}% | {v['mean']:+.2f}% | {v['median']:+.2f}% |")
    lines.append("")
    if rec["score_quartile"]:
        q = rec["score_quartile"]
        lines.append(f"## Does the score predict? Top-25% vs bottom-25% by score")
        lines.append(f"- bottom quartile mean {q['bottom_q_mean']:+.2f}%, "
                     f"top quartile mean {q['top_q_mean']:+.2f}%, "
                     f"**spread {q['spread']:+.2f}pt**")
        if q["spread"] <= 0:
            lines.append("- **The score does NOT predict returns - the spread is flat or "
                         "backwards, the same result as the BUY SCORE calibration.**")

    with open("research/track-record.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open("research/track-record.json", "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1)
    print("\n".join(lines))
    print(f"\nwrote research/track-record.md + .json, snapshot {rec['snapshot']}")


if __name__ == "__main__":
    main()
