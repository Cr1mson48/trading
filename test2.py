session_auth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key='gw90bhuJCb29ZaeDU9',
    api_secret='KwqbUpaV1CyCv9CLcSiRHcbzv6S1bgxogAsb'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)