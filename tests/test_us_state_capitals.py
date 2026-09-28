"""Checks data/us-state-capitals.csv lists all 50 US states with their capitals."""
import csv
import unittest
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "us-state-capitals.csv"


def load_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


class USStateCapitalsTest(unittest.TestCase):
    def setUp(self):
        self.rows = load_rows()

    def test_has_50_entries(self):
        self.assertEqual(len(self.rows), 50)

    def test_states_and_abbreviations_are_unique(self):
        self.assertEqual(len({r["state"] for r in self.rows}), 50)
        self.assertEqual(len({r["abbreviation"] for r in self.rows}), 50)

    def test_every_state_has_a_capital(self):
        for row in self.rows:
            self.assertTrue(row["capital"].strip(), f"missing capital for {row['state']}")

    def test_excludes_non_states(self):
        abbreviations = {r["abbreviation"] for r in self.rows}
        for non_state in ("DC", "PR", "GU", "VI", "AS", "MP"):
            self.assertNotIn(non_state, abbreviations)


if __name__ == "__main__":
    unittest.main()
