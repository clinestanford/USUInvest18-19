
import pandas as pd 
import numpy as np 
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt


PATH_TO_DATA = '../StockData/'

class Pair:

	##window will be the number of days to look back
	##in order to calculate the mean
	def __init__(self, pair1, pair2, window, gap):
		self.pair1 = pair1
		self.pair2 = pair2
		self.window = window
		self.gap = gap		

	def backtest(self, start_date, cash):

		start_cash = cash

		df1 = pd.read_pickle(PATH_TO_DATA + self.pair1 + '.pkl')
		df2 = pd.read_pickle(PATH_TO_DATA + self.pair2 + '.pkl')

		assert df1 is not None
		assert df2 is not None

		df1 = df1[['close', 'changePercent', 'volume']]
		df2 = df2[['close', 'changePercent', 'volume']]

		df1 = df1.rename(columns={"close": "close_pair1", "changePercent":"chg_pct_pair1", 'volume':'vol_pair1'})
		df2 = df2.rename(columns={"close": "close_pair2", "changePercent":"chg_pct_pair2", 'volume':'vol_pair2'})

		merge = df1.merge(df2, how='inner', left_index=True, right_index=True)

		merge['spread'] = merge['close_pair1'] - merge['close_pair2']

		#I will need to calculate the 'spread_pct'
		## merge['spread_pct'] = (merge['spread'] - merge['spread'].mean()) / merge['spread'].std()

		#this will test the two members for cointegration
		#print(adfuller(merge['close_pair1'] - merge['close_pair2']), len(merge['close_pair1']))

		# this will display a graph with a histogram
		# merge['spread_pct'].hist(bins=30)
		# plt.show(block=True)


		bought = False 
		shares = 0

		##TODO will need to set a mask to handle the time frame

		mask = merge.index > start_date
		delta = pd.Timedelta(str(self.window) + ' days')

		for date in merge[mask].index:

			##by iterating over this, I can create a new dataframe
			##that will be masked for the last window days
			day = merge.loc[date]

			##need to calculate the spread_pct
			temp_mask = (merge.index > date - delta) & (merge.index <= date)
			temp_df = merge[temp_mask]
			
			spread_pct = day.spread - temp_df['spread'].mean()

			if spread_pct > self.gap and bought == False:
				##sell the high, buy the low
				#print(day.close_pair1, day.close_pair2)
				bought = True
				#sell the one
				cash += day.close_pair1 * shares
				#buy the other
				shares = cash // day.close_pair2
				cash -= shares * day.close_pair2


			elif spread_pct < -1 * self.gap and bought == True:
				##buy
				#print(day.close_pair1, day.close_pair2)
				bought = False
				#sell the one
				cash += day.close_pair2 * shares
				#buy the other
				shares = cash // day.close_pair1
				cash -= shares * day.close_pair1

		if bought:
			cash += merge.loc[merge.index[-1]].close_pair2 * shares 
		else:
			cash += merge.loc[merge.index[-1]].close_pair1 * shares

		print(f"end Cash: ${cash}")

		print(f"total returns: {cash/start_cash - 1}%")

		return (cash, cash/start_cash - 1)


if __name__ == '__main__':

	# delta = np.linspace(.4, .6, 20)

	# results = []
	# for val in delta:

	pair = Pair('AKAM', 'ALLE', 30, .5)
	start_cash = 25000
	end_cash, end_perc = pair.backtest('2018-09-26', start_cash)

	print(end_cash, end_perc)

	#results.append((end_cash, end_perc, val))

	# #results = sorted(results, key=lambda x: x[1])
	# for r in results:
	# 	print(r)