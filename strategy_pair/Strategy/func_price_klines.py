import pandas as pd
from config_strategy_api import client
from binance.client import Client
import time


def get_price_klines(symbol):

    df = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, '1 Aug, 2023')
    df = pd.DataFrame(df, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df = df.set_index('Date')
    df = df.astype(float)

    # manage API calls
    time.sleep(0.1)

    return df['Close'].values.tolist()

