# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:07:30 2018

@author: Akshay Govindaraj
"""

##### This script is used to fetch market data 
##### Source : CoinApi

apikey = "A908490D-575F-47AB-B729-3C9553F5990A"

import requests
import json


#url = 'https://rest.coinapi.io/v1/exchanges'
#headers = {'X-CoinAPI-Key' : apikey}
#response = requests.get(url, headers=headers)

### CoinApi General functions
def CA_excnginfo():
    url = 'https://rest.coinapi.io/v1/exchanges'
    return coin_json(url)

def CA_assetsinfo():
    url = 'https://rest.coinapi.io/v1/assets'
    return coin_json(url)

def CA_symbolsinfo():                                 ### Returns a very huge dataset. Be Careful
    url = 'https://rest.coinapi.io/v1/symbols'
    return coin_json(url)

### Exchange Rate Functions
def CA_currentrate(target = 'BTC', reference = 'USD'):  #For One pair
    url = 'https://rest.coinapi.io/v1/exchangerate/' + target + '/' + reference
    return coin_json(url)

def CA_allrates(target = 'BTC'):                       #Better function to reduce no. of requests
    url = 'https://rest.coinapi.io/v1/exchangerate/' + target
    return coin_json(url)

### OHLCV Data
def CA_periods():                                       # Retruns identifiers for different time periods
    url = 'https://rest.coinapi.io/v1/ohlcv/periods'
    return coin_json(url)

def CA_fetchdata(symbol='BITSTAMP_SPOT_BTC_USD', period = '1MIN'):
    url = 'https://rest.coinapi.io/v1/ohlcv/' + symbol + '/latest?period_id=' + period
    return coin_json(url)
    
### Data Retreival
def coin_json(url):
    headers = {'X-CoinAPI-Key' : apikey}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    return json_data
