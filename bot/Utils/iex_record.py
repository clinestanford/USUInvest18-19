


class iex_record(object):

	def __init__(self,date,symbol,start,high,low,close,volume,change,changePercent,vwap):
		self.date = date
		self.symbol = symbol
		self.open = start
		self.high = high
		self.low = low
		self.close = close
		self.volume = volume
		self.change = change
		self.changePercent = changePercent
		self.vwap = vwap


	def get_date(self):
		return self.date
	def get_symbol(self):
		return self.symbol
	def get_open(self):
		return self.open
	def get_high(self):
		return self.high
	def get_low(self):
		return self.low
	def get_close(self):
		return self.close
	def get_volume(self):
		return self.volume
	def get_change(self):
		return self.change
	def get_changePercent(self):
		return self.changePercent
	def get_vwap(self):
		return self.vwap

	def __str__(self):
		return str(self.date) + " close: " + str(self.close)