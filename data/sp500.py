# S&P 500 Tickers (Top ~500 US stocks by market cap)
# This is a curated list of liquid, well-covered stocks

SP500_TICKERS = [
    # Technology
    "AAPL", "MSFT", "GOOGL", "GOOG", "META", "NVDA", "AVGO", "ORCL", "CSCO", "ADBE",
    "CRM", "ACN", "IBM", "INTC", "AMD", "QCOM", "TXN", "NOW", "INTU", "AMAT",
    "MU", "LRCX", "ADI", "KLAC", "SNPS", "CDNS", "MCHP", "FTNT", "PANW", "CRWD",
    "WDAY", "TEAM", "DDOG", "ZS", "SPLK", "HUBS", "SNOW", "PLTR", "NET", "MDB",
    
    # Healthcare
    "UNH", "JNJ", "LLY", "ABBV", "MRK", "PFE", "TMO", "ABT", "DHR", "BMY",
    "AMGN", "GILD", "VRTX", "REGN", "ISRG", "MDT", "SYK", "BSX", "ZBH", "EW",
    "DXCM", "IDXX", "IQV", "CI", "HUM", "CVS", "ELV", "MCK", "CAH", "CNC",
    "BIIB", "MRNA", "ILMN", "A", "BDX", "MTD", "WAT", "HOLX", "TECH", "ALGN",
    
    # Financials
    "BRK.B", "JPM", "V", "MA", "BAC", "WFC", "GS", "MS", "SPGI", "BLK",
    "C", "AXP", "SCHW", "CB", "MMC", "PGR", "AON", "ICE", "CME", "USB",
    "TFC", "PNC", "AIG", "MET", "PRU", "AFL", "ALL", "TRV", "CINF", "L",
    "BK", "STT", "NTRS", "FITB", "RF", "KEY", "CFG", "HBAN", "ZION", "CMA",
    
    # Consumer Discretionary
    "AMZN", "TSLA", "HD", "MCD", "NKE", "LOW", "SBUX", "TJX", "BKNG", "CMG",
    "MAR", "HLT", "YUM", "ORLY", "AZO", "ROST", "DHI", "LEN", "PHM", "NVR",
    "GM", "F", "APTV", "EBAY", "ETSY", "W", "DECK", "LULU", "ULTA", "BBY",
    "DRI", "LVS", "WYNN", "MGM", "CZR", "RCL", "CCL", "NCLH", "EXPE", "ABNB",
    
    # Consumer Staples
    "PG", "KO", "PEP", "COST", "WMT", "PM", "MO", "MDLZ", "CL", "EL",
    "KMB", "GIS", "K", "HSY", "SJM", "HRL", "CAG", "CPB", "MKC", "CHD",
    "KHC", "KR", "SYY", "WBA", "TGT", "DG", "DLTR", "CLX", "TSN", "ADM",
    
    # Energy
    "XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO", "OXY", "PXD",
    "HAL", "DVN", "HES", "FANG", "BKR", "KMI", "WMB", "OKE", "TRGP", "LNG",
    
    # Industrials
    "GE", "CAT", "HON", "UNP", "UPS", "RTX", "BA", "DE", "LMT", "MMM",
    "FDX", "CSX", "NSC", "WM", "RSG", "ETN", "EMR", "ROK", "ITW", "PH",
    "PCAR", "CTAS", "FAST", "ODFL", "GWW", "URI", "VRSK", "IR", "DOV", "AME",
    "XYL", "SWK", "GNRC", "TT", "CARR", "OTIS", "J", "LHX", "GD", "NOC",
    
    # Materials
    "LIN", "APD", "SHW", "ECL", "FCX", "NEM", "NUE", "DD", "DOW", "PPG",
    "VMC", "MLM", "ALB", "EMN", "CE", "CF", "MOS", "FMC", "IFF", "BALL",
    
    # Real Estate
    "PLD", "AMT", "CCI", "EQIX", "PSA", "SPG", "O", "WELL", "DLR", "AVB",
    "EQR", "VTR", "ARE", "ESS", "MAA", "UDR", "SUI", "EXR", "PEAK", "HST",
    
    # Utilities
    "NEE", "DUK", "SO", "D", "AEP", "SRE", "EXC", "XEL", "PEG", "ED",
    "WEC", "ES", "AWK", "DTE", "PPL", "AEE", "CMS", "CNP", "EVRG", "FE",
    
    # Communication Services
    "NFLX", "DIS", "CMCSA", "T", "VZ", "TMUS", "CHTR", "EA", "ATVI", "TTWO",
    "WBD", "PARA", "FOX", "FOXA", "LYV", "MTCH", "ZG", "PINS", "SNAP", "RBLX",
]

# Sector mapping for each ticker
SECTOR_MAP = {
    # Technology
    "AAPL": "Technology", "MSFT": "Technology", "GOOGL": "Technology", "GOOG": "Technology",
    "META": "Technology", "NVDA": "Technology", "AVGO": "Technology", "ORCL": "Technology",
    "CSCO": "Technology", "ADBE": "Technology", "CRM": "Technology", "ACN": "Technology",
    "IBM": "Technology", "INTC": "Technology", "AMD": "Technology", "QCOM": "Technology",
    "TXN": "Technology", "NOW": "Technology", "INTU": "Technology", "AMAT": "Technology",
    "MU": "Technology", "LRCX": "Technology", "ADI": "Technology", "KLAC": "Technology",
    "SNPS": "Technology", "CDNS": "Technology", "MCHP": "Technology", "FTNT": "Technology",
    "PANW": "Technology", "CRWD": "Technology", "WDAY": "Technology", "TEAM": "Technology",
    "DDOG": "Technology", "ZS": "Technology", "SPLK": "Technology", "HUBS": "Technology",
    "SNOW": "Technology", "PLTR": "Technology", "NET": "Technology", "MDB": "Technology",
    
    # Healthcare
    "UNH": "Healthcare", "JNJ": "Healthcare", "LLY": "Healthcare", "ABBV": "Healthcare",
    "MRK": "Healthcare", "PFE": "Healthcare", "TMO": "Healthcare", "ABT": "Healthcare",
    "DHR": "Healthcare", "BMY": "Healthcare", "AMGN": "Healthcare", "GILD": "Healthcare",
    "VRTX": "Healthcare", "REGN": "Healthcare", "ISRG": "Healthcare", "MDT": "Healthcare",
    "SYK": "Healthcare", "BSX": "Healthcare", "ZBH": "Healthcare", "EW": "Healthcare",
    "DXCM": "Healthcare", "IDXX": "Healthcare", "IQV": "Healthcare", "CI": "Healthcare",
    "HUM": "Healthcare", "CVS": "Healthcare", "ELV": "Healthcare", "MCK": "Healthcare",
    "CAH": "Healthcare", "CNC": "Healthcare", "BIIB": "Healthcare", "MRNA": "Healthcare",
    "ILMN": "Healthcare", "A": "Healthcare", "BDX": "Healthcare", "MTD": "Healthcare",
    "WAT": "Healthcare", "HOLX": "Healthcare", "TECH": "Healthcare", "ALGN": "Healthcare",
    
    # Financials
    "BRK.B": "Financials", "JPM": "Financials", "V": "Financials", "MA": "Financials",
    "BAC": "Financials", "WFC": "Financials", "GS": "Financials", "MS": "Financials",
    "SPGI": "Financials", "BLK": "Financials", "C": "Financials", "AXP": "Financials",
    "SCHW": "Financials", "CB": "Financials", "MMC": "Financials", "PGR": "Financials",
    "AON": "Financials", "ICE": "Financials", "CME": "Financials", "USB": "Financials",
    "TFC": "Financials", "PNC": "Financials", "AIG": "Financials", "MET": "Financials",
    "PRU": "Financials", "AFL": "Financials", "ALL": "Financials", "TRV": "Financials",
    "CINF": "Financials", "L": "Financials", "BK": "Financials", "STT": "Financials",
    "NTRS": "Financials", "FITB": "Financials", "RF": "Financials", "KEY": "Financials",
    "CFG": "Financials", "HBAN": "Financials", "ZION": "Financials", "CMA": "Financials",
    
    # Consumer Discretionary
    "AMZN": "Consumer Discretionary", "TSLA": "Consumer Discretionary", "HD": "Consumer Discretionary",
    "MCD": "Consumer Discretionary", "NKE": "Consumer Discretionary", "LOW": "Consumer Discretionary",
    "SBUX": "Consumer Discretionary", "TJX": "Consumer Discretionary", "BKNG": "Consumer Discretionary",
    "CMG": "Consumer Discretionary", "MAR": "Consumer Discretionary", "HLT": "Consumer Discretionary",
    "YUM": "Consumer Discretionary", "ORLY": "Consumer Discretionary", "AZO": "Consumer Discretionary",
    "ROST": "Consumer Discretionary", "DHI": "Consumer Discretionary", "LEN": "Consumer Discretionary",
    "PHM": "Consumer Discretionary", "NVR": "Consumer Discretionary", "GM": "Consumer Discretionary",
    "F": "Consumer Discretionary", "APTV": "Consumer Discretionary", "EBAY": "Consumer Discretionary",
    "ETSY": "Consumer Discretionary", "W": "Consumer Discretionary", "DECK": "Consumer Discretionary",
    "LULU": "Consumer Discretionary", "ULTA": "Consumer Discretionary", "BBY": "Consumer Discretionary",
    "DRI": "Consumer Discretionary", "LVS": "Consumer Discretionary", "WYNN": "Consumer Discretionary",
    "MGM": "Consumer Discretionary", "CZR": "Consumer Discretionary", "RCL": "Consumer Discretionary",
    "CCL": "Consumer Discretionary", "NCLH": "Consumer Discretionary", "EXPE": "Consumer Discretionary",
    "ABNB": "Consumer Discretionary",
    
    # Consumer Staples
    "PG": "Consumer Staples", "KO": "Consumer Staples", "PEP": "Consumer Staples",
    "COST": "Consumer Staples", "WMT": "Consumer Staples", "PM": "Consumer Staples",
    "MO": "Consumer Staples", "MDLZ": "Consumer Staples", "CL": "Consumer Staples",
    "EL": "Consumer Staples", "KMB": "Consumer Staples", "GIS": "Consumer Staples",
    "K": "Consumer Staples", "HSY": "Consumer Staples", "SJM": "Consumer Staples",
    "HRL": "Consumer Staples", "CAG": "Consumer Staples", "CPB": "Consumer Staples",
    "MKC": "Consumer Staples", "CHD": "Consumer Staples", "KHC": "Consumer Staples",
    "KR": "Consumer Staples", "SYY": "Consumer Staples", "WBA": "Consumer Staples",
    "TGT": "Consumer Staples", "DG": "Consumer Staples", "DLTR": "Consumer Staples",
    "CLX": "Consumer Staples", "TSN": "Consumer Staples", "ADM": "Consumer Staples",
    
    # Energy
    "XOM": "Energy", "CVX": "Energy", "COP": "Energy", "SLB": "Energy",
    "EOG": "Energy", "MPC": "Energy", "PSX": "Energy", "VLO": "Energy",
    "OXY": "Energy", "PXD": "Energy", "HAL": "Energy", "DVN": "Energy",
    "HES": "Energy", "FANG": "Energy", "BKR": "Energy", "KMI": "Energy",
    "WMB": "Energy", "OKE": "Energy", "TRGP": "Energy", "LNG": "Energy",
    
    # Industrials
    "GE": "Industrials", "CAT": "Industrials", "HON": "Industrials", "UNP": "Industrials",
    "UPS": "Industrials", "RTX": "Industrials", "BA": "Industrials", "DE": "Industrials",
    "LMT": "Industrials", "MMM": "Industrials", "FDX": "Industrials", "CSX": "Industrials",
    "NSC": "Industrials", "WM": "Industrials", "RSG": "Industrials", "ETN": "Industrials",
    "EMR": "Industrials", "ROK": "Industrials", "ITW": "Industrials", "PH": "Industrials",
    "PCAR": "Industrials", "CTAS": "Industrials", "FAST": "Industrials", "ODFL": "Industrials",
    "GWW": "Industrials", "URI": "Industrials", "VRSK": "Industrials", "IR": "Industrials",
    "DOV": "Industrials", "AME": "Industrials", "XYL": "Industrials", "SWK": "Industrials",
    "GNRC": "Industrials", "TT": "Industrials", "CARR": "Industrials", "OTIS": "Industrials",
    "J": "Industrials", "LHX": "Industrials", "GD": "Industrials", "NOC": "Industrials",
    
    # Materials
    "LIN": "Materials", "APD": "Materials", "SHW": "Materials", "ECL": "Materials",
    "FCX": "Materials", "NEM": "Materials", "NUE": "Materials", "DD": "Materials",
    "DOW": "Materials", "PPG": "Materials", "VMC": "Materials", "MLM": "Materials",
    "ALB": "Materials", "EMN": "Materials", "CE": "Materials", "CF": "Materials",
    "MOS": "Materials", "FMC": "Materials", "IFF": "Materials", "BALL": "Materials",
    
    # Real Estate
    "PLD": "Real Estate", "AMT": "Real Estate", "CCI": "Real Estate", "EQIX": "Real Estate",
    "PSA": "Real Estate", "SPG": "Real Estate", "O": "Real Estate", "WELL": "Real Estate",
    "DLR": "Real Estate", "AVB": "Real Estate", "EQR": "Real Estate", "VTR": "Real Estate",
    "ARE": "Real Estate", "ESS": "Real Estate", "MAA": "Real Estate", "UDR": "Real Estate",
    "SUI": "Real Estate", "EXR": "Real Estate", "PEAK": "Real Estate", "HST": "Real Estate",
    
    # Utilities
    "NEE": "Utilities", "DUK": "Utilities", "SO": "Utilities", "D": "Utilities",
    "AEP": "Utilities", "SRE": "Utilities", "EXC": "Utilities", "XEL": "Utilities",
    "PEG": "Utilities", "ED": "Utilities", "WEC": "Utilities", "ES": "Utilities",
    "AWK": "Utilities", "DTE": "Utilities", "PPL": "Utilities", "AEE": "Utilities",
    "CMS": "Utilities", "CNP": "Utilities", "EVRG": "Utilities", "FE": "Utilities",
    
    # Communication Services
    "NFLX": "Communication Services", "DIS": "Communication Services", "CMCSA": "Communication Services",
    "T": "Communication Services", "VZ": "Communication Services", "TMUS": "Communication Services",
    "CHTR": "Communication Services", "EA": "Communication Services", "ATVI": "Communication Services",
    "TTWO": "Communication Services", "WBD": "Communication Services", "PARA": "Communication Services",
    "FOX": "Communication Services", "FOXA": "Communication Services", "LYV": "Communication Services",
    "MTCH": "Communication Services", "ZG": "Communication Services", "PINS": "Communication Services",
    "SNAP": "Communication Services", "RBLX": "Communication Services",
}
