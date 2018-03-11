# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:25:44 2018

@author: Akshay Govindaraj
"""

###### THis is the library or getting https requests from bittrex api
###### Convert response from string fromats to the appropriate varialbes

import requests
import json

##### Number of requests to simplify
### Public Information
#getmarkets - Initiated
#getcurrencies - Initiated
#getticker - Pending
#getmarketsummaries - Initiated
#    - getusdt_mrktsummary - Initiated
#getmarketsummary - Pending
#getorderbook - Pending
#getmarkethistory - Pending

### Private Information - Pending




##### Public information functions
def bittrex_getmarkets():
    results = jsonresults("https://bittrex.com/api/v1.1/public/getmarkets")
    markets_number = len(results)
    return markets_number

def bittrex_getcurrencies():
    results = jsonresults("https://bittrex.com/api/v1.1/public/getcurrencies")
    n_currencies = len(results)
    currency_list = []
    for i in range(0,n_currencies-1):
        currency_list.append(results[i]['Currency'])
    return currency_list
 
def bittrex_getmarketsummaries():
    results = jsonresults("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    return results

def bittrex_getmarkethistory():
    results = jsonresults("https://bittrex.com/api/v1.1/public/getmarkethistory?market=USDT-BTC")
    return results

#### Sister functions
def btrx_getusdt_mrktsummary():
    results = jsonresults("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    usdt_results = []
    for i in range(0,len(results)-1):
        if 'USDT-' in results[i]['MarketName']:
            usdt_results.append(results[i])
    return usdt_results
  
##### Fetching functions
def jsonresults(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    if json_data['success'] == True:
        results = json_data['result']
        return results
    else:
        return "No response"
