

import requests as r
import pandas as pd
from record import record
from datetime import datetime

headers = {"X-CMC_PRO_API_KEY": '80bf0944-68cf-48da-a665-92218a6ae1eb'}

r = r.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=headers)

json = r.json()

time = datetime.now()

columns = ['date', 'name', 'symbol', 'rank', 'price', 'volume', 'ch1h', 'ch24h', 'ch7d', 'cap']

for coin in json['data']:


	quote = coin['quote']['USD']
	# get data to datetime
	# dt = datetime.strptime("21/11/08 16:30", "%d/%m/%y %H:%M")
	rec = record(date   = time.strftime("%d/%m/%y %H:%M"),  
				 name   = coin['name'],
				 symbol = coin['symbol'],
				 rank   = coin['cmc_rank'],
				 price  = quote['price'],
				 vol    = quote['volume_24h'],
				 ch1h   = quote['percent_change_1h'],
				 ch24h  = quote['percent_change_24h'],
				 ch7d   = quote['percent_change_7d'],
				 cap    = quote['market_cap'])

	try:
		df = pd.read_pickle("data/" + rec.get_symbol() + ".pkl")
	except FileNotFoundError:
		df = pd.DataFrame(columns=columns)
		
	df = df.append({'date': rec.get_date(), 
			   'name': rec.get_name(),
			   'symbol': rec.get_symbol(),
			   'rank': rec.get_rank(),
			   'price': rec.get_price(),
			   'volume': rec.get_volume(),
			   'ch1h': rec.get_ch1h(),
			   'ch24h': rec.get_ch24h(), 
			   'ch7d': rec.get_ch7d(),
			   'cap': rec.get_cap()},
				ignore_index=True)
	# print(df.head())
	df.to_pickle('data/'+coin['symbol']+'.pkl')



