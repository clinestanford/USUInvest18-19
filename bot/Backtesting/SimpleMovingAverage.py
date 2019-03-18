
import pandas as pd 
import math



def testSimpleMovingAverage(symbol, window, percentAbove, percentBelow, backTestDays, cash):
	
	try:
		security = pd.read_pickle('../StockData/' + symbol + '.pkl')  
	except FileNotFoundError:
		print("couldn't find the file")

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
			print('sold ', num_bought, ' at: ', row.close, ' on: ', row.date)
			num_bought = 0

		elif row.close < row.mean_close * percentBelow and bought == False:
			#buy
			num_bought = math.floor(cash / row.close)
			cash = cash - num_bought*row.close
			bought = True
			print('bought ', num_bought, ' at: ', row.close, ' on: ', row.date)

	if bought == True:
		cash = cash + float(merge[-1:].close) * num_bought

	print('start cash: ', start_cash, ' end cash: ', cash)





if __name__ == '__main__':
	testSimpleMovingAverage('GE', 15, 1.03, 1.03, 120, 1500)

