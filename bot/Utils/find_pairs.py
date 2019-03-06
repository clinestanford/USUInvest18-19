
# input is two tickers. Output is correlation factor between -1 and 1
# makes the two list the same length for the correlation calculation between -1 and 1
# if one is longer, it will cut off the oldest data of the longer set

from statsmodels.tsa.stattools import coint
import math
from pathlib2 import Path


def pearson_coor(data1: list, data2: list) -> float:  # find the correlation of 2 list of even length

	x, y = data1, data2
	assert len(x) == len(y)
	n = len(x)
	assert n > 0
	avg_x = average(x)
	avg_y = average(y)
	diffprod = 0
	xdiff2 = 0
	ydiff2 = 0
	for idx in range(n):
		xdiff = x[idx] - avg_x
		ydiff = y[idx] - avg_y
		diffprod += xdiff * ydiff
		xdiff2 += xdiff * xdiff
		ydiff2 += ydiff * ydiff
	return diffprod / math.sqrt(xdiff2 * ydiff2)


def average(x: list) -> float:
	assert len(x) > 0
	return float(sum(x)) / len(x)


def coint_test(ticker1: list, ticker2: list) -> float:
	return coint(ticker1, ticker2)


def ticker_list(data_dir) -> list:
	path = Path.iterdir(data_dir)
	data_file_names = [f for f in path]
	return data_file_names


def ranged_price_list(file: str, days: int=120, type: str='close'):
	# open data and save last n days in list. Its saved as a pandas data frame that i don't yet know how to use
	data = []
	return data


# warning this function will take around 40 - 60 minutes to complete if comparing ~500 securities
def find_all_pairs(days: int, data_dir: str='StockData', corr_value=.9, p_value=.01):
	data_dir = Path.joinpath(Path.cwd(), data_dir)
	data_file_names = ticker_list(data_dir)
	# symbols = symbols[:10] # testing not 124000 possibilities
	cointegrated = []

	for i in range(len(data_file_names)):
		for j in range(i + 1, len(data_file_names)):
			data_list_1 = ranged_price_list(data_file_names[i], 120, 'close')
			data_list_2 = ranged_price_list(data_file_names[j], 120, 'close')

			# correlation test
			if corr_value < pearson_coor(data_list_1, data_list_2):
				coint_value = coint(data_list_1, data_list_2)

				# cointegration test
				if coint_value < p_value:
					cointegrated.append(
						(coint_value, data_file_names[i].split('\\')[-1], data_file_names[j].split('\\')[j]))

	return cointegrated
