# Validation plan and AI-use record

**AI-use disclosure:** AI was used to organize requirements and draft project code, tests, and prose. The project preserves supplied source observations and does not fabricate market data, holdings, validation evidence, the student's prediction, or experiment results.

**Education-only disclosure:** This application and report are educational materials, not investment advice.

## Source mapping

| Project element | Existing reference | Treatment |
|---|---|---|
| Client mandate, benchmark, liquidity, reserve, issuer, turnover, horizon, unresolved loss rule | `lab13_mandate_defense.md`, `mandate.py` | Transcribed; actual CPI + 4% distinguished from the Lab 14 comparison proxy |
| Training asset assumptions and baseline calculations | `portfolio.py`, `lab14_portfolio_baselines.md` | Reused transparently as classroom inputs; not called ETF forecasts |
| Historical ETF data | `prices.csv`, `lab15_historical.py`, `lab15_portfolio_stability.md` | CSV copied unchanged; descriptive calculations in app |
| DGS10 definition, timing, and sparse checks | `lab17_DGS10_data_card.md` | Four reported rows retained; current-only row excluded from PIT selection |
| App organization and user interaction pattern | `lab19_panel_app.py` | Streamlit UI pattern used as a reference; no original Lab 19 files modified |

## Validation status

Implemented automated tests cover model calculations, portfolio mandate
outcomes, invalid inputs, historical metrics, transaction-cost arithmetic,
release-time gating, the experiment gate, and source-data row/date integrity.
Run them with `pytest -q` in the project virtual environment.

Not completed or not independently evidenced:

- Independent verification of ETF history retrieval, adjusted-price methodology,
  survivorship/point-in-time limitations, and historical source values.
- A full ALFRED vintage archive and a backtest aligning signal observation,
  publication, decision, and execution times.
- ETF prospectus/settlement evidence for five-day liquidity and fund look-through
  holdings for issuer concentration.
- Starting portfolio holdings and an agreed turnover calculation.
- CPI input and a valid five-year net-of-costs test for CPI + 4%.
- Forward estimates, independent model validation, out-of-sample performance,
  and completed stress-test evidence.
- CIO resolution of the calendar-year loss rule.
- Student-authored prediction, GitHub commit, and locked changed-input result.

The app's scenario panel can calculate user-selected what-if assumptions. Such
outputs are not external evidence. The DGS10 display remains quarantined; there
is no "admit" switch that promotes it to a trading signal.

## Human-authored prediction record

The student is responsible for writing the changed-input prediction without AI,
then saving and committing that exact file before using the locked test. The app
requires a matching input, commit SHA, commit URL, and a student attestation. It
does not query GitHub and cannot independently establish authorship or commit
contents. The prediction/result evidence files are created only after the
student uses the app buttons.

## Locked Changed-Input Record — Pre-Run Prediction

**Date:** November 21, 2026

**Portfolio:** Equal-weight portfolio (BIL, IEF, LQD, VT)

**Input being changed:** Transaction cost (basis points per traded dollar)

**Original value:** 25 basis points (0.25%)

**New value:** 50 basis points (0.50%)

**Annual portfolio turnover assumption:** 25%

### My Prediction Before Running the Experiment

I predict that increasing transaction costs from 25 to 50 basis points will decrease the portfolio's expected return after costs while leaving its gross expected return and volatility unchanged.

Under the original assumptions, my equal-weight portfolio has a gross expected annual return of 5.20%. At 25 basis points of transaction costs and 25% annual turnover, the estimated net return is approximately 5.14%.

After increasing transaction costs to 50 basis points, I expect the transaction-cost drag to increase from approximately 0.06% to 0.125%. Therefore, I predict that the portfolio's expected return after costs will decrease to approximately **5.08%**.

### Expected Effect on the Investment Decision

I predict that the equal-weight portfolio will continue to fail the 6.5% classroom return comparison, since its expected return is already below that threshold.

I do not expect this change to reverse my overall committee recommendation. My decision will remain **PILOT — NOT AUTHORIZED**, because the process still has unresolved point-in-time data validity and full mandate-compliance requirements.

However, the higher transaction costs will further weaken the case for the equal-weight portfolio.

### Prediction Status

This prediction has been recorded before executing the changed-input experiment. The observed results will be documented separately after the pre-run GitHub commit.

**Pre-run GitHub commit:** Pending

**Observed result:** Not yet tested

**Decision after experiment:** Pending