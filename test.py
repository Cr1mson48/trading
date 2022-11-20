import time
from pybit import usdt_perpetual, inverse_perpetual
from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import time
import re

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key='gw90bhuJCb29ZaeDU9',
    api_secret='KwqbUpaV1CyCv9CLcSiRHcbzv6S1bgxogAsb'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])
balance = session_auth.get_wallet_balance()['result']['USDT']['equity']
order = balance / 100 * 5
print(order)

chats = []
last_date = None
size_chats = 200
groups=[]


name = 'anon'
api_id = "11323339"                  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "3dc8f15b3fdef03e259062d938a3311a"              # API Hash (оттуда же)
phone_number = "+79525974084"    # Номер телефона аккаунта, с которого будет выполняться код
chat = 'https://t.me/+Gw9duznm9bc3NmE6'

old_message = ''

with TelegramClient(name, api_id, api_hash) as client2:
    for dialog in client2.iter_dialogs():
        if dialog.name == "Crypto Futures":
            my_private_channel = dialog
            my_private_channel_id = dialog.id
            break

while True:
    try:
        with TelegramClient(name, api_id, api_hash) as client2:
            for dialog in client2.iter_dialogs():
                if dialog.name == "Crypto Futures":
                    my_private_channel = dialog
                    my_private_channel_id = dialog.id
                    break
        print(my_private_channel.message.message)
        if old_message != my_private_channel.message.message:
            new_message = my_private_channel.message.message
            if ('#SHORT' in new_message or '#LONG' in new_message) and '#SCALPING_session' not in new_message:
                if '#SHORT' in new_message:
                    poss = 'SHORT'
                if '#LONG' in new_message:
                    poss = 'LONG'
                if 'Take Profit' in new_message:
                    if 'Stop loss' in new_message:
                        lines = new_message.split('\n')
                        for i in lines:
                            if 'Пара' in i:
                                for j in i.split(' '):
                                    if j[0] == '#':
                                        symbol = j[1:]
                                        try:
                                            print(session_auth.set_leverage(
                                                symbol=symbol,
                                                buy_leverage=10,
                                                sell_leverage=10
                                            ))
                                        except Exception as e:
                                            print(e)
                            if 'Текущая цена' in i and 'entry' in i:
                                market = re.findall("\d+\.\d+", i)
                                if len(market) == 0:
                                    market = re.findall("\d+", i)[0]
                                else:
                                    market = market[0]
                                market_procent = re.findall("\d+\%", i)[0]
                            if '1st' in i and 'order' in i:
                                st_one = re.findall("\d+\.\d+", i)
                                if len(st_one) == 0:
                                    st_one = re.findall("\d+", i)[0]
                                else:
                                    st_one = st_one[0]
                                st_one_procent = re.findall("\d+\%", i)[0]
                            if '2nd' in i and 'order' in i:
                                st_two = re.findall("\d+\.\d+", i)
                                if len(st_two) == 0:
                                    st_two = re.findall("\d+", i)[0]
                                else:
                                    st_two = st_two[0]
                                st_two_procent = re.findall("\d+\%", i)[0]
                            if 'Take Profit 1' in i:
                                tk1 = re.findall("\d+\.\d+", i)
                                if len(tk1) == 0:
                                    tk1 = re.findall("\d+", i)[0]
                                else:
                                    tk1 = tk1[0]
                            if 'Take Profit 2' in i:
                                tk2 = re.findall("\d+\.\d+", i)
                                if len(tk2) == 0:
                                    tk2 = re.findall("\d+", i)[0]
                                else:
                                    tk2 = tk2[0]
                            if 'Take Profit 3' in i:
                                tk3 = re.findall("\d+\.\d+", i)
                                if len(tk3) == 0:
                                    tk3 = re.findall("\d+", i)[0]
                                else:
                                    tk3 = tk3[0]
                            if 'Stop loss' in i:
                                stop_loss = re.findall("\d+\.\d+", i)
                                if len(stop_loss) == 0:
                                    stop_loss = re.findall("\d+", i)[0]
                                else:
                                    stop_loss = stop_loss[0]
                        try:
                            price = session_unauth.latest_information_for_symbol(
                                symbol=symbol
                            )['result'][0]['last_price']
                            balance = session_auth.get_wallet_balance()['result']['USDT']['equity']
                            order = float(balance) / 100 * 5
                            qty = float(order) / float(price)
                            qty_m = qty / 100 * float(market_procent[0:-2])
                            qty_m = qty_m * 10
                            qty_2 = qty / 100 * float(st_one_procent[0:-2])
                            qty_2 = qty_2 * 10
                            qty_3 = qty / 100 * float(st_two_procent[0:-2])
                            qty_3 = qty_3 * 10
                            print(f'Qty_m {qty_m} qty_2 {qty_2} qty_3 {qty_3}')
                            print(f'Procent {st_one_procent[0:-2]}')
                            if poss == 'SHORT':
                                side = 'Sell'
                            if poss == 'LONG':
                                side = 'Buy'
                            print(session_auth.place_active_order(
                                symbol=symbol,
                                side=side,
                                order_type="Market",
                                qty=round(qty_m, 3),
                                take_profit=tk1,
                                stop_loss=stop_loss,
                                time_in_force="GoodTillCancel",
                                reduce_only=False,
                                close_on_trigger=False
                            ))
                            print(session_auth.place_active_order(
                                symbol=symbol,
                                side=side,
                                order_type="Limit",
                                qty=round(qty_2, 3),
                                price=st_one,
                                take_profit=tk2,
                                stop_loss=stop_loss,
                                time_in_force="GoodTillCancel",
                                reduce_only=False,
                                close_on_trigger=False
                            ))
                            print(session_auth.place_active_order(
                                symbol=symbol,
                                side=side,
                                order_type="Limit",
                                qty=round(qty_3, 3),
                                price=st_two,
                                take_profit=tk3,
                                stop_loss=stop_loss,
                                time_in_force="GoodTillCancel",
                                reduce_only=False,
                                close_on_trigger=False
                            ))
                            print(f'''
                                    Направление: {poss} \n
                                    Пара: {symbol} \n
                                    Market order приблизительная цена покупки: {market};{market_procent} от размера позиции \n
                                    2 order цена покупки: {st_one};{st_one_procent} от размера позиции \n
                                    3 order цена покупки: {st_two};{st_two_procent} от размера позиции \n
                                    Take Profit 1: {tk1} \n
                                    Take Profit 2: {tk2} \n
                                    Take Profit 3: {tk3} \n
                                    Stop loss: {stop_loss}''')
                        except Exception as e:
                            print(e)
            elif '#SCALPING_session' in new_message:
                new_message = my_private_channel.message.message
                lines = new_message.split('\n')
                print(lines)
                for i in lines:
                    print(i)
                    if 'Пара' in i:
                        for j in i.split(' '):
                            print(j)
                            if j[0] == '#':
                                symbol = j[1:]
                                try:
                                    print(session_auth.set_leverage(
                                        symbol=symbol,
                                        buy_leverage=10,
                                        sell_leverage=10
                                    ))
                                except Exception as e:
                                    print(e)
                    if '#SHORT' in new_message:
                        poss = 'SHORT'
                    if '#LONG' in new_message:
                        poss = 'LONG'
                    if 'Текущая цена' in i:
                        market = re.findall("\d+\.\d+", i)
                        if len(market) == 0:
                            market = re.findall("\d+", i)[0]
                        else:
                            market = market[0]
                    if 'Take Profit 1' in i:
                        tk1 = re.findall("\d+\.\d+", i)
                        if len(tk1) == 0:
                            tk1 = re.findall("\d+", i)[0]
                        else:
                            tk1 = tk1[0]
                    if 'Stop' in i:
                        stop_loss = re.findall("\d+\.\d+", i)
                        print(f'STop loss {stop_loss}')
                        if len(stop_loss) == 0:
                            stop_loss = re.findall("\d+", i)[0]
                        else:
                            stop_loss = stop_loss[0]
                try:
                    price = session_unauth.latest_information_for_symbol(
                        symbol=symbol
                    )['result'][0]['last_price']
                    balance = session_auth.get_wallet_balance()['result']['USDT']['equity']
                    order = float(balance) / 100 * 5
                    qty = float(order) / float(price)
                    print(poss)
                    if poss == 'SHORT':
                        side = 'Sell'
                    if poss == 'LONG':
                        side = 'Buy'
                    print(f'Баланс {balance}')
                    print(f'Количество {qty}')
                    qty = qty * 10
                    print(session_auth.place_active_order(
                        symbol=symbol,
                        side=side,
                        order_type="Market",
                        qty=round(qty, 3),
                        take_profit=tk1,
                        stop_loss=stop_loss,
                        time_in_force="GoodTillCancel",
                        reduce_only=False,
                        close_on_trigger=False
                    ))
                except Exception as e:
                    print(e)

        old_message = my_private_channel.message.message
    except Exception as r:
        print(r)