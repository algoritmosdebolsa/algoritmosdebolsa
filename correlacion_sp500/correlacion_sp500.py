import os
import pandas as pd
from datetime import datetime
from pandas_datareader.data import DataReader

df = pd.read_csv("constituents_sp500.csv")
tickers = df['Symbol'].values
problems = ['BF.B','BRK.B','CTL','ETFC']

def stocks_yahoo():
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')
    
    start = datetime(2017,12,1)
    end = datetime(2020,12,1)
    
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)) and ticker not in problems:
            df = DataReader(ticker,'yahoo',start,end)
            df.to_csv('stocks_dfs/{}.csv'.format(ticker))

def join_data():
    main_df = pd.DataFrame()
    for ticker in tickers:
        print(ticker)
        if os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
            df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker))
            df.set_index('Date',inplace=True)
            
            df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
            df.rename(columns = {'Adj Close': ticker}, inplace=True)
            
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df,how='outer')
    main_df.to_csv("sp500_stocks_joined.csv")
            
def corr_heatmap():
        
    df = pd.read_csv('sp500_stocks_joined.csv')
    df_corr = df.corr()

    import matplotlib.pyplot as plt
    from numpy import arange
    
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()
    
    return df_corr            

#stocks_yahoo()
#join_data()
df_corr = corr_heatmap()

