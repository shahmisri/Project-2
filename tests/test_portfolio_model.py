from __future__ import annotations

import pandas as pd
import unittest

from portfolio_model import (
    PORTFOLIOS,
    TRAINING_CORRELATIONS,
    TRAINING_RETURNS,
    TRAINING_VOLATILITIES,
    eligible_dgs10_observation,
    historical_metrics,
    historical_portfolio_metrics,
    LOCKED_BASE_TRANSACTION_COST_BPS,
    LOCKED_CHANGED_TRANSACTION_COST_BPS,
    locked_transaction_cost_comparison,
    locked_experiment_ready,
    mandate_checks,
    observation_published_by,
    portfolio_metrics,
    portfolio_verdict,
    transaction_cost_drag,
)


class PortfolioModelTests(unittest.TestCase):
    def test_training_baselines_calculate_return_and_risk(self) -> None:
        equal = portfolio_metrics(PORTFOLIOS["Equal weight"])
        benchmark = portfolio_metrics(PORTFOLIOS["Benchmark 40% LQD / 60% VT"])
        candidate = portfolio_metrics(PORTFOLIOS["Constrained candidate"])

        self.assertAlmostEqual(equal["expected_return"], 0.052)
        self.assertAlmostEqual(benchmark["expected_return"], 0.068)
        self.assertAlmostEqual(candidate["expected_return"], 0.0658)
        self.assertGreater(equal["volatility"], 0)
        self.assertGreater(benchmark["volatility"], equal["volatility"])
        self.assertAlmostEqual(candidate["reserve_share"], 0.20)

    def test_mandate_verdicts_show_failures_and_unverified_gates(self) -> None:
        results: dict[str, str] = {}
        for name, weights in PORTFOLIOS.items():
            metrics = portfolio_metrics(weights)
            checks = mandate_checks(weights, expected_return=metrics["expected_return"])
            results[name] = portfolio_verdict(checks)

        self.assertTrue(results["Equal weight"].startswith("FAILS"))
        self.assertTrue(results["Benchmark 40% LQD / 60% VT"].startswith("FAILS"))
        self.assertTrue(results["Constrained candidate"].startswith("NOT CLEARED"))

    def test_rejects_invalid_correlation_and_weights(self) -> None:
        correlations = TRAINING_CORRELATIONS.copy()
        correlations[0, 1] = 1.2
        with self.assertRaisesRegex(ValueError, "between -1 and 1"):
            portfolio_metrics(
                PORTFOLIOS["Equal weight"],
                returns=TRAINING_RETURNS,
                volatilities=TRAINING_VOLATILITIES,
                correlations=correlations,
            )
        with self.assertRaisesRegex(ValueError, "sum to 100"):
            portfolio_metrics((0.2, 0.2, 0.2, 0.2))

    def test_historical_window_and_drawdown_are_explicit(self) -> None:
        prices = pd.DataFrame(
            {
                "BIL": [100.0, 101.0, 100.0, 102.0, 101.0],
                "IEF": [100.0, 100.0, 99.0, 101.0, 100.0],
                "LQD": [100.0, 101.0, 99.0, 102.0, 100.0],
                "VT": [100.0, 103.0, 97.0, 105.0, 101.0],
            },
            index=pd.date_range("2024-01-31", periods=5, freq="ME"),
        )
        history = historical_metrics(prices, window_months=3)
        candidate = historical_portfolio_metrics(
            PORTFOLIOS["Constrained candidate"], history
        )

        self.assertEqual(history["observations"], 3)
        self.assertLess(candidate["max_drawdown"], 0)
        self.assertGreaterEqual(candidate["annualized_volatility"], 0)

    def test_transaction_cost_drag_uses_turnover_and_cost(self) -> None:
        self.assertAlmostEqual(transaction_cost_drag(0.25, 40), 0.001)
        with self.assertRaisesRegex(ValueError, "between 0% and 100%"):
            transaction_cost_drag(1.2, 40)

    def test_locked_transaction_cost_comparison_reports_gross_and_net_returns(self) -> None:
        results = locked_transaction_cost_comparison()

        self.assertEqual(results["portfolio"], "Equal-weight BIL/IEF/LQD/VT")
        self.assertEqual(results["annual_turnover"], 0.25)
        self.assertEqual(
            results["before"]["transaction_cost_bps_per_traded_dollar"],
            LOCKED_BASE_TRANSACTION_COST_BPS,
        )
        self.assertEqual(
            results["after"]["transaction_cost_bps_per_traded_dollar"],
            LOCKED_CHANGED_TRANSACTION_COST_BPS,
        )
        self.assertAlmostEqual(results["before"]["gross_expected_return"], 0.052)
        self.assertAlmostEqual(results["after"]["gross_expected_return"], 0.052)
        self.assertAlmostEqual(results["before"]["transaction_cost_drag"], 0.000625)
        self.assertAlmostEqual(results["after"]["transaction_cost_drag"], 0.00125)
        self.assertAlmostEqual(results["before"]["net_expected_return"], 0.051375)
        self.assertAlmostEqual(results["after"]["net_expected_return"], 0.05075)
        self.assertEqual(results["before"]["classroom_comparison_result"], "FAIL")
        self.assertEqual(results["after"]["classroom_comparison_result"], "FAIL")
        self.assertFalse(results["classroom_comparison_changes"])
        self.assertFalse(results["committee_decision_changes"])
        self.assertEqual(
            results["committee_decision"],
            "NO PILOT AUTHORIZATION",
        )

    def test_release_time_excludes_same_day_before_415(self) -> None:
        observations = pd.DataFrame(
            [
                {
                    "observation_date": "2026-10-01",
                    "value": 5.24,
                    "vintage_date": "2026-10-05",
                    "point_in_time_checked": True,
                },
                {
                    "observation_date": "2026-10-02",
                    "value": 5.28,
                    "vintage_date": "2026-10-05",
                    "point_in_time_checked": True,
                },
                {
                    "observation_date": "2026-10-30",
                    "value": 4.94,
                    "vintage_date": "2026-11-03",
                    "point_in_time_checked": False,
                },
            ]
        )
        after_release = eligible_dgs10_observation(
            observations, "2026-11-03", "16:15"
        )

        self.assertFalse(
            observation_published_by("2026-10-02", "2026-10-02", "16:14")
        )
        self.assertTrue(
            observation_published_by("2026-10-02", "2026-10-02", "16:15")
        )
        self.assertIsNotNone(after_release)
        self.assertEqual(after_release["observation_date"].isoformat(), "2026-10-02")
        self.assertAlmostEqual(after_release["value"], 5.28)

    def test_locked_experiment_requires_matching_committed_prediction(self) -> None:
        prediction = (
            "# Changed-input prediction\n"
            "Changed input: transaction cost = 50 basis points per traded dollar\n\n"
            "Prediction:\n"
            "I expect expected return to decline.\n"
        )
        allowed, _ = locked_experiment_ready(
            prediction,
            LOCKED_CHANGED_TRANSACTION_COST_BPS,
            "0123456789abcdef",
            "https://github.com/example/course/commit/0123456789abcdef",
            True,
        )
        changed_input, _ = locked_experiment_ready(
            prediction,
            LOCKED_BASE_TRANSACTION_COST_BPS,
            "0123456789abcdef",
            "https://github.com/example/course/commit/0123456789abcdef",
            True,
        )
        not_committed, _ = locked_experiment_ready(
            prediction,
            LOCKED_CHANGED_TRANSACTION_COST_BPS,
            "",
            "",
            False,
        )

        self.assertTrue(allowed)
        self.assertFalse(changed_input)
        self.assertFalse(not_committed)
