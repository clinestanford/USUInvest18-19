

from statsmodels.tsa.stattools import adfuller
from itertools import combinations
import pandas as pd
from os import getcwd as cwd
from pathlib2 import Path
import Config

PATH_CONFIG = Config.PATH_CONFIG


class ADF_two:

	def __init__(self, t1, t2, start):
		self.t1 = t1
		self.t2 = t2
		self.start = start
		self.t1_df = pd.read_pickle(PATH_CONFIG["StockDataPath"] / (f"{self.t1}.pkl"))
		self.t2_df = pd.read_pickle(PATH_CONFIG["StockDataPath"] / (f"{self.t2}.pkl"))
		

	def p_value(self):
		pass


def main():
	a = ADF_two('MMM', 'ABT', '2018-09-26')
	a.p_value()


if __name__ == '__main__':
	main()