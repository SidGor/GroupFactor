# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:20:49 2018

Introducing TuShare Library to save my ass on data source issues.

@author: szlsd
"""

import pandas as pd
import tushare as ts

def TokenSetup(token):
#    You should have a Tushare account and token to access the data.
    try:
        ts.set_token(token)
    except Exception as e:
        return(e)
        

def UpdateBasicStockInfo():
# function to setup a local csv data with stock basic information        
    pro = ts.pro_api()        
    
    basic_data = pro.stock_basic()
    basic_data.to_csv("D:/PythonDir/tusharedata/listing_StockInfo.csv", index = False, encoding = "gbk")
    
#    pd.read_csv("D:/PythonDir/tusharedata/listing_StockInfo.csv",  encoding = "gbk", dtype = 'str') #just for checking
      