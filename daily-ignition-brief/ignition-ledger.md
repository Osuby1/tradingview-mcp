# 🔥 Ignition Signal Ledger — running tally & scorecard

Running record of every name the Early Ignition system flags (grade A or B), tracked forward so we learn what we should have acted on and what we were right to skip. Companion TradingView watchlist tab: **"Ignition Tracker"**.

**Conventions**
- **Grade A** = Tier-1 quality momentum (real business + durable tailwind — the SanDisk archetype). **Grade B** = Tier-2 speculative (small float / squeeze / hype). **SKIP** = seen and deliberately not flagged/entered — logged too, because misses teach as much as hits.
- **Flag px** = last close on flag day (live TradingView feed when logged locally; web-approx if seeded from a cloud brief — marked ~).
- Performance columns refresh during the local daily scan (live feed only, per data-sourcing standard). Fill +1w/+1m as the calendar allows.
- **Status:** RUNNING (thesis intact) · FADING (rolling over) · KILLED (thesis dead / trigger never confirmed) · WATCH (waiting on trigger) · CLOSED-VERDICT (final lesson written).
- At ~1 month each row gets a **verdict**: ✅ WORKED · ❌ FAILED · 🟡 CHOP · 🎯 CORRECT-SKIP · 😤 MISSED (should have acted).

## Ledger

| Flagged | Ticker | Grade | Flag px | +1w | +1m | Latest (date) | Since flag | Status | Verdict | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-20 | SNDK | A | 1,914.46 (6/24 ref) | — | — | 1,411.08 (7/16) | **−26.3%** | FADING | pending (verdict due ~7/20) | System archetype (~40x from $36). Flagged extended (RVOL 0.6, no fresh fire). NAND-glut narrative won: Kioxia listing, WDC stake sale, SK Hynix US debut sell-through; −12.6% 7/13, −7.8% 7/16 (low 1,390). SMH CE still SHORT (651.30). Trending to 🎯 CORRECT-SKIP — "extended, don't initiate" saved −26%. |
| 2026-06-22 | NVTS | B | 26.00 trigger (never hit) | — | — | 14.46 (7/2) | −44% vs trigger | KILLED | 🎯 CORRECT-SKIP | Breakout alert @26 NEVER fired (last_fired null) → no entry per discipline → avoided −44%. **Lesson: the "wait for the trigger" rule is the edge — do not anticipate breakouts.** |
| 2026-06-24 | MU | A (extended — don't initiate) | 1,048.51 | — | — | 975.56 (7/2) | −7.0% | CLOSED-VERDICT | 🎯 CORRECT-SKIP | Blowout ER (+16% AH to ~1,215) but tagged "extended, manage as momentum, don't initiate." From the AH peak it round-tripped −20%. **Lesson: even a monster beat doesn't fix an extended entry — the 6/24 "hold the gap or fade it?" question resolved FADE.** |
| 2026-06-24 | STX | A (complex read-through) | 993.25 | — | — | 820.16 (7/2) | −17.4% | CLOSED-VERDICT | 🎯 CORRECT-SKIP | Mizuho PT $1,090 on AI-storage crunch; rule applied was "momentum adds on pullbacks, NOT chase-the-gap." Gap faded −17%. Same lesson as MU — sympathy names after a group gap are the worst entries. |
| 2026-07-06 | AXON | SKIP @ 618.88 | 618.88 | 599.80 (7/8) | — | 541.75 (7/16) | **−12.5%** | WATCH | pending (verdict ~8/6) | Deliberate skip at the 620 alert: +51% in 12 sessions, RVOL 0.39 on the cross, RSbeat 0, no fresh EI flag. Broke down −6.3% on 7/8, then fell THROUGH the 560–580 buy-pullback zone without any volume/trigger confirmation (7/16 low 520.68) — the pullback plan correctly never armed. Trending to 🎯 CORRECT-SKIP. |
| 2026-07-01 | HOPE | B+ starter | 13.95 (7/2 entry ref) | 13.45 (7/8) | — | 13.98 (7/16) | +0.2% | WATCH | pending (verdict ~8/1) | EI IGNITE fired 7/1 (+18% >200SMA, ADX 27, RSbeat 1) but at/above analyst PT cluster. Omar round-tripped 700sh 13.95→13.75 (−$140, flat-into-holiday rule). Re-entry alerts NOT re-wired. 7/16 scan: PASS strong (+19.4% >200d, CE 13.12, RVOL 1.37) riding the KRE/regional-bank rotation. **Earnings Tue 7/21 — no full size into print.** |

## Lessons bank (append as verdicts land)

1. **2026-07-04 (from NVTS):** Anticipating a breakout is not a strategy. The 26.00 trigger never fired and the stock fell 44%. Never front-run the trigger — the alert IS the entry permission.
2. **2026-07-04 (from MU/STX):** Post-earnings gap chasing in an extended group fails even when the news is historic (MU's $7B guide-raise still round-tripped). The "adds on pullbacks, not chase" rule for sympathy names is confirmed — both faded double digits within a week.
3. **2026-07-04 (meta):** The 6/24 EOD brief asked the exact right question ("does the complex hold the gap or fade it?") but nothing tracked the answer — that's why this ledger exists. The SMH Chandelier SELL flip on 7/2 was the answer arriving.

## Maintenance protocol (local sessions only — cloud routines can't write to the repo)

1. **Each local session / daily scan:** read the morning brief's Tier-1/Tier-2 tables → append any NEW names as rows (grade, flag px from live feed). Refresh "Latest" + "Since flag" for all non-CLOSED rows from the live feed. Mirror adds/removals to the "Ignition Tracker" TV watchlist.
2. **When a calendar checkpoint passes** (+1w/+1m), fill the column.
3. **At ~1 month or thesis resolution:** write the verdict + move the takeaway into the Lessons bank. CLOSED rows stay in the table (the tally IS the history).
4. **Also log deliberate SKIPs** on big movers we reviewed — a 😤 MISSED verdict is only visible if the skip was recorded.
