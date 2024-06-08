# Cryptocurrency Trading Bot with Machine Learning

This project implements a basic cryptocurrency trading bot using machine learning to predict market trends. The bot fetches market data, performs feature engineering, trains a Random Forest model, and makes trading decisions based on predictions.

## Features

- Fetches historical market data from Binance
- Computes technical indicators (moving average, RSI)
- Generates dummy sentiment scores
- Trains a Random Forest model for trend prediction
- Places trades based on model predictions

## Requirements

- Python 3.6+
- `ccxt` library
- `pandas` library
- `scikit-learn` library
- `numpy` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/crypto-trading-bot.git
    cd crypto-trading-bot
    ```

2. Install the required libraries:
    ```sh
    pip install ccxt pandas scikit-learn numpy
    ```

3. Set up your Binance API keys in the script:
    ```python
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET_KEY'
    })
    ```

## Usage

1. Save the script as `trading_bot.py`.

2. Run the script:
    ```sh
    python trading_bot.py
    ```

The bot will fetch market data, compute features, train the model, and execute trades every hour.

## Important Notes

- **API Keys**: Ensure your Binance API keys are securely stored and not hard-coded in the script for production use.
- **Sentiment Analysis**: The sentiment feature is currently a dummy. Replace it with real sentiment data from a reliable source for better performance.
- **Risk Management**: Implement risk management strategies (e.g., stop-loss and take-profit) to handle trades safely.
- **Backtesting**: Thoroughly backtest the bot with historical data before running it with real money.

## License

This project is licensed under the MIT License.
