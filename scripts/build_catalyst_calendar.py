#!/usr/bin/env python3
"""Build the ALL-SECTOR catalyst calendar -> research/catalyst-calendar.json.

Two free layers (scope: research/catalyst-feed-scope.md):
  A. EARNINGS (all sectors) - TV scanner earnings_release_next_date, names reporting within
     EARN_DAYS. The universal catalyst; carries the PEAD/SUE edge.
  B. BIOPHARMA BINARY - ClinicalTrials.gov v2 Phase 2/3 INDUSTRY readouts (primary completion
     in the next ~9 months), sponsor mapped to ticker via SEC company_tickers.json.

Each record: {ticker, company, sector, event_type, date_or_window, detail, metric, source, view}
where 'view' ALWAYS ends with a suggested action (earnings = SUE/PEAD lens + trim-into-print;
biopharma = BINARY defined-risk). Consumed by compile_universe_report_v2.py (Catalyst columns).
"""
import json, os, sys, datetime, urllib.request, urllib.parse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "research", "catalyst-calendar.json")
EARN_DAYS = 7
BIO_MONTHS = 9


def _post(url, body):
    req = urllib.request.Request(url, data=body, headers={
        "User-Agent": "Mozilla/5.0", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=40).read())


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "catalyst-feed/1.0 (research)"})
    return json.loads(urllib.request.urlopen(req, timeout=40).read())


# ---------------- Layer A: earnings (all sectors) ----------------
def earnings_layer():
    today = datetime.date.today()
    lo = datetime.datetime(today.year, today.month, today.day).timestamp()
    hi = lo + EARN_DAYS * 86400
    body = json.dumps({
        "filter": [
            {"left": "market_cap_basic", "operation": "greater", "right": 300_000_000},
            {"left": "close", "operation": "greater", "right": 5},
            {"left": "type", "operation": "equal", "right": "stock"},
            {"left": "exchange", "operation": "in_range", "right": ["NASDAQ", "NYSE", "AMEX"]},
        ],
        "options": {"lang": "en"}, "markets": ["america"],
        "columns": ["name", "description", "earnings_release_next_date",
                    "earnings_per_share_forecast_next_fq", "sector", "market_cap_basic"],
        "sort": {"sortBy": "earnings_release_next_date", "sortOrder": "asc"},
        "range": [0, 800],
    }).encode()
    data = _post("https://scanner.tradingview.com/america/scan", body).get("data", [])
    out = []
    for r in data:
        tkr = r["s"].split(":")[-1]
        name, desc, nd, est, sector, mcap = r["d"]
        if not isinstance(nd, (int, float)) or nd < lo or nd > hi:
            continue
        ed = datetime.date.fromtimestamp(nd).isoformat()
        est_s = f"{est:+.2f}" if isinstance(est, (int, float)) else "n/a"
        out.append({
            "ticker": tkr, "company": desc or name, "sector": sector or "?",
            "event_type": "Earnings", "date_or_window": ed,
            "detail": f"Q report; est EPS {est_s}", "metric": est,
            "source": "tv-scanner",
            "view": (f"Reports {ed} (est EPS {est_s}). If long & extended, TRIM into the print - "
                     "do NOT hold full size through a binary. Fresh entry only POST-print if it "
                     "beats AND holds the gap (PEAD drift = our one measured edge); else awareness-only."),
        })
    return out


# ---------------- SEC name -> ticker map ----------------
_SUFFIX = (" INCORPORATED", " CORPORATION", " HOLDINGS", " HOLDING", " COMPANY", " LIMITED",
           " PHARMACEUTICALS", " THERAPEUTICS", " BIOSCIENCES", " PLC", " LTD", " INC",
           " CORP", " CO", " LLC", " SA", " NV", " AG", " THE", ",", ".")


def _norm(name):
    n = " " + (name or "").upper().strip() + " "
    n = n.replace("&", " AND ")
    for s in _SUFFIX:
        n = n.replace(s, " ")
    return " ".join(n.split())


def sec_ticker_map():
    try:
        d = _get("https://www.sec.gov/files/company_tickers.json")
    except Exception as e:
        print(f"  SEC map failed: {e}")
        return {}
    m = {}
    for v in d.values():
        key = _norm(v.get("title", ""))
        if key and key not in m:
            m[key] = v.get("ticker", "").upper()
    return m


# ---------------- Layer B: biopharma binary ----------------
def biopharma_layer(tmap):
    if not tmap:
        return []
    today = datetime.date.today()
    end = (today + datetime.timedelta(days=BIO_MONTHS * 30)).isoformat()
    adv = (f"AREA[Phase]PHASE3 AND AREA[LeadSponsorClass]INDUSTRY "
           f"AND AREA[PrimaryCompletionDate]RANGE[{today.isoformat()},{end}]")
    url = ("https://clinicaltrials.gov/api/v2/studies?"
           + urllib.parse.urlencode({
               "filter.advanced": adv,
               "fields": ("NCTId,BriefTitle,LeadSponsorName,PrimaryCompletionDate,Phase,"
                          "Condition,OverallStatus"),
               "pageSize": 300, "sort": "PrimaryCompletionDate"},
               quote_via=urllib.parse.quote))
    try:
        studies = _get(url).get("studies", [])
    except Exception as e:
        print(f"  ClinicalTrials failed: {e}")
        return []
    seen, out = set(), []
    for s in studies:
        p = s.get("protocolSection", {})
        sp = p.get("sponsorCollaboratorsModule", {}).get("leadSponsor", {})
        tkr = tmap.get(_norm(sp.get("name", "")))
        if not tkr or tkr in seen:
            continue
        st = p.get("statusModule", {})
        status = st.get("overallStatus", "")
        if status in ("TERMINATED", "WITHDRAWN", "SUSPENDED"):
            continue
        pcd = st.get("primaryCompletionDateStruct", {}).get("date", "")
        phase = "/".join(p.get("designModule", {}).get("phases", []) or ["?"]).replace("PHASE", "Ph")
        cond = ", ".join((p.get("conditionsModule", {}).get("conditions", []) or [])[:2])
        seen.add(tkr)
        out.append({
            "ticker": tkr, "company": sp.get("name", ""), "sector": "Health",
            "event_type": "Trial readout", "date_or_window": f"~{pcd} (window)",
            "detail": f"{phase} {cond}".strip(), "metric": None, "source": "clinicaltrials.gov",
            "view": (f"{phase} readout window ~{pcd}. BINARY - can gap +/-50%. Do NOT hold a "
                     "momentum long through it; awareness / defined-risk spec only, sized for total loss."),
        })
    return out


def main():
    print("Building all-sector catalyst calendar...")
    earn = earnings_layer()
    print(f"  earnings (next {EARN_DAYS}d): {len(earn)}")
    tmap = sec_ticker_map()
    print(f"  SEC ticker map: {len(tmap)} companies")
    bio = biopharma_layer(tmap)
    print(f"  biopharma readouts (mapped): {len(bio)}")

    # earnings wins if a ticker has both (earnings is the nearer, dated catalyst)
    by_ticker = {}
    for rec in bio + earn:
        by_ticker[rec["ticker"]] = rec
    records = sorted(by_ticker.values(), key=lambda r: str(r["date_or_window"]))

    out = {
        "built": datetime.date.today().isoformat(),
        "earn_days": EARN_DAYS, "bio_months": BIO_MONTHS,
        "counts": {"earnings": len(earn), "biopharma": len(bio), "unique_tickers": len(records)},
        "records": records,
    }
    json.dump(out, open(OUT, "w"), indent=1)
    print(f"wrote {OUT} | {len(records)} unique-ticker catalysts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
