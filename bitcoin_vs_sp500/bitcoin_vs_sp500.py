import pandas as pd

df_bitcoin = pd.read_csv("bitcoin_historical.csv",index_col='Date',parse_dates=True)
df_bitcoin['returns'] = df_bitcoin['Close'].pct_change()
df_bitcoin['Realized Volatility %'] = df_bitcoin['returns'].rolling(window=365).std()*365**(0.5)*100

df_bitcoin_yearly = df_bitcoin.iloc[::365].reset_index()
df_bitcoin_yearly['Yearly Return %'] = 100*(df_bitcoin_yearly['Close']/df_bitcoin_yearly['Close'].shift(1) - 1)
df_bitcoin_yearly = df_bitcoin_yearly.set_index('Date')
df_bitcoin_yearly.drop(['Open','Low','High','Vol.','returns','Change %'],1,inplace=True)

from pandas_datareader.data import DataReader
from datetime import datetime

start = datetime(2015,12,28)
end = datetime(2020,12,29)

df_sp500 = DataReader('SPY','yahoo', start, end)
df_sp500['returns'] = df_sp500['Close'].pct_change()
df_sp500['Realized Volatility %'] = df_sp500['returns'].rolling(window=252).std()*252**(0.5)*100

df_sp500_yearly = df_sp500[::252].reset_index()
df_sp500_yearly['Yearly Return %'] = 100*(df_sp500_yearly['Close']/df_sp500_yearly['Close'].shift(1) - 1)
df_sp500_yearly = df_sp500_yearly.set_index('Date')
df_sp500_yearly.drop(['High','Low','Open','Volume','Adj Close','returns'],1,inplace=True)

import mplfinance as mpf
mpf.plot(df_sp500,type='candle',style='charles',title='S&P500',ylabel='Price ($)')

df_btc_2020 = df_bitcoin[-365:].reset_index()
df_btc_2020 = df_btc_2020.set_index('Date')
mpf.plot(df_btc_2020,type='candle',style='charles',title='Bitcoin',ylabel='Price ($)')
