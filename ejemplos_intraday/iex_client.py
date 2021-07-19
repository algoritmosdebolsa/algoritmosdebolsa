import datetime as dt
import pandas as pd
import os

IEX_API_TOKEN = os.environ.get('IEX_API_TOKEN')

ticker = 'NFLX'
day = dt.datetime(2020,4,1) # (Year, Month, Day)

url = f'https://cloud.iexapis.com/stable/stock/{ticker}/chart/date/{day.strftime("%Y%m%d")}?token={IEX_API_TOKEN}'
df = pd.read_json(url, orient='columns')