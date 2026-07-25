"""Tests for the data contract.

The contract exists because universe-results-<date>.json changed shape seven
times in seven days and og_shadow.py silently read nothing for four of them.
These tests pin the three behaviours that actually matter:

  * a producer that drops a required field is caught at WRITE time
  * a LEGACY (unstamped) file still reads, so history stays available
  * an UNKNOWN FUTURE version is fatal, not shrugged at

Run:  python -m unittest discover -s tests -p "test_*.py" -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

import schema  # noqa: E402


def good():
    """A minimal object that satisfies the CURRENT (v3) contract.

    v3 added the real, tradeable prices alongside the Heikin-Ashi ones:
    `last` stays HA (signals), `plan_entry`/`real_close` are what a plan quotes.
    """
    return {
        "date": "2026-07-24",
        "universe_size": 494,
        "scanned": 492,
        "fresh_count": 48,
        "data_quality": [],
        "hits": [{"sym": "SJM", "verdict": "CANDIDATE - passes every gate",
                  "gates": {}, "plan_entry": 118.32}],
        "all_names": [{"sym": "AAPL", "ce_mode": "BUY", "last": 327.7,
                       "real_close": 333.02}],
    }


class TestStampAndValidate(unittest.TestCase):
    def test_good_object_validates(self):
        obj = schema.stamp(good())
        self.assertEqual(obj["schema_version"], schema.CURRENT_VERSION)
        self.assertEqual(obj["schema_kind"], schema.KIND)
        schema.validate(obj)

    def test_missing_top_level_field_is_caught_at_write_time(self):
        for field in ("date", "scanned", "hits", "all_names", "data_quality"):
            with self.subTest(missing=field):
                obj = good()
                del obj[field]
                with self.assertRaises(schema.SchemaError) as ctx:
                    schema.validate(obj)
                self.assertIn(field, str(ctx.exception))

    def test_the_exact_og_shadow_regression_is_caught(self):
        """all_names[].mode -> ce_mode was the rename that killed the shadow lane."""
        obj = good()
        obj["all_names"] = [{"sym": "AAPL", "mode": "long", "last": 327.7}]  # old shape
        with self.assertRaises(schema.SchemaError) as ctx:
            schema.validate(obj)
        self.assertIn("all_names[].ce_mode", str(ctx.exception))

    def test_missing_row_field_is_caught(self):
        obj = good()
        obj["hits"] = [{"sym": "SJM"}]        # no verdict, no gates
        with self.assertRaises(schema.SchemaError) as ctx:
            schema.validate(obj)
        self.assertIn("hits[].verdict", str(ctx.exception))

    def test_empty_lists_are_legitimate(self):
        """A day with no fresh signals is a real outcome, not a broken file."""
        obj = good()
        obj["hits"] = []
        obj["all_names"] = []
        schema.validate(obj)

    def test_error_message_tells_you_what_to_do(self):
        obj = good()
        del obj["hits"]
        with self.assertRaises(schema.SchemaError) as ctx:
            schema.validate(obj)
        self.assertIn("bump CURRENT_VERSION", str(ctx.exception))


class TestRequireOnRead(unittest.TestCase):
    def test_legacy_unstamped_file_still_reads(self):
        """Breaking history would be a worse bug than the one being fixed."""
        warned = []
        obj = good()                       # no stamp
        got = schema.require(obj, understood=(2, 3), path="old.json", warn=warned.append)
        self.assertIsNone(got)
        self.assertTrue(warned and "LEGACY" in warned[0])

    def test_current_version_reads_clean(self):
        warned = []
        got = schema.require(schema.stamp(good()), understood=(2, 3), warn=warned.append)
        self.assertEqual(got, schema.CURRENT_VERSION)
        self.assertEqual(warned, [])

    def test_unknown_future_version_is_fatal(self):
        """The og_shadow scenario: a newer file handed to an older reader."""
        obj = schema.stamp(good())
        obj["schema_version"] = 99
        with self.assertRaises(schema.SchemaError) as ctx:
            schema.require(obj, understood=(2, 3), path="future.json")
        self.assertIn("v99", str(ctx.exception))
        self.assertIn("only understands", str(ctx.exception))

    def test_file_that_lies_about_its_version_is_fatal(self):
        obj = schema.stamp(good())
        del obj["all_names"]
        with self.assertRaises(schema.SchemaError) as ctx:
            schema.require(obj, understood=(2, 3))
        self.assertIn("not what it says it is", str(ctx.exception))


class TestRealFilesOnDisk(unittest.TestCase):
    """The contract is worthless if it rejects the files we actually have."""

    def test_every_historical_results_file_is_still_readable(self):
        import glob
        import json
        repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        files = sorted(glob.glob(os.path.join(repo, "watchlists", "universe-results-*.json")))
        self.assertTrue(files, "no results files found - test cannot prove anything")
        for f in files:
            with self.subTest(file=os.path.basename(f)):
                with open(f, encoding="utf-8") as fh:
                    d = json.load(fh)
                schema.require(d, understood=(2, 3), path=f, warn=lambda m: None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
