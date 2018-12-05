# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:24:50 2018

Aiming to provide mothods in dealing with recently IPO companies(hard to trade
and have total different behavior in China) or suspension stocks(also an unique
situation in China that stocks will be suspended from trading for days even years.)

@author: szlsd
"""

import pandas as pd
import numpy as np
import datetime
import GroupFactor

raw_data = pd.read_csv('D:/PythonDir/winddata/AS_%Ret20040101_20181113_wkly.csv')
o_file = open('D:/PythonDir/tusharedata/listing_StockInfo.csv')
IPO_table = pd.read_csv(o_file, dtype = 'str')

def RmvNewStocks(raw_data, IPO_table, silience_date = 30):
    
    IPO_table.list_date = IPO_table.list_date.apply(lambda x: datetime.datetime.strptime(x, '%Y%m%d'))
    raw_data.Date = raw_data.Date.apply(lambda x: datetime.datetime.strptime(x, '%Y/%m/%d'))
    
    NotIn_list = list(set(raw_data.columns.drop('Date')) - set(IPO_table.ts_code))
    
    
    
    pass

