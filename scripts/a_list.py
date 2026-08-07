"""A-LIST: the flag-to-fill conversion engine (Omar-approved 2026-08-06).

Nightly, after the scan chain: pick the 1-3 most compelling gate-passers,
wire REAL entry-door alerts at their plan limits (phone rings at the
actionable price), log forced ACT/PASS verdict slots, and write funnel
metrics so Friday reviews grade the conversion pipeline itself.

Leaks this fixes (diagnosed 8/6): firehose without hierarchy, no forced
decision, doors not pre-wired, funnel unmeasured.

DESIGN DECISION 2026-08-06 (Omar, overruling me): NO BOOK AWARENESS. I
proposed filtering cards that conflict with open positions after the first
run surfaced SPXL (3x long S&P) while Omar holds a SPY put hedge. Omar
overruled: "I want to see what is favored when it works." He is right - a
card that contradicts an open position is not noise to suppress, it is the
selector telling you your existing thesis may be wrong. Filtering it would
hide precisely the signal worth having, and would have hidden the exact
rotation Omar wants available (out of the put, into SPXL, on a benign jobs
print). The ONLY book filter that stays is the existing "exclude what you
already own" rule, which prevents duplicate cards, not contradictory ones.
Consequence accepted: cards may argue against the book, and the human
resolves it. Revisit only if the unfiltered version demonstrably misleads.

Usage:
  python scripts/a_list.py              # full run (select + wire doors)
  python scripts/a_list.py --dry-run    # select + print only
Scheduled: Task 'AListNightly' daily 15:50 CT (after the 15:15 chain).
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "watchlists" / "a-list-state.json"
VERDICTS = REPO / "research" / "a-list-verdicts.json"
DOOR_ACTIONS = REPO / "watchlists" / "door-actions.json"
BOOK = REPO / "watchlists" / "open-book.json"

MAX_CARDS = 3
MIN_READY = 55
MIN_DOLLAR_VOL = 20e6


def _resolve_exchange(sym):
    """Return the exchange-qualified ticker, ASKING rather than assuming.

    2026-08-06: the first live A-List run failed to wire SPXL's door because
    this defaulted to "NASDAQ:" for any bare ticker - SPXL is NYSE Arca. Same
    class of bug as the EQR/SFL/FITB traps already in the notes: a guessed
    prefix silently kills the alert, so the door that was supposed to ring
    never exists. The scanner drops bad tickers, so submit all three US
    listings and keep whichever one comes back.
    """
    if ":" in sym:
        return sym
    try:
        import requests
        cands = [f"{ex}:{sym}" for ex in ("NASDAQ", "NYSE", "AMEX")]
        r = requests.post("https://scanner.tradingview.com/america/scan",
                          json={"symbols": {"tickers": cands, "query": {"types": []}},
                                "columns": ["close"]},
                          timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        rows = [e["s"] for e in r.json().get("data", []) if e.get("d", [None])[0]]
        if len(rows) == 1:
            return rows[0]
        if rows:                      # ambiguous - report it, never coin-flip
            print(f"[doors] AMBIGUOUS exchange for {sym}: {rows} - using {rows[0]}")
            return rows[0]
    except Exception as e:
        print(f"[doors] exchange lookup failed for {sym}: {e}")
    return f"NASDAQ:{sym}"            # last resort, logged by the caller on failure


def latest_results():
    files = sorted((REPO / "watchlists").glob("universe-results-*.json"))
    if not files:
        sys.exit("no universe results found")
    return files[-1], json.loads(files[-1].read_text(encoding="utf-8"))


SCANNER_LOG = Path.home() / "Documents" / "Equities_Scanner" / "recommendations_log.csv"
BUY_TABS = {"COILED", "FRESH IGNITION", "BUY ZONE"}
VETO_TAB = "COOLING"


def origination_candidates(date, held):
    """Second feed into the A-List: the origination scanner (Omar 2026-08-06).

    WHY: the selector saw only the Chandelier sweep, while the Winner-DNA third
    cut found the origination COILED tab is the ONLY source with a credible edge
    (+2.72% vs IWM at 21 sessions, CI [+0.66,+5.14], stable across both halves).
    The one source with measured evidence in its favour could not produce a card.

    COOLING VETO: Omar confirmed COOLING means "this already ran, wait for it to
    settle" - a watch state, not a buy list - and it measures -5.52% vs IWM over
    112 flags with the interval excluding zero. Any name sitting in COOLING on
    this date is dropped NO MATTER WHICH TAB ALSO SURFACED IT. That also cleans up
    BUY ZONE, which is 94% contained inside COOLING.

    Ranking currency: readiness, recomputed on the SAME 0-100 scale the sweep
    uses, so the merged pool is ranked like-for-like. Source is recorded on every
    card but does NOT yet alter the ranking - per the rule freeze the detector
    weighting stays in the shadow lane until September grades it.
    """
    if not SCANNER_LOG.exists():
        print(f"[orig] {SCANNER_LOG} not found - sweep-only tonight")
        return []
    try:
        import pandas as pd
        df = pd.read_csv(SCANNER_LOG)
    except Exception as e:
        print(f"[orig] could not read scanner log: {e}")
        return []
    day = df[df["date"].astype(str).str[:10] == date]
    if day.empty:
        print(f"[orig] no scanner rows dated {date} - sweep-only tonight")
        return []

    vetoed = {str(r["ticker"]).strip().upper()
              for _, r in day.iterrows()
              if str(r.get("tab", "")).strip().upper() == VETO_TAB}
    out, seen = [], set()
    for _, r in day.iterrows():
        sym = str(r["ticker"]).strip().upper()
        tab = str(r.get("tab", "")).strip().upper()
        if tab not in BUY_TABS or sym in held or sym in seen:
            continue
        if sym in vetoed:
            print(f"[orig] VETO {sym}: also in COOLING today (watch state)")
            continue
        try:
            entry, stop = float(r["price"]), float(r["stop"])
        except (TypeError, ValueError):
            print(f"[orig] skip {sym}: no usable price/stop"); continue
        if not (entry > 0 and 0 < stop < entry):
            print(f"[orig] skip {sym}: price/stop not sane ({entry}/{stop})"); continue
        seen.add(sym)
        out.append({"sym": sym, "source": f"orig-{tab}",
                    "grade": str(r.get("grade", "")).strip(),
                    "plan_entry": round(entry, 2), "plan_stop": round(stop, 2),
                    # protocol minimum: a plan must offer 2x its risk
                    "plan_target": round(entry + 2 * (entry - stop), 2),
                    "real_close": entry})

    if not out:
        print("[orig] no buy-intent candidates survived the COOLING veto")
        return []

    sys.path.insert(0, str(REPO / "scripts"))
    import options_analysis as _oa
    import yfinance as _yf
    kept = []
    for c in out:
        try:
            c["readiness"] = _oa.readiness(c["sym"], "CALL")
        except Exception as e:
            print(f"[orig] readiness failed for {c['sym']}: {e} - EXCLUDED, not guessed")
            continue
        try:
            h = _yf.Ticker(c["sym"]).history(period="1mo")
            dv = float((h["Close"] * h["Volume"]).tail(20).mean())
        except Exception:
            dv = 0.0
        c["gates"] = {"avg_dollar_vol": dv}
        kept.append(c)
    print(f"[orig] {len(kept)} buy-intent candidates scored "
          f"({len(vetoed)} names vetoed by COOLING)")
    return kept


def main():
    dry = "--dry-run" in sys.argv
    src, res = latest_results()
    date = res.get("date", "?")
    held = {p["sym"] for p in json.loads(BOOK.read_text()).get("positions", [])}

    passers = [h for h in res.get("hits", [])
               if "passes every gate" in str(h.get("verdict", "")).lower()]
    for h in passers:
        h.setdefault("source", "sweep-CE")

    # SECOND FEED (Omar 2026-08-06): the origination scanner ranks into the same
    # pool. Both detectors compete on one readiness scale; COOLING vetoes across
    # every source, including the sweep.
    orig = origination_candidates(date, held)
    cooling_today = set()
    if SCANNER_LOG.exists():
        try:
            import pandas as _pd
            _d = _pd.read_csv(SCANNER_LOG)
            _day = _d[_d["date"].astype(str).str[:10] == date]
            cooling_today = {str(r["ticker"]).strip().upper()
                             for _, r in _day.iterrows()
                             if str(r.get("tab", "")).strip().upper() == VETO_TAB}
        except Exception:
            pass

    pool, vetoed_sweep = passers + orig, []
    eligible = []
    for h in pool:
        r = (h.get("readiness") or {}).get("score") or 0
        dv = (h.get("gates") or {}).get("avg_dollar_vol") or 0
        if h["sym"] in held or r < MIN_READY or dv < MIN_DOLLAR_VOL:
            continue
        if h["sym"] in cooling_today:      # veto applies to sweep names too
            vetoed_sweep.append(h["sym"]); continue
        eligible.append(h)
    if vetoed_sweep:
        print(f"[veto] COOLING blocked {len(vetoed_sweep)} otherwise-eligible "
              f"name(s): {', '.join(sorted(set(vetoed_sweep)))}")
    eligible.sort(key=lambda h: -h["readiness"]["score"])
    cards = eligible[:MAX_CARDS]

    # funnel metrics (stage counts for the Friday review)
    funnel = {
        "date": date, "scanned": res.get("scanned"), "fresh": res.get("fresh_count"),
        "full_passers": len(passers), "eligible": len(eligible),
        "a_list": [h["sym"] for h in cards],
        "doors_wired": 0, "note": f"selector: ready>={MIN_READY}, $vol>={MIN_DOLLAR_VOL/1e6:.0f}M, not-held, top {MAX_CARDS} by readiness",
        # SELECTOR CONTROL GROUP (Omar's challenge 8/6: how do we KNOW the
        # picks are right?): every eligible name is snapshotted with its
        # entry reference so Friday reviews can grade SELECTED vs REJECTED
        # vs random-3 vs a buy-score ordering - the selector must EARN its
        # ranking or be demoted to "any 3 passers with doors".
        "sources_in_pool": {src: sum(1 for h in pool if h.get("source") == src)
                            for src in sorted({h.get("source", "?") for h in pool})},
        "cooling_vetoed": sorted(set(vetoed_sweep)),
        "eligible_cohort": [{"sym": h["sym"], "readiness": h["readiness"]["score"],
                             "source": h.get("source"), "grade": h.get("grade", ""),
                             "ref_price": h.get("real_close"), "selected": h in cards}
                            for h in eligible],
        "passers_below_floor": [{"sym": h["sym"],
                                 "readiness": (h.get("readiness") or {}).get("score")}
                                for h in passers if h not in eligible and h["sym"] not in held],
    }

    state = {"date": "", "doors": {}}
    if STATE.exists():
        state = json.loads(STATE.read_text())

    actions = []
    # drop doors for names no longer on the list (or now held)
    keep = {h["sym"] for h in cards}
    for sym, door in list(state.get("doors", {}).items()):
        if sym not in keep:
            actions.append({"op": "delete", "alert_id": door["alert_id"], "sym": sym})
            del state["doors"][sym]
    # wire doors for new cards
    for h in cards:
        sym = h["sym"]
        if sym in state["doors"]:
            continue  # door already live from a prior night
        entry, stop, target = h["plan_entry"], h["plan_stop"], h["plan_target"]
        risk_sh = int(5000 / max(entry - stop, 0.01))
        notional = min(100000, risk_sh * entry)
        shares = int(notional / entry)
        msg = (f"A-LIST DOOR: {sym.split(':')[-1]} at plan entry {entry} "
               f"(readiness {h['readiness']['score']}). Plan: ~{shares}sh, stop {round(stop,2)} "
               f"(${int((entry-stop)*shares)} risk), checkpoint {round(target,2)}. "
               f"VERIFY earnings + gate-recheck + sizing per protocol, then ACT or PASS - "
               f"verdict gets logged either way.")
        exch_sym = h.get("full_sym") or _resolve_exchange(sym)
        actions.append({"op": "create", "sym": exch_sym, "level": entry, "msg": msg, "tag": sym})
    # audit fire-state of surviving doors (conversion tracking)
    for sym, door in state.get("doors", {}).items():
        actions.append({"op": "audit", "alert_id": door["alert_id"], "sym": sym})

    # forced-verdict slots
    verdicts = []
    if VERDICTS.exists():
        verdicts = json.loads(VERDICTS.read_text())
    existing = {(v["date"], v["sym"]) for v in verdicts}
    for h in cards:
        if (date, h["sym"]) not in existing:
            verdicts.append({"date": date, "sym": h["sym"],
                             "source": h.get("source"), "grade": h.get("grade", ""),
                             "readiness": h["readiness"]["score"],
                             "plan_entry": h["plan_entry"], "plan_stop": h["plan_stop"],
                             "verdict": "PENDING", "reason": "",
                             "grade_at": "+1w and +1m vs plan entry"})

    # STRUCTURE TAG (added 8/6 after the BA-vs-GE post-mortem: BA was called
    # "the GE profile" when GE's defining trait - band width in the 2nd
    # percentile - was absent from BA entirely. A card may never be described
    # as a coil without the compression to prove it.)
    import re as _re
    def structure(h):
        """COILED / POST-BREAKOUT / NEITHER from the MEASURED band-width percentile.

        2026-08-06 bug, found the same night this tag shipped: v1 parsed the
        readiness DRIVER STRING for a band-width mention. The driver only names
        the top two scoring components, so a name whose compression scored 15/20
        but placed third got stamped "POST-BREAKOUT (no compression component)" -
        factually false. RYTM was tagged post-breakout while sitting at the 11th
        percentile with the squeeze ON, i.e. a textbook coil. A tag built to stop
        me calling things coils without the number was itself guessing at the
        number. Now it MEASURES, and says so honestly when it cannot.
        """
        sym = h["sym"]
        try:
            sys.path.insert(0, str(REPO / "scripts"))
            import options_analysis as _oa
            r = _oa.readiness(sym, "CALL")
            p = r.get("squeeze_pctile")
            on = r.get("squeeze_on")
            if p is not None:
                if p <= 25:
                    return (f"COILED (band width {p}th pctile"
                            f"{' + TTM squeeze ON' if on else ''} - GE-type compression)")
                if p >= 60:
                    return f"POST-BREAKOUT (band width {p}th pctile - expansion already underway)"
                return f"NEITHER (band width {p}th pctile - middling)"
        except Exception as e:
            print(f"[structure] MEASUREMENT FAILED for {sym}: {e}")
        return "UNKNOWN (band width could not be measured - do NOT call this a coil)"

    print(f"A-LIST {date} | pool {len(pool)} from "
          + ", ".join(f"{k}:{v}" for k, v in funnel["sources_in_pool"].items()))
    print("  cards: " + (", ".join(f"{h['sym']}(r{h['readiness']['score']},{h.get('source','?')})"
                                   for h in cards) or "EMPTY - no eligible candidates"))
    for h in cards:
        print(f"  {h['sym']:<6} [{h.get('source','?')}{('/'+h['grade']) if h.get('grade') else ''}] "
              f"entry {h['plan_entry']} stop {round(h['plan_stop'],2)} "
              f"target {round(h['plan_target'],2)} | STRUCTURE: {structure(h)}")
        _drv = str(h["readiness"].get("driver") or
                   "; ".join(h["readiness"].get("notes") or []))
        print(f"         driver: {_drv[:110]}")
        if h.get("source", "").startswith("orig-") and h.get("real_close") and                 abs(h["plan_entry"] - h["real_close"]) < 0.005 * h["real_close"]:
            print("         NOTE: scanner level = today's close, so this door is "
                  "AT MARKET, not a pullback limit - it will ring immediately.")
    funnel["structure_tags"] = {h["sym"]: structure(h) for h in cards}
    if dry:
        print(f"[dry-run] would wire {sum(1 for a in actions if a['op']=='create')} door(s), "
              f"delete {sum(1 for a in actions if a['op']=='delete')}")
        return 0

    VERDICTS.write_text(json.dumps(verdicts, indent=1))
    if actions:
        DOOR_ACTIONS.write_text(json.dumps(actions, indent=1))
        rc = subprocess.run(["node", str(REPO / "scripts" / "wire_door_alerts.mjs")],
                            capture_output=True, text=True, timeout=180)
        print(rc.stdout.strip())
        if rc.returncode != 0:
            print("DOOR WIRING PARTIAL/FAILED:", rc.stderr.strip()[:300])
        # 2026-08-06: record whatever ACTUALLY got created, pass or fail. The
        # first live run wired RYTM and HSIC, failed on SPXL, took the failure
        # branch and saved NO state - so the re-run created duplicate alerts at
        # the same levels on the same names (deleted by hand). One bad door must
        # never erase the memory of the good ones.
        results = json.loads(DOOR_ACTIONS.read_text()) if DOOR_ACTIONS.exists() else []
        for r in results:
            if r.get("op") == "create" and r.get("alert_id"):
                state["doors"][r["tag"]] = {"alert_id": r["alert_id"], "level": r["level"],
                                            "wired": date}
                funnel["doors_wired"] += 1
            if r.get("op") == "audit" and r.get("fired"):
                state["doors"].get(r["sym"], {})["fired"] = r["fired"]
    state["date"] = date
    STATE.write_text(json.dumps(state, indent=1))
    (REPO / "reports" / f"funnel-{date}.json").write_text(json.dumps(funnel, indent=1))
    print(f"funnel: {funnel['fresh']} fresh -> {funnel['full_passers']} passers -> "
          f"{len(cards)} A-list -> {funnel['doors_wired']} new doors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
