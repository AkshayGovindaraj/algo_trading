# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:06:33 2018

@author: Akshay Govindaraj
"""

###### THis file tests the basic functions from CoinApi

from coinapi import CA_currentrate, CA_fetchdata
import matplotlib.pyplot as plt

btcusd = CA_currentrate('BTC', 'USD')
ethusd = CA_currentrate('ETH', 'USD')
ltcusd = CA_currentrate('LTC', 'USD')

print("Current Bitcoin Price is " + str(round(btcusd['rate'],3)) + " USD")
print("Current Ethereum Price is " + str(round(ethusd['rate'],3)) + " USD")
print("Current Litecoin Price is " + str(round(ltcusd['rate'],3)) + " USD")

# Plotting BTC price on Bitstamp for past 100 days

ts_btc = CA_fetchdata(symbol='BITTREX_SPOT_NEO_USDT', period = '1DAY')
date_list = []
price_list = []
for i in range(0, len(ts_btc)-1):
    date_list.append(ts_btc[i]['time_period_end'])
    price_list.append(ts_btc[i]['price_close'])

#Plotting BTC price chart
plt.plot(date_list, price_list)
plt.show()