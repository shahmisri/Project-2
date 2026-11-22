# Project 2 — Known-Answer Reconciliation

## Purpose

Verify that the Project 2 portfolio model reproduces the known-answer results from FIN 43900 Lab 14 before relying on its calculations for investment decisions.

## Reference

FIN 43900 Lab 14 — Portfolio Baselines, using the course-provided training assumptions.

## Known-Answer Comparison

| Portfolio | Lab 14 Expected Return | Project 2 Expected Return | Lab 14 Volatility | Project 2 Volatility | Result |
|---|---:|---:|---:|---:|---|
| Equal Weight | 5.20% | 5.20% | 5.21% | 5.21% | PASS |
| Benchmark (40% LQD / 60% VT) | 6.80% | 6.80% | 10.46% | 10.46% | PASS |

## Interpretation

Both portfolio baselines reproduce the Lab 14 reference results to two decimal places. This provides a known-answer check for the expected-return and volatility calculations.

However, matching the classroom results does not independently validate the underlying assumptions or establish that the portfolios meet the actual CPI + 4% investment objective.

## Validation Evidence

The Project 2 automated test suite was run on November 21, 2026, from a fresh GitHub download.

**Result:** Nine tests passed, zero failures.

The fresh-download Streamlit application also launched successfully and displayed the baseline portfolio results.

## Conclusion

The known-answer comparison supports the correctness of the baseline calculations under the course-provided training assumptions. Additional data integrity, mandate, stress-testing, and point-in-time checks remain necessary before the investment process can be authorized.