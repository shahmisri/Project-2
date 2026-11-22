# Meridian Foundation — Investment Management Decision Memo

**AI-use disclosure:** AI assisted in organizing the analysis and drafting this memo. Calculations use the stated classroom assumptions and supplied Lab 15 data; no market observations or experiment results were invented.

**Education-only disclosure:** This memo is for educational purposes only and is not investment advice.

**Decision:** Do not authorize a pilot on the evidence currently available.

**Potential next step:** Reconsider a 5%–10% pilot sleeve only after the outstanding data-integrity, mandate-compliance, and validation requirements are satisfied. This range is a conditional committee discussion parameter, not an approved allocation.

## 1. Mandate and Decision Frame

The Meridian Foundation has a seven-year investment horizon with annual rebalancing. Its primary objective is to earn CPI + 4% annually, net of costs, over rolling five-year periods.

The mandate also specifies:

- Benchmark: 60% global equities / 40% U.S. investment-grade bonds.
- Investment universe: BIL, IEF, LQD, and VT.
- Long-only investing with no leverage.
- Minimum 3% reserve-eligible assets.
- At least 90% of assets redeemable within five business days.
- Maximum 8% exposure to any single nonexempt company.
- Maximum 25% annual turnover without committee approval.
- Calendar-year loss requirement requiring further CIO clarification.

Lab 14 uses a 6.5% expected-return threshold as a classroom comparison proxy. This is **not equivalent to the Foundation's CPI + 4% objective**, which cannot currently be validated from the supplied information.

## 2. Portfolio Baseline Comparison

The following results use Lab 14 classroom assumptions rather than independently validated market forecasts.

| Portfolio | BIL / IEF / LQD / VT | Expected Return | Volatility | Reserve Eligible |
|---|---|---:|---:|---:|
| Equal weight | 25 / 25 / 25 / 25% | 5.20% | 5.21% | 50% |
| Benchmark | 0 / 0 / 40 / 60% | 6.80% | 10.46% | 0% |
| Constrained candidate | 10 / 10 / 20 / 60% | 6.58% | 9.99% | 20% |

**Key findings:**

The equal-weight portfolio fails the 6.5% classroom comparison despite satisfying the simplified reserve check.

The benchmark exceeds the classroom comparison threshold but fails the 3% reserve requirement.

The constrained candidate passes both the 6.5% classroom comparison and simplified reserve check, but its full mandate compliance remains unverified.

All three portfolios remain **NOT CLEARED** because the supplied evidence does not establish issuer look-through concentration, fund-level liquidity, actual CPI + 4% performance, full transaction costs, previous holdings and turnover, or the calendar-year loss procedure.

The constrained candidate should not be interpreted as an optimized or approved portfolio.

## 3. Historical Data and Point-in-Time Evidence

The supplied Lab 15 monthly ETF price file covers October 2021 through September 2026. Lab 15 identifies Yahoo Finance as the source and October 22, 2026 as the download date.

Because complete retrieval settings and adjustment details are unavailable, the historical results are descriptive rather than independently validated forecasts.

The DGS10 interest-rate signal is also not cleared for live decision-making.

Lab 17 identified three unchanged ALFRED vintage observations for September 30 through October 2, 2026. However, these limited observations do not establish complete historical point-in-time availability.

The application excludes same-day DGS10 observations before the reported 4:15 p.m. ET release time, but additional historical vintage and execution-time validation is required.

**Decision:** Keep the DGS10 signal quarantined until point-in-time integrity is established.

## 4. Sensitivity and Stress Testing

The application allows scenario analysis of:

- Expected-return assumptions.
- Historical estimation windows.
- LQD/VT correlation assumptions.
- Transaction costs and annual turnover.
- Portfolio constraints and stopping conditions.

These scenarios help identify model sensitivity but should not be interpreted as independently validated forecasts.

A formal Locked Changed-Input Experiment was completed on November 21, 2026.

## 5. Locked Changed-Input Experiment

**Experiment:** Increase transaction costs from 25 to 50 basis points per traded dollar while holding annual turnover constant at 25%.

**Portfolio tested:** Equal-weight BIL/IEF/LQD/VT.

**Pre-run prediction commit:** `b7deec38cddd2f6c0177e89ff522f5092e7e1ed1`

**Commit URL:** https://github.com/shahmisri/Project-2/commit/b7deec38cddd2f6c0177e89ff522f5092e7e1ed1

### Observed Results

| Metric | Before | After |
|---|---:|---:|
| Transaction cost | 25 bps | 50 bps |
| Annual turnover | 25% | 25% |
| Gross expected return | 5.2000% | 5.2000% |
| Transaction-cost drag | 0.0625% | 0.1250% |
| Net expected return | 5.1375% | 5.0750% |
| 6.5% classroom comparison | FAIL | FAIL |
| Committee authorization | Not authorized | Not authorized |

### Prediction Reconciliation

The pre-run prediction expected that doubling transaction costs would reduce the equal-weight portfolio's net expected return from approximately 5.14% to 5.08%, while leaving gross expected return and the committee decision unchanged.

The observed model output confirmed that direction and approximate magnitude.

Net expected return declined by **0.0625 percentage points (6.25 basis points)**.

Gross expected return remained at 5.20%, and both scenarios failed the 6.5% classroom comparison.

The committee decision did not change.

### Interpretation

The experiment demonstrates that higher implementation costs reduce the portfolio's expected net return without improving its ability to satisfy the classroom return comparison.

This is a deterministic model sensitivity result, not independent evidence of future investment performance.

**Conclusion:** The prediction was supported, but the results do not justify authorizing a pilot allocation.

## 6. Final Investment Recommendation

**Recommendation: NO PILOT AUTHORIZATION.**

Although the constrained candidate produces a model expected return of 6.58% and volatility of 9.99%, there is insufficient evidence to confirm full compliance with the Foundation's investment mandate.

The current approved pilot allocation is **0%**.

A potential **5%–10% pilot sleeve** could be reconsidered only after the investment committee receives satisfactory evidence addressing the outstanding concerns.

### Conditions for Reconsideration

1. **Return objective:** Establish CPI observations and a valid method for testing the CPI + 4% objective, net of costs, over rolling five-year periods.

2. **Point-in-time integrity:** Verify DGS10 vintage availability, release timestamps, portfolio decision times, and execution times before permitting the signal to influence allocations.

3. **Liquidity:** Confirm that at least 90% of the portfolio is redeemable within five business days.

4. **Reserve requirement:** Maintain at least 3% reserve-eligible assets.

5. **Issuer concentration:** Confirm that no single nonexempt company exceeds 8% exposure on a look-through basis.

6. **Turnover:** Maintain annual turnover at or below 25% unless the committee explicitly approves an exception.

7. **Historical validation:** Independently reconcile historical inputs and evaluate performance using out-of-sample tests, rolling windows, and realistic transaction costs.

8. **Loss controls:** Obtain CIO clarification of the calendar-year loss measure, monitoring process, and required response to a breach before enforcing a numerical loss rule.

### Quantified Decision and Reversal Triggers

The following measurable conditions would prevent approval or trigger reconsideration of any subsequently authorized pilot:

| Measure | Trigger | Committee Response |
|---|---|---|
| Reserve-eligible assets | Below 3% | Escalate and restore compliance |
| Five-day redeemability | Below 90% | Suspend additional allocation pending review |
| Single nonexempt issuer | Above 8% | Require concentration remediation |
| Annual turnover | Above 25% without approval | Halt unapproved turnover |
| Classroom return comparison | Below 6.5% | Flag proxy failure; do not treat as a test of CPI + 4% |
| DGS10 data validity | Any unresolved look-ahead or availability issue | Keep signal quarantined |
| Calendar-year loss | Undefined until CIO approval | Do not assert compliance with an unapproved rule |

These are monitoring and escalation thresholds, not proof that the overall investment mandate has been met.

## 7. Monitoring and Implementation

If a pilot is eventually authorized, the Foundation should review portfolio weights, estimated risk, realized drawdowns, liquidity, issuer concentration, turnover, and costs monthly.

Any verified mandate breach should be escalated to the committee. The calendar-year loss process must be formally approved before implementation.

The portfolio should not be expanded merely because it passes a classroom expected-return threshold.

## 8. Final Conclusion

The Project 2 application provides a reproducible framework for comparing portfolios, evaluating simplified mandate constraints, reviewing historical evidence, and examining sensitivity to changed assumptions.

The Locked Changed-Input Experiment demonstrated that increasing transaction costs reduces expected net performance, confirming the pre-run prediction without changing the investment decision.

However, unresolved point-in-time data integrity, incomplete mandate verification, and insufficient forward-looking validation prevent a defensible allocation recommendation.

**Final committee decision: Maintain 0% pilot allocation and withhold authorization until the identified evidence requirements are satisfied.**