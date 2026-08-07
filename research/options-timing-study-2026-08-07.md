# Squeeze-ticket entry timing — intraday study of the HTZ and SOUN chains (8/6)

Omar's question 2026-08-07: both tickets marked down after purchase — is there a
timing lesson? Data: TradeStation 30-min bars for the OPTION contracts themselves
(discovered today the barcharts endpoint serves option symbols), with implied vol
and delta solved per bar. No estimates — the actual tape we traded into.

## What actually happened, bar by bar

**SOUN Sep $10C — filled 0.28 at ~8:56 AM with stock ~7.70**
- Option opened the day printing 0.34-0.35 in the first minutes (stock opened
  8.045, high 8.19 in the first half hour), then spent the ENTIRE rest of the day
  between 0.17 and 0.23. Our fill caught the opening rush.
- **IV was flat all day: 88-93% every single bar.** There was NO intraday vol
  crush. The 0.28 → 0.17 loss decomposes almost entirely to DELTA: stock faded
  7.70 → 7.06 (−8%) × ~0.20 delta ≈ the whole markdown.
- The "volatility crush" story I gave in the midday brief was wrong for SOUN.
  We simply bought the stock near its morning level and it faded all afternoon.

**HTZ Sep $3C — filled 0.35 at ~2:14 PM with stock ~2.15**
- The option traded **0.07-0.10 ALL MORNING** (stock 1.68-1.80, IV 142-152%).
- The squeeze went vertical 1:00-2:15 PM: stock 1.81 → 2.19, option 0.10 → 0.39,
  **IV spiking to 211% — the peak of the entire day**. The blast alert fired at
  ~1:55, mid-spike, and we filled 19 minutes later, 2 bars from the day high.
- By the close: stock 2.01, option 0.24, IV 185%. Loss decomposition of the
  0.35 → 0.24 markdown: roughly HALF delta (stock −7% × ~0.45Δ), HALF IV
  normalization (211% → 185%). We paid a ~40-IV-point premium over the day's own
  baseline for buying inside the vertical move — and the spike also made it a
  45-delta ticket at peak price when the design calls for ~20-delta lottery.

## The counterfactual table — same thesis, different clock

| Entry window | SOUN C10 | HTZ C3 | vs our fills |
|---|--:|--:|---|
| Our actual fills | 0.28 | 0.35 | — |
| **Ignition-day final hour** | **0.17** | **0.24** | **−39% / −31%** |
| Day-2 open | ~0.19-0.22 | **0.41** | mixed: cheaper / **+17% dearer** |

- The final hour of ignition day beat our fills on BOTH tickets AND beat the
  day-2 open on both (0.17 vs 0.22; 0.24 vs 0.41).
- Day-2 open is NOT the lesson — HTZ gapped 20% and the option opened above our
  fill. Waiting overnight pays only if the squeeze fails, which is not the bet.
- Mechanism, not luck: spike premium (price AND vol) deflates into the close,
  while the overnight gap risk has not yet been taken. AND by the final hour the
  day-1 health verdict — the exact rule we already use for HOLDING (close above
  prior low, upper-half close or heavy volume) — is readable for ENTRY. The
  final-hour buyer pays less and knows more.
- Combined cost of our actual timing: **$220 on $630 deployed (~35%)** — the
  measurable "chase tax" of filling mid-spike / at the open rush.

## Pre-registered rule candidate — SHADOW LANE per the rule freeze (n=2 is a pattern, not proof)

**"Ignition-day tickets fill in the FINAL 60 MINUTES, at a limit no worse than
the prevailing mid, and only if the health check passes at that moment (on
track to close above the prior day's low, with an upper-half close or ≥2x
volume). A blast alert starts the clock — it is never itself the buy signal.
Exception: fill immediately only if the stock is already through the target
strike (chain running away)."**

Grading protocol from the NEXT ticket forward: at every future ticket, record
(a) the price at alert/card time and (b) the final-hour price, whether we fill
early or late. 5+ tickets of both numbers → promote, amend, or kill the rule at
a Friday review. Until then it influences nothing live.

Honest limits: two cases, same week, same regime. A true day-one runner that
closes ON its high makes the final-hour fill MORE expensive — that is the cost
of confirmation, and the study accepts it knowingly. IOVA (today, day-2 entry
at 0.45 after the +43% day HELD) is consistent with the confirmation logic but
was not part of this sample.

Correction on the record: the 8/6 midday brief attributed SOUN's markdown to
"post-event volatility crush." The bars show IV flat at ~90% all day — the
markdown was delta (stock fade). HTZ was genuinely half vol. The invisible-tax
story was half right on one ticket and wrong on the other; this study replaces it.
