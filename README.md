# Nifty500-close-prices
This script will fetch Nifty 500 close prices and the main purpose of closing price is explain in details below,

![Nifty 500 Volatility Breadth](images/Percentage%20Stocks%20with%20Short-Term%20Volatility%20Expansion.png)


📊 NIFTY 500 VOLATILITY BREADTH FRAMEWORK
Weekly Data Pipeline for Market Regime Analysis
1. Project Overview (Why This Exists)

The primary purpose of this project is to build a reliable, automated data foundation for computing and tracking the following key market breadth indicator:

% of Nifty 500 stocks with Short-Term Volatility Expansion
(20-Day Volatility > 60-Day Volatility)

This indicator is used to understand market volatility regimes, not to generate trade signals.

The entire Python + GitHub automation exists only to support this volatility breadth analysis.

2. Core Indicator: Volatility Breadth (Primary Purpose)
Definition

For each stock in the Nifty 500 universe:

Compute 20-day rolling volatility

Compute 60-day rolling volatility

Check condition:

20D Volatility > 60D Volatility


Then calculate:

Percentage of Nifty 500 stocks where short-term volatility is expanding

This percentage is plotted as a time-series chart.

3. Why This Volatility Breadth Matters

This indicator helps identify market regimes:

High % values

Broad volatility expansion

Emotion-driven / FOMO markets

Higher probability of false breakouts

Low & contracting values

Volatility compression

Healthier risk-reward

Better environment for structured participation

As guided by the mentor:

Volatility expansion phases require patience

FOMO moves are natural

Action should be taken only after:

Volatility settles

Structure improves (HH–HL on lower timeframe)

This chart acts as a decision filter, not a timing tool.

4. Logical Flow of the Framework
Daily Closing Prices (Nifty 500, 1 Year)
        ↓
Rolling Volatility Calculation
(20D and 60D per stock)
        ↓
Stock-level Condition Check
(20D > 60D ?)
        ↓
Cross-sectional Aggregation
(% of stocks satisfying condition)
        ↓
Volatility Breadth Time-Series Chart


This repository focuses only on the first and most critical step:

Generating clean, versioned closing price data

All further calculations depend on this foundation.

5. Data Strategy

Universe: Nifty 500 stocks

Symbol source: Fixed CSV (nifty500_symbols.csv)

Price source: Yahoo Finance (yfinance)

Frequency: Daily (trading days)

Lookback: Last 1 year (~250 sessions)

Using a fixed symbol file ensures:

No NSE API dependency

No random failures

Reproducible results

6. Automation Philosophy

The system is designed to be:

Fully automated

Emotion-free

Repeatable

Independent of local machines

Why weekly data?

Market regime changes are slow

Daily noise is unnecessary

Weekly snapshots provide clarity

7. Schedule (Important)

Runs every Friday at 6:00 PM IST

Captures weekly closing state

Suitable for weekend analysis

Technical detail:

GitHub Actions uses UTC

6:00 PM IST = 12:30 UTC

Cron:

30 12 * * 5


Manual runs are always possible.

8. Repository Structure
Nifty500-close-prices/
│
├── data/
│   └── nifty500/
│       ├── nifty500_close_prices_1y_YYYY-MM-DD.xlsx
│       └── ...
│
├── images/
│   └── nifty500_volatility_breadth.png
│
├── nifty500_symbols.csv
├── generate_close_prices.py
├── .github/workflows/run.yml
└── README.md

9. Data Storage & Versioning

Each run creates a date-stamped Excel file

Files are stored under:

data/nifty500/


Old files are automatically cleaned

Only the latest N snapshots are retained

This allows:

Historical regime comparison

Easy rollback

Controlled repository size

10. What This Project Does NOT Do

❌ No trade signals

❌ No intraday timing

❌ No discretionary bias

❌ No chart plotting inside automation

This is a data foundation, not an execution system.

11. Secondary Uses (Extensions)

While volatility breadth is the primary use, the same dataset can later be reused for:

Momentum breadth

% stocks above/below moving averages

Drawdown studies

Relative strength analysis

Custom dashboards

These are extensions, not the core objective.

12. Verification Checklist

Manual run → GitHub Actions → ✅ Green

Scheduled run → Appears automatically on Friday

Output file:

~250 rows (trading days)

~480–500 columns (stocks)

New dated file appears under:

data/nifty500/

13. Key Takeaway

This project exists because of volatility breadth.

Everything else — automation, GitHub, Python — is simply infrastructure to support disciplined market understanding.

Volatility tells you when not to act.
Breadth tells you whether the environment is healthy.
