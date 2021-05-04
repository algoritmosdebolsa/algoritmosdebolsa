from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from datetime import datetime, timedelta
import pandas as pd

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        cols = ['date', 'open', 'high', 'low', 'close']
        self.df = pd.DataFrame(columns=cols)
    
    def historicalData(self, reqId, bar):
        print(" Date:", bar.date, "Open:", bar.open, "High:", bar.high, "Low:", bar.low, "Close:", bar.close) #, "Volume: ", bar.volume, "Count: ", bar.barCount)
        dftemp = pd.DataFrame({'date':bar.date,'open':bar.open,'high':bar.high,'low':bar.low, 'close':bar.close}, index=[0])
        self.df = pd.concat([self.df, dftemp], axis=0)
        
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.df.to_csv("GBP_USD_1Y_15mins.csv",index=False)
        self.disconnect()

app = IBapi()
app.connect('127.0.0.1', 4002, 0)

#Create contract object
def defineContract(symbol,secType,exchange,currency='USD'):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = secType
    contract.exchange = exchange
    contract.currency = currency
    return contract

contract = defineContract(symbol='GBP',secType='CASH',exchange='IDEALPRO')
queryTime = (datetime.today() - timedelta(days=30)).strftime("%Y%m%d %H:%M:%S")
#queryTime = ""
duration = '1 Y'
barsize = '15 mins'
priceType = 'MIDPOINT'

app.reqHistoricalData(1, contract, queryTime, duration, barsize, priceType, 1, 1, False, [])
app.run()