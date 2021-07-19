from tiingo import TiingoClient
import datetime as dt
import os

config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = os.environ.get("TIINGO_API_KEY")

# Initialize
client = TiingoClient(config)

# Get historical GOOGL
startDate = dt.datetime(2017,8,1)
endDate = dt.datetime(2017,8,31)

historical_prices = client.get_dataframe("GOOGL", startDate=startDate,
                                         endDate=endDate,frequency='1Min')