import pandas as pd
from ..Utils.StockData import StockData
from ..Utils.Order import Order

# Methods:
#	trade - trade on simple MACD signals
#
# Params:
#	stock - ticker string
#	shortTermWindow - window for short-term MVA
#	longTermWindow - window for long-term MVA
#	quantity - quantity of each stock to order
#		ToDo: implement way to specify quantity on a by-ticker basis
class SimpleMACD(BaseAlgorithm):
	def __init__(self, stock=['AAPL'], shortTermWindow=12, longTermWindow=26, quantity=1):
		super(SimpleMACD, self).__init__()
		self.stock = stock
		self.shortTermWindow = shortTermWindow
		self.shortTermWindow = longTermWindow
		self.quantity = quantity


	# Buys when short-term momentum is positive
	# Sells when short-term momentum is negative
	# return orders - list of order objects
	def getOrder(self):
		df = StockData.Get(stock)
		shortTermMVA = df['close'][-shortTermMVA:].mean()
		longTermMVA = df['close'][-longTermMVA:].mean()

		alpaca = Alpaca(keyID, secretKey, isPaper=True)

		if longTermMVA < shortTermMVA:
			#buy
			order = Order(stock, self.quantity, 'buy', 'market', 'day')

		elif longTermMVA > shortTermMVA:
			#sell
			order = Order(stock, self.quantity, 'sell', 'market', 'day')

		return order


