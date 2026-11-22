from pathlib import Path
import unittest

import pandas as pd

from portfolio_model import load_price_data


PROJECT = Path(__file__).resolve().parents[1]


class DataIntegrityTests(unittest.TestCase):
    def test_all_clone_runtime_files_are_in_project_root(self) -> None:
        required_files = (
            PROJECT / "app.py",
            PROJECT / "portfolio_model.py",
            PROJECT / "requirements.txt",
            PROJECT / "data" / "etf_monthly_prices.csv",
            PROJECT / "data" / "dgs10_observations.csv",
            PROJECT / "data" / "DGS10-data-card.md",
            PROJECT / "data" / "ETF-data-card.md",
        )

        for path in required_files:
            with self.subTest(path=path.relative_to(PROJECT)):
                self.assertTrue(path.is_file())

    def test_supplied_price_data_has_expected_range_and_no_missing_values(self) -> None:
        prices = load_price_data(PROJECT / "data" / "etf_monthly_prices.csv")

        self.assertEqual(len(prices), 60)
        self.assertEqual(prices.index.min(), pd.Timestamp("2021-10-31"))
        self.assertEqual(prices.index.max(), pd.Timestamp("2026-09-30"))
        self.assertTrue(prices.notna().all().all())
        self.assertTrue((prices > 0).all().all())
