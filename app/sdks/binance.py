import hashlib
import time
import requests
from requests.auth import AuthBase


class Client:
    def __init__(self, key, secret):
        self.url = 'https://www.binance.com/api/v1'
        self.auth = BinanceAuth(api_key=key, secret_key=secret)

    def get_accounts(self):
        r = requests.get(self.url + '/account', auth=self.auth)
        return r.json()


class BinanceAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(round(time.time()*1000))
        from urllib import parse
        q = parse.urlparse(request.path_url).query
        q_pre = '?'
        if q:
            q_pre = '&'
        request.url = request.url + f'{q_pre}timestamp={timestamp}'
        message = f'{self.secret_key}|{request.url.split("?")[1]}'
        message = message.encode('ascii')
        signature = hashlib.sha256(message).hexdigest()
        request.headers.update({
            'Content-Type': 'application/json',
            'X-MBX-APIKEY': self.api_key,
        })
        request.url = request.url + f'&signature={signature}'
        return request
