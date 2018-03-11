# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 01:53:20 2018

@author: Akshay Govindaraj
"""

# This file fetches JSON requests

import requests
import json
import datetime
import matplotlib.pyplot as plt

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
json_data = json.loads(response.text)
print(json_data['bpi']['USD']['rate_float'])

response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json")
btc_hist = json.loads(response.text)
btc_hist_list = btc_hist['bpi']

#Get the date list
n_days = len(btc_hist['bpi'])
today = datetime.datetime.today()

date_list = []
for i in range(0,n_days):
    date_list.append(today - datetime.timedelta(days = (n_days-i+1) ))

# Getting the price in a list
btc_price = []
for i in range(0,n_days-1):
    btc_price.append(btc_hist_list[date_list[i].strftime('%Y-%m-%d')])

#Plotting BTC price chart
plt.plot(date_list, btc_price)
plt.show()
