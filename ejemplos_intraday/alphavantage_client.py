import os
ALPHA_VANTAGE_KEY = os.environ.get("ALPHA_VANTAGE_KEY")

def stock():
    from alpha_vantage.timeseries import TimeSeries    
    ts = TimeSeries(key=ALPHA_VANTAGE_KEY, output_format='pandas')
    msft, _ = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    # msft['4. close'].plot(title='Intraday Times Series for the MSFT stock (1 min)',grid=True)
    return msft

def fx():
    from alpha_vantage.foreignexchange import ForeignExchange    
    fx = ForeignExchange(key=ALPHA_VANTAGE_KEY, output_format='pandas')
    eurusd, _ = fx.get_currency_exchange_intraday(from_symbol='EUR',to_symbol='USD',interval='1min',outputsize='full')
    # eurusd['4. close'].plot(title='Daily close value for EUR/USD',grid=True)
    return eurusd

def crypto():
    from alpha_vantage.cryptocurrencies import CryptoCurrencies
    cc = CryptoCurrencies(key=ALPHA_VANTAGE_KEY, output_format='pandas')
    eth, _ = cc.get_digital_currency_daily(symbol='ETH', market='CNY')
    # eth['4b. close (USD)'].plot(title='Daily close value for Ethereum (ETH)',grid=True)
    return eth
    
df_msft = stock()
df_eurusd = fx()
df_eth = crypto()