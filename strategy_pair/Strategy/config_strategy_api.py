"""
    API Documentation for Strategy

"""

# API Imports
from pybit.unified_trading import HTTP

# Binance API
from binance.client import Client

client = Client('ZqMKfAowteSNb4ezHzxbidCOuLboxNXmzgv82221O9XNgnLpCPkJOohc79tpEO09',
                 'vXTnQF5cWmVwGvScxu7rHLAFIBhfXYtEwxWdoh5k9iw64sobe91nP44s96Ut0ckQ', testnet=False)   

# config
mode = 'test'
timeframe = 60
kline_limit = 200
z_score_window = 21

# live api
api_key_mainnet = ''
api_secret_mainnet = ''

# test api
api_key_testnet = 'IQp3KRUFW4SAklmp75'
api_secret_testnet = '60mqSnl9vjADtkdoMLKWXz8xIDqao5uwQzrE'

# selected API
api_key = api_key_testnet if mode == 'test' else api_key_mainnet
api_secret = api_secret_testnet if mode == 'test' else api_secret_mainnet

# select URL
api_url = 'https://api-testnet.bybit.com'

# session activation
session = HTTP(testnet=True, api_key=api_key_testnet, api_secret=api_secret_testnet)

# session = HTTP(api_key=api_key, api_secret=api_secret, testnet=True if mode == 'test' else False)

# websocket connection
# ws = WebSocket('wss://stream-testnet.bybit.com/unified/private/v3')

print(session.get_tickers(category='linear'))