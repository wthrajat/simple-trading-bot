# Cryptocurrency Trading Bot with Machine Learning

This project implements a basic cryptocurrency trading bot using machine learning to predict market trends. The bot fetches market data, performs feature engineering, trains a Random Forest model, and makes trading decisions based on predictions.

## Features

- Fetches historical market data from Binance
- Computes technical indicators (moving average, RSI)
- Generates dummy sentiment scores
- Trains a Random Forest model for trend prediction
- Places trades based on model predictions

## Installation

1. Umm do this:
    ```sh
    git clone https://github.com/wthrajat/simple-trading-bot.git
    cd crypto-trading-bot
    pip install ccxt pandas scikit-learn numpy
    ```

2. Set up your Binance API keys in the script:
    ```python
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET_KEY'
    })
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```