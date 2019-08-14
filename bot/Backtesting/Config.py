
from pathlib2 import Path

PATH_CONFIG = {
	'StockDataPath': Path("../StockData"),
	'StockDataLogs': Path("../StockLogs"),
	'CryptoDataPath': Path("../CryptoData"),
	'CryptoDataLogs': Path("../CryptoLogs"),
	'secret_key': '',
	'public_key': '',
	'base_url': 'https://cloud.iexapis.com',
	'batch_extension': '/v1/stock/market/batch?',
	'df_columns':  ['open','high', 'low', 'close', 'volume', 'change', 'changePercent']
}