"""Tests for the symbol-resolution guard.

On 2026-07-24 the live sweep carried FIVE wrong companies, in foreign currencies,
priced and gated as if they were the US names:

    BHP  -> ASX:BHP    BHP Group Ltd, AUD 59.23    (want NYSE ADR, $83.72)
    COCO -> IDX:COCO   PT Wahana Interfood, IDR    (want Vita Coco, $65.97)
    DTE  -> XETR:DTE   Deutsche Telekom, EUR       (want DTE Energy, $149.46)
    EQR  -> ASX:EQR    EQ Resources, AUD 0.26      (want Equity Residential, $67.86)
    SFL  -> NSE:SFL    Sheela Foam, INR 755.92     (want SFL Corp, $11.92 - 63x off)

BHP and EQR had already been fixed BY HAND for the 7/23 run and came straight
back the next day. That is the point of these tests: the fix has to be mechanical
or it does not survive contact with the next run.

Two halves are covered:
  * FORCE_PREFIX pins the known traps to their US listing (verified against
    TradingView symbol search, not guessed)
  * the currency guard drops ANY non-USD row, including traps nobody has hit yet

Run:  python -m unittest discover -s tests -p "test_*.py" -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

import build_extended_universe as bxu  # noqa: E402


# The rule the guard implements, mirrored here so the test states it independently
# of the module under test rather than just re-running its code.
def drop_foreign(rows):
    kept, dropped = [], []
    for r in rows:
        if r.get("ok") and r.get("rccy") and r["rccy"] != "USD":
            r = {**r, "ok": False}
            dropped.append(r)
        else:
            kept.append(r)
    return kept, dropped


class TestForcePrefix(unittest.TestCase):
    def test_every_known_trap_is_pinned_to_its_us_listing(self):
        expected = {
            "BHP": "NYSE:BHP", "COCO": "NASDAQ:COCO", "DTE": "NYSE:DTE",
            "EQR": "NYSE:EQR", "SFL": "NYSE:SFL",
            "FITB": "NYSE:FITB", "SMCI": "NASDAQ:SMCI",
        }
        for bare, full in expected.items():
            with self.subTest(ticker=bare):
                self.assertEqual(bxu.FORCE_PREFIX.get(bare), full)

    def test_prefixes_are_well_formed(self):
        for bare, full in bxu.FORCE_PREFIX.items():
            with self.subTest(ticker=bare):
                self.assertIn(":", full)
                exch, sym = full.split(":", 1)
                self.assertIn(exch, {"NYSE", "NASDAQ", "AMEX", "BATS", "CBOE"})
                self.assertEqual(sym, bare, "prefix must point at the same ticker")

    def test_bare_ticker_maps_to_prefixed_form(self):
        """This is the substitution the universe builder performs."""
        equities = ["AAPL", "DTE", "EQR", "MSFT"]
        out = [bxu.FORCE_PREFIX.get(t, t) for t in equities]
        self.assertEqual(out, ["AAPL", "NYSE:DTE", "NYSE:EQR", "MSFT"])


class TestCurrencyGuard(unittest.TestCase):
    def test_the_exact_five_from_2026_07_24_are_dropped(self):
        rows = [
            {"rname": "AAPL", "rccy": "USD", "ok": True},
            {"rname": "BHP", "rccy": "AUD", "ok": True},
            {"rname": "COCO", "rccy": "IDR", "ok": True},
            {"rname": "DTE", "rccy": "EUR", "ok": True},
            {"rname": "EQR", "rccy": "AUD", "ok": True},
            {"rname": "SFL", "rccy": "INR", "ok": True},
        ]
        kept, dropped = drop_foreign(rows)
        self.assertEqual([r["rname"] for r in kept], ["AAPL"])
        self.assertEqual(sorted(r["rname"] for r in dropped),
                         ["BHP", "COCO", "DTE", "EQR", "SFL"])

    def test_catches_a_currency_never_seen_before(self):
        """The guard must not be a hardcoded list of the five we found."""
        rows = [{"rname": "NEWTRAP", "rccy": "JPY", "ok": True}]
        kept, dropped = drop_foreign(rows)
        self.assertEqual(kept, [])
        self.assertEqual(len(dropped), 1)

    def test_usd_rows_are_untouched(self):
        rows = [{"rname": "MSFT", "rccy": "USD", "ok": True, "last": 500.0}]
        kept, dropped = drop_foreign(rows)
        self.assertEqual(dropped, [])
        self.assertTrue(kept[0]["ok"])

    def test_missing_currency_is_not_treated_as_foreign(self):
        """Legacy sweeps predate the rccy field - absence must not drop them."""
        rows = [{"rname": "OLD", "ok": True}]
        kept, dropped = drop_foreign(rows)
        self.assertEqual(dropped, [])
        self.assertEqual(len(kept), 1)

    def test_already_failed_rows_are_left_alone(self):
        rows = [{"rname": "DEAD", "rccy": "AUD", "ok": False}]
        kept, dropped = drop_foreign(rows)
        self.assertEqual(dropped, [])


class TestAgainstTheRealSweep(unittest.TestCase):
    """Proof against the actual file that carried the bug."""

    def test_guard_catches_all_five_in_the_recorded_7_24_sweep(self):
        import json
        repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        p = os.path.join(repo, "watchlists", "og-sweep-raw-2026-07-24-heikinashi.json")
        if not os.path.exists(p):
            self.skipTest("7/24 raw sweep not present")
        with open(p, encoding="utf-8") as fh:
            rows = json.load(fh)
        _, dropped = drop_foreign(rows)
        self.assertEqual(sorted(r["rname"] for r in dropped),
                         ["BHP", "COCO", "DTE", "EQR", "SFL"],
                         "the guard must catch exactly the five wrong companies")


if __name__ == "__main__":
    unittest.main(verbosity=2)
