import time
import requests
import pandas as pd
import yfinance as yf

def fetch_nifty500_symbols():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "application/json,text/plain,*/*",
        "Connection": "keep-alive",
    }

    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers, timeout=30)
    data = session.get(url, headers=headers, timeout=30).json()

    symbols = []
    for item in data.get("data", []):
        sym = str(item.get("symbol", "")).strip()
        if sym and not sym.upper().startswith("NIFTY"):
            symbols.append(sym + ".NS")

    return sorted(list(set(symbols)))

def download_close_prices(symbols, period="1y", chunk_size=50, pause=1):
    all_close = []

    for i in range(0, len(symbols), chunk_size):
        chunk = symbols[i:i + chunk_size]
        df = yf.download(
            chunk,
            period=period,
            auto_adjust=True,
            threads=True,
            progress=False
        )

        if df is not None and not df.empty and "Close" in df.columns:
            all_close.append(df["Close"].copy())

        time.sleep(pause)

    if not all_close:
        return pd.DataFrame()

    close_prices = pd.concat(all_close, axis=1)
    close_prices = close_prices.dropna(axis=1, how="all")
    close_prices = close_prices.sort_index()

    return close_prices

def main():
    symbols = fetch_nifty500_symbols()
    close_prices = download_close_prices(symbols)

    if close_prices.empty:
        raise RuntimeError("No price data downloaded")

    close_prices.to_excel("nifty500_close_prices_1y.xlsx")

    print("Saved: nifty500_close_prices_1y.xlsx")
    print("Rows (trading days):", close_prices.shape[0])
    print("Stocks:", close_prices.shape[1])

if __name__ == "__main__":
    main()
