import yfinance as yf
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_path = os.path.join(BASE_DIR, 'data', 'raw', 'TSLA_stock_data.csv')

def fetch_tsla_data(period='1y', interval='1d'):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_path = os.path.join(base_dir, 'data', 'raw', 'TSLA_stock_data.csv')

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    print("Loading TSLA stock data...")
    df = yf.download("TSLA", period=period, interval=interval).reset_index()

    if df.empty:
        print("No data fetched! Check internet connection or symbol.")
    else:
        print(df)
        df.to_csv(save_path, index=False)
        print(f"Data saved in: {save_path}")
    return df

if __name__ == "__main__":
    fetch_tsla_data()