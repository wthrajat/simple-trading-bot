import ccxt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import time

def fetch_market_data(symbol='BTC/USDT', timeframe='1h'):
    # Binance se market data fetch karo
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def compute_rsi(series, period=14):
    # RSI (Relative Strength Index) compute karo
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def feature_engineering(df):
    # Features ko generate karo
    df['ma50'] = df['close'].rolling(window=50).mean()
    df['rsi'] = compute_rsi(df['close'])
    df['sentiment'] = np.random.uniform(-1, 1, len(df))  # Dummy sentiment data hai
    return df.dropna()

def train_model(df):
    # Model ko train karo
    X = df[['ma50', 'rsi', 'sentiment']]
    y = (df['close'].shift(-1) > df['close']).astype(int)
    X = X.iloc[:-1]
    y = y.iloc[:-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def trading_decision(prediction):
    # Trading decision le lo
    return 'buy' if prediction == 1 else 'sell'

def execute_trade(decision, symbol='BTC/USDT', amount=0.01):
    # Trade execute karo
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET_KEY'
    })
    if decision == 'buy':
        exchange.create_market_buy_order(symbol, amount)
    elif decision == 'sell':
        exchange.create_market_sell_order(symbol, amount)

def run_trading_bot():
    # Trading bot ko chalao
    df = fetch_market_data()
    df = feature_engineering(df)
    model = train_model(df)
    while True:
        df = fetch_market_data()
        df = feature_engineering(df)
        X_new = df[['ma50', 'rsi', 'sentiment']].iloc[-1].values.reshape(1, -1)
        prediction = model.predict(X_new)
        decision = trading_decision(prediction)
        execute_trade(decision)
        print(f"Executed {decision} trade")
        time.sleep(3600)  # har ghanta ek trade

if __name__ == "__main__":
    run_trading_bot()
