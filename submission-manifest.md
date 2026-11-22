# Project 2 — Submission Manifest

**Project:** Meridian Foundation — Investment Management Application

**GitHub Repository:** https://github.com/shahmisri/Project-2

**Status:** Application implemented, investment decision documented, and locked changed-input experiment completed. Final video links, transcripts, and repository verification remain to be completed.

## 1. Project Deliverables

| # | Deliverable | Status | Location / Evidence |
|---|---|---|---|
| 1 | Runnable Streamlit application | Complete locally | `app.py`, `portfolio_model.py` |
| 2 | README and setup instructions | Included | `README.md`, `requirements.txt` |
| 3 | Investment mandate and decision framework | Complete with limitations | Streamlit dashboard and `docs/decision-memo.md` |
| 4 | Portfolio baselines and constrained candidate | Implemented | Equal-weight, benchmark, and constrained portfolio comparisons |
| 5 | Historical ETF data and documentation | Included | `data/etf_monthly_prices.csv`, `data/ETF-data-card.md` |
| 6 | Point-in-time DGS10 evidence | Included; signal quarantined | `data/dgs10_observations.csv`, `data/DGS10-data-card.md` |
| 7 | Risk analysis, mandate checks, and stress testing | Implemented | Interactive Streamlit application |
| 8 | Automated tests, reconciliation, and reproducibility | Documented | `tests/`, `evidence/test-results.txt`, `evidence/known-answer-reconciliation.md`, `docs/github-cold-run.md` |
| 9 | Locked changed-input experiment | Completed | Pre-run GitHub commit, prediction, and observed result |
| 10 | Final investment decision memo | Updated | `docs/decision-memo.md` |
| 11 | Validation and evidence documentation | Updated | `docs/validation-and-ai-use.md` |
| 12 | Three presentation videos and transcripts | Recorded; final submission pending | YouTube links and transcript links to be added below |

## 2. Locked Changed-Input Experiment Evidence

**Pre-run GitHub commit:** `b7deec38cddd2f6c0177e89ff522f5092e7e1ed1`

**Commit URL:** https://github.com/shahmisri/Project-2/commit/b7deec38cddd2f6c0177e89ff522f5092e7e1ed1

**Experiment date:** November 21, 2026

**Portfolio:** Equal-weight BIL/IEF/LQD/VT

**Changed input:** Transaction costs increased from 25 to 50 basis points per traded dollar.

**Annual turnover:** 25%

### Observed Results

| Metric | Before | After |
|---|---:|---:|
| Transaction cost | 25 bps | 50 bps |
| Gross expected return | 5.2000% | 5.2000% |
| Transaction-cost drag | 0.0625% | 0.1250% |
| Net expected return | 5.1375% | 5.0750% |
| 6.5% classroom comparison | FAIL | FAIL |
| Committee decision | No pilot authorization | No pilot authorization |

The model results supported the pre-run prediction that higher transaction costs would reduce expected net returns without changing gross expected returns or the committee decision.

**Evidence files:**
- `evidence/changed_input_prediction.md`
- `evidence/changed_input_results.json`
- `docs/validation-and-ai-use.md`

## 3. Presentation Videos

### Video 1 — Application Demonstration

**YouTube link:** https://youtu.be/bOSxfeaUE6Q 

**Transcript:** https://github.com/shahmisri/Project-2/blob/main/docs/video-1-transcript.md

**Content:** Application overview, portfolio comparison, mandate checks, sensitivity controls, historical data limitations, and final recommendation.

### Video 2 — Validation and Sensitivity

**YouTube link:** https://youtu.be/fqmVKurWSbA

**Transcript:** https://github.com/shahmisri/Project-2/blob/main/docs/video-2-transcript.md 

**Content:** Automated testing, known-answer reconciliation, stress testing, locked changed-input experiment, and point-in-time data integrity.

### Video 3 — Investment Recommendation and Committee Defense

**YouTube link:** https://youtu.be/SToZYf-3IFY

**Transcript:** https://github.com/shahmisri/Project-2/blob/main/docs/video-3-transcript.md

**Content:** Investment mandate, portfolio comparison, recommendation rationale, experiment evidence, quantified decision triggers, and conditions for reconsideration.

## 4. Final Investment Decision

**Recommendation: Do not authorize a pilot allocation.**

The currently supported pilot allocation is **0%**.

A conditional **5%–10% pilot sleeve** may be reconsidered only after the outstanding mandate-compliance, point-in-time data-integrity, and validation requirements are resolved.

The constrained candidate passes the simplified classroom return comparison and reserve checks, but full investment mandate compliance has not been established.

The DGS10 signal remains quarantined pending sufficient point-in-time validation.

This application is an educational decision-support tool and does not establish an executable investment recommendation.

## 5. Final Submission Reference

**Repository:** https://github.com/shahmisri/Project-2

**Decision memo:** `docs/decision-memo.md`

**Validation record:** `docs/validation-and-ai-use.md`

**Submission manifest:** `submission-manifest.md`

**Final recommendation:** NO PILOT AUTHORIZATION — 0% allocation.
