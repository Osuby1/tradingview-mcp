"""One-off: fold the 2026-07-23 BHP/EQR re-reads into the raw HA sweep.

Bare "BHP" and "EQR" both resolved to their ASX listings (BHP Group Ltd and
EQ Resources Limited, priced in AUD, last bar 2026-07-22) instead of the US
lines. This is the documented symbol-resolution trap; the sweep's identity
guard cannot catch it because the ticker genuinely matches - it is the wrong
EXCHANGE, not the wrong ticker.

Replaces those two rows with NYSE:BHP / NYSE:EQR reads (USD, 2026-07-23),
keeping the original requested key so downstream joins still work, and records
what was swapped.
"""
import json

RAW = "watchlists/og-sweep-raw-2026-07-23-heikinashi.json"
FIX = "watchlists/_fixups-2026-07-23.json"

rows = json.load(open(RAW, encoding="utf-8"))
fixes = {r["req"].split(":")[-1]: r for r in json.load(open(FIX, encoding="utf-8"))}

out, swapped = [], []
for r in rows:
    key = r["req"].split(":")[-1]
    if key in fixes:
        bad = r
        new = dict(fixes[key])
        new["req"] = r["req"]                      # keep universe join key
        new["resolution_fixup"] = {
            "from": bad.get("rfull"), "from_desc": bad.get("rdesc"),
            "from_ccy": bad.get("rccy"), "from_last": bad.get("last"),
            "from_bar": bad.get("bar_date"),
            "to": new.get("rfull"), "requested_as": fixes[key]["req"],
            "reason": "bare ticker resolved to a foreign listing in %s"
                      % bad.get("rccy"),
        }
        out.append(new)
        swapped.append("%s: %s (%s %s, bar %s) -> %s (%s %s, bar %s)" % (
            key, bad.get("rfull"), bad.get("rccy"), bad.get("last"), bad.get("bar_date"),
            new.get("rfull"), new.get("rccy"), new.get("last"), new.get("bar_date")))
    else:
        out.append(r)

assert len(out) == len(rows), "row count changed"
assert len(swapped) == len(fixes), "not every fixup landed"
json.dump(out, open(RAW, "w", encoding="utf-8"), indent=1)
for s in swapped:
    print("SWAPPED", s)
print("rows=%d ok=%d" % (len(out), sum(1 for r in out if r.get("ok"))))
