




class AlgoDriver(object):

	def __init__(self, alpaca):
		self.strategies = []
		self.cash = cash 

	def addStrategy(self, strat):
		self.strategies.append(strat)

	def getStrategies(self):
		return self.strategies

	def buyAndSell(self):
		for i in self.strategies:
			print(i)