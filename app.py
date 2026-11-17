from __future__ import annotations

from datetime import date, time
import json
from pathlib import Path

import pandas as pd
import streamlit as st

from portfolio_model import (
    ASSETS,
    PORTFOLIOS,
    TRAINING_CORRELATIONS,
    TRAINING_RETURNS,
    TRAINING_VOLATILITIES,
    eligible_dgs10_observation,
    historical_metrics,
    historical_portfolio_metrics,
    load_price_data,
    locked_experiment_ready,
    mandate_checks,
    portfolio_metrics,
    portfolio_verdict,
    run_changed_input_test,
    transaction_cost_drag,
)


ROOT = Path(__file__).resolve().parent
PRICE_PATH = ROOT / "data" / "etf_monthly_prices.csv"
DGS10_PATH = ROOT / "data" / "dgs10_observations.csv"
PREDICTION_PATH = ROOT / "evidence" / "changed_input_prediction.md"
EXPERIMENT_RESULTS_PATH = ROOT / "evidence" / "changed_input_results.json"

st.set_page_config(
    page_title="Meridian Foundation | Investment Management",
    layout="wide",
)

st.title("Meridian Foundation — Investment Management")
st.caption(
    "FIN 43900 Project 2 · Decision support with explicit evidence and mandate gates"
)
st.warning(
    "**Education only — not investment advice.** Prior reported lab outputs and "
    "course assumptions are not independently validated forecasts or a trading recommendation."
)
st.error(
    "**PILOT STATUS: NOT AUTHORIZED.** The current evidence does not establish "
    "point-in-time signal validity, full mandate compliance, or a supported forward return."
)

with st.expander("Mandate, objective, benchmark, and asset universe", expanded=True):
    st.markdown(
        """
        - **Client and horizon:** Meridian Foundation; seven-year investment horizon
          with annual rebalancing, as recorded in Lab 13.
        - **Primary objective:** CPI + 4% annually, net of costs, over rolling
          five-year periods. The actual CPI + 4% objective is **not testable here**:
          no CPI series or validated forward return estimates are supplied.
        - **Classroom comparison proxy:** 6.5% expected return from Lab 14. It is
          displayed separately and must not be presented as the CPI + 4% objective.
        - **Benchmark:** 60% global equity / 40% U.S. investment-grade bonds;
          represented here as 60% VT / 40% LQD for transparent comparison only.
        - **Universe:** BIL (Treasury bills), IEF (7–10 year Treasury exposure),
          LQD (investment-grade corporate bonds), and VT (global equities).
        - **Risk measures:** model expected return and volatility from Lab 14
          training assumptions; historical annualized return, volatility, and
          maximum drawdown from the supplied Lab 15 monthly price file.
        - **Constraints:** long-only/no leverage; at least 3% reserve-eligible
          assets; at least 90% redeemable within five business days; 8% single
          nonexempt-company cap; 25% annual turnover absent approval; and the
          seven-year horizon. Lab 13 marks the calendar-year loss requirement as
          unresolved pending CIO definition.
        """
    )

st.info(
    "The 6.5% proxy and risk assumptions below are from Lab 14's classroom asset "
    "assumptions, not ETF forecasts. The fund-level liquidity, issuer look-through, "
    "turnover, and actual CPI + 4% tests remain unverified."
)

tabs = st.tabs(
    [
        "Portfolios",
        "Historical data",
        "Point-in-time signal",
        "Stress tests",
        "Locked experiment",
        "Committee view",
    ]
)


def percent(value: float) -> str:
    return f"{value:.2%}"


def portfolio_summary() -> tuple[pd.DataFrame, dict[str, list[dict[str, str]]]]:
    rows: list[dict[str, str | float]] = []
    checks_by_name: dict[str, list[dict[str, str]]] = {}
    for name, weights in PORTFOLIOS.items():
        metrics = portfolio_metrics(weights)
        checks = mandate_checks(weights, expected_return=metrics["expected_return"])
        checks_by_name[name] = checks
        rows.append(
            {
                "Portfolio": name,
                **{
                    ticker: f"{weight:.0%}"
                    for ticker, weight in zip(ASSETS, weights)
                },
                "Expected return*": percent(metrics["expected_return"]),
                "Volatility*": percent(metrics["volatility"]),
                "Reserve eligible": percent(metrics["reserve_share"]),
                "Mandate verdict": portfolio_verdict(checks),
            }
        )
    return pd.DataFrame(rows), checks_by_name


with tabs[0]:
    st.subheader("Transparent portfolio comparison")
    st.caption(
        "*Expected return and volatility use Lab 14 training assumptions. The "
        "constrained candidate is a transparent allocation proposal, not an optimizer "
        "output or a validated recommendation."
    )
    summary, checks_by_name = portfolio_summary()
    st.dataframe(summary, hide_index=True, width="stretch")
    for name, checks in checks_by_name.items():
        with st.expander(f"{name}: requirement-by-requirement results"):
            st.dataframe(pd.DataFrame(checks), hide_index=True, width="stretch")
    weights = pd.DataFrame(
        [
            {"Portfolio": name, **dict(zip(ASSETS, values))}
            for name, values in PORTFOLIOS.items()
        ]
    ).set_index("Portfolio")
    st.bar_chart(weights)
    st.warning(
        "A model PASS is not a full mandate approval. Liquidity settlement, ETF "
        "look-through issuer exposure, turnover, and CPI + 4% are not established "
        "by the supplied evidence; all portfolios therefore remain uncleared."
    )

with tabs[1]:
    st.subheader("Historical ETF evidence")
    st.markdown(
        "The local file is an unchanged copy of the Lab 15 `prices.csv`. Its Lab 15 "
        "report attributes the data to Yahoo Finance, downloaded October 22, 2026; "
        "retrieval parameters and adjustment methodology were not supplied."
    )
    prices = load_price_data(PRICE_PATH)
    st.caption(
        f"{len(prices)} monthly prices · {prices.index.min():%Y-%m-%d} to "
        f"{prices.index.max():%Y-%m-%d} · no external data request is made."
    )
    st.line_chart(prices)
    window_choice = st.radio(
        "Descriptive estimation window",
        ("Full supplied sample", "Most recent 36 monthly returns"),
        horizontal=True,
    )
    window = 36 if window_choice.startswith("Most recent") else None
    history = historical_metrics(prices, window_months=window)
    stats_rows = []
    for ticker in ASSETS:
        stats_rows.append(
            {
                "ETF": ticker,
                "Annualized arithmetic return": percent(
                    float(history["annual_returns"][ticker])
                ),
                "Annualized volatility": percent(
                    float(history["annual_volatility"][ticker])
                ),
            }
        )
    st.dataframe(pd.DataFrame(stats_rows), hide_index=True, width="stretch")
    historical_rows = []
    for name, portfolio_weights in PORTFOLIOS.items():
        metrics = historical_portfolio_metrics(portfolio_weights, history)
        historical_rows.append(
            {
                "Portfolio": name,
                "Annualized historical return": percent(
                    metrics["annualized_arithmetic_return"]
                ),
                "Annualized historical volatility": percent(
                    metrics["annualized_volatility"]
                ),
                "Historical max drawdown": percent(metrics["max_drawdown"]),
            }
        )
    st.dataframe(
        pd.DataFrame(historical_rows), hide_index=True, width="stretch"
    )
    st.caption(
        "These are in-sample, arithmetic annualizations from monthly returns. "
        "Maximum drawdown is a historical peak-to-trough statistic, not a loss limit "
        "or a forecast. See `data/ETF-data-card.md` for provenance limits."
    )

with tabs[2]:
    st.subheader("DGS10 — quarantined")
    st.error(
        "The point-in-time rate input remains quarantined. No investment signal or "
        "portfolio weight is generated from DGS10."
    )
    dgs10 = pd.read_csv(DGS10_PATH)
    decision_day = st.date_input(
        "Hypothetical decision date",
        value=date(2026, 11, 3),
        key="dgs_decision_date",
    )
    decision_clock = st.time_input(
        "Decision time (Eastern Time)",
        value=time(16, 30),
        key="dgs_decision_time",
    )
    observation = eligible_dgs10_observation(
        dgs10,
        pd.Timestamp(decision_day),
        decision_clock.strftime("%H:%M"),
    )
    st.caption(
        "Release control: same-day DGS10 is excluded before 4:15 p.m. ET, the "
        "H.15 publication time reported in Lab 17. This illustration does not model "
        "holidays, complete ALFRED vintages, or a trading/execution lag."
    )
    if observation is None:
        st.info("No checked point-in-time observation is eligible for this selection.")
    else:
        st.metric(
            "Latest checked observation available in this sparse file",
            f"{float(observation['value']):.2f}%",
            help=(
                f"Observation {observation['observation_date']} · "
                f"vintage {observation['vintage_date']}"
            ),
        )
    st.dataframe(dgs10, hide_index=True, width="stretch")
    st.warning(
        "The table has only three checked vintage observations and one current-FRED "
        "row excluded from point-in-time selection. A complete daily vintage history "
        "and decision/execution-time validation are still required."
    )
    with st.expander("Open the DGS10 data card"):
        st.markdown((ROOT / "data" / "DGS10-data-card.md").read_text(encoding="utf-8"))

with tabs[3]:
    st.subheader("Assumption, rolling-window, cost, constraint, and stop tests")
    st.caption(
        "Interactive scenarios are recalculations, not reported experiment results. "
        "The locked changed-input experiment is separate and remains gated."
    )
    selected_name = st.selectbox("Portfolio for stress display", list(PORTFOLIOS))
    selected_weights = PORTFOLIOS[selected_name]
    c1, c2, c3 = st.columns(3)
    with c1:
        return_shock_pp = st.slider(
            "VT expected-return shock (percentage points)",
            min_value=-3.0,
            max_value=3.0,
            value=0.0,
            step=0.5,
        )
        bond_equity_corr = st.slider(
            "LQD–VT correlation",
            min_value=-0.10,
            max_value=0.50,
            value=0.25,
            step=0.05,
        )
    with c2:
        transaction_cost_bps = st.number_input(
            "Transaction cost (basis points per traded dollar)",
            min_value=0.0,
            max_value=500.0,
            value=25.0,
            step=5.0,
        )
        assumed_turnover_pct = st.number_input(
            "Scenario annual turnover (%)",
            min_value=0.0,
            max_value=100.0,
            value=25.0,
            step=5.0,
        )
    with c3:
        scenario_liquidity_pct = st.number_input(
            "Scenario share redeemable within five days (%)",
            min_value=0.0,
            max_value=100.0,
            value=100.0,
            step=5.0,
            help="A user-entered scenario only; it is not fund-level evidence.",
        )
        scenario_largest_issuer_pct = st.number_input(
            "Scenario largest nonexempt issuer exposure (%)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=1.0,
            help="A user-entered scenario only; ETF look-through data were not supplied.",
        )

    stressed_returns = TRAINING_RETURNS.copy()
    stressed_returns[3] += return_shock_pp / 100
    stressed_correlations = TRAINING_CORRELATIONS.copy()
    stressed_correlations[2, 3] = stressed_correlations[3, 2] = bond_equity_corr
    try:
        stressed_metrics = portfolio_metrics(
            selected_weights,
            returns=stressed_returns,
            correlations=stressed_correlations,
        )
        cost_drag = transaction_cost_drag(
            assumed_turnover_pct / 100, transaction_cost_bps
        )
        st.write(
            {
                "Scenario expected return before costs": percent(
                    stressed_metrics["expected_return"]
                ),
                "Scenario volatility": percent(stressed_metrics["volatility"]),
                "Scenario return after entered transaction-cost drag": percent(
                    stressed_metrics["expected_return"] - cost_drag
                ),
                "Transaction-cost drag": percent(cost_drag),
            }
        )
        stress_checks = mandate_checks(
            selected_weights,
            expected_return=stressed_metrics["expected_return"] - cost_drag,
            redeemable_share=scenario_liquidity_pct / 100,
            largest_company_share=scenario_largest_issuer_pct / 100,
            annual_turnover=assumed_turnover_pct / 100,
        )
        st.dataframe(
            pd.DataFrame(stress_checks), hide_index=True, width="stretch"
        )
    except ValueError as exc:
        st.error(f"Stress scenario is invalid: {exc}")

    st.markdown("**Stopping conditions to resolve before any live pilot**")
    st.markdown(
        """
        - Stop/review if any verified hard mandate rule fails: reserve below 3%,
          five-day liquidity below 90%, issuer exposure above 8%, or annual turnover
          above 25% without approval.
        - Stop if portfolio weights are invalid, a risk calculation fails validation,
          or any required input is missing or not point-in-time eligible.
        - Review if scenario return falls below the 6.5% Lab 14 proxy after entered
          costs. This is not a test of the actual CPI + 4% objective.
        - Do not automate a 10% calendar-year loss trigger until the CIO defines the
          measurement, monitoring frequency, and breach action.
        """
    )

with tabs[4]:
    st.subheader("AI-off, changed-input prediction — locked workflow")
    st.warning(
        "This test has not been run. Write your own prediction without AI, save it, "
        "commit that prediction to GitHub, then enter the matching commit details. "
        "The app cannot verify who authored the text or query GitHub; the checkbox "
        "is your attestation."
    )
    st.write(
        "The test changes the VT expected-return training assumption and compares "
        "the three model portfolio returns and volatilities. It does not change or "
        "validate market data."
    )
    changed_vt_return = st.slider(
        "Changed VT expected return (%)",
        min_value=3.0,
        max_value=12.0,
        value=7.0,
        step=0.5,
        key="locked_changed_vt_return",
    )
    prediction_text = st.text_area(
        "Your own pre-test prediction (write this yourself, without AI)",
        placeholder="Write the direction and expected magnitude you predict, and why.",
        height=150,
        key="locked_prediction_text",
    )
    if st.button("Save my prediction before testing"):
        if not prediction_text.strip():
            st.error("Enter your own prediction before saving.")
        else:
            PREDICTION_PATH.parent.mkdir(parents=True, exist_ok=True)
            document = (
                "# Changed-input prediction (AI-off; written by student)\n\n"
                f"Changed input: VT expected return = {changed_vt_return:.2f}%\n\n"
                "Prediction:\n"
                f"{prediction_text.strip()}\n"
            )
            PREDICTION_PATH.write_text(document, encoding="utf-8")
            st.success(
                "Saved. Do not run the test yet: commit this file to GitHub first."
            )

    prediction_document = (
        PREDICTION_PATH.read_text(encoding="utf-8")
        if PREDICTION_PATH.is_file()
        else ""
    )
    if prediction_document:
        st.caption(f"Saved prediction: {PREDICTION_PATH.relative_to(ROOT)}")
        st.code(prediction_document, language="markdown")
    sha_col, url_col = st.columns(2)
    with sha_col:
        commit_sha = st.text_input("GitHub commit SHA containing the prediction")
    with url_col:
        github_commit_url = st.text_input("Matching GitHub commit URL")
    personally_committed = st.checkbox(
        "I personally wrote this prediction without AI and committed this exact "
        "prediction to GitHub before running the test."
    )
    ready, gate_message = locked_experiment_ready(
        prediction_document,
        changed_vt_return,
        commit_sha,
        github_commit_url,
        personally_committed,
    )
    if EXPERIMENT_RESULTS_PATH.exists():
        st.info(
            "A changed-input result file already exists. This workflow is locked "
            "to one run; do not overwrite or rerun it."
        )
        ready = False
    elif ready:
        st.success(gate_message)
    else:
        st.info(gate_message)

    if st.button("Run locked changed-input test", disabled=not ready):
        result = run_changed_input_test(changed_vt_return)
        EXPERIMENT_RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        result_document = {
            "changed_vt_expected_return_percent": changed_vt_return,
            "prediction_file": str(PREDICTION_PATH.relative_to(ROOT)),
            "github_commit_sha": commit_sha,
            "github_commit_url": github_commit_url,
            "results": result,
        }
        EXPERIMENT_RESULTS_PATH.write_text(
            json.dumps(result_document, indent=2) + "\n", encoding="utf-8"
        )
        st.success("The committed-prediction gate passed; the test has now run.")
        st.json(result_document)
    if EXPERIMENT_RESULTS_PATH.is_file():
        st.subheader("Previously saved changed-input test result")
        st.json(json.loads(EXPERIMENT_RESULTS_PATH.read_text(encoding="utf-8")))
    st.caption(
        "No prediction, commit, or experiment result has been supplied or generated "
        "by this setup. Do not commit generated local results unless they are part "
        "of your own submission."
    )

with tabs[5]:
    st.subheader("Committee view")
    st.error("Recommendation now: NO PILOT AUTHORIZATION — evidence is insufficient.")
    st.markdown(
        """
        A **conditional 5%–10% pilot sleeve** may be brought back to the committee
        only after the open evidence gates below are met. This range is a proposed
        decision parameter, not an allocation recommendation or a supported
        portfolio weight.

        **Required before reconsideration**

        1. Confirm the mandate's actual CPI + 4% objective and cost measurement.
        2. Verify point-in-time DGS10 vintages and decision/execution availability;
           keep the signal quarantined until that is complete.
        3. Supply current ETF liquidity/settlement evidence, look-through issuer
           exposures, starting holdings, and a turnover definition.
        4. Independently validate the price history, assumptions, out-of-sample
           results, rolling windows, transaction costs, and stop rules.
        5. Obtain the CIO's definition and response process for the calendar-year
           loss statement.

        **Monitoring proposal if the committee later authorizes a pilot**

        - Review monthly weights, realized volatility, drawdown, costs, and
          benchmark-relative results; rebalance only under the approved schedule.
        - Escalate immediately on a verified breach of the 3% reserve, 90%
          five-day-liquidity, 8% issuer, or 25% turnover limits.
        - Use the 10% loss statement only after the CIO defines it; until then it is
          an unresolved review item, not an automated stop threshold.
        - Re-evaluate the thesis at each committee review and stop expansion if
          data integrity, point-in-time availability, or mandate compliance cannot
          be demonstrated.
        """
    )
