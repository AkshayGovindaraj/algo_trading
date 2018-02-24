# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 02:12:52 2018

@author: Akshay Govindaraj
"""

######### A trial script

from bittrex_api import bittrex_getmarketsummaries

markets = bittrex_getmarketsummaries()

if 'BTC-' in markets[1]['MarketName']:
    print('True')
else:
    print('False')