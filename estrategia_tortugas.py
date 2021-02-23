import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime

start = datetime(2000,10,1)
end = datetime(2020,10,1)
df = DataReader('EURUSD=X','yahoo',start,end)

window = 10
df['highest high'] = df['High'].rolling(window=window).max()
df['lowest low'] = df['Low'].rolling(window=window).min()

df['trigger'] = np.where(df['High']==df['highest high'],-1,np.nan)
df['trigger'] = np.where(df['Low']==df['lowest low'],1,df['trigger'])
df['position'] = df['trigger'].ffill().fillna(0)

df['returns'] = df['Adj Close']/df['Adj Close'].shift(1)
df['strategy'] = df['returns'] ** df['position'].shift(1)

plt.style.use('seaborn')
df[['returns', 'strategy']].dropna().cumprod().plot(figsize=(10, 6))




