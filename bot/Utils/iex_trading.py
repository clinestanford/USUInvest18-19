
import numpy as np
import requests
from Config import PATH_CONFIG
from datetime import datetime, timedelta
import pandas as pd
from pathlib2 import Path
from os import getcwd as cwd 
import json

class Stocks():

	def __init__(self):
		
		## if you want more things to be downloaded, 
		# add it to the stock_data.csv in the StockData directory
		self.path_main = Path(cwd()) / (Path(__file__).parent)
		self.path_data = self.path_main / PATH_CONFIG["StockDataPath"]
		self.stock_meta = pd.read_csv(self.path_data / "stock_data.csv")

	def prep_stocks(self):
		for stock in self.stock_meta["Symbol"].values:
			try:
				print(f"working on: {stock}")
				stock_df = pd.read_pickle(self.path_data / f"{stock}.pkl")
				Stock(stock, stock_df)

				
			except FileNotFoundError:
				# could kick off a call to download the last month of data
				# or something like that.
				print(f"{stock} wasn't found")

	#def save_stock(self, symbol, df):




class Stock():

	def __init__(self, symbol, df):
		self.path_main = Path(cwd()) / (Path(__file__).parent)
		self.path_data = self.path_main / PATH_CONFIG["StockDataPath"]
		self.df = df 
		self.symbol = symbol
		try:
			self.df = self.df[PATH_CONFIG['df_columns']]
			self.df.index = pd.to_datetime(self.df.index)
			self.df.sort_index(inplace=True)
			prev_start = self.df.index.values[-1]
			# will not include the date prev_start
			downloader = Downloader(self.symbol, pd.to_datetime(prev_start))
			df = downloader.get_df()
			self.df = pd.concat([self.df, df])
			self.save_df()

		except KeyError:
			print(f"could not assert columns onto df for {self.symbol}")

	def save_df(self):
		self.df.to_pickle(self.path_data / f"{self.symbol}.pkl")

# This Downloader takes a start date and a symbol
# calling get_df will return DataFrame with data between start 
# date and the current day for that symbol

class Downloader():
	base = PATH_CONFIG["base_url"]
	batch_extension = PATH_CONFIG["batch_extension"]
	s_key = PATH_CONFIG["secret_key"]

	def __init__(self, symbol, s_date):
		self.s_date = s_date
		self.symbol = symbol
		self.columns = PATH_CONFIG['df_columns']

	## given a start date, this returns a list of all days since
	## that day not including weekends
	def get_days(self, s_date):
		today = datetime.today()
		prev_date = s_date + timedelta(days=1) #s_date is a date we have
		days = []

		while prev_date < today - timedelta(days=1):
			if prev_date.weekday() not in [5,6]:
				days.append(prev_date.date())
			prev_date += timedelta(days=1)

		return days

	def get_df(self):
		days = self.get_days(self.s_date)

		df = pd.DataFrame(index=days, columns=self.columns)
		df.index.name = 'date'
		print(len(days), days)

		for day in days:
			f_url = self.get_single_url(self.symbol, day)
			
			try:
				cont = requests.get(f_url).content
				series = pd.read_json(cont)
			except ValueError:
				print(f"couldn't parse.... {self.symbol}")
				print(cont)
				break
			# need to give the series the column date to be able to set_index
			# if it can't limit the columns (KeyError) we will drop the day
			try:
				series = series[self.columns + ['date']]
				series.set_index("date", inplace=True)
				df.update(series)
			except KeyError:
				df.drop(day, inplace=True)
		return df

	def get_single_url(self, symbol, date):
		return f"{self.base}/v1/stock/{symbol}/chart/date/{date}?chartByDay=True&token={self.s_key}&format=json"
		

if __name__ == '__main__':
	#d = Downloader(datetime.today() - timedelta(days = 5), "JNUG").get_df()
	#print(d)
	stocks = Stocks().prep_stocks()

	# s_date = datetime.today() - timedelta(days=5)
	# print(s_date)
	#print(d.get_batch_date(["JNUG", "ZION"], '1m'))



