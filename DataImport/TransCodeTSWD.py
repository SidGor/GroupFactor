# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:26:04 2018

This function aims to transform two different coding systems into each other.
Different stock tickers(e.g., "600001.SZ" and "SZ600001") from two different 
lines of Chinese stock market systems represent exactly the same stock 
different only between coding style. Therefore, such function will prove to 
be useful in stock data manipulation especially in the case that user need to 
handle cross system comparison.

@author: szlsd
"""

import pandas as pd
test_data_1 = "SH600021"
test_data_2 = "600021.SZ"
test_data_3 = ["SH600021", "SZ300621", "SH602391"]
test_data_4 = ["600021.SH", "300621.SZ", "602391.SH"]
test_data_5 = pd.Series(test_data_4)
test_data_6 = {1:"600021.SH", 2:"300621.SZ", 3:"602391.SH"}

def TransCodeT2W(tickers):
    # Function that transform SHxxxxxx codes into xxxxxx.SH
    TofD = type(tickers)
    
    if TofD == str:
        
        converted = [tickers[2:8] + "." + tickers[0:2]]
    else :
        try:
            converted = [(i[2:8] + "." + i[0:2]) for i in tickers]
        except Exception as e:
            return e
        
    return converted


def TransCodeW2T(tickers):

    # Function that transform xxxxxx.SH codes into SHxxxxxx    
    TofD = type(tickers)
    
    if TofD == str:
        
        converted = [tickers[7:9] + tickers[0:6]]
        
    else :
        try:
            converted = [(i[7:9] + i[0:6]) for i in tickers]
        except Exception as e:
            return e
        
    return converted