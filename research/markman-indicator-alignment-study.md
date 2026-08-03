# Markman trades vs our indicators (2026-08-03)

34 closed archive trades, indicators computed at their entry dates.

| Indicator | Aligned | Contradicting |
|---|---|---|
| O.G Chandelier (HA CE 1/2) | 24: 18W-5L, 75% win, +22% avg | 10: 4W-6L, 40% win, -26% avg |
| HQ Swing v1 (regime+ADX+DI) | 10: 8W-2L, 80% win, +12% | 24: 14W-9L, 58% win, +7% |
| Magical CCI-20 (entering stretched) | not-stretched 21: 52% win, +3% | STRETCHED 13: 85% win, +16% (BACKWARDS) |
| CE + HQ both aligned | 6: 5W-1L, 83% win, med +52% | 28: 61% win, +6% |

Consequences: skip line 6 added (Chandelier contradiction = SKIP);
Magical explicitly excluded (backwards); HQ Swing logged, no veto (too
strict - would remove 24/34 trades for modest lift). Wipeout coverage:
delta<0.45 line catches 8/8 disasters, Chandelier 4/8 (independent).
Caveats: n=34, subgroups 6-13, shadow port ~84% chart fidelity,
multiple-comparison inflation. Full per-trade data in
markman-history-trades.json + this study reproducible from the archive.
