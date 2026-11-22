# DGS10 point-in-time data card

**AI-use disclosure:** AI assisted in organizing this project and drafting its code and documentation. The data below were transcribed from the existing Lab 17 card; no observations were invented or fetched for this project.  
**Education-only disclosure:** This application is for educational purposes only and is not investment advice.

**Source series:** DGS10, Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, percent, not seasonally adjusted.  
**FRED download date in Lab 17:** November 3, 2026.  
**Point-in-time vintage cited in Lab 17:** ALFRED vintage dated October 5, 2026.  
**Release-time control:** H.15 schedule is stated in Lab 17 as 4:15 p.m. Eastern Time on business days, subject to holidays and Board closures.

`dgs10_observations.csv` contains only the four observations present in the Lab 17 data card. The three September 30–October 2 observations have the October 5 vintage and were reported unchanged in the November 3 comparison. The October 30 value is a current-FRED observation only and is deliberately marked not point-in-time checked; the app excludes it from point-in-time selection.

This is a sparse spot-check, not a daily history or complete vintage archive. The app always labels the series quarantined and does not create an allocation signal. A date/time selection only demonstrates the 4:15 p.m. release rule over the checked rows; it does not validate a complete backtest.

Sources cited by Lab 17:

- [FRED DGS10 series page](https://fred.stlouisfed.org/series/DGS10)
- [FRED current CSV](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)
- [ALFRED October 5, 2026 vintage CSV](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=DGS10&vintage_date=2026-10-05)
- [Federal Reserve H.15 release schedule](https://www.federalreserve.gov/releases/h15/)
