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

## Run
`$ python run.py`

To watch the market, I have a watch file for watching gdax realtime BTC exchange prices. 
`$ python watch.py`
