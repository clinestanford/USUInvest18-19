
import requests as r
import pandas as pd
from record import record
from datetime import datetime
from chart import chart

startsmall = "AAPL,F,GE,SPY,FB&"

url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='

urlType = 'types=chart&'
urlRange = 'range=5y'

columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']


r = r.get(url + startsmall + urlType + urlRange)

json = r.json()

for stock in json:

	try:
		df = pd.read_pickle("stocks/" + stock + ".pkl")
	except IOError:
		df = pd.DataFrame(columns=columns)
	for day in json[stock]['chart']:
		temp = chart(day['date'], stock, day['open'], day['high'], day['low'], day['close'], day['volume'], day['change'], day['changePercent'], day['vwap'])
		df = df.append({'date': temp.get_date(),
						'symbol': stock,
						'open': temp.get_open(),
						'high': temp.get_high(),
						'low': temp.get_low(),
						'close': temp.get_close(),
						'volume': temp.get_volume(),
						'change': temp.get_change(),
						'changePercent': temp.get_changePercent(),
						'vwap': temp.get_vwap()},
						ignore_index=True)
		
	print(df.head())
	print(df.tail())
	df.to_pickle("stocks/" + stock + ".pkl")	