


class AlgoDriver(object):

	def __init__(self, alpaca):
		self.strategies = []
		self.alpaca = alpaca 

	def addStrategy(self, strat):
		self.strategies.append(strat)

	def getCash(self):


	def getStrategies(self):
		return self.strategies

	def buyAndSell(self):
		for i in self.strategies:
			print(i)