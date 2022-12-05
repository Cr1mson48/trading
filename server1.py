import time
from pybit import usdt_perpetual, inverse_perpetual
from telethon import TelegramClient
from telethon.sync import TelegramClient
import threading
from telethon import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from time import sleep
import re
import random
import string
import logging
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string



#session_auth = usdt_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com",
#    api_key='fV9iCHzzWZoJc3POp0',
#    api_secret='I5mjlAgcQTf5m2Io2E9S5cTdJTr9AhbDzUVj'
#)
#session_unauth = usdt_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com"
#)
#
##API Ignat
#session_auth_2 = usdt_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com",
#    api_key='fV9iCHzzWZoJc3POp0',
#    api_secret='I5mjlAgcQTf5m2Io2E9S5cTdJTr9AhbDzUVj'
#)
#
#session_auth_3 = usdt_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com",
#    api_key='fV9iCHzzWZoJc3POp0',
#    api_secret='I5mjlAgcQTf5m2Io2E9S5cTdJTr9AhbDzUVj'
#)

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='YJ8Ptkh0j4Wve9TTet',
    api_secret='YqbiQKv6e9KOAbbI3eLRicNDsF6WvBBUIoZ5'
)
session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com"
)

#API Ignat
session_auth_2 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='26wf91Mya8j8kmAgA8',
    api_secret='8bXwuY3fUYMXqJSjnUm9LtbzuUeqtiIbKxPR'
)

session_auth_3 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='ZxFhRDOMbPEsy07Rwt',
    api_secret='1c0nbURfhXSlxcc4Jx7dqPDXeB3W3VBY2h8L'
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])

print(session_auth_2.get_wallet_balance()['result']['USDT']['equity'])
balance = session_auth.get_wallet_balance()['result']['USDT']['equity']
balance2 = session_auth_2.get_wallet_balance()['result']['USDT']['equity']
order = balance / 100 * 3
print(order)
order2 = balance2 / 100 * 2
print(order2)
chats = []
last_date = None
size_chats = 200
groups=[]

v1_old = ''
v2_old = ''
v3_old = ''
v4_old = ''
v5_old = ''
v6_old = ''

andrey = 5


orders = {}
ignat_orders = {}
maks_orders = {}
cancel_orders = {}

name = 'vip'
api_id = "26762841"                  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "7121d5eaf2355b59b7a12f0be22d2a80"              # API Hash (оттуда же)
phone_number = "+79952334882"    # Номер телефона аккаунта, с которого будет выполняться код
chat = 'https://t.me/+Gw9duznm9bc3NmE6'

ws_linear = usdt_perpetual.WebSocket(
    test=False,
    api_key="YJ8Ptkh0j4Wve9TTet",
    api_secret="YqbiQKv6e9KOAbbI3eLRicNDsF6WvBBUIoZ5",
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

ws_linear_ignat = usdt_perpetual.WebSocket(
    test=False,
    api_key="26wf91Mya8j8kmAgA8",
    api_secret="8bXwuY3fUYMXqJSjnUm9LtbzuUeqtiIbKxPR",
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

ws_linear_maks = usdt_perpetual.WebSocket(
    test=False,
    api_key="ZxFhRDOMbPEsy07Rwt",
    api_secret="1c0nbURfhXSlxcc4Jx7dqPDXeB3W3VBY2h8L",
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)

#ws_linear_maks = usdt_perpetual.WebSocket(
#    test=False,
#    api_key="3B3Bek9eVk7HQx6cW7",
#    api_secret="uHGYQNdkABFIqlPnj9SVa9MllxsRwzF2uhNM",
#    ping_interval=30,  # the default is 30
#    ping_timeout=10,  # the default is 10
#    domain="bybit"  # the default is "bybit"
#)
#
#ws_linear_ignat = usdt_perpetual.WebSocket(
#    test=False,
#    api_key="jkVW1Q7h6GvTawBHIT",
#    api_secret="I0gX1MLecoi8SlyCIIUEWo315VrWD2bs6moL",
#    ping_interval=30,  # the default is 30
#    ping_timeout=10,  # the default is 10
#    domain="bybit"  # the default is "bybit"
#)
#
#ws_linear_maks = usdt_perpetual.WebSocket(
#    test=False,
#    api_key="3B3Bek9eVk7HQx6cW7",
#    api_secret="uHGYQNdkABFIqlPnj9SVa9MllxsRwzF2uhNM",
#    ping_interval=30,  # the default is 30
#    ping_timeout=10,  # the default is 10
#    domain="bybit"  # the default is "bybit"
#)


def thread_function():
    def handle_message(msg):
        print(msg)
        try:
            if msg['data'][0]['side'] != side:
                print(side)
                print('Прошло!')
                sl = orders[msg['data'][0]['order_link_id']]
                print(sl)
                print(session_auth.set_trading_stop(
                    symbol=sl[0],
                    side=side,
                    stop_loss=sl[1]
                ))
                for a in cancel_orders[sl[0]]:
                    print(session_auth.cancel_active_order(
                        symbol=sl[0],
                        order_link_id=a
                    ))
        except Exception as e:
            print(e)


    ws_linear.execution_stream(
        handle_message
    )
    while True:
        sleep(1)


def thread_function2():
    def handle_message2(msg):
        print(msg)
        try:
            if msg['data'][0]['side'] != side:
                print(side)
                print('Прошло!')
                sl_i = ignat_orders[msg['data'][0]['order_link_id']]
                print(sl_i)
                print(session_auth_2.set_trading_stop(
                    symbol=sl_i[0],
                    side=side,
                    stop_loss=sl_i[1]
                ))
                for g in cancel_orders[sl_i[0] + 'ignat']:
                    print(session_auth_2.cancel_active_order(
                        symbol=sl_i[0],
                        order_link_id=g
                    ))
        except Exception as e:
            print(e)


    ws_linear_ignat.execution_stream(
        handle_message2
    )
    while True:
        sleep(1)


def thread_function3():
    def handle_message3(msg):
        print(msg)
        try:
            if msg['data'][0]['side'] != side:
                print(side)
                print('Прошло!')
                sl_i = maks_orders[msg['data'][0]['order_link_id']]
                print(sl_i)
                print(session_auth_3.set_trading_stop(
                    symbol=sl_i[0],
                    side=side,
                    stop_loss=sl_i[1]
                ))
                for g in cancel_orders[sl_i[0] + 'maks']:
                    print(session_auth_3.cancel_active_order(
                        symbol=sl_i[0],
                        order_link_id=g
                    ))
        except Exception as e:
            print(e)


    ws_linear_maks.execution_stream(
        handle_message3
    )
    while True:
        sleep(1)


с = threading.Thread(target=thread_function)
i = threading.Thread(target=thread_function2)
b = threading.Thread(target=thread_function3)
с.start()
i.start()
b.start()

def order_andrey(symbol, side, qty_m, qty_2, qty_3, count_l, stop_loss, st_one, st_two ):
    limit_link_id1 = generate_random_string(8)
    limit_link_id2 = generate_random_string(8)
    print(session_auth.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Market",
        qty=round(float(qty_m), 3),
        stop_loss=stop_loss,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_one,
        qty=round(float(qty_2), 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id1,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_two,
        qty=round(float(qty_3), 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id2,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))
    cancel_orders[symbol] = [limit_link_id1, limit_link_id2]

def order_ignat_1(symbol, side, stop_loss, count_l, qty_m_ignat, qty_2_ignat, qty_3_ignat, st_one,  st_two ):
    limit_link_id1_ignat = generate_random_string(8)
    limit_link_id2_ignat = generate_random_string(8)
    #position_idx=2,
    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Market",
        qty=round(qty_m_ignat, 3),
        stop_loss=stop_loss,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_one,
        qty=round(qty_2_ignat, 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id1_ignat,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_two,
        qty=round(qty_3_ignat, 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id2_ignat,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))
    cancel_orders[symbol + 'ignat'] = [limit_link_id1_ignat, limit_link_id2_ignat]


def order_maks_1(symbol, side, stop_loss, count_l, qty_m_maks, qty_2_maks, qty_3_maks, st_one,  st_two ):
    limit_link_id1_maks = generate_random_string(8)
    limit_link_id2_maks = generate_random_string(8)
    #position_idx=2,
    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Market",
        qty=round(qty_m_maks, 3),
        stop_loss=stop_loss,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_one,
        qty=round(qty_2_maks, 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id1_maks,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Limit",
        price=st_two,
        qty=round(qty_3_maks, 3),
        stop_loss=stop_loss,
        order_link_id=limit_link_id2_maks,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))
    cancel_orders[symbol + 'maks'] = [limit_link_id1_maks, limit_link_id2_maks]

def anti_order(symbol, anti_side, tk1, tk2, tk3, anti_qty_1, anti_qty_2, anti_qty_3, price_m):
    order_link_id1 = generate_random_string(8) + '1'
    order_link_id2 = generate_random_string(8) + '2'
    order_link_id3 = generate_random_string(8) + '3'

    #position_idx=0,

    print(session_auth.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk1,
        order_type="Limit",
        qty=round(anti_qty_1, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_id1,
        reduce_only=True,
        close_on_trigger=False
    ))
    orders[order_link_id1] = [symbol, price_m]

    print(session_auth.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk2,
        order_type="Limit",
        qty=round(anti_qty_2, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_id2,
        reduce_only=True,
        close_on_trigger=False
    ))
    orders[order_link_id2] = [symbol, tk1]

    print(session_auth.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk3,
        order_type="Limit",
        qty=round(anti_qty_3, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_id3,
        reduce_only=True,
        close_on_trigger=False
    ))
    orders[order_link_id2] = [symbol, tk2]

def anti_order_ignat(symbol, anti_side, tk1, tk2, tk3, anti_qty_1_ignat, anti_qty_2_ignat, anti_qty_3_ignat, price_m):
    order_link_ignat_id1 = generate_random_string(8) + '4'
    order_link_ignat_id2 = generate_random_string(8) + '5'
    order_link_ignat_id3 = generate_random_string(8) + '6'

    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk1,
        qty=round(anti_qty_1_ignat, 3),
        order_type="Limit",
        time_in_force="GoodTillCancel",
        order_link_id=order_link_ignat_id1,
        reduce_only=True,
        close_on_trigger=False
    ))

    ignat_orders[order_link_ignat_id1] = [symbol, price_m]

    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk2,
        order_type="Limit",
        qty=round(anti_qty_2_ignat, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_ignat_id2,
        reduce_only=True,
        close_on_trigger=False
    ))

    ignat_orders[order_link_ignat_id2] = [symbol, tk1]
    print(session_auth_2.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk3,
        order_type="Limit",
        qty=round(anti_qty_3_ignat, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_ignat_id3,
        reduce_only=True,
        close_on_trigger=False
    ))
    ignat_orders[order_link_ignat_id3] = [symbol, tk2]


def anti_order_maks(symbol, anti_side, tk1, tk2, tk3, anti_qty_1_maks, anti_qty_2_maks, anti_qty_3_maks, price_m):
    order_link_maks_id1 = generate_random_string(8) + '4'
    order_link_maks_id2 = generate_random_string(8) + '5'
    order_link_maks_id3 = generate_random_string(8) + '6'

    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk1,
        qty=round(anti_qty_1_maks, 3),
        order_type="Limit",
        time_in_force="GoodTillCancel",
        order_link_id=order_link_maks_id1,
        reduce_only=True,
        close_on_trigger=False
    ))

    maks_orders[order_link_maks_id1] = [symbol, price_m]

    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk2,
        order_type="Limit",
        qty=round(anti_qty_2_maks, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_maks_id2,
        reduce_only=True,
        close_on_trigger=False
    ))

    maks_orders[order_link_maks_id2] = [symbol, tk1]
    print(session_auth_3.place_active_order(
        symbol=symbol,
        side=anti_side,
        price=tk3,
        order_type="Limit",
        qty=round(anti_qty_3_maks, 3),
        time_in_force="GoodTillCancel",
        order_link_id=order_link_maks_id3,
        reduce_only=True,
        close_on_trigger=False
    ))
    maks_orders[order_link_maks_id3] = [symbol, tk2]


old_message = ''
print('Запуск')
with TelegramClient(name, api_id, api_hash) as client2:
    for dialog in client2.iter_dialogs():
        if dialog.name == "VIP 3.0 HANDMADE":
            my_private_channel = dialog
            my_private_channel_id = dialog.id
            break

while True:
    try:
        for x in range(1,5):
            if x == 1:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 3.0 HANDMADE":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v1 = my_private_channel.message.message
                            break
            if x == 2:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 4.0 BEAUTIFUL":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v2 = my_private_channel.message.message
                            break
            if x == 3:
                with TelegramClient(name, api_id, api_hash) as client2:
                    for dialog in client2.iter_dialogs():
                        if dialog.name == "VIP 5.0 INTRADAY":
                            my_private_channel = dialog
                            my_private_channel_id = dialog.id
                            v3 = my_private_channel.message.message
                            break


            if v1_old != my_private_channel.message.message and v2_old != my_private_channel.message.message and v3_old != my_private_channel.message.message:
                new_message = my_private_channel.message.message
                if '#SHORT' in new_message or '#LONG' in new_message:
                    if '#SHORT' in new_message:
                        poss = 'SHORT'
                    if '#LONG' in new_message:
                        poss = 'LONG'
                    if 'Take Profit' in new_message:
                        print('Прошло 3')
                        if 'Stop Loss' in new_message or 'Stop loss' in new_message:
                            print('Прошло 4')
                            lines = new_message.split('\n')
                            for i in lines:
                                if 'Пара' in i:
                                    for j in i.split(' '):
                                        if j[0] == '#':
                                            symbol = j[1:]
                                            try:
                                                print(session_auth.position_mode_switch(
                                                    symbol=symbol,
                                                    mode="BothSide"
                                                ))
                                            except Exception as e:
                                                print(e)
                                            try:
                                                print(session_auth_2.position_mode_switch(
                                                    symbol=symbol,
                                                    mode="BothSide"
                                                ))
                                            except Exception as e:
                                                print(e)
                                            try:
                                                print(session_auth_3.position_mode_switch(
                                                    symbol=symbol,
                                                    mode="BothSide"
                                                ))
                                            except Exception as e:
                                                print(e)
                                            try:
                                                print(session_auth.cross_isolated_margin_switch(
                                                    symbol=symbol,
                                                    is_isolated=False,
                                                    buy_leverage=20,
                                                    sell_leverage=20
                                                ))
                                                print(session_auth_2.cross_isolated_margin_switch(
                                                    symbol=symbol,
                                                    is_isolated=False,
                                                    buy_leverage=20,
                                                    sell_leverage=20
                                                ))
                                                print(session_auth_3.cross_isolated_margin_switch(
                                                    symbol=symbol,
                                                    is_isolated=False,
                                                    buy_leverage=20,
                                                    sell_leverage=20
                                                ))
                                            except Exception as e:
                                                print(e)

                                            try:
                                                print(session_auth.set_leverage(
                                                    symbol=symbol,
                                                    buy_leverage=20,
                                                    sell_leverage=20
                                                ))
                                                print(session_auth_2.set_leverage(
                                                    symbol=symbol,
                                                    buy_leverage=20,
                                                    sell_leverage=20
                                                ))
                                                print(session_auth_3.set_leverage(
                                                    symbol=symbol,
                                                    buy_leverage=20,
                                                    sell_leverage=20
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
                                    print(tk1)
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
                                if 'Stop Loss' in i or 'Stop loss' in i:
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
                            balance_ignat = session_auth_2.get_wallet_balance()['result']['USDT']['equity']
                            balance_maks = session_auth_3.get_wallet_balance()['result']['USDT']['equity']
                            order = float(balance) / 100 * 4
                            order_ignat = float(balance_ignat) / 100 * 3
                            order_maks = float(balance_maks) / 100 * 4
                            qty = float(order) / float(price)
                            qty_ignat = float(order_ignat) / float(price)
                            qty_maks = float(order_maks) / float(price)
                            qty = qty * 20
                            qty2_ignat = qty_ignat * 20
                            qty2_maks = qty_maks * 20
                            qty_m = qty / 100 * float(market_procent[0:-1])
                            qty_2 = qty / 100 * float(st_one_procent[0:-1])
                            qty_3 = qty / 100 * float(st_two_procent[0:-1])
                            qty_m_ignat = qty2_ignat / 100 * float(market_procent[0:-1])
                            qty_2_ignat = qty2_ignat / 100 * float(st_one_procent[0:-1])
                            qty_3_ignat = qty2_ignat / 100 * float(st_two_procent[0:-1])
                            qty_m_maks = qty2_maks / 100 * float(market_procent[0:-1])
                            qty_2_maks = qty2_maks / 100 * float(st_one_procent[0:-1])
                            qty_3_maks = qty2_maks / 100 * float(st_two_procent[0:-1])
                            anti_qty_1 = qty_m / 100 * 30
                            anti_qty_2 = qty_m / 100 * 50
                            anti_qty_3 = qty_m / 100 * 20
                            anti_qty_1_ignat = qty_m_ignat / 100 * 30
                            anti_qty_2_ignat = qty_m_ignat / 100 * 50
                            anti_qty_3_ignat = qty_m_ignat / 100 * 20
                            anti_qty_1_maks = qty_m_maks / 100 * 30
                            anti_qty_2_maks = qty_m_maks / 100 * 50
                            anti_qty_3_maks = qty_m_maks / 100 * 20
                            print(f'Qty_m {qty_m} qty_2 {qty_2} qty_3 {qty_3}')
                            print(f'Procent {st_one_procent[0:-1]}')
                            if poss == 'SHORT':
                                side = 'Sell'
                                anti_side = 'Buy'
                            if poss == 'LONG':
                                side = 'Buy'
                                anti_side = 'Sell'
                            count = 2
                            count_l = 2
                            if len(str(tk1)) <= 5:
                                count = 2
                            else:
                                count = int(len(str(tk1))) - 3
                            if len(str(stop_loss)) <= 5:
                                count_l = 2
                            else:
                                count_l = int(len(str(tk1))) - 3
                            order_andrey(symbol, side, qty_m, qty_2, qty_3, count_l, stop_loss, st_one, st_two)
                            order_ignat_1(symbol, side, stop_loss, count_l, qty_m_ignat, qty_2_ignat, qty_3_ignat, st_one,  st_two)
                            order_maks_1(symbol, side, stop_loss, count_l, qty_m_maks, qty_2_maks, qty_3_maks, st_one, st_two)
                            anti_order(symbol, anti_side, tk1, tk2, tk3, anti_qty_1, anti_qty_2, anti_qty_3, market)
                            anti_order_ignat(symbol, anti_side, tk1, tk2, tk3, anti_qty_1_ignat, anti_qty_2_ignat,
                                             anti_qty_3_ignat, market)
                            anti_order_maks(symbol, anti_side, tk1, tk2, tk3, anti_qty_1_maks, anti_qty_2_maks,
                                            anti_qty_3_maks, market)
                        except Exception as e:
                            if x == 1:
                                v1_old = v1
                            if x == 2:
                                v2_old = v2
                            if x == 3:
                                v3_old = v3
                            print(e)
            if x == 1:
                v1_old = v1
            if x == 2:
                v2_old = v2
            if x == 3:
                v3_old = v3
    except Exception as r:
        if x == 1:
            v1_old = v1
        if x == 2:
            v2_old = v2
        if x == 3:
            v3_old = v3
        print(r)
