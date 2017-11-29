import os

import gdax

from app.connectors.excint import ExchangeInterface


class Gdax(ExchangeInterface):
    def __init__(self):
        self._client = gdax.AuthenticatedClient(
            key=os.getenv('gdax_api_key'),
            b64secret=os.getenv('gdax_api_secret'),
            passphrase=os.getenv('gdax_passphrase'))

    def get_coins(self):
        accounts = self._client.get_accounts()
        for account in accounts:
            if float(account['balance']) != 0.0:
                coin = {}
                coin.update({'name': account['currency']})
                coin.update({'type': account['currency']})
                coin.update({'amount':
                            format(float(account['balance']), '.8f')})
                yield coin
