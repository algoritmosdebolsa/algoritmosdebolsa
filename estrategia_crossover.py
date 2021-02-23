import pandas_datareader.data as web
import datetime as dt
from numpy import where

start = dt.datetime(2015,3,1)
end = dt.datetime(2020,3,1)

df = web.DataReader('AAPL','yahoo',start,end)

df['42ma'] = df['Close'].rolling(window=42,min_periods=0).mean()
df['252ma'] = df['Close'].rolling(window=252,min_periods=0).mean()
df['diferencia'] = df['42ma'] - df['252ma']
df['Regime'] = where(df['diferencia']>0,1,0)
df['Regime'] = where(df['diferencia']<0,-1,df['Regime'])

#df[['Close','42ma','252ma']].plot(grid=True)

df['Market'] = df['Close']/df['Close'].shift(1)
df['Strategy'] = df['Market']**df['Regime'].shift(1)
df[['Market','Strategy']].cumprod().plot(grid=True)
