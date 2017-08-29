import os
from app.sdks.binance import Client
from app.connectors.excint import ExchangeInterface


class Binance(ExchangeInterface):
    def __init__(self):
        self._client = Client(os.getenv('binance_api_key'),
                              os.getenv('binance_api_secret'))

    def get_coins(self):
        accounts = self._client.get_accounts().get('balances')
        for account in accounts:
            if float(account['free']) != 0.0:
                coin = {}
                coin.update({'name': account['asset']})
                coin.update({'type': account['asset']})
                coin.update({'amount': format(float(account['free']), '.8f')})
                yield coin
