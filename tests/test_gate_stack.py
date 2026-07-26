"""Tests for THE GATE STACK - the module that decides whether a name is tradeable.

Written 2026-07-25. Before this file, gate_stack.py had no tests at all: its only
validation was running the full ~3-hour EOD chain and eyeballing the funnel, so
every regression was found in production at 15:15 CT, once a day.

The gate stack's whole promise is that it FAILS CLOSED - missing data raises
rather than letting a name through. That promise is exactly the kind of thing
that rots silently, because the failure mode is a name quietly passing. These
tests pin every gate and every boundary.

Stdlib unittest on purpose: no pytest dependency, so this can run inside
run_eod_chain.bat.

Run:  python -m unittest discover -s tests -p "test_*.py" -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

import gate_stack as gs  # noqa: E402


def row(**over):
    """A row that passes every gate. Each test breaks exactly one thing.

    stop 92 vs last 100 and ATR 5 -> 1.6x ATR (inside the 1-4 band) and 8.0%
    away (inside the 12% cap). ADV 100M -> max position 10M, comfortably above
    the 85k default.
    """
    base = {"sym": "TEST", "last": 100.0, "zlsma": 90.0, "regime": "PASS",
            "pct_vs_200": 15.0, "adx": 25.0, "plus_di": 25.0, "minus_di": 10.0,
            "avg_dollar_vol": 100_000_000.0, "atr": 5.0, "long_stop": 92.0}
    base.update(over)
    return base


class TestPassingBaseline(unittest.TestCase):
    def test_clean_row_passes_every_gate(self):
        verdict, fails, detail = gs.evaluate(row())
        self.assertEqual(verdict, "CANDIDATE - passes every gate")
        self.assertEqual(fails, [])
        self.assertTrue(detail["above_zlsma"])
        self.assertEqual(detail["stop_x_atr"], 1.6)


class TestFailsClosed(unittest.TestCase):
    """The core promise: absent data must never become a silent pass."""

    def test_every_required_field_raises_when_missing(self):
        for field in gs.REQUIRED:
            with self.subTest(missing=field):
                with self.assertRaises(gs.MissingGateData):
                    gs.evaluate(row(**{field: None}))

    def test_missing_field_names_itself_in_the_message(self):
        with self.assertRaises(gs.MissingGateData) as ctx:
            gs.evaluate(row(adx=None))
        self.assertIn("adx", str(ctx.exception))

    def test_non_strict_blocks_rather_than_passing(self):
        """strict=False is the documented escape hatch - it must still BLOCK."""
        verdict, fails, _ = gs.evaluate(row(adx=None), strict=False)
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertIn("adx", fails[0])

    def test_zero_atr_blocks_instead_of_dividing(self):
        """ATR 0 is present-but-useless: it must fail, not sneak through."""
        verdict, fails, _ = gs.evaluate(row(atr=0.0))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("no ATR available" in f for f in fails))


class TestRegimeGate(unittest.TestCase):
    def test_deep_fail_blocks(self):
        verdict, fails, _ = gs.evaluate(row(regime="DEEP-FAIL", pct_vs_200=-12.4))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertIn("DEEP-FAIL", fails[0])

    def test_repair_is_starter_only_not_blocked(self):
        """REPAIR is a size instruction, not a veto - LHX 2026-07-24."""
        verdict, notes, _ = gs.evaluate(row(regime="REPAIR", pct_vs_200=-4.7))
        self.assertEqual(verdict, "STARTER ONLY - regime REPAIR")
        self.assertTrue(any("starter size" in n for n in notes))


class TestTrendAndDirectionGates(unittest.TestCase):
    def test_adx_below_minimum_blocks(self):
        verdict, fails, _ = gs.evaluate(row(adx=19.9))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("ADX" in f for f in fails))

    def test_adx_exactly_at_minimum_passes(self):
        verdict, _, _ = gs.evaluate(row(adx=gs.ADX_MIN))
        self.assertEqual(verdict, "CANDIDATE - passes every gate")

    def test_minus_di_above_plus_di_blocks(self):
        verdict, fails, _ = gs.evaluate(row(plus_di=10.0, minus_di=25.0))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("sellers in control" in f for f in fails))

    def test_equal_di_blocks(self):
        """Ties go to blocked: +DI must be strictly greater."""
        verdict, _, _ = gs.evaluate(row(plus_di=15.0, minus_di=15.0))
        self.assertTrue(verdict.startswith("BLOCKED"))


class TestStructureGate(unittest.TestCase):
    def test_price_below_zlsma_blocks(self):
        verdict, fails, _ = gs.evaluate(row(last=89.0, long_stop=85.0))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("ZLSMA" in f for f in fails))

    def test_price_equal_to_zlsma_blocks(self):
        verdict, _, _ = gs.evaluate(row(last=90.0, zlsma=90.0, long_stop=85.0))
        self.assertTrue(verdict.startswith("BLOCKED"))


class TestStopGates(unittest.TestCase):
    def test_stop_inside_one_atr_blocks(self):
        """The FRT case 2026-07-22: a stop inside daily noise gets hit by nothing."""
        verdict, fails, _ = gs.evaluate(row(long_stop=97.0))  # 0.6x ATR
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("inside daily noise" in f for f in fails))

    def test_stop_beyond_atr_ceiling_blocks(self):
        verdict, fails, _ = gs.evaluate(row(atr=1.0, long_stop=94.0))  # 6x ATR
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("token" in f for f in fails))

    def test_wide_percentage_stop_blocks_on_the_volatility_cap(self):
        """The DELL case: 2.78x ATR is fine, but a 20%-away stop = too wild to
        size. (Renamed 2026-07-26: was the '2:1 cap'; same behavior, honest name.)"""
        verdict, fails, _ = gs.evaluate(row(atr=8.0, long_stop=80.0))  # 2.5x ATR, 20%
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("volatility cap" in f for f in fails))

    def test_stop_read_from_stop_key_when_long_stop_absent(self):
        r = row()
        r.pop("long_stop")
        r["stop"] = 92.0
        verdict, _, detail = gs.evaluate(r)
        self.assertEqual(verdict, "CANDIDATE - passes every gate")
        self.assertEqual(detail["stop_x_atr"], 1.6)


class TestLiquidityGate(unittest.TestCase):
    def test_thin_name_blocks(self):
        """The SKK case 2026-07-22: $84k ADV was auto-scored PASSING by hand-code."""
        verdict, fails, _ = gs.evaluate(row(avg_dollar_vol=84_000.0))
        self.assertTrue(verdict.startswith("BLOCKED"))
        self.assertTrue(any("illiquid" in f for f in fails))

    def test_position_exactly_at_the_cap_passes(self):
        adv = gs.DEFAULT_POSITION * gs.ADV_MULTIPLE
        verdict, _, _ = gs.evaluate(row(avg_dollar_vol=adv))
        self.assertEqual(verdict, "CANDIDATE - passes every gate")

    def test_smaller_position_clears_a_thinner_name(self):
        verdict, _, _ = gs.evaluate(row(avg_dollar_vol=1_000_000.0), position_size=50_000)
        self.assertEqual(verdict, "CANDIDATE - passes every gate")


class TestFunnel(unittest.TestCase):
    def test_counts_survivors_at_each_stage(self):
        rows = [row(sym="GOOD"),
                row(sym="THIN", avg_dollar_vol=84_000.0),
                row(sym="NOADX", adx=10.0)]
        stages, survivors = gs.funnel(rows)
        self.assertEqual(stages[0], ("fresh signals", 3))
        self.assertEqual(dict(stages)["ADX >= 20"], 2)
        self.assertEqual([r["sym"] for r in survivors], ["GOOD"])

    def test_funnel_drops_repair_names_that_evaluate_only_starter_sizes(self):
        """KNOWN DIVERGENCE, pinned deliberately, not endorsed.

        funnel()'s first stage keeps only regime == "PASS", so a REPAIR name is
        counted out of the funnel entirely - while evaluate() returns
        "STARTER ONLY" for that same name and it lands in gated_longs (LHX,
        2026-07-24). The published funnel therefore UNDERSTATES how many names
        the stack would actually let you size.

        Left as-is under the rule freeze through 2026-08-31. This test is here so
        the divergence is a recorded decision rather than a surprise.
        """
        repair = row(sym="REPAIR1", regime="REPAIR", pct_vs_200=-4.7)
        verdict, _, _ = gs.evaluate(repair)
        self.assertEqual(verdict, "STARTER ONLY - regime REPAIR")

        stages, survivors = gs.funnel([repair])
        self.assertEqual(dict(stages)["regime PASS"], 0)
        self.assertEqual(survivors, [])

    def test_funnel_drops_rows_carrying_stop_instead_of_long_stop(self):
        """SECOND KNOWN DIVERGENCE, same status.

        evaluate() reads `long_stop` OR `stop`; funnel()'s ATR stage reads only
        `long_stop`. gated_longs rows carry `stop`, so feeding them to funnel()
        silently zeroes the ATR stage and everything after it.
        """
        r = row(sym="STOPKEY")
        r.pop("long_stop")
        r["stop"] = 92.0
        self.assertEqual(gs.evaluate(r)[0], "CANDIDATE - passes every gate")

        stages, survivors = gs.funnel([r])
        self.assertEqual(dict(stages)["stop >= 1x ATR"], 0)
        self.assertEqual(survivors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
