# GitHub upload checklist and cold-run verification

## Upload layout

Create/use a **separate GitHub repository for FIN 43900 Project 2**. Upload the
contents of this local `FIN43900_Project2` folder directly to that repository's
root. Do not upload the enclosing `classrepo/TICKER-research/FIN43900_Project2`
path as a nested directory.

The root of the fresh clone must look like this:

```text
.
├── .gitignore
├── README.md
├── app.py
├── portfolio_model.py
├── requirements.txt
├── submission-manifest.md
├── data/
│   ├── DGS10-data-card.md
│   ├── ETF-data-card.md
│   ├── dgs10_observations.csv
│   └── etf_monthly_prices.csv
├── docs/
│   ├── decision-memo.md
│   ├── github-cold-run.md
│   ├── validation-and-ai-use.md
│   └── video-script.md
├── evidence/
│   └── README.md
└── tests/
    ├── test_data_integrity.py
    └── test_portfolio_model.py
```

Upload exactly those files and folders. Do **not** upload `.venv/`,
`__pycache__/`, personal environment files, or any prediction/result file that
the student has not personally created. The two CSVs and documentation are
non-private project inputs; `etf_monthly_prices.csv` is byte-for-byte the
existing Lab 15 `prices.csv`.

The current configured GitHub remote is the broader `TICKER-research` course
repository. It does not contain a `FIN43900_Project2/` directory, and its root
`app.py` belongs to Project 1. Do not upload this project's root files over
that repository root; that would collide with existing coursework. Instead,
make a separate Project 2 repository and put the files above at its root.

## Verify after GitHub upload

1. On GitHub, open the Project 2 repository and confirm the root contains
   `app.py`, `requirements.txt`, `data/`, `docs/`, `evidence/`, and `tests/`.
2. Clone that repository into a new directory and open the clone root in VS Code.
3. In the VS Code terminal, run the README commands exactly from that root:

   ```bash
   python3 -m pip install -r requirements.txt
   python3 -m streamlit run app.py
   ```

4. Open the local Streamlit URL printed in the terminal. Confirm the Historical
   data and Point-in-time signal tabs load. DGS10 should say **quarantined**.
5. Stop Streamlit with **Control+C**, then run:

   ```bash
   python3 -m unittest discover -s tests -v
   ```

6. Confirm the tests pass and inspect Git status. No prediction or
   changed-input result should appear unless the student has later completed
   that workflow.

This checklist is a procedure, not a claim that a GitHub upload or a fresh
clone was performed.
