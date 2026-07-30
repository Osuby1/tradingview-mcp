"""Digest of the 7/29 chain outputs for the EOD brief."""
import json
import os

REPO = r"C:\Users\osuby\tradingview-mcp"

res = json.load(open(os.path.join(REPO, "watchlists", "universe-results-2026-07-29.json")))
hits = {h["sym"]: h for h in res.get("hits", [])}
passing = [s for s, h in hits.items()
           if str(h.get("verdict", "")).startswith(("CANDIDATE", "STARTER"))]
print("UNIVERSE: scanned", res.get("scanned"), "| fresh", res.get("fresh_count"),
      "| sell-mode", len(res.get("sell_mode", [])), "| passing", len(passing))
print("PASSING:", ", ".join(sorted(passing)))

ms = json.load(open(os.path.join(REPO, "watchlists", "market-structure-2026-07-29.json")))
p = ms.get("index_path") or {}
print("\nSPY:", p.get("shape"), "| day", p.get("day_pct"), "| range_pos", p.get("range_pos"))
rows = sorted(ms.get("rows", []), key=lambda r: -(r.get("day_pct") or 0))
print("BEST:", [(r["group"], r["day_pct"]) for r in rows[:4]])
print("WORST:", [(r["group"], r["day_pct"]) for r in rows[-4:]])
u = ms.get("unwind") or {}
print("UNWIND:", str(u.get("verdict"))[:130])

allmap = {a["sym"]: a for a in res.get("all_names", [])}
book = json.load(open(os.path.join(REPO, "watchlists", "open-book.json")))
print("\nBOOK:")
for pos in book.get("positions", []):
    a = allmap.get(pos["sym"], {})
    now = a.get("real_last") or a.get("real_close")
    if now:
        pnl = round((now - pos["entry"]) * pos["shares"])
        print(f"  {pos['sym']}: close {now} | pnl {pnl:+} ({(now/pos['entry']-1)*100:+.1f}%) "
              f"| high_close {pos.get('high_close')} | stop {pos['stop']} | ce_mode {a.get('ce_mode')}")

print("\nWATCH NAMES:")
for s in ("FTRE", "KNSA", "ITRI", "JNJ", "DGX", "URI", "MLI"):
    a = allmap.get(s, {})
    h = hits.get(s, {})
    print(f"  {s}: close {a.get('real_last') or a.get('real_close')} | ce {a.get('ce_mode')} "
          f"| verdict {str(h.get('verdict'))[:34]}")

for d in res.get("data_quality", []):
    print("DQ:", d.get("severity"), "|", str(d.get("finding"))[:110])
