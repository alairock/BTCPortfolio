

class ExchangeInterface:
    def get_coins(self):
        """ Should return
        [{'amount': '0.00000000', 'name': 'LTC Wallet', 'type': 'LTC'}, ...]
        """
        raise Exception('You mest implement get_coins()')

    def get_btc_value(self):
        raise Exception('You mest implement get_btc_value()')

    def get_usd_value(self):
        raise Exception('You mest implement get_usd_value()')

