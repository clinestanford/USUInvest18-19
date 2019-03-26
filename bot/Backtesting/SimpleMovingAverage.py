
import pandas as pd 
import numpy as np
import math



def testSimpleMovingAverage(security, window, percentAbove, percentBelow, backTestDays, cash):

	assert isinstance(security, pd.DataFrame)

	average = security.rolling(window=window).mean()
	average = average[['high', 'low', 'close', 'open']]

	average.rename(columns = {'close':'mean_close', 
							  'low':'mean_low', 
							  'high':'mean_high',
							  'open':'mean_open'},
							  inplace=True)

	merge = pd.merge(security, average, how='inner', left_index=True, right_index=True)

	start_cash = cash

	bought = False
	num_bought = 0

	for row in merge[-backTestDays:].itertuples():
		if row.close > row.mean_close * percentAbove and bought == True:
			#sell
			bought = False
			cash = cash + num_bought * row.close
			#print('sold ', num_bought, ' at: ', row.close, ' on: ', row.date)
			num_bought = 0

		elif row.close < row.mean_close * percentBelow and bought == False:
			#buy
			num_bought = math.floor(cash / row.close)
			cash = cash - num_bought*row.close
			bought = True
			#print('bought ', num_bought, ' at: ', row.close, ' on: ', row.date)

	if bought == True:
		cash = cash + float(merge[-1:].close) * num_bought

	print('start: $', start_cash, ' end: $', cash, " window: ", window, " above: ", percentAbove, " below: ", percentBelow)

	return (cash / start_cash, window, percentAbove, percentBelow)


if __name__ == '__main__':

	# AMD, 

	symbol = "AMD"
	backTestDays = 60
	startingCash = 1500

	try:
		security = pd.read_pickle('../StockData/' + symbol + '.pkl')  
	except FileNotFoundError:
		raise Exception("Couldn't find file or doesn't exist")

	highest = [0,0,0,0]

	for i in np.arange(.94, 1, .005):
		for j in np.arange(1.06, 1, -.005):
			for k in np.arange(5, 30, 5):

				temp = testSimpleMovingAverage(security, k, j, i, backTestDays, startingCash)
				if temp[0] > highest[0]:
					highest = temp

	print('percent: ', highest[0], " window: ", highest[1], " above: ", highest[2], " below: ", highest[3])
