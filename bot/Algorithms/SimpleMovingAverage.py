
import pandas as pd
from DailyData import DailyData


class SimpleMovingAverage(object):

	def __init__(self, stock, window):
		self.stock = stock
		self.window = window

	def buy_or_sell(self):
		df = pd.read_pickle("../StockData/" + self.stock + ".pkl")
		mean = df['close'][-window:].mean()
		close = df['close'].iloc[len(df)-1]

		if mean < close:
			#buy


		elif mean > close:
			#sell




