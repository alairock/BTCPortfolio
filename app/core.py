import requests
import time
import datetime
from app.connectors.btrx import BittRex
from app.connectors.coinbase import CoinBase
from app.connectors.gdax import Gdax
from app.connectors.binance import Binance
import os
import errno

BASE = 'https://api.coinmarketcap.com/v1/ticker'
r = requests.get(f'{BASE}/?convert=USD&limit=500')
CACHE = r.json()
BTCPRICE = price = [x for x in CACHE if x['symbol'] == 'BTC'][0]

VERBOSE = 0


def normalize(name, coins):
    n_coins = []
    for coin in coins:
        n_coin = {}
        amount = coin.pop('amount')
        price = [x for x in CACHE if x['symbol'] == coin['type']]
        price = {} if len(price) <= 0 else price[0]
        value = float(amount) * float(price.get('price_usd', 0))
        n_coin.update(coin)
        n_coin.update({'value': value})
        n_coin.update({'amount': amount})
        n_coins.append(n_coin)
        track_balance(
            name, n_coin['name'], n_coin['amount'], n_coin['value'],
            float(price.get('price_usd', 0))
        )
    if VERBOSE == 1:
        print_values(n_coins)
    total = sum_stuff(n_coins)
    print(f'{name}Total:', total)
    return total


def sum_stuff(coin):
    return sum(x['value'] for x in coin)


def print_values(coin):
    for x in coin:
        print('Name:', x['name'],
              '| Amount:', x['amount'],
              '| Value:', format(x['value'], '.2f'))


def track_balance(name, coin, amount, value, market_value):
    filename = 'logs.csv'
    if VERBOSE == 1:
        print(f'{name},{coin},{amount},{value},{market_value}')
    try:
        h = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    else:
        with os.fdopen(h, 'w') as fo:
            fo.write("date,name,coin,amount,value,market_value\n")
    with open(filename, 'a') as fo:
        new_time = datetime.datetime. \
            fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        fo.write(f'{new_time},{name},{coin},{amount},{value},{market_value}\n')


def run():
    b = BittRex()
    c = CoinBase()
    g = Gdax()
    bi = Binance()

    total = 0
    _coinbase = normalize('Coinbase', c.get_coins())
    _bittrex = normalize('Bittrex', b.get_coins())
    _gdax = normalize('Gdax', g.get_coins())
    _binance = normalize('Binance', bi.get_coins())

    total = _binance + _gdax + _bittrex + _coinbase
    percent_win = format(total / 356 * 100 - 100, '.2f')
    number_win = format(total - 356, '.2f')
    print(f'\nTotal: {format(total, ".2f")} '
          f'| %{percent_win} '
          f'| ${number_win}')

