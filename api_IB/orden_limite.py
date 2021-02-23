from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time
#from time import sleep

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.nextorderId = orderId
		print('The next valid order id is: ', self.nextorderId)

	def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
		print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
	
	def openOrder(self, orderId, contract, order, orderState):
		print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

	def execDetails(self, reqId, contract, execution):
		print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)


app = IBapi()
app.connect('127.0.0.1', 4002, 0)
app.nextorderId = None

def run_loop():
	app.run()
    
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

while True:
	if isinstance(app.nextorderId, int):
		print('connected')
		break
	else:
		print('waiting for connection')
		time.sleep(1)

def defineContract(symbol,secType,exchange,currency='USD'):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = secType
    contract.exchange = exchange
    contract.currency = currency
    return contract

# Definimos el par GBP/USD
contract = defineContract(symbol='GBP',secType='CASH',exchange='IDEALPRO')

def createOrder(action,totalQuantity,orderType,lmtPrice=False):
    order = Order()
    order.action = action
    order.totalQuantity = totalQuantity
    order.orderType = orderType
    if orderType == 'LMT':
        order.lmtPrice = lmtPrice
    return order

# Compramos 25000 libras
order = createOrder(action='BUY',totalQuantity=25000,orderType='LMT',lmtPrice='1.36')

app.placeOrder(app.nextorderId, contract, order)
time.sleep(3)

print('cancelling order')
app.cancelOrder(app.nextorderId)

time.sleep(3)
app.disconnect()