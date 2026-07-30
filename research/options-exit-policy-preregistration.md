# Options Overlay — Exit-Policy A/B Test + Kill Criteria (PRE-REGISTERED)

Registered 2026-07-29 (git-timestamped), BEFORE any closed trades exist.
Per the anti-sycophancy/validation mandate: the questions, the policies, and
the failure conditions are fixed now so results can't quietly bend them later.

## Question 1 — do symmetric exits amputate the right tail?

Long-options profitability usually lives in a few big winners. Our launch rule
(Policy A) sells the whole position at +100%. That may cap exactly the tail
that pays for everything else. Folklore says "let winners run" — folklore is
not evidence, so both policies run in parallel on the SAME paper trades:

**Policy A (launch rule, the one the live ledger executes):**
sell 100% at +100% premium; stop at −50%; time exit at ~21 days to expiry;
thesis break (Chandelier flip on the underlying) exits immediately.

**Policy B (shadow, computed from the daily mark history):**
at +100%, bank HALF the contracts (round down; a 1-contract position banks
nothing and switches to trailing); the remainder trails a stop at 65% of the
highest daily-mark premium since entry; stop/time/thesis exits unchanged.

Mechanics: every open trade's EOD mark is appended to its `mark_history`
array in research/options-paper-ledger.json. Policy B outcomes are computed
retrospectively from those marks — same entries, same data, zero hindsight.

**Verdict rule:** after 30 closed trades, whichever policy shows higher
per-trade expectancy (win% × avg win − loss% × avg loss) becomes the rule.
If they're within $100/trade of each other, Policy A stays (simpler).

## Question 2 — when does the whole overlay admit failure?

**Kill criterion (expectancy):** after 30 closed trades (voided picks
excluded), if Policy A expectancy per trade is NEGATIVE, the overlay STOPS.
No new picks until a redesign is itself pre-registered. Tinkering after
losses without a written plan is how options accounts die.

**Drawdown breaker (any time):** if total paper P&L (banked + open marks)
drops below **−$12,500** (five max-size losses), the overlay pauses
immediately and gets a red-team review before any new pick.

**No goalpost moves:** these numbers change only by editing this file in a
commit that explains why — never retroactively.

## Also fixed at registration
- Concentration cap: max 2 open positions expressing the same theme
  (each trade carries a `theme` tag; the EOD picker enforces it).
- Regime gate: REPAIR blocks new calls unless PRIME SETUP; DEEP-FAIL blocks
  new calls entirely. Backed by the HQ Swing finding that the regime filter
  was the edge.
- Macro blackout: no new entries when the fill day sits on/next to a Fed
  decision, CPI, or jobs report (research/macro-calendar-2026H2.json + first-
  Friday rule).
