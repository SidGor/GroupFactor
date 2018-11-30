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
import itertools

sys.path.insert(0, 'D:/PythonDir')  # to enable SummaryCSdata import, shall be updated later

from GroupFactor.FactorDist.SmryDist import SummaryCSdata # should have a much more elengent way once formed a package


# test_data = pd.read_csv("D:/PythonDir/winddata/AS_Mcap20040101_20181113_wkly.csv")
# test_sum = SummaryCSdata(test_data, NAasZero = True)
# test_ret_data = pd.read_csv("D:/PythonDir/winddata/AS_%Ret20040101_20181113_wkly.csv")

def Fsort(series, levels = 5, sortMtd = "q", ascending = True):
    
    #Test
    # series = dataframe.loc[0]
    if 'Date' in series.index:
        s_series = copy.copy(series).drop('Date').dropna().sort_values(ascending = ascending)
    else:
        s_series = copy.copy(series).dropna().sort_values(ascending = ascending)
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
        dataframe = dataframe.apply(Fsort, axis = 1, levels = levels)    
#            print("%s row done" % j)        
    return(dataframe)

    # define groups
    # dataframe = test_sum['Cdata']
    # 1. generate groups
    # 2. 
    
#a = datetime.datetime.now()     #performance test
#    
#test = SglSort(test_sum['Cdata']) 
#
#datetime.datetime.now() - a     # should return within 6 sec for test data.

# dataframe.groupby(by = ['Date']).apply(lambda df:Fsort(pd.Series([df.T]))) an example for groupby and apply

def DblSort(dataframe_a, dataframe_b, future_ret_df, level_a = 5, level_b = 5,  ret_data_type = 'w'):
    
    Asorted_df = SglSort(dataframe_a, levels = level_a)
    Bsorted_df = SglSort(dataframe_b, levels = level_b)
    result_dict = {} # to save the results
    
# test environment
#     dataframe_a = pd.read_csv("D:/PythonDir/winddata/AS_Mcap20040101_20181113_wkly.csv")
#     dataframe_b = pd.read_csv("D:/PythonDir/winddata/AS_B2P20040101_20181113_wkly.csv")
#     
#     ret_data = pd.read_csv("D:/PythonDir/winddata/AS_%Ret20040101_20181113_wkly.csv") # remember to check for forward looking error
#    future_ret_df = pd.concat([ret_data.Date, ret_data.drop('Date', axis = 1).shift(-1, )],axis = 1)
##########################################    
    C_df = copy.copy(Asorted_df)
        
    C_df.iloc[:,1:] = Asorted_df.iloc[:,1:].applymap(lambda x:'(' + format(x,'.0f') + ', ') + Bsorted_df.iloc[:,1:].applymap(lambda x:format(x,'.0f') + ')')
    
    combinations = list(itertools.product(*[list(range(1,level_a + 1)),list(range(1,level_b + 1))]))  #In the future we shall see how to do 2x2x2x2 sorting by changing the iter lists here
    
    
    
    for i in range(0,len(combinations)):
        subset_df = C_df.drop('Date', axis = 1) == str(combinations[i])
        sector_ret_df = pd.concat([future_ret_df.Date,future_ret_df.drop('Date', axis = 1)[subset_df]], axis = 1)
        retNV_series = ((sector_ret_df.drop('Date', axis = 1).mean(axis = 1))/100) + 1
        ttl_NV = retNV_series.prod()
        
        if ret_data_type == 'w':
            
            annual_ret = ttl_NV**(52/len(retNV_series.dropna())) - 1
            result_dict['A%s-B%s' % (combinations[i][0],combinations[i][1])] = annual_ret
            
        else:
            return('Currently support weekly data only')
            
            
    return(result_dict)

a = datetime.datetime.now()     #performance test
    
"""
%%timeit
"""
DblSort(dataframe_a, dataframe_b, future_ret_df)

datetime.datetime.now() - a     # should return within 6 sec for test data.   
    
    