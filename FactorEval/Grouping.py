# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:02:53 2018

Provides grouping methods for intial evaluation.

Starting with grouping performance functino and FF sorting methods

@author: szlsd
"""

# should be calling from SmryDist so that we can have a somewhat clearer dataset.

# 1. single sorting and return performance by groups(plots and data)
    
    #input1: a table containing factor value and ticker and dates
    #input2: a table containing returns of each stock(should have same time structure as input1(check on datetime))
    #output1: 
# 2. double sorting and return performance by groups(plots and data)
    
import pandas as pd
import numpy as np
import datetime
import sys
import copy
import datetime

sys.path.insert(0, 'D:/PythonDir')  # to enable SummaryCSdata import, shall be updated later

from GroupFactor.FactorDist.SmryDist import SummaryCSdata # should have a much more elengent way once formed a package


# test_data = pd.read_csv("D:/PythonDir/winddata/AS_Mcap20040101_20181113_wkly.csv")
# test_sum = SummaryCSdata(test_data, NAasZero = True)
# test_ret_date = pd.read_csv("D:/PythonDir/winddata/AS_%Ret20040101_20181113_wkly.csv")

def Fsort(series, levels = 5, sortMtd = "q", ascending = True):
    
    #Test
    # series = dataframe.loc[0]
    s_series = copy.copy(series).drop('Date').dropna().sort_values(ascending = ascending)
    n_series = copy.copy(series)
    group_dict = {}
    if sortMtd == "q":
        for i in range(1,levels + 1):
            group_dict['G' + str(i)] = s_series[int(((i-1)/levels)*len(s_series)) : int(((i)/levels)*len(s_series))]
            n_series.loc[group_dict['G' + str(i)].index] = i

        
    return n_series
    # currently we support only 1 methods by quantile 
    
def SglSort(INdataframe, levels = 5, sortMtd = "q", ascending = True):
    
    dataframe = copy.copy(INdataframe)
    
    class InputError(Exception):
        pass
    
    if type(dataframe) != pd.DataFrame:
        raise InputError("Pandas dataframe as input only!")
    else:
        dataframe = dataframe.apply(Fsort, axis = 1)    
#            print("%s row done" % j)        
    return(dataframe)

    # define groups
    # dataframe = test_sum['Cdata']
    # 1. generate groups
    # 2. 
    
a = datetime.datetime.now()    
    
test = SglSort(test_sum['Cdata']) 

datetime.datetime.now() - a

def DblSort(dataframe_a, dataframe_b, level_a = 5, level_b = 5):
    
    pass


    
    
    