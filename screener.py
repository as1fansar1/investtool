"""
Stock Screener Module
Fetches stock data from yfinance and applies screening criteria.
"""

import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Optional
import warnings

warnings.filterwarnings('ignore')


def fetch_single_stock(ticker: str) -> Optional[Dict]:
    """Fetch data for a single stock."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Skip if no valid data
        if not info or 'regularMarketPrice' not in info:
            return None
        
        # Extract key metrics
        data = {
            'ticker': ticker,
            'name': info.get('shortName', info.get('longName', ticker)),
            'price': info.get('regularMarketPrice', info.get('currentPrice', 0)),
            'target_price': info.get('targetMeanPrice', None),
            'market_cap': info.get('marketCap', 0),
            'pe_ratio': info.get('forwardPE', info.get('trailingPE', None)),
            'dividend_yield': info.get('dividendYield', 0) or 0,
            'payout_ratio': info.get('payoutRatio', None),
            'revenue_growth': info.get('revenueGrowth', None),
            'earnings_growth': info.get('earningsGrowth', None),
            'recommendation': info.get('recommendationKey', 'none'),
            'recommendation_mean': info.get('recommendationMean', None),  # 1=Strong Buy, 5=Sell
            'num_analysts': info.get('numberOfAnalystOpinions', 0),
            'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 0),
            'fifty_two_week_low': info.get('fiftyTwoWeekLow', 0),
            'fifty_day_avg': info.get('fiftyDayAverage', 0),
            'two_hundred_day_avg': info.get('twoHundredDayAverage', 0),
            'sector': info.get('sector', 'Unknown'),
            'industry': info.get('industry', 'Unknown'),
        }
        
        # Calculate derived metrics
        if data['price'] and data['target_price']:
            data['upside_pct'] = ((data['target_price'] - data['price']) / data['price']) * 100
        else:
            data['upside_pct'] = None
            
        if data['price'] and data['fifty_two_week_high']:
            data['pct_from_high'] = ((data['price'] - data['fifty_two_week_high']) / data['fifty_two_week_high']) * 100
        else:
            data['pct_from_high'] = None
            
        return data
        
    except Exception as e:
        return None


def fetch_stock_data(tickers: List[str], max_workers: int = 10) -> pd.DataFrame:
    """
    Fetch stock data for multiple tickers in parallel.
    
    Args:
        tickers: List of stock tickers
        max_workers: Number of parallel threads
        
    Returns:
        DataFrame with stock data
    """
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_ticker = {executor.submit(fetch_single_stock, ticker): ticker for ticker in tickers}
        
        for future in as_completed(future_to_ticker):
            result = future.result()
            if result:
                results.append(result)
    
    if not results:
        return pd.DataFrame()
    
    return pd.DataFrame(results)


def apply_filters(df: pd.DataFrame, criteria: Dict) -> pd.DataFrame:
    """
    Apply user-selected filters to the stock data.
    
    Args:
        df: DataFrame with stock data
        criteria: Dictionary with filter criteria
        
    Returns:
        Filtered DataFrame
    """
    if df.empty:
        return df
    
    filtered = df.copy()
    
    # Sector filter
    if criteria.get('sectors') and len(criteria['sectors']) > 0:
        filtered = filtered[filtered['sector'].isin(criteria['sectors'])]
    
    # Market cap filter (risk tolerance)
    if criteria.get('min_market_cap'):
        filtered = filtered[filtered['market_cap'] >= criteria['min_market_cap']]
    if criteria.get('max_market_cap'):
        filtered = filtered[filtered['market_cap'] <= criteria['max_market_cap']]
    
    # Minimum analyst coverage
    if criteria.get('min_analysts', 0) > 0:
        filtered = filtered[filtered['num_analysts'] >= criteria['min_analysts']]
    
    # Minimum upside
    if criteria.get('min_upside'):
        filtered = filtered[filtered['upside_pct'].notna() & (filtered['upside_pct'] >= criteria['min_upside'])]
    
    # Only buy/strong buy ratings
    if criteria.get('buy_ratings_only'):
        buy_ratings = ['buy', 'strong_buy', 'strongBuy', 'outperform']
        filtered = filtered[filtered['recommendation'].str.lower().isin(buy_ratings)]
    
    return filtered


def calculate_score(stock: pd.Series, style: str) -> float:
    """
    Calculate a composite score for a stock based on investing style.
    
    Args:
        stock: Series with stock data
        style: One of 'growth', 'value', 'dividend', 'blend'
        
    Returns:
        Composite score (higher is better)
    """
    score = 0.0
    
    # Define weights based on style
    weights = {
        'growth': {
            'upside': 0.25,
            'analyst': 0.20,
            'revenue_growth': 0.35,
            'earnings_growth': 0.15,
            'dividend': 0.0,
            'value': 0.05,
        },
        'value': {
            'upside': 0.40,
            'analyst': 0.20,
            'revenue_growth': 0.05,
            'earnings_growth': 0.05,
            'dividend': 0.10,
            'value': 0.20,
        },
        'dividend': {
            'upside': 0.15,
            'analyst': 0.15,
            'revenue_growth': 0.05,
            'earnings_growth': 0.05,
            'dividend': 0.40,
            'value': 0.20,
        },
        'blend': {
            'upside': 0.25,
            'analyst': 0.20,
            'revenue_growth': 0.15,
            'earnings_growth': 0.10,
            'dividend': 0.15,
            'value': 0.15,
        },
    }
    
    w = weights.get(style.lower(), weights['blend'])
    
    # Upside score (0-100 scale, capped at 50% upside)
    if stock.get('upside_pct') is not None:
        upside_score = min(stock['upside_pct'] * 2, 100)  # 50% upside = 100 score
        upside_score = max(upside_score, 0)  # No negative scores
        score += w['upside'] * upside_score
    
    # Analyst score (recommendation_mean: 1=Strong Buy, 5=Sell)
    if stock.get('recommendation_mean') is not None:
        analyst_score = (5 - stock['recommendation_mean']) * 25  # Convert to 0-100
        analyst_score = max(min(analyst_score, 100), 0)
        score += w['analyst'] * analyst_score
    
    # Revenue growth score
    if stock.get('revenue_growth') is not None:
        rev_score = min(stock['revenue_growth'] * 200, 100)  # 50% growth = 100
        rev_score = max(rev_score, 0)
        score += w['revenue_growth'] * rev_score
    
    # Earnings growth score
    if stock.get('earnings_growth') is not None:
        earn_score = min(stock['earnings_growth'] * 200, 100)
        earn_score = max(earn_score, 0)
        score += w['earnings_growth'] * earn_score
    
    # Dividend score
    if stock.get('dividend_yield') is not None:
        div_score = min(stock['dividend_yield'] * 100 * 20, 100)  # 5% yield = 100
        score += w['dividend'] * div_score
    
    # Value score (inverse of P/E, normalized)
    if stock.get('pe_ratio') is not None and stock['pe_ratio'] > 0:
        # Lower P/E = higher score, P/E of 10 = 100, P/E of 50 = 20
        value_score = min(1000 / stock['pe_ratio'], 100)
        score += w['value'] * value_score
    
    return round(score, 2)


def rank_candidates(df: pd.DataFrame, style: str, top_n: int = 20) -> pd.DataFrame:
    """
    Rank stocks by composite score and return top candidates.
    
    Args:
        df: Filtered DataFrame
        style: Investing style
        top_n: Number of candidates to return
        
    Returns:
        Ranked DataFrame with top candidates
    """
    if df.empty:
        return df
    
    # Calculate scores
    df = df.copy()
    df['score'] = df.apply(lambda row: calculate_score(row, style), axis=1)
    
    # Sort by score descending
    df = df.sort_values('score', ascending=False)
    
    # Return top N
    return df.head(top_n)


def get_signal(row: pd.Series) -> str:
    """Generate a simple buy/hold signal based on metrics."""
    signals = []
    
    # Upside signal
    if row.get('upside_pct') is not None:
        if row['upside_pct'] >= 20:
            signals.append("🚀 Strong Upside")
        elif row['upside_pct'] >= 10:
            signals.append("✅ Undervalued")
        elif row['upside_pct'] <= -10:
            signals.append("⚠️ Overvalued")
    
    # Analyst signal
    rec = row.get('recommendation', '').lower()
    if rec in ['strong_buy', 'strongbuy']:
        signals.append("💪 Strong Buy")
    elif rec == 'buy':
        signals.append("👍 Buy")
    elif rec == 'sell':
        signals.append("👎 Sell")
    
    # Near 52-week low (contrarian opportunity)
    if row.get('pct_from_high') is not None and row['pct_from_high'] <= -30:
        signals.append("📉 Near 52w Low")
    
    return " | ".join(signals) if signals else "—"


def format_market_cap(value: float) -> str:
    """Format market cap in billions/millions."""
    if value >= 1e12:
        return f"${value/1e12:.1f}T"
    elif value >= 1e9:
        return f"${value/1e9:.1f}B"
    elif value >= 1e6:
        return f"${value/1e6:.0f}M"
    else:
        return f"${value:,.0f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a decimal as percentage string."""
    if value is None:
        return "—"
    return f"{value*100:.{decimals}f}%" if abs(value) < 10 else f"{value:.{decimals}f}%"
