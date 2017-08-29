import os

from coinbase.wallet.client import Client

from app.connectors.excint import ExchangeInterface


class CoinBase(ExchangeInterface):
    def __init__(self):
        self._client = Client(
            os.getenv('coinbase_api_key'),
            os.getenv('coinbase_api_secret'))

    def get_coins(self):
        accounts = self._client.get_accounts()
        assert isinstance(accounts.data, list)
        assert accounts[0] is accounts.data[0]
        assert len(accounts[::]) == len(accounts.data)
        for account in accounts.get('data'):
            if float(account['balance']['amount']) != 0.0:
                coin = {}
                coin.update({'name': account['currency']})
                coin.update({'type': account['currency']})
                coin.update(
                    {'amount':
                         format(float(account['balance']['amount']), '.8f')})
                yield coin
