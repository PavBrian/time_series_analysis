from func_price_klines import get_price_klines
import json

# store price history for all available pairs
def store_price_history(symbols):
    

    # get price history for all symbols
    counts = 0
    price_history_dict = {}
    for sym in symbols:
        # symbol_name = sym['name']
        price_history = get_price_klines(sym)
        if len(price_history) > 0:
            price_history_dict[sym] = price_history
            counts += 1
            print(f'{counts} items stored')
        else:
            print(f'{counts} items not stored')

    # Output prices to json file
    if len(price_history_dict) > 0:
        with open('1_price_list.json', 'w') as fp:
            json.dump(price_history_dict, fp, indent=4)
        print('Price sabed successfully.')

    return
    
