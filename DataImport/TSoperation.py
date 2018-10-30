# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:48:01 2018

Provides all neccessary operational functions in the tinysoft system.

Require Python 3 environment
Require TSLPy3 package
Need Accesable TinySoft accounts


@author: szlsd
"""
import TSLPy3 as ts
import pandas as pd
import os
import datetime
import time

# 1. Login
# Please config your account information loccally, first column "Account" sec column "Password"
# TinySoft python application require local setups, please read LanguageGuide in the TS user console.

def TSreadSingleStock(Ticker, Factor = ["close"], TsAccount = None, TsPassword = None):

    
    if (TsAccount == None) or (TsPassword == None):
        
        try:
            acc_f = pd.read_csv("D:/TSaccount.csv")
        except Exception as e:
            return e

    try:

        ts.ConnectServer("tsl.tinysoft.com.cn",443) 
        
        dl = ts.LoginServer(acc_f.Account[0], acc_f.Password[0]) #Tuple(ErrNo,ErrMsg) Login
        
        
        
        ts.Disconnect()  # Log out.
        
        
    except Exception as e:
        return e
# 2. GetData


# 3. Export(save data)