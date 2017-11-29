from app.connectors.gdax import Gdax
import yaml
import os
import time
import gdax as g
from pprint import pprint

f = yaml.load(open('env.yml'))
for x in f:
    os.environ[x] = f[x]

gdax = Gdax()


btc = 0.03795374
arstnew = 0.0384111


class myWebsocketClient(g.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["BTC-USD"]
        self.price = 0.00
        self.buys = []
        self.sells = []
        self.last_trade_sides = []
        self.counts = 100
        self.last_fill = None
        print("Lets count the messages!")

    def on_message(self, msg):
        if msg.get('type') not in ['open', 'done', 'received']:
            self.price = msg.get('price')
            self.last_trade_sides.insert(0, msg.get('side'))
            if msg.get('side') == 'sell':
                self.sells.insert(0, float(msg.get('size')))
            if msg.get('side') == 'buy':
                self.buys.insert(0, float(msg.get('size')))
            if len(self.last_trade_sides) > self.counts:
                self.last_trade_sides.pop()
                if msg.get('side') == 'sell':
                    self.sells.pop()
                if msg.get('side') == 'buy':
                    self.buys.pop()

            print(format(float(self.price), '.2f'), '|',
                  self.last_trade_sides.count('sell'), '/',
                  self.last_trade_sides.count('buy'), '|',
                  format(sum(self.sells), '.2f'), '/',
                  format(sum(self.buys), '.2f')
                  )
            self.check_for_transaction_condition()

    def on_close(self):
        print("-- Goodbye! --")

    def check_for_transaction_condition(self):
        if self.last_fill is None:
            print('\n\n\n\n', 'here', '\n\n\n\n\n\n\n\n')
            self.last_fill = gdax._client.get_fills(product_id='BTC-USD')[0][0]
        pprint(self.last_fill)


try:
    wsClient = myWebsocketClient()
    wsClient.start()
    print(wsClient.url, wsClient.products)
    while (True):
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    wsClient.close()


# for coin in gdax.get_coins():
#    print(coin)
