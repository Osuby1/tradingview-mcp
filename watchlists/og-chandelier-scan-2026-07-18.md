# O.G Chandelier scan — Saturday 2026-07-18 catch-up run (FAST variant)

**What this is:** the autonomous EOD chain missed its Friday run (the chain was only registered today), so per the weekend rule this is a **catch-up run on the latest settled data = Friday 7/17 closes**, using the **fast convergence variant**. No new bars have printed since Friday's close.

**Bottom line: zero new fresh buys.** The tradeable set is unchanged from Friday's full scan — the six plans in `research/plans-2026-07-20.md` (with the Saturday regime downgrades) stand as written, alerts already wired. Machine-readable results: `universe-results-2026-07-18.json` → compiled to `reports/universe_2026-07-18.xlsx`.

## What was scanned vs reused
- **Chart-scanned live today (32 names)** — origination-tab names (fresh 7/18 tab basis) never before read on this data, on the O.G Chandelier layout (id 91698392, stack verified: CE 1/2 + ZLSMA(50) + Magical ±100, daily):
  - Buy Zone (8): CLYM HELE TVTX ATEN OSCR BRKR ASTH TBLA
  - Fresh Ignitions (4): SION TFIN ESQ DX
  - Coiled → convergence filter (20): radar 7/17 has XBI/IBB/XLV on WATCH + KWEB IGNITING, so Coiled was filtered to its biotech/healthcare names: DNTH GKOS CGON MIRM NUVL COGT AMLX SEPN BIOA SRRK SNDX KURA PRAX PCVX PTCT BCAX VRTX MRK IRMD MLAB. (Coiled holds no China-internet names; the other ~130 Coiled names sit in NEUTRAL/ROLLING sectors and were skipped by design — that's the fast variant.)
- **Reused on identical settled data (disclosed):** the 250-name watchlist sweep from `og-chandelier-scan-2026-07-17.md` (run Friday post-close on these same closes — re-scanning would reproduce it bar-for-bar) and this morning's smoke-test reads (FNB, COCO, NWPX, EXTR, VISN, GTX, NVST). Fast-variant "watchlists fresh check" is therefore satisfied by the Friday sweep.

## Scan results (the 32 live reads)
- **Fresh buys (≤5 sessions): NONE.**
- **Long but stale (21):** every Buy-Zone name in long mode signaled mid-May→early-July and is now pulling back into its zone — which is exactly what that tab screens for; the O.G overlay just confirms none is a fresh entry. Notables: TVTX/ATEN/BRKR months-old signals far above stops; SEPN Magical −160 (washout, watch for a turn); COGT/PCVX/PRAX/BCAX/SNDX/CGON/AMLX/DNTH = the biotech-coil cluster, all long-stale, none fresh.
- **Chasing-hot flags:** SION +160, ESQ +158, DX +174 Magical — Fresh Ignitions tab names already extended; no entries.
- **Sell mode (15 new to the roster):** OSCR MIRM BIOA SRRK KURA PTCT VRTX MRK IRMD MLAB (today) + EXTR VISN NWPX GTX NVST (smoke test, same data). Combined veto roster now 152 names in the JSON.
- **FNB (Fresh Ignitions):** the smoke test's one hit — fresh buy ~7/15 but **ZLSMA gate FAIL** (18.99 < 19.71) and a high-volume post-earnings fade despite a beat → **watch**, reassess on a reclaim of ~19.7.

## Carried plan set (from Friday's full scan — unchanged)
Priority: **1-NUE** (only full regime pass, half $45k), **2-XPO** (half $43k, no-chase), **3-COST starter $50k**, **4-AMT starter $30k**; **CEG/PFE = watch**. Blocked: HAS GS CVNA BHP TLN LCID SHAK (+SPXL borderline, +COCO near-miss). Combined risk if all actives fill ≈ **$8.9k** — under the $10k weekly flag. Fri closes re-verified on the feed today: NUE 234.35 / XPO 216.50 / COST 950.12 / AMT 170.90 / CEG 249.75 / PFE 25.27 — all sitting 1.4–3.9% ABOVE their pullback limits, so nothing chases at Monday's open by construction.

## Blockers & caveats logged (autonomous run — nothing waited on input)
1. **NUVL unresolvable** on NASDAQ/NYSE (bare symbol resolves only to a CFD) — possibly delisted/acquired. Omar: confirm and clean it from the scanner universe.
2. **TV feed dropped ~5 min** mid-scan (chunk 2) and stalled briefly during quote pulls — self-recovered both times; chunk restarted from its first symbol; no gaps.
3. **The O.G layout is a Heikin-Ashi chart** — "last" prices are HA composite closes from Omar's own layout (COST/PFE cross-check plan prices exactly; treat sub-1% distances as approximate).
4. `quote_get` serves stale prior-symbol data after a symbol switch with the market closed — worked around via `data_get_ohlcv` + readiness retries.
5. `pine/~$ctor_rotation_detector.pine` is an Office temp lock file — deliberately left uncommitted.
