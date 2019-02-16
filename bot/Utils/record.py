




class record(object):

	def __init__(self, date=None, name=None, symbol=None, rank=None, price=None, vol=None, ch1h=None, ch24h=None, ch7d=None, cap=None, delim='|'):
		self.date = date
		self.name = name
		self.symbol = symbol
		self.rank = rank
		self.price = price
		self.volume = vol
		self.ch1h = ch1h
		self.ch24h = ch24h
		self.ch7d = ch7d
		self.cap = cap
		self.delim = delim

	def get_date(self):
		return self.date

	def get_name(self):
		return self.name

	def get_symbol(self):
		return self.symbol

	def get_rank(self):
		return self.rank

	def get_price(self):
		return self.price

	def get_volume(self):
		return self.volume

	def get_ch1h(self):
		return self.ch1h

	def get_ch24h(self):
		return self.ch24h

	def get_ch7d(self):
		return self.ch7d

	def get_cap(self):
		return self.cap

	def __str__(self):
		return f"{self.name} ==> date: {self.date}, price: {self.price}"#.format(self.symbol, self.date, self.price)



