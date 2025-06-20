import pandas as pd
import os

input_path = 'C:/Users/Lenovo/VisualProjects/stock-analysis-tsla/data/raw/TSLA_stock_data.csv'
output_path = 'C:/Users/Lenovo/VisualProjects/stock-analysis-tsla/data/processed/TSLA_clean.csv'

def compute_rsi(series, period=20):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def clean_stock_data():
    df = pd.read_csv(input_path)

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.sort_values('Date').reset_index(drop=True)

    print(f"Các cột có trong dữ liệu: {df.columns.tolist()}")

    possible_numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    for col in possible_numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()

    if 'Close' in df.columns:
        z_scores = (df['Close'] - df['Close'].mean()) / df['Close'].std()
        df = df[(z_scores > -3) & (z_scores < 3)]

        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
        df['RSI_20'] = compute_rsi(df['Close'], period=20)
        
        # MACD calculation
        ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema_12 - ema_26
        df['Signal Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    else:
        print("Cột 'Close' không tồn tại — không thể tính toán chỉ báo kỹ thuật.")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data with indicators saved to: {output_path}")

if __name__ == "__main__":
    clean_stock_data()