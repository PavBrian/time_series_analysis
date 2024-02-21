import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from func_get_symbols import get_tradeable_symbols
from func_prices_json import store_price_history
from func_cointegration import get_cointegrated_pairs
import json

""" STRATEGY CoDE"""
if __name__ == "__main__":
    # # Step 1 - Get list of symbols
    # # Get list of symbols
    # print('Getting list of symbols...')
    # sym_response = get_tradeable_symbols()

    # # Step 2 - Construct and save price hystory
    # print('Constructing and saving price history...')
    # if len(sym_response) > 0:
    #     store_price_history(sym_response)

    # Step 3 - Find cointegrated pairs
    print('Finding cointegrated pairs...')
    with open('1_price_list.json') as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            coint_pairs = get_cointegrated_pairs(price_data)
    print('Done!')



