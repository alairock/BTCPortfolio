import os

from bittrex.bittrex import Bittrex

from app.connectors.excint import ExchangeInterface


class BittRex(ExchangeInterface):
    def __init__(self):
        self._client = Bittrex(api_key=os.getenv('bittrex_api_key'),
                               api_secret=os.getenv('bittrex_api_secret'))
        r = self._client.get_balances()
        if not r.get('success'):
            if r.get('message') == 'APIKEY_INVALID':
                raise Exception('Invalid API Keys')
            raise Exception('Error: ' + r.get('message'))

    def get_coins(self):
        accounts = self._client.get_balances().get('result')
        for account in accounts:
            if float(account['Balance']) != 0.0:
                coin = {}
                coin.update({'name': account['Currency']})
                coin.update({'type': account['Currency']})
                coin.update({'amount': format(float(account['Balance']), '.8f')})
                yield coin
