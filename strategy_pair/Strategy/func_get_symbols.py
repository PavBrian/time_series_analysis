import pandas as pd
from config_strategy_api import client

def get_tradeable_symbols():
    x = pd.DataFrame(client.get_ticker())
    y = x[x.symbol.str.contains('USDT')]
    z = y[~((y.symbol.str.contains('UP')) | (y.symbol.str.contains('DOWN')))]
    list_of_tickers = z.symbol.to_list()
    return list_of_tickers