import requests

from app.connectors.btrx import BittRex
from app.connectors.coinbase import CoinBase
from app.connectors.gdax import Gdax
from app.connectors.binance import Binance

BASE = 'https://api.coinmarketcap.com/v1/ticker'
r = requests.get(f'{BASE}/?convert=USD&limit=500')
CACHE = r.json()
BTCPRICE = price = [x for x in CACHE if x['symbol'] == 'BTC'][0]


def normalize(coins):
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
    return n_coins


def print_values(name, coin):
    for x in coin:
        print('Name:', x['name'],
              '| Amount:', x['amount'],
              '| Value:', format(x['value'], '.2f'))
    total = sum([x['value'] for x in coin])
    print(f'{name}Total:', total)
    return total


def run():
    b = BittRex()
    c = CoinBase()
    g = Gdax()
    bi = Binance()

    total = 0
    _coinbase = normalize(c.get_coins())
    _bittrex = normalize(b.get_coins())
    _gdax = normalize(g.get_coins())
    _binance = normalize(bi.get_coins())
    total += print_values('Gdax', _gdax)
    total += print_values('Coinbase', _coinbase)
    total += print_values('Bittrex', _bittrex)
    total += print_values('Binance', _binance)
    percent_win = format(total / 356 * 100 - 100, '.2f')
    number_win = format(total - 356, '.2f')
    print(f'\nTotal: {format(total, ".2f")} '
          f'| %{percent_win} '
          f'| ${number_win}')

