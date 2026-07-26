"""The ratchet-watch promise: the exit line = max(stop, 0.8 x highest close),
it only ever moves UP, and no TV action is emitted while the stop still
governs. Runs in EOD chain step 0 with the other gate tests."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

from ratchet_watch import build_actions, ratchet_level  # noqa: E402


def book(**pos):
    base = {"sym": "DVN", "shares": 1000, "entry": 45.11, "stop": 43.9,
            "opened": "2026-07-24", "high_close": None, "ratchet_alert": None,
            "notes": ""}
    base.update(pos)
    return {"ratchet_pct": 0.20, "positions": [base]}


class TestRatchetLevel(unittest.TestCase):
    def test_stop_governs_below_threshold(self):
        # +10% high: 0.8 x 49.6 = 39.7 < stop 43.9 -> no ratchet yet
        self.assertIsNone(ratchet_level(49.6, 43.9, 0.20))

    def test_ratchet_takes_over_above_threshold(self):
        self.assertEqual(ratchet_level(60.0, 43.9, 0.20), 48.0)

    def test_no_high_no_level(self):
        self.assertIsNone(ratchet_level(None, 43.9, 0.20))


class TestBuildActions(unittest.TestCase):
    def test_no_action_while_stop_governs(self):
        b = book()
        self.assertEqual(build_actions(b, {"DVN": [45.5, 49.6]}), [])
        self.assertEqual(b["positions"][0]["high_close"], 49.6)

    def test_wires_new_alert_once_in_profit(self):
        b = book()
        acts = build_actions(b, {"DVN": [45.5, 58.0, 60.0]})
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["level"], 48.0)
        self.assertIsNone(acts[0]["delete_id"])
        self.assertNotIn("do NOT", acts[0]["message"])  # exit msg, not checkpoint
        self.assertIn("EXIT", acts[0]["message"])

    def test_raises_existing_alert_on_new_high(self):
        b = book(ratchet_alert={"id": 111, "level": 48.0})
        acts = build_actions(b, {"DVN": [65.0]})
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["level"], 52.0)
        self.assertEqual(acts[0]["delete_id"], 111)

    def test_never_moves_down_or_sideways(self):
        b = book(ratchet_alert={"id": 111, "level": 52.0})
        self.assertEqual(build_actions(b, {"DVN": [60.0]}), [])   # 48 < 52
        self.assertEqual(build_actions(b, {"DVN": [65.0]}), [])   # 52 == 52

    def test_missing_closes_keeps_state_untouched(self):
        b = book(high_close=60.0, ratchet_alert={"id": 111, "level": 48.0})
        acts = build_actions(b, {})
        self.assertEqual(len(acts), 0)
        self.assertEqual(b["positions"][0]["high_close"], 60.0)


if __name__ == "__main__":
    unittest.main()
