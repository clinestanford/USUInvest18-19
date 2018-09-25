import pandas as pd
import numpy as np
import sys

print("there are: ",len(sys.argv), "command line arguments")
path = "/home/stan/Projects/TensorFlow/CryptoData_MOD_Clean/MOD_"

iterations = len(sys.argv) - 1;

for i in range(iterations):
	#read it into the dataframe
	csvfile = path + sys.argv[i+1] + ".txt"
	df = pd.read_csv(csvfile, sep="|")
	
	#all we want is the USD price

	price = np.array(df["PRICE_USD"])
	

	i = buys = sells = 0
	buyp = profit = mva = 0
	mvgAvgInc = 0
	best = index = 0

	#get a np.array with reasonable intervals for the mva
	#don't want to get every single possible digit
	intervals = np.linspace(2, 100, 99)

	#iterate through all of the prices 
	for j in range(len(intervals)):
		mvgAvgInc = intervals[j]
		buyp = sells = profit = i = 0
		#print("starting:",intervals[j])
		#print("profit prior: ", profit)
		for p in price:
			if i>int(mvgAvgInc):

				mva = np.sum(price[int(i-mvgAvgInc):int(i)])/float(mvgAvgInc)
				if p > mva and buyp == 0:
					buyp =  p
					#print("bought at:", p)
					buys += 1
				elif p<mva and buyp != 0.0:
					profit += (p - buyp)
					buyp = 0
					#print("sold at:", p)
					sells+=1
			if profit > best:
				best = profit
				index = intervals[j]
			i+=1
		print("profit:", profit, "at index", intervals[j])

		#profit = profit * 100
	print("\n\n\nbest profit:", best)
	print("done at: ", index, "moving averages")



