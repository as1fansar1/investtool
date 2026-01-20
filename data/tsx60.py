# TSX 60 + Additional Liquid Canadian Stocks
# These are the most liquid and well-covered Canadian stocks

TSX_TICKERS = [
    # TSX 60 Components (with .TO suffix for yfinance)
    "RY.TO",    # Royal Bank
    "TD.TO",    # TD Bank
    "BNS.TO",   # Bank of Nova Scotia
    "BMO.TO",   # Bank of Montreal
    "CM.TO",    # CIBC
    "ENB.TO",   # Enbridge
    "CNR.TO",   # Canadian National Railway
    "CP.TO",    # Canadian Pacific Railway
    "TRP.TO",   # TC Energy
    "BCE.TO",   # BCE Inc
    "T.TO",     # Telus
    "SU.TO",    # Suncor Energy
    "CNQ.TO",   # Canadian Natural Resources
    "CVE.TO",   # Cenovus Energy
    "IMO.TO",   # Imperial Oil
    "ABX.TO",   # Barrick Gold
    "NTR.TO",   # Nutrien
    "FTS.TO",   # Fortis
    "TRI.TO",   # Thomson Reuters
    "CSU.TO",   # Constellation Software
    "SHOP.TO", # Shopify
    "ATD.TO",   # Alimentation Couche-Tard
    "QSR.TO",   # Restaurant Brands
    "L.TO",     # Loblaw
    "MFC.TO",   # Manulife
    "SLF.TO",   # Sun Life
    "IFC.TO",   # Intact Financial
    "POW.TO",   # Power Corp
    "GWO.TO",   # Great-West Lifeco
    "FFH.TO",   # Fairfax Financial
    "WCN.TO",   # Waste Connections
    "DOL.TO",   # Dollarama
    "RCI-B.TO", # Rogers Communications
    "MRU.TO",   # Metro Inc
    "EMA.TO",   # Emera
    "H.TO",     # Hydro One
    "PPL.TO",   # Pembina Pipeline
    "KEY.TO",   # Keyera
    "AQN.TO",   # Algonquin Power
    "CU.TO",    # Canadian Utilities
    "CCO.TO",   # Cameco
    "FM.TO",    # First Quantum
    "TECK-B.TO", # Teck Resources
    "WPM.TO",   # Wheaton Precious Metals
    "AEM.TO",   # Agnico Eagle
    "K.TO",     # Kinross Gold
    "MG.TO",    # Magna International
    "TIH.TO",   # Toromont
    "WSP.TO",   # WSP Global
    "CAE.TO",   # CAE Inc
    "STN.TO",   # Stantec
    "TFII.TO",  # TFI International
    "GIB-A.TO", # CGI Group
    "OTEX.TO",  # Open Text
    "BB.TO",    # BlackBerry
    "LSPD.TO",  # Lightspeed
    "REAL.TO",  # Real Matters
    "WELL.TO",  # WELL Health
    "BAM.TO",   # Brookfield Asset Management
    "BN.TO",    # Brookfield Corporation
    "BIP-UN.TO", # Brookfield Infrastructure Partners
    "BEP-UN.TO", # Brookfield Renewable Partners
    
    # Additional Canadian ETFs (popular for RRSP)
    "XIU.TO",   # iShares S&P/TSX 60 ETF
    "XIC.TO",   # iShares Core S&P/TSX Capped Composite
    "VFV.TO",   # Vanguard S&P 500 Index ETF (CAD)
    "XQQ.TO",   # iShares NASDAQ 100 ETF (CAD Hedged)
    "ZSP.TO",   # BMO S&P 500 Index ETF
    "VCN.TO",   # Vanguard FTSE Canada All Cap
    "XEI.TO",   # iShares S&P/TSX Composite High Dividend
    "ZDV.TO",   # BMO Canadian Dividend ETF
    "VDY.TO",   # Vanguard FTSE Canadian High Dividend Yield
    "XDV.TO",   # iShares Canadian Select Dividend
]

# Sector mapping for TSX stocks
TSX_SECTOR_MAP = {
    # Financials
    "RY.TO": "Financials", "TD.TO": "Financials", "BNS.TO": "Financials",
    "BMO.TO": "Financials", "CM.TO": "Financials", "MFC.TO": "Financials",
    "SLF.TO": "Financials", "IFC.TO": "Financials", "POW.TO": "Financials",
    "GWO.TO": "Financials", "FFH.TO": "Financials", "BAM.TO": "Financials",
    "BN.TO": "Financials",
    
    # Energy
    "ENB.TO": "Energy", "TRP.TO": "Energy", "SU.TO": "Energy",
    "CNQ.TO": "Energy", "CVE.TO": "Energy", "IMO.TO": "Energy",
    "PPL.TO": "Energy", "KEY.TO": "Energy",
    
    # Materials
    "ABX.TO": "Materials", "NTR.TO": "Materials", "CCO.TO": "Materials",
    "FM.TO": "Materials", "TECK-B.TO": "Materials", "WPM.TO": "Materials",
    "AEM.TO": "Materials", "K.TO": "Materials",
    
    # Industrials
    "CNR.TO": "Industrials", "CP.TO": "Industrials", "WCN.TO": "Industrials",
    "MG.TO": "Industrials", "TIH.TO": "Industrials", "WSP.TO": "Industrials",
    "CAE.TO": "Industrials", "STN.TO": "Industrials", "TFII.TO": "Industrials",
    
    # Technology
    "SHOP.TO": "Technology", "CSU.TO": "Technology", "GIB-A.TO": "Technology",
    "OTEX.TO": "Technology", "BB.TO": "Technology", "LSPD.TO": "Technology",
    "REAL.TO": "Technology",
    
    # Communication Services
    "BCE.TO": "Communication Services", "T.TO": "Communication Services",
    "RCI-B.TO": "Communication Services",
    
    # Consumer Staples
    "ATD.TO": "Consumer Staples", "L.TO": "Consumer Staples",
    "MRU.TO": "Consumer Staples", "DOL.TO": "Consumer Staples",
    
    # Consumer Discretionary
    "QSR.TO": "Consumer Discretionary",
    
    # Utilities
    "FTS.TO": "Utilities", "EMA.TO": "Utilities", "H.TO": "Utilities",
    "AQN.TO": "Utilities", "CU.TO": "Utilities",
    
    # Real Estate
    "BIP-UN.TO": "Real Estate", "BEP-UN.TO": "Real Estate",
    
    # Healthcare
    "WELL.TO": "Healthcare",
    
    # Miscellaneous / Multi-sector
    "TRI.TO": "Industrials",
    
    # ETFs (marked as ETF for special handling)
    "XIU.TO": "ETF", "XIC.TO": "ETF", "VFV.TO": "ETF", "XQQ.TO": "ETF",
    "ZSP.TO": "ETF", "VCN.TO": "ETF", "XEI.TO": "ETF", "ZDV.TO": "ETF",
    "VDY.TO": "ETF", "XDV.TO": "ETF",
}
