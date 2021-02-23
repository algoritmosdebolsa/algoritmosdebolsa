import pandas_datareader.data as web
import datetime as dt
import mplfinance as mpf

start = dt.datetime(2020,6,1)
end = dt.datetime(2020,7,1)
df = web.DataReader('MSFT','yahoo',start,end)

mpf.plot(df,type='candle',style='charles',title='Microsoft daily',ylabel='Price ($)')
