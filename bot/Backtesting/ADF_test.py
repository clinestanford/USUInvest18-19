
from statsmodels.tsa.stattools import adfuller
from itertools import combinations
import pandas as pd 


PATH_TO_DATA = '../StockData/'
START_DATE = '2018-9-26'

#give it a string and then use the .split(',')
tickers = "MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS"

tickers = tickers.strip().split(',')

dfs = [] 

for ticker in tickers:
	dfs.append((pd.read_pickle(PATH_TO_DATA + f"{ticker}.pkl")[START_DATE:], ticker))

results = []
count = 0
for pair in combinations(tickers, 2):
	count += 1 
	ind1 = tickers.index(pair[0])
	ind2 = tickers.index(pair[1])

	df1 = dfs[ind1][0]
	df2 = dfs[ind2][0]

	#need to verify they are coming from the correct dataframe
	assert pair[0] == dfs[ind1][1]
	assert pair[1] == dfs[ind2][1]

	if len(df1) != len(df2):
		continue 

	results.append((f"{pair[0]}, {pair[1]}", adfuller(df1['close'] - df2['close'])[1]))

results = sorted(results, key=lambda x: x[1])
results = [r for r in results if r[1] < .05]

print('cointegrated tickers:\n******************************')
for r in results:
	print(r)
	
sig = len(results)

print(f"out of {count} pairs, there were {sig} that were statistically significant\n{sig/count}%")