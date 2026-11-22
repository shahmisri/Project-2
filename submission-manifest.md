# Project 2 — Submission Manifest

**Status:** Application implemented and locked changed-input experiment completed. Final video submissions and independent validation requirements remain outstanding.

| Deliverable | Status | Notes |
|---|---|---|
| Streamlit dashboard (`app.py`) | Complete | Runnable investment management dashboard with portfolio comparisons, risk analysis, and mandate checks |
| Setup instructions (`README.md`) | Complete | Includes installation, Streamlit launch, and test instructions; previously verified through a fresh local run |
| Mandate, objectives, benchmark, universe | Complete with limitations | Actual CPI + 4% objective distinguished from the 6.5% classroom comparison |
| Equal-weight and benchmark baselines | Complete | Based on Lab 14 classroom assumptions |
| Constrained candidate and mandate checks | Implemented; not cleared | Some checks pass, but full compliance remains unverified |
| Historical ETF data and data card | Included | Lab 15 data; independent source verification remains incomplete |
| DGS10 data and data card | Included; quarantined | Incomplete point-in-time history prevents signal authorization |
| Risk and stress-test controls | Implemented | Interactive scenario analysis; not independently validated forecasts |
| Automated tests | Passed locally | Copilot reported 10 passing tests; final uploaded version should be tested again |
| Known-answer reconciliation | Documented | `evidence/known-answer-reconciliation.md` |
| Decision memo | Updated | `docs/decision-memo.md`; recommends 0% pilot allocation |
| Validation record | Updated | `docs/validation-and-ai-use.md`; includes prediction and observed results |
| Pre-run prediction commit | Complete | GitHub commit `b7deec38cddd2f6c0177e89ff522f5092e7e1ed1` |
| Locked changed-input experiment | Complete | Transaction costs increased from 25 to 50 bps; net expected return declined from 5.1375% to 5.0750% |
| Experiment evidence files | Generated locally; upload to verify | `evidence/changed_input_prediction.md` and `evidence/changed_input_results.json` |
| Cold-run evidence | Documented | `docs/github-cold-run.md`; update to reflect the latest application changes |
| Video script | Drafted | `docs/video-script.md` |
| Video 1 — Application demonstration | Not yet submitted | Maximum 3 minutes |
| Video 2 — Validation and sensitivity | Not yet submitted | Maximum 5 minutes |
| Video 3 — Recommendation and decision defense | Not yet submitted | Maximum 5 minutes |
| Video links and transcripts | Pending | Add links and transcripts to submission materials |
| Full mandate verification and pilot approval | Not cleared | Requires further market data, validation, and CIO/committee decisions |

## Locked Changed-Input Experiment Evidence

**Pre-run GitHub commit:**
https://github.com/shahmisri/Project-2/commit/b7deec38cddd2f6c0177e89ff522f5092e7e1ed1

**Input change:** Transaction costs increased from 25 to 50 basis points per traded dollar.

**Annual turnover:** 25%.

**Portfolio:** Equal-weight BIL/IEF/LQD/VT.

**Observed results:**
- Gross expected return remained 5.2000%.
- Transaction-cost drag increased from 0.0625% to 0.1250%.
- Net expected return decreased from 5.1375% to 5.0750%.
- Both scenarios failed the 6.5% classroom comparison.
- Committee authorization remained unchanged: no pilot authorization.

The model results supported the pre-run prediction.

## Outstanding Submission Items

- Verify that all updated Python files, experiment evidence, and documentation are present in GitHub.
- Run the automated tests on the final repository version.
- Complete and upload the three presentation videos.
- Include required video links and transcripts in the final submission.
- Confirm all repository links and submission instructions before submitting.

## Final Investment Decision

**Recommendation: Do not authorize a pilot.**

The current supported pilot allocation is 0%. A conditional 5%–10% pilot may be reconsidered only after resolving outstanding mandate-compliance, point-in-time data-integrity, and validation requirements.

The application is an educational decision-support tool and does not establish an executable investment recommendation.