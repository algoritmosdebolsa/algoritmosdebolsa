import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import datetime
from pytrends.request import TrendReq

def getSearchPopularity(terms: list, start, end):
    pytrends = TrendReq(hl='en-US', tz=360) 
    start = datetime.strftime(start,"%Y-%m-%d")
    end = datetime.strftime(end,"%Y-%m-%d")
    timeframe = f'{start} {end}'
    
    pytrends.build_payload(kw_list=terms, cat=0, timeframe=timeframe)
    data = pytrends.interest_over_time()
    return data

def delete_extra_dates(trends_df,df):
    dates_together_df = pd.concat([trends_df,df])
    dates_together_df = dates_together_df.sort_index()
    delete_dates = dates_together_df.loc[~(dates_together_df["debt"] * \
                                           dates_together_df["debt"].shift(1)).isna()].index
    new_trends_df = trends_df.drop(index=delete_dates)
    return new_trends_df

start = datetime(2006,4,30)
end = datetime(2011,6,30)
term = "debt"

df = web.DataReader("^GSPC","yahoo",start,end,)
df = df[::5]

trends_df = getSearchPopularity([term], start,end)
trends_df = delete_extra_dates(trends_df, df)

df["Search Popularity"] = trends_df[term].values
df["3-week Popularity MA"] = df["Search Popularity"].rolling(window=3, min_periods=3).mean()
df["Position"] = np.where(df["Search Popularity"] < df["3-week Popularity MA"], 1, 0)
df["Position"] = np.where(df["Search Popularity"] > df["3-week Popularity MA"], -1, df["Position"])

df["Price change"] = df["Close"]/df["Close"].shift(1)
df["Strategy"] = df["Price change"]**df["Position"]
df["Equity"] = df["Strategy"].cumprod()

df[["Equity","Price change"]].plot(title="S&P500 Google Trends Strategy", 
                                   ylabel = "Returns/1",
                                   grid=True)








