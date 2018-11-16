# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:59:15 2018

@author: szlsd
"""

import pandas as pd
import numpy as np
import matplotlib

# test environment

test_data = pd.read_csv("D:/PythonDir/winddata/AS_Mcap20040101_20181113_wkly.csv")

def SummaryCSdata(dataframe, NAasZero = False):
    # test
    # dataframe = test_data
    
    class InputError(Exception):
        pass
    
    if type(dataframe) != pd.DataFrame:
        raise InputError("Pandas dataframe as input only!")
    else:
        CountRows = dataframe.shape[0]
        CountCols = dataframe.shape[1]
        
        if NAasZero == True:
            dataframe = dataframe.replace(0,np.nan)
        
        summaries = dict()
        summaries['mean'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().mean(), axis = 1)
        summaries['median'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().describe(percentiles = [i/10 for i in range(0, 10, 2)])['50%'], axis = 1)        
        summaries['kurtosis'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().kurtosis(), axis = 1)
        summaries['skewness'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().skew(), axis = 1)
        summaries['tile_20'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().describe(percentiles = [i/10 for i in range(0, 10, 2)])['20%'], axis = 1)      
        summaries['tile_40'] =dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().describe(percentiles = [i/10 for i in range(0, 10, 2)])['40%'], axis = 1)      
        summaries['tile_60'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().describe(percentiles = [i/10 for i in range(0, 10, 2)])['60%'], axis = 1)      
        summaries['tile_80'] = dataframe.drop("Date", axis = 1).apply(func = lambda x:x.dropna().describe(percentiles = [i/10 for i in range(0, 10, 2)])['80%'], axis = 1)      
        

        return {'Cdata':dataframe, 'Periods': CountRows, 'MaxStockNum':CountCols, 'Summaries':summaries}