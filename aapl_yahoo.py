import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2015,3,1)
end = dt.datetime(2020,3,1)

df = web.DataReader('AAPL','yahoo',start,end)