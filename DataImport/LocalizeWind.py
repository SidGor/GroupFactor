# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:20:38 2018

Provide methods to localize Wind data sets.

Require local access to Wind Terminal, and key words of data.

@author: szlsd
"""


from WindPy import *
import pandas as pd


def WriteWFactorData(fac_list, start_date = "2010-01-01", end_date = "2018-09-30", 
                     unit = 1, rptType = 1, currencyType = "", Period = "Q", PriceAdj = "B"):
      
    # The function downloads Chinese A stock factor data given 
    
    if len(pd.unique(fac_list)) != len(fac_list):
        raise ValueError("Duplicate elements in fac_list!")
    
    w.start()
    #test
    #fac_list = ['wgsd_net_inc','wgsd_assets','wgsd_assets']
    factors = ",".join(fac_list)
    O_arguments = "unit=%s;rptType=%s;currencyType=%s;Period=%s;PriceAdj=%s" % (unit, rptType,currencyType,Period,PriceAdj)
    
    A_Stock_Tickers_Data = w.wset("sectorconstituent","date=2018-10-30;sectorid=a001010100000000") # Get the tickers of all Chinese A-Stocks
    A_S_Ticker_t = pd.DataFrame(A_Stock_Tickers_Data.Data, columns = A_Stock_Tickers_Data.Data[1], index = ['DateTime', 'Ticker', 'Name'])
    
    # Test
    
    P_Ticker_L = list(A_S_Ticker_t.loc['Ticker'])
    
    Maj_Table = pd.DataFrame()
    
    for i in range(0,len(P_Ticker_L)):
        temp_data = w.wsd(P_Ticker_L[i], factors, start_date, end_date, O_arguments)
        temp_data.Data.append(temp_data.Codes * len(temp_data.Data[0]))
        temp_data.Data.append(temp_data.Times)
        temp_table = pd.DataFrame(data = temp_data.Data).transpose()
        temp_table.columns = temp_data.Fields + ["Ticker"] + ["Date"]
        temp_table = temp_table[['Date'] + ['Ticker'] + temp_data.Fields]
        
        Maj_Table = pd.concat([Maj_Table, temp_table], axis = 0)
        
        print("Stock %s collected" % temp_data.Codes[0])
        
        del temp_data
        
        
    Maj_Table.reset_index(drop = True)
    
    return Maj_Table


def DownloadSecData(fac_list, path, trade_date = "20100101", rpt_date = "20100630", stock_list_date = "2018-10-30",
                     unit = 1, rptType = 1, currencyType = ""):
      
    # The function downloads Chinese A stock factor data given 
    
    # Still need a module to control variable format
    
    if len(pd.unique(fac_list)) != len(fac_list):
        raise ValueError("Duplicate elements in fac_list!")
    
    w.start()
    #test
    #fac_list = ['wgsd_net_inc','wgsd_assets','wgsd_assets']
    factors = ",".join(fac_list)
    O_arguments = "unit=%s;tradeDate=%s;rptDate=%s;rptType=%s;currencyType=%s" % (unit, trade_date,rpt_date,rptType,currencyType)
    
    A_Stock_Tickers_Data = w.wset("sectorconstituent","date=%s;sectorid=a001010100000000" % stock_list_date) # Get the tickers of all Chinese A-Stocks
    A_S_Ticker_t = pd.DataFrame(A_Stock_Tickers_Data.Data, columns = A_Stock_Tickers_Data.Data[1], index = ['DateTime', 'Ticker', 'Name'])
    
    P_Ticker_L = list(A_S_Ticker_t.loc['Ticker'])
    
    out_data = w.wss(",".join(P_Ticker_L),factors,O_arguments)
    out_data.Data.append(out_data.Codes)
    out_table = pd.DataFrame(data = out_data.Data).T
    out_table.columns = out_data.Fields + ["Ticker"]
    out_table = out_table[['Ticker'] + out_data.Fields]
    
    return out_table

def GetTradeDates(StartDate, EndDate, DateType):
    
    
    

RData = WriteWFactorData([ "wgsd_net_inc","ev","wgsd_assets"])


a = w.wss(",".join(P_Ticker_L),"ev,wgsd_assets,wgsd_net_inc","unit=1;tradeDate=20181029;rptDate=20171231;rptType=1;currencyType=")