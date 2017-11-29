# BTCPortfolio

This is some work that I did to manage my cryptocurrency portfolio as I was trying to play with other exchanges and currencies.

This project serves as a simple example of connecting to those exchanges and reading out your converted profit/losses. 

BTCPortfolio uses an interface to denormalize the various API's and SDK's you have to interact with across exchanges/currencies. These are not at all fleshed out, but someday that would might be something this could become. 

## Requirements
Python 3.5 (Newer versions of Python will probably work as well)

## Install

Clone this repository, then 

`$ python3 -m venv venv`

`$ ./venv/bin/activate`

`$ pip install -r requirements`

## Configure

A sample configuration file might look like: 

- env.yml
```
bittrex_api_key: XXXXXXXXXXX
bittrex_api_secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

coinbase_api_key: XXXXXXXXXXXXXXXXX
coinbase_api_secret: XXXXXXXXXXXXXXXXXXXXXXX

binance_api_key: XXXXXXXXXXXXXXXXXXXXXXXXX
binance_api_secret: XXXXXXXXXXXXXXXXXXXXXXXXXX

gdax_passphrase: XXXX
gdax_api_key: XXXXXXXXXXXXXXXXXXXXXXXXXXXX
gdax_api_secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Run
`$ python run.py`

To watch the market, I have a watch file for watching gdax realtime BTC exchange prices. 
`$ python watch.py`
