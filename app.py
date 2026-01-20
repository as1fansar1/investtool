"""
RRSP Stock Screener
An interactive tool to find investment candidates based on your criteria.
"""

import streamlit as st
import pandas as pd
from screener import (
    fetch_stock_data,
    apply_filters,
    rank_candidates,
    get_signal,
    format_market_cap,
)
from data.sp500 import SP500_TICKERS, SECTOR_MAP
from data.tsx60 import TSX_TICKERS, TSX_SECTOR_MAP

# Page configuration
st.set_page_config(
    page_title="RRSP Stock Screener",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f0f1a 100%);
    }
    .signal-positive {
        color: #10b981;
        font-weight: 600;
    }
    .signal-negative {
        color: #ef4444;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">📈 RRSP Stock Screener</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Find investment candidates based on your criteria</p>', unsafe_allow_html=True)

# Sidebar with filters
with st.sidebar:
    st.markdown("## 🎯 Screening Criteria")
    st.markdown("---")
    
    # Market Selection
    st.markdown("### 🌍 Markets")
    market = st.radio(
        "Select markets to screen:",
        options=["Both US & Canadian", "US Stocks Only", "Canadian (TSX) Only"],
        index=0,
        help="Choose which markets to include in your search"
    )
    
    st.markdown("---")
    
    # Investing Style
    st.markdown("### 💼 Investing Style")
    style = st.selectbox(
        "What's your investment approach?",
        options=["Blend", "Growth", "Value", "Dividend"],
        index=0,
        help="""
        • Growth: Focus on revenue/earnings growth
        • Value: Focus on undervalued stocks (low P/E, high upside)
        • Dividend: Focus on yield and payout sustainability
        • Blend: Balanced approach
        """
    )
    
    st.markdown("---")
    
    # Sector Filter
    st.markdown("### 🏢 Sectors")
    all_sectors = [
        "Technology",
        "Healthcare", 
        "Financials",
        "Consumer Discretionary",
        "Consumer Staples",
        "Energy",
        "Industrials",
        "Materials",
        "Real Estate",
        "Utilities",
        "Communication Services",
    ]
    
    select_all_sectors = st.checkbox("Select All Sectors", value=True)
    
    if select_all_sectors:
        sectors = all_sectors
    else:
        sectors = st.multiselect(
            "Select sectors to include:",
            options=all_sectors,
            default=["Technology", "Healthcare", "Financials"],
            help="Filter stocks by sector"
        )
    
    st.markdown("---")
    
    # Risk Tolerance
    st.markdown("### ⚖️ Risk Tolerance")
    risk = st.select_slider(
        "Market cap preference:",
        options=["Large Cap Only", "Include Mid Cap", "Include Small Cap"],
        value="Include Mid Cap",
        help="""
        • Large Cap: >$10B market cap (safer, more stable)
        • Mid Cap: $2B-$10B market cap
        • Small Cap: <$2B market cap (higher risk/reward)
        """
    )
    
    st.markdown("---")
    
    # Additional Filters
    st.markdown("### 🔧 Additional Filters")
    
    min_analysts = st.slider(
        "Minimum analyst coverage",
        min_value=0,
        max_value=20,
        value=5,
        help="Only show stocks covered by at least this many analysts"
    )
    
    min_upside = st.slider(
        "Minimum upside to target (%)",
        min_value=-10,
        max_value=50,
        value=10,
        help="Filter stocks with at least this much upside potential"
    )
    
    buy_only = st.checkbox(
        "Buy ratings only",
        value=False,
        help="Only show stocks with Buy or Strong Buy recommendations"
    )
    
    st.markdown("---")
    
    # Number of results
    top_n = st.slider(
        "Number of candidates",
        min_value=5,
        max_value=50,
        value=20,
        help="How many top candidates to show"
    )

# Main content area
col1, col2 = st.columns([3, 1])

with col2:
    screen_button = st.button(
        "🔍 Find Candidates",
        type="primary",
        use_container_width=True,
    )

# Build the screening criteria
criteria = {
    'sectors': sectors,
    'min_analysts': min_analysts,
    'min_upside': min_upside,
    'buy_ratings_only': buy_only,
}

# Set market cap filters based on risk tolerance
if risk == "Large Cap Only":
    criteria['min_market_cap'] = 10e9  # $10B
elif risk == "Include Mid Cap":
    criteria['min_market_cap'] = 2e9   # $2B
else:
    criteria['min_market_cap'] = 500e6  # $500M minimum for liquidity

# Get ticker list based on market selection
def get_tickers(market_selection: str) -> list:
    tickers = []
    if market_selection in ["Both US & Canadian", "US Stocks Only"]:
        tickers.extend(SP500_TICKERS)
    if market_selection in ["Both US & Canadian", "Canadian (TSX) Only"]:
        tickers.extend(TSX_TICKERS)
    return tickers

# Screen stocks when button is clicked
if screen_button:
    tickers = get_tickers(market)
    
    # Show progress
    progress_text = st.empty()
    progress_bar = st.progress(0)
    
    progress_text.text(f"📊 Fetching data for {len(tickers)} stocks...")
    
    # Fetch data
    with st.spinner("Fetching stock data... This may take 1-2 minutes."):
        df = fetch_stock_data(tickers)
    
    progress_bar.progress(50)
    progress_text.text("🔍 Applying filters...")
    
    if df.empty:
        st.error("❌ Could not fetch stock data. Please check your internet connection and try again.")
    else:
        # Apply filters
        filtered_df = apply_filters(df, criteria)
        
        progress_bar.progress(75)
        progress_text.text("📈 Ranking candidates...")
        
        if filtered_df.empty:
            st.warning("⚠️ No stocks match your criteria. Try relaxing some filters.")
        else:
            # Rank and get top candidates
            results = rank_candidates(filtered_df, style.lower(), top_n)
            
            progress_bar.progress(100)
            progress_text.empty()
            progress_bar.empty()
            
            # Display summary metrics
            st.markdown("---")
            st.markdown("### 📊 Screening Results")
            
            metric_cols = st.columns(4)
            with metric_cols[0]:
                st.metric("Stocks Screened", len(df))
            with metric_cols[1]:
                st.metric("Passed Filters", len(filtered_df))
            with metric_cols[2]:
                avg_upside = results['upside_pct'].mean()
                st.metric("Avg Upside", f"{avg_upside:.1f}%" if pd.notna(avg_upside) else "—")
            with metric_cols[3]:
                avg_score = results['score'].mean()
                st.metric("Avg Score", f"{avg_score:.1f}")
            
            st.markdown("---")
            st.markdown(f"### 🏆 Top {len(results)} Candidates ({style} Strategy)")
            
            # Add signal column
            results['signal'] = results.apply(get_signal, axis=1)
            
            # Format display DataFrame
            display_df = results[[
                'ticker', 'name', 'price', 'target_price', 'upside_pct',
                'recommendation', 'num_analysts', 'score', 'signal', 'market_cap', 'sector'
            ]].copy()
            
            # Rename columns for display
            display_df.columns = [
                'Ticker', 'Company', 'Price', 'Target', 'Upside %',
                'Rating', 'Analysts', 'Score', 'Signal', 'Market Cap', 'Sector'
            ]
            
            # Format columns
            display_df['Price'] = display_df['Price'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
            display_df['Target'] = display_df['Target'].apply(lambda x: f"${x:.2f}" if pd.notna(x) else "—")
            display_df['Upside %'] = display_df['Upside %'].apply(lambda x: f"{x:+.1f}%" if pd.notna(x) else "—")
            display_df['Market Cap'] = display_df['Market Cap'].apply(format_market_cap)
            display_df['Score'] = display_df['Score'].apply(lambda x: f"{x:.1f}")
            
            # Display as interactive table
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Ticker": st.column_config.TextColumn("Ticker", width="small"),
                    "Company": st.column_config.TextColumn("Company", width="medium"),
                    "Price": st.column_config.TextColumn("Price", width="small"),
                    "Target": st.column_config.TextColumn("Target", width="small"),
                    "Upside %": st.column_config.TextColumn("Upside %", width="small"),
                    "Rating": st.column_config.TextColumn("Rating", width="small"),
                    "Analysts": st.column_config.NumberColumn("Analysts", width="small"),
                    "Score": st.column_config.TextColumn("Score", width="small"),
                    "Signal": st.column_config.TextColumn("Signal", width="medium"),
                    "Market Cap": st.column_config.TextColumn("Mkt Cap", width="small"),
                    "Sector": st.column_config.TextColumn("Sector", width="medium"),
                }
            )
            
            # Expandable details for each stock
            st.markdown("---")
            st.markdown("### 📋 Detailed View")
            st.markdown("Click on a stock below to see more details:")
            
            for idx, row in results.head(10).iterrows():
                with st.expander(f"**{row['ticker']}** - {row['name']} (Score: {row['score']:.1f})"):
                    detail_cols = st.columns(3)
                    
                    with detail_cols[0]:
                        st.markdown("**Valuation**")
                        st.write(f"• Current Price: ${row['price']:.2f}")
                        if pd.notna(row['target_price']):
                            st.write(f"• Target Price: ${row['target_price']:.2f}")
                            st.write(f"• Upside: {row['upside_pct']:+.1f}%")
                        if pd.notna(row['pe_ratio']):
                            st.write(f"• P/E Ratio: {row['pe_ratio']:.1f}")
                    
                    with detail_cols[1]:
                        st.markdown("**Analyst Coverage**")
                        st.write(f"• Recommendation: {row['recommendation'].title()}")
                        st.write(f"• Number of Analysts: {row['num_analysts']}")
                        if pd.notna(row['recommendation_mean']):
                            st.write(f"• Rating Score: {row['recommendation_mean']:.1f}/5")
                    
                    with detail_cols[2]:
                        st.markdown("**Growth & Dividends**")
                        if pd.notna(row['revenue_growth']):
                            st.write(f"• Revenue Growth: {row['revenue_growth']*100:.1f}%")
                        if pd.notna(row['earnings_growth']):
                            st.write(f"• Earnings Growth: {row['earnings_growth']*100:.1f}%")
                        if row['dividend_yield'] > 0:
                            st.write(f"• Dividend Yield: {row['dividend_yield']*100:.2f}%")
            
            # Download option
            st.markdown("---")
            csv = results.to_csv(index=False)
            st.download_button(
                label="📥 Download Full Results (CSV)",
                data=csv,
                file_name="rrsp_screener_results.csv",
                mime="text/csv",
            )

else:
    # Show instructions when app first loads
    st.info("""
    👈 **Configure your screening criteria in the sidebar, then click "Find Candidates"**
    
    **How it works:**
    1. Select your target markets (US, Canadian, or both)
    2. Choose your investing style (Growth, Value, Dividend, or Blend)
    3. Filter by sectors you're interested in
    4. Set your risk tolerance (market cap preference)
    5. Adjust additional filters as needed
    6. Click "Find Candidates" to run the screener
    
    The tool will fetch live data for ~500+ stocks, apply your filters, and rank them based on your investing style.
    """)
    
    # Show example of what each style prioritizes
    st.markdown("---")
    st.markdown("### 📚 What Each Style Prioritizes")
    
    style_cols = st.columns(4)
    
    with style_cols[0]:
        st.markdown("**🚀 Growth**")
        st.write("• Revenue growth")
        st.write("• Earnings growth")
        st.write("• Momentum")
        st.write("• Analyst upgrades")
    
    with style_cols[1]:
        st.markdown("**💰 Value**")
        st.write("• Price below target")
        st.write("• Low P/E ratio")
        st.write("• Strong fundamentals")
        st.write("• Margin of safety")
    
    with style_cols[2]:
        st.markdown("**📊 Dividend**")
        st.write("• High dividend yield")
        st.write("• Sustainable payout")
        st.write("• Dividend growth")
        st.write("• Stability")
    
    with style_cols[3]:
        st.markdown("**⚖️ Blend**")
        st.write("• Balanced approach")
        st.write("• All factors weighted")
        st.write("• Diversified")
        st.write("• Lower risk")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #6b7280; font-size: 0.9rem;">
        📊 Data provided by Yahoo Finance via yfinance. Prices may be delayed 15-20 minutes.<br>
        ⚠️ This tool is for informational purposes only and is not financial advice.
    </div>
    """,
    unsafe_allow_html=True
)
