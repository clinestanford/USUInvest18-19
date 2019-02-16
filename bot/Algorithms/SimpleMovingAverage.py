import pandas as pd
from ..Utils.StockData import StockData
from ..Utils.Order import Order


# Methods:
#	trade - trade on simple MACD signals
#
# Params:
#	stocks - list of ticker strings
#	shortTermWindow - window for short-term MVA
#	longTermWindow - window for long-term MVA
#	quantity - quantity of each stock to order
#		ToDo: implement way to specify quantity on a by-ticker basis
class SimpleMACD(object):
	def __init__(self, stocks=['AAPL'], shortTermWindow=12, longTermWindow=26, quantity=1):
		self.stocks = stocks
		self.shortTermWindow = shortTermWindow
		self.shortTermWindow = longTermWindow
		self.quantity = quantity


	# Buys when short-term momentum is positive
	# Sells when short-term momentum is negative
	# return orders - list of order objects
	def trade(self):
		orders = []

		for stock in self.stocks:
			df = StockData.Get(stock)
			shortTermMVA = df['close'][-shortTermMVA:].mean()
			longTermMVA = df['close'][-longTermMVA:].mean()

			alpaca = Alpaca(keyID, secretKey, isPaper=True)

			if longTermMVA < shortTermMVA:
				#buy
				order = Order(stock, quantity, 'buy', 'market', 'day')

			elif longTermMVA > shortTermMVA:
				#sell
				order = Order(stock, quantity, 'sell', 'market', 'day')

		return orders
