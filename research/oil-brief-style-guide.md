# Oil Morning Brief — style guide (built from Omar's broker specimens)
Specimens analyzed: 2026-07-30 (crisis day: CENTCOM/CPC), 2026-06-17
(data/analysis day: EIA Wed, post-deal repricing), 2026-07-29 (escalation
day: US/Saudi strikes + Iran rejects Oman proposal), 2026-07-13
(acute-crisis day: Hormuz traffic collapse, Qatar maritime suspension).
The daily writer READS THIS FILE before composing and follows it.

## Skeleton (all specimens)
1. Headline: two-to-four clauses chained with semicolons, price level +
   top stories. Acute/data days may prefix "Morning Highlights:"; big
   escalation days use a bare declarative headline ("Brent Jumps 5% to
   $88.00 as ..."). Either way the headline alone must tell the day.
2. "<Weekday>, <date> | 5:45 AM CT" (specimens ran 6:30-6:45 ET; ours
   keeps its own dateline).
3. Price line: "Brent (<month>) $X | WTI (<month>) $Y" with contract
   months ALWAYS labeled; expiry flagged when near ("expires Friday");
   day change in $ AND % for both benchmarks in the same breath.
3b. TERM STRUCTURE STRIP (mandatory, Omar's standing order 2026-08-05):
   directly under the price line, both benchmarks' first three calendar
   spreads - WTI M1-M2, M2-M3, M3-M4 and Brent M1-M2, M2-M3, M3-M4 - in
   $/bbl with month labels (e.g., "WTI Sep-Oct +$1.05, Oct-Nov +$0.70,
   Nov-Dec +$0.45"). Positive = backwardation (prompt tightness),
   negative = contango (glut/storage economics). Flag the day-over-day
   CHANGE in the front spread whenever sourced - the flip or steepening
   is the story, not the level alone.
   SOURCING (Omar's method, taught 8/6 after the first brief wrongly
   claimed spreads were 'blocked'): spreads are COMPUTED, never quoted -
   pull individual contract outrights and subtract adjacent months
   (CL1!-CL2! / CLU-CLV for WTI; BZ or BRN legs for Brent). The desk
   publishes them pre-computed in research/crude-curve-latest.json
   (real-time TradeStation legs, liveness-guarded); the writer READS
   that file and labels its as-of time. A strip is NEVER 'unavailable' -
   the legs are always quotable one contract at a time.
4. THE SIGNATURE: one dense digest paragraph - day changes with %,
   session ranges/context ("steadying after two ~5% declines"), API/EIA
   numbers VS EXPECTATIONS, then semicolon-chained top stories.
   Everything in one breath. On data-pending days it ENDS with what's
   due ("EIA figures are due later today"). This paragraph IS the
   product for a skimming reader.

## Analytical hierarchy (the house's actual edge - replicate)
- PHYSICAL SIGNALS OUTRANK HEADLINES: term structure and differentials
  are "the most important signal" tier (Dubai contango flip, WTI
  Midland-Houston basis, Oman/Murban differentials, floating storage,
  OSPs). Flows/arbitrage (VLCC fixtures, tender premiums, vessel counts)
  are used as CONFIRMATION of the structure story, never standalone
  trivia.
- HEADLINE TRIAGE (7/29): when two big stories compete, explicitly rank
  them and lead with the more consequential one even if it's the quieter
  one - "Iran rejecting the Oman proposal is the more consequential
  headline today, even though the strikes will get the attention." Say
  WHY it outranks (it killed the only concrete diplomatic mechanism).
- REVEALED PREFERENCE BEATS STATEMENTS (7/29, 7/13): what buyers PAY is
  more reliable than what governments SAY - "buyers are paying up for
  cargoes that can actually move, which is a more reliable signal than
  either government's public statements." State official-claim-vs-data
  contradictions bluntly: "Trump said Sunday the strait remains open to
  commercial traffic, though the data shows otherwise."
- MECHANISM TRACING: "the mechanism is straightforward:" - every big
  claim gets its causal chain spelled out, including downstream
  consequences. Include SECOND-ORDER mechanisms (7/13: not just outbound
  loaded tankers - INBOUND EMPTY tankers, because without vessels
  entering the Gulf to load, restarted production can't be sustained).
- THE ONE-NUMBER ARC (7/13): when one number captures a whole cycle,
  build a paragraph on it (Murban OSP $101.48 -> $80.01 in one month =
  the full scarcity-to-glut-to-repricing arc). Then explain the LAG:
  why the physical market can't reprice instantly (Asian refiners
  already covered through August).
- RUNNING TALLIES (7/29): carry cumulative counters day over day -
  "seventh tender since June... total sales past 86 million barrels",
  vessel counts by corridor with AIS/dark-mode status, "highest weekly
  pace since July 19". Superlatives always dated: "first blanket
  maritime suspension by any Gulf state since the conflict began",
  "sharper deterioration than anything seen since the MOU was signed".
- TIME-HORIZON TAGGING (7/29, 7/13): label each driver's clock. Fast =
  strikes/traffic. Medium = "a slower-moving but important layer"
  (OPEC+ policy). Slow = structural, tagged explicitly - "that is a
  2027-2028 story, not today's" (pipeline bypass build-out). Products
  tightness framed as a LAYER "on top of whatever the crude side does".
- DATA-VS-NARRATIVE DIVERGENCE (7/29): when two datasets tell opposite
  stories (Bab el-Mandeb traffic up vs Hormuz scant), name the
  divergence as "a defining feature of this market" and mine it.
- THE UNDERPRICED RISK: each edition names the risk "the market is not
  fully pricing yet" (6/17: Israel-in-Lebanon as deal-breaker variable).
- NEXT CONCRETE MILESTONE + the variable that could destabilize it
  (6/17: "MOU signing Friday... but Israeli behavior is the variable").
- ANALYST SCENARIO BANDS (7/29): quote named-analyst price paths with
  floor/ceiling logic - DBS's Sarkar: Brent whipsaws $80-100 as conflict
  ebbs and flows, stop-start negotiation cycles mean no clean
  resolution, floor near $80 even in de-escalation.
- FACT VS CHARACTERIZATION: attributions handled explicitly (7/30: CPC's
  "terrorist attack" labeled as CPC's own characterization).

## Day-type templates
- CRISIS DAY (7/30 model): lead = the incident deserving most scrutiny,
  with sourcing caveats; analyst risk-premium framing (KCM Trade); a
  "small but genuine" counter-datapoint (the Qatari LNG transit).
- ESCALATION DAY (7/29 model - strikes/rejections on top of an existing
  crisis): lead = headline triage (which story actually matters and
  why); analyst scenario band with floor logic; the data-vs-narrative
  divergence block with tender/premium evidence; then the slower policy
  layer (OPEC+); then the products layer (diesel ban) as a second
  tightness source.
- ACUTE-CRISIS DAY (7/13 model - physical flows breaking down): lead =
  raw traffic data, corridor by corridor, with vessel counts and
  AIS/dark-mode status; the second-order production risk (inbound
  tankers); the one-number arc (OSP); close with the long-term
  structural frame, explicitly time-tagged as not today's story.
- DATA/ANALYSIS DAY (6/17 model): lead = price-action interpretation
  ("the price action over three sessions tells the story"), then the
  agency-forecast anchor (IEA first-look), then the physical signal,
  then flows-as-confirmation, then the underpriced risk.
- EIA WEDNESDAYS: API recap with number-vs-consensus in the digest AND a
  titled block; "EIA data due today" always flagged.

## Mandatory inventory block — SPR & CUSHING (Omar's standing order 2026-08-05)
Every edition carries a titled "SPR & Cushing" block (inside or beside
the fundamentals section) with data AND implications, never levels alone:
- CUSHING: latest EIA weekly stock level (million barrels) + week change
  + vs the 5-year range, and the operational context - Cushing is the
  WTI delivery point; sub-~20mb approaches tank bottoms (WTI prompt
  spreads blow out, cash basis strengthens, backwardation steepens),
  builds toward capacity (~78mb shell) do the reverse. Tie the read to
  the WTI spread strip in the skeleton - they must tell the same story,
  and if they diverge, SAY SO (that divergence is signal).
- SPR: current level (million barrels) + week change, any announced
  refill purchases/solicitations, exchanges, or releases with volumes
  and delivery windows, and what it implies - refill bids = a soft floor
  under prompt WTI; releases = temporary supply relief that later
  reverses; a paused program = the floor is gone. Note days of import
  cover or historical context when the level is at multi-decade extremes.
- On API-Tuesday/EIA-Wednesday, run the Cushing number vs expectations
  like the headline crude number. On quiet days one tight paragraph is
  fine, but the block NEVER disappears.

## Fundamental dashboard layer (Omar's standing order 2026-08-05)
Omar maintains a quantitative fair-value model (Crude_Fundamental_
Dashboard workbook, refreshed weekly). Its latest committed baseline
lives at research/crude-dashboard-snapshot.md - READ IT every morning
and carry a titled "DASHBOARD CHECK" block in the brief:
- FAIR-VALUE GAP: the model's WTI M1-M2, Brent M1-M2 and WTI-Brent
  fair values vs where the market trades THIS morning (use the day's
  term-structure strip). State the mispricing direction in plain terms
  ("the model says the WTI front spread is trading far below fair value
  - structurally cheap") and whether today's move widened or closed the
  gap. Thresholds: WTI M1-M2 ±$0.25, Brent M1-M2 ±$0.30, WTI-Brent
  ±$0.50 - inside the band = no edge, say so.
- DRIVER REFRESH: re-source what's fresh daily and compare to the
  model's driver set - Cushing level/z-context and capacity %, OECD/
  hub inventories (ARA, Singapore, Fujairah when quoted), floating
  storage with the IRAN OVERHANG called out specifically, OPEC+ spare
  capacity estimates, USGC/NWE 3-2-1 and Singapore gasoil-Dubai cracks,
  Brent-Dubai EFS when quoted, refiner-margin procurement logic (fat
  cracks = sour grades get bid - name the grades).
- OSP WATCH: around Aramco OSP announcements (~5th of month), compare
  actual vs the model's predicted direction; ADNOC Murban OSP same
  treatment. An OSP surprise vs model = Aramco choosing share vs price
  - say which.
- STALENESS DISCIPLINE: the snapshot carries its as-of date. Label
  model numbers with that date and today's sourced numbers as fresh -
  never present week-old model inputs as today's market. If fresh data
  contradicts a model signal, the FRESH data wins the narrative and the
  divergence gets named.
- SOURCE-TIER DISCIPLINE (from the dashboard's triangulation engine):
  satellite/AIS trackers (Kpler, Vortexa, Kayrros) outrank official
  aggregations (IEA/EIA/PPAC), which outrank surveys (teapot polls,
  OPEC secondary sources), which outrank China NBS official prints
  (cross-check only). When tiers disagree materially, flag the data
  point as low-confidence rather than picking a side silently.

## Structure after the essay paragraphs (all specimens)
"Top Developments" = 3-5 titled blocks, each title a full mini-headline
with numbers ("Bab el-Mandeb Traffic Hits Highest Level Since Mid-July
as ADNOC Sells 12 Million Barrels at Premium"), each block 3-6 sentences
that can stand alone - a reader who only reads the blocks gets the day.

## Source rolodex (grow it)
Wires: Reuters, Bloomberg, CNBC. Agencies: IEA/EIA/API/OPEC. Analytics:
Kpler (flows - Naveen Das), Energy Aspects (balances), Sparta Commodities
(arb/freight - James Noel-Beswick), KCM Trade (macro framing - Tim
Waterer), Windward (maritime intelligence - dark-mode/AIS calls). Banks:
UBS (Giovanni Staunovo - the house's most-quoted; flows + production
risk), DBS (Suvro Sarkar - scenario bands), ING (de-escalation
skepticism), ANZ (shipping caution). Companies: ADNOC (tenders + OSPs),
Reliance/Jamnagar, Dynacom, CPC statements, TotalEnergies/Exxon
fixtures. State media handled as state media (Fars).

## Phrasing conventions
Volumes in bpd / million barrels with comparisons ("nearly double the
4.6mb expectation", "lowest since 2014", "first since January", "highest
in ten months"); freight in $/ton with route economics; timelines
concrete ("weeks to months, citing mine clearance"); tender premiums as
"$3 to $4 over Dubai quotes". No filler adjectives - the drama comes
from the numbers.

## Historical anchors (from specimens, for continuity)
War began ~Feb 28 2026 (Brent 71->77). Crisis peak: March, Dubai premiums
>$60, Brent >$109 intraday June. June 14 (Sun): deal announced, Brent -10%
in 3 sessions to ~79. June 19 (Fri): MOU signed in Switzerland. July 7-8:
ceasefire "over", oil resurged. July 13 (Mon): Hormuz collapsed to six
dark-mode vessels, Qatar issued first blanket Gulf maritime suspension of
the conflict, IRGC hit US bases in Kuwait/Bahrain, ADNOC cut Aug Murban
OSP to $80.01 from $101.48 (Brent ~78). Mid-July: Houthis announced Red
Sea blockade ~July 19; Bab el-Mandeb became the working counter-corridor.
July 29 (Wed): US/Saudi struck Iran-backed groups in Iraq, Iran rejected
Oman's Hormuz proposal (Brent +4.5% to ~86); ADNOC tender sales since
June passed 86mb at premiums; OPEC+ track = +188k bpd for September then
hold through year-end pending capacity audit (~2mbpd cuts still in
place); Russia diesel ban extended (loadings ~234k bpd early July vs
400k June). July 30: Sep Brent $91, backwardated ~$3+ over Oct. Aug 3-5:
Hormuz corridor talks, WTI briefly <75. Structural frames: IEA 2027
first-look +8mbpd supply vs +2mbpd demand = surplus thesis; Mideast
pipeline build-out = 3.8mbpd bypass by end-2027, 7.3mbpd by end-2028
(>60% of pre-war Gulf exports insulated) = downward pressure on
long-dated security premium, a 2027-28 story.

## Delivery format — LARGE BOLD TYPE (Omar's standing order 2026-08-05)
The emailed brief must be easy to read on a phone. Compose the Gmail
draft body as HTML, not plain text:
- Everything bold: wrap the whole body so ALL text renders bold
  (font-weight:700).
- Large type: body text ~18px; section titles (Top Developments, What
  I'm Watching, Trends Watch, each development title) ~20px; the
  headline ~24px.
- Simple inline-styled divs/paragraphs only (Gmail-safe); no external
  CSS, no images required.
- The plain-text skeleton/order above is unchanged - this is purely how
  it renders.
