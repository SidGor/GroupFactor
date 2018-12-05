# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:24:50 2018

Aiming to provide mothods in dealing with recently IPO companies(hard to trade
and have total different behavior in China) or suspension stocks(also an unique
situation in China that stocks will be suspended from trading for days even years.)

@author: szlsd
"""

import pandas as pd
import GroupFactor

raw_data = pd.read_csv('D:\PythonDir\winddata\AS_%Ret20040101_20181113_wkly.csv')
IPO_table = pd.read_csv('D:\PythonDir\winddata\AS_IPOdate20040101_20181113_wkly.csv')

def RmvNewStocks(raw_data, IPO_table, silience_date = 30):
    pass
