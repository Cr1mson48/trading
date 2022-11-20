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
    endpoint="https://api.bybit.com",
    api_key='H9X78xMQgIP5yDSyok',
    api_secret='YeQTC5zNr7PvHcmjwkJVBFywPnie9pdLe0cw'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com"
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])
balance = session_auth.get_wallet_balance()['result']['USDT']['equity']
order = balance / 100 * 5
print(order)

chats = []
last_date = None
size_chats = 200
groups=[]


name = 'vip'
api_id = "26762841"                  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "7121d5eaf2355b59b7a12f0be22d2a80"              # API Hash (оттуда же)
phone_number = "+79952334882"    # Номер телефона аккаунта, с которого будет выполняться код
chat = 'https://t.me/+Gw9duznm9bc3NmE6'

old_message = ''

with TelegramClient(name, api_id, api_hash) as client2:
    for dialog in client2.iter_dialogs():
        if dialog.name == "VIP 2.0 SCALP":
            my_private_channel = dialog
            my_private_channel_id = dialog.id
            break

while True:
    try:
        for i in range(1,6):
            if i == 1:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 2.0 SCALP":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v2 = my_private_channel.message.message
                            break
            if i == 2:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 3.0 HANDMADE":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v3 = my_private_channel.message.message
                            break
            if i == 3:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 4.0 BEAUTIFUL":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v4 = my_private_channel.message.message
                            break
            if i == 4:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 5.0 INTRADAY":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v5 = my_private_channel.message.message
                            break
            if i == 5:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "Indicator by Cryptonec":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v5 = my_private_channel.message.message
                            break
            print(my_private_channel.message.message)
            if v2 != my_private_channel.message.message and v3 != my_private_channel.message.message and v4 != my_private_channel.message.message\
                    and v5 != my_private_channel.message.message:
                new_message = my_private_channel.message.message
                if ('#SHORT' in new_message or '#LONG' in new_message) and '#SUPER_SCALPING_SESSION' not in new_message:
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
                                                print(session_auth.cross_isolated_margin_switch(
                                                    symbol=symbol,
                                                    is_isolated=True,
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
                                    qty=round(qty, 3),
                                    take_profit=tk1,
                                    stop_loss=stop_loss,
                                    time_in_force="GoodTillCancel",
                                    reduce_only=False,
                                    close_on_trigger=False
                                ))
                            except Exception as e:
                                print(e)
                elif '#SUPER_SCALPING_SESSION' in new_message:
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
                                        print(session_auth.cross_isolated_margin_switch(
                                            symbol=symbol,
                                            is_isolated=True,
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

            if i == 1:
                v2_old = v2
            if i == 2:
                v3_old = v3
            if i == 3:
                v4_old = v4
            if i == 4:
                v5_old = v5
    except Exception as r:
        print(r)