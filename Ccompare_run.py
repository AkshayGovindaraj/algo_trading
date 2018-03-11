# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 02:43:18 2018

@author: Akshay Govindaraj
"""

#### File to check source data from 

# Example requests
#https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=JPY,EUR
#https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR

import requests
import json
from matplotlib import pyplot as plt

# Single price request
url_base_1 = 'https://min-api.cryptocompare.com/data/price?'
url_base_2 = 'https://min-api.cryptocompare.com/data/pricemulti?'

# Preparing the query
target = 'BTC,ETH,LTC,XMR'
benchmark = 'USD'
url = url_base_2 + 'fsyms=' + target + '&' + 'tsyms=' + benchmark

# Retrieving Data
response = requests.get(url)
json_data = json.loads(response.text)

# Converting to lists
keys_list = []
values_list = []
for key, value in json_data.items():
    keys_list.append(key)
    values_list.append(value)

# Plotting the data
plt.bar(keys_list,values_list)
plt.show()