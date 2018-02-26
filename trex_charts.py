# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:44:30 2018

@author: Akshay Govindaraj
"""

##### THis file is used for the basic analysis of bittrex data
##### Output charts in a descriptive format

from bittrex_api import btrx_getusdt_mrktsummary
from matplotlib import pyplot as plt

def vol_graph():                    #THrough Bittrex API
    usdt = btrx_getusdt_mrktsummary()
    ccy_list = []
    vol_list = []
    for i in range(0,len(usdt)-1):
        ccy_list.append(usdt[i]['MarketName'].replace('USDT-',''))
        vol_list.append(usdt[i]['Volume']*usdt[i]['Last'])
    plt.bar(ccy_list,vol_list)
    plt.show()

#plt.savefig("figure.pdf")