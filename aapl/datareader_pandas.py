import pandas_datareader as pdr
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# get stocks data from yahoo
def get_stock_data(ticker, start, end):
    data = pdr.data.DataReader(ticker, 'yahoo', start, end)
    data.insert(0, "Ticker", ticker)
    return data

#set start and end dates
start = datetime(2012, 1, 1)
end = datetime(2014, 12, 31)
#get data for each stock 
df_msft = get_stock_data("MSFT", start, end)
df_aapl = get_stock_data("AAPL", start, end)
df_dal = get_stock_data("DAL", start, end)
df_ge = get_stock_data("GE", start, end)
df_pep = get_stock_data("PEP", start, end)
df_ual = get_stock_data("UAL", start, end)
df_ibm = get_stock_data("IBM", start, end)
df_ko = get_stock_data("KO", start, end)

#save to file
df_msft.to_csv('msft.csv')
df_aapl.to_csv('aapl2.csv')
df_dal.to_csv('dal.csv')
df_ge.to_csv('ge.csv')
df_pep.to_csv('pep.csv')
df_ual.to_csv('ual.csv')
df_ibm.to_csv('ibm.csv')
df_ko.to_csv('ko.csv')

#df_msft['Close'].plot()
#plt.show()