import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_latest_excel(folder="data/nifty500", pattern="nifty500_close_prices_1y_*.xlsx"):
    files = sorted(glob.glob(os.path.join(folder, pattern)))
    if not files:
        raise FileNotFoundError(f"No files found in {folder} matching {pattern}")
    return files[-1]  # latest by filename date

def compute_vol_breadth(close_prices: pd.DataFrame, short=20, long=60) -> pd.Series:
    # Daily returns
    rets = close_prices.pct_change(fill_method=None)

    # Rolling vol (std dev of daily returns)
    vol_s = rets.rolling(short).std()
    vol_l = rets.rolling(long).std()

    # Valid points (need both vols)
    valid = vol_s.notna() & vol_l.notna()

    # Condition: short-term vol > long-term vol
    expansion = (vol_s > vol_l) & valid

    # % of stocks in expansion each day
    pct = expansion.sum(axis=1) / valid.sum(axis=1) * 100
    pct = pct.dropna()
    pct.name = f"pct_st_vol_expansion_{short}gt{long}"
    return pct

def plot_series(pct: pd.Series, out_png: str):
    plt.figure(figsize=(16, 7))
    plt.plot(pct.index, pct.values, linewidth=2.5)

    plt.title("% Stocks with Short-Term Volatility Expansion (20d > 60d)", fontsize=16, pad=15)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Percent", fontsize=12)

    plt.ylim(0, 80)  # adjust if you prefer 0-100
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.savefig(out_png, dpi=150)
    plt.close()

def main():
    # 1) Find latest close-price excel
    latest_file = find_latest_excel()
    print("Using latest file:", latest_file)

    # 2) Load close prices
    close_prices = pd.read_excel(latest_file, index_col=0)
    close_prices.index = pd.to_datetime(close_prices.index, errors="coerce")
    close_prices = close_prices.sort_index()

    # 3) Compute volatility breadth
    pct = compute_vol_breadth(close_prices, short=20, long=60)

    # 4) Output folders
    os.makedirs("output", exist_ok=True)
    os.makedirs("images", exist_ok=True)

    # 5) Save series CSV
    out_csv = "output/nifty500_volatility_breadth_series.csv"
    pct.to_csv(out_csv, index=True)

    # 6) Save chart PNG
    out_png = "images/nifty500_volatility_breadth.png"
    plot_series(pct, out_png)

    print("Saved series:", out_csv)
    print("Saved chart :", out_png)
    print("Last value  :", float(pct.iloc[-1]))

if __name__ == "__main__":
    main()
