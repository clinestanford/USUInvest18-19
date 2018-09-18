
import pandas as pd
import matplotlib.pyplot as plt


csv = pd.read_csv("sma.csv")
csv = csv.set_index("date")

cash = 100000
bought = False
buyPrice = sellPrice = 0
number = 0


for index, row in csv.iterrows():
	
	if row["close"] > row["sma_close"] and not bought:
		buyPrice = row["close"]
		number = cash//buyPrice
		cash = cash - (number*buyPrice)
		bought = True

		print("{0:6} {1:2d} at ${2:.2f}".format("bought", int(number), buyPrice))

	if row["close"] < row["sma_close"] and bought:
		sellPrice = row["close"]
		cash = cash + number*sellPrice
		profit = sellPrice*number - buyPrice*number
		bought = False

		print("{0:6} {1:2d} at ${2:.2f} profit: ${3:.2f}".format("sold", int(number), sellPrice, profit))

print("total: " + str(cash))














