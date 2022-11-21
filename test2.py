from pybit import usdt_perpetual, inverse_perpetual

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='H9X78xMQgIP5yDSyok',
    api_secret='YeQTC5zNr7PvHcmjwkJVBFywPnie9pdLe0cw'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com"
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])




session_auth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key='gw90bhuJCb29ZaeDU9',
    api_secret='KwqbUpaV1CyCv9CLcSiRHcbzv6S1bgxogAsb'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])