# Pre-registration: does stock picking beat just buying the sector?

Registered 2026-07-25 **before writing any code**, at Omar's instruction not to
force-fit the data.

## The question

When our scan fires a gate-passing BUY on a stock, would you have done better
just buying that stock's **sector ETF** on the same day and holding it the same
length of time?

This isolates **selection**. It does not test entries, exits, or timing.

## What is fixed now

### Sectors and their benchmarks
Twelve sectors, each with one benchmark ETF, chosen now and not changeable:

| Sector | ETF |
|---|---|
| Semiconductors | SOXX |
| Energy | XLE |
| Financials | XLF |
| Healthcare | XLV |
| Biotech | XBI |
| Industrials | XLI |
| Software | IGV |
| Consumer discretionary | XLY |
| Materials | XLB |
| Utilities | XLU |
| Homebuilders | ITB |
| Retail | XRT |

### Constituents
A fixed basket of large/mid-cap members per sector, written into the script and
printed in full in the results. Chosen **before any return was computed**.

### Period
**2021-01-01 → 2025-12-31**, five full calendar years, reported year by year.
This deliberately includes **2022**, a bear market — the system has never been
tested in one, and excluding it would be the single easiest way to fake a good
answer.

### Method
- Entries: the **live gate stack, unchanged and imported**, on fresh Chandelier
  BUY signals. No parameter is touched.
- **Pure hold, no exit rule.** Exits are already known to destroy value; leaving
  them in would measure the exit, not the selection.
- Horizons: **21, 60 and 120 trading days.** All three reported. **60 days is the
  primary** — declared now so the horizon cannot be picked after the fact.
- Every stock signal is compared with its own sector ETF **over the identical
  calendar window**, bought at the same close.
- Fills at real closes throughout.

## The measures

1. **Mean excess return per signal** (stock minus its sector ETF, same window).
2. **Hit rate** — the share of signals that beat their sector ETF. 50% is the
   coin-flip line.

## Pre-committed conclusions

| Result at 60 days | Conclusion |
|---|---|
| Mean excess **≥ +2pt and hit rate > 55%** | Stock picking adds real value. Keep it. |
| Mean excess **between −2 and +2pt**, hit rate 45–55% | Selection adds nothing. The sector is doing the work — buy the ETF instead and save the single-name risk. |
| Mean excess **≤ −2pt or hit rate < 45%** | Stock picking is actively worse than the ETF. Stop picking stocks inside a sector we already know is moving. |

## Anti-force-fit rules

1. **Every sector and every year gets reported**, including the ugly ones. No
   sector dropped, no year excluded, no "outliers" removed — whatever the totals
   look like.
2. **No parameter is tuned.** No sweeps, no thresholds chosen to improve the
   answer. One run of a fixed rule.
3. **The horizon is pre-declared** (60 days). 21 and 120 are shown for context
   and may not be promoted to headline if they look better.
4. **The sector list is frozen above.** No swapping a benchmark after seeing a
   result.
5. If the code has a genuine bug it will be fixed and re-run, and the fact of the
   re-run plus the pre-fix numbers will be stated in the results.

## Which way the biases run — stated in advance

- **Survivorship favours the STOCKS.** The constituent baskets contain companies
  that still exist and are still liquid today; the ones that blew up are absent.
  The ETF return is real and includes its own losers and turnover.
- **The universe is chosen by me, now, with knowledge of which names are
  well-known.** That also favours the stock side.
- **No trading costs.** Picking stocks means many more transactions than buying
  one ETF, so this too favours the stock side.

**All three biases favour stock picking.** So a result showing stock picking
losing is conservative and hard to argue with. A result showing it winning should
be discounted.

## What this cannot answer

Whether the *sector choice itself* is any good — that is the rotation radar's
job and is still ungraded. This test asks only: given that we are looking at a
sector, is picking names inside it better than owning the whole thing.
