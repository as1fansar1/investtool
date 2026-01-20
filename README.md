# RRSP Stock Screener

An interactive tool to find investment candidates based on your criteria.

## Features

- **Market Selection**: Screen US stocks (S&P 500), Canadian stocks (TSX 60+), or both
- **Investing Styles**: Growth, Value, Dividend, or Blend strategies
- **Sector Filtering**: Focus on specific sectors or screen across all
- **Risk Tolerance**: Filter by market cap (large, mid, small cap)
- **Analyst Data**: Filter by coverage and ratings
- **Smart Ranking**: Composite scoring based on your selected style

## Quick Start

### 1. Install Dependencies

```bash
cd jan20_investing
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. **Configure filters** in the sidebar:
   - Select markets (US/Canadian/Both)
   - Choose your investing style
   - Pick sectors to include
   - Set risk tolerance
   - Adjust minimum analyst coverage and upside thresholds

2. **Click "Find Candidates"** to run the screener

3. **Review results**:
   - Summary metrics at the top
   - Ranked table of candidates
   - Expandable details for each stock
   - Download results as CSV

## Scoring System

Each stock gets a composite score (0-100) based on:

| Factor | Growth | Value | Dividend | Blend |
|--------|--------|-------|----------|-------|
| Upside to Target | 25% | 40% | 15% | 25% |
| Analyst Rating | 20% | 20% | 15% | 20% |
| Revenue Growth | 35% | 5% | 5% | 15% |
| Earnings Growth | 15% | 5% | 5% | 10% |
| Dividend Yield | 0% | 10% | 40% | 15% |
| Value (P/E) | 5% | 20% | 20% | 15% |

## Data Sources

- **Stock Data**: Yahoo Finance via `yfinance` (free, no API key required)
- **Coverage**: ~300 S&P 500 stocks + ~70 TSX stocks + Canadian ETFs

## Limitations

- Data may be delayed 15-20 minutes during market hours
- Analyst ratings update less frequently
- Some smaller stocks may have limited coverage
- ETFs don't have analyst ratings

## Disclaimer

This tool is for informational purposes only and is not financial advice. Always do your own research before making investment decisions.
