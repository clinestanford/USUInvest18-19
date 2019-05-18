#Class to handle the previous days data


import sys
import requests
import pandas as pd
from iex_record import iex_record
from datetime import datetime
import os.path
from Config import PATH_CONFIG
from os import getcwd as cwd 
from pathlib2 import Path

class StockData:

	##if you want to add other tickers to simply add their ticker here. It should be able to 
	##download any ticker data you are interested in having.
	def __init__(self):
		self.batches = ['MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&',
		 	'CNC,CNP,CTL,CERN,CF,SCHW,CHTR,CVX,CMG,CB,CHD,CI,XEC,CINF,CTAS,CSCO,C,CFG,CTXS,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,CXO,COP,ED,STZ,COO,CPRT,GLW,COST,COTY,CCI,CSX,CMI,CVS,DHI,DHR,DRI,DVA,DE,DAL,XRAY,DVN,DLR,DFS,DISCA,DISCK,DISH,DG,DLTR,D,DOV,DWDP,DTE,DRE,DUK,DXC,ETFC,EMN,ETN,EBAY,ECL,EIX,EW,EA,EMR,ETR,EOG,EFX,EQIX,EQR,ESS,EL,EVRG,ES,RE,EXC,EXPE,EXPD,ESRX,EXR,XOM,FFIV,FB,FAST,FRT,FDX,FIS,FITB,FE,FISV,FLT,FLIR,FLS&',
			'FLR,FMC,FL,F,FTNT,FTV,FBHS,BEN,FCX,GPS,GRMN,IT,GD,GE,GIS,GM,GPC,GILD,GPN,GS,GT,GWW,HAL,HBI,HOG,HRS,HIG,HAS,HCA,HCP,HP,HSIC,HSY,HES,HPE,HLT,HFC,HOLX,HD,HON,HRL,HST,HPQ,HUM,HBAN,HII,IDXX,INFO,ITW,ILMN,IR,INTC,ICE,IBM,INCY,IP,IPG,IFF,INTU,ISRG,IVZ,IPGP,IQV,IRM,JKHY,JEC,JBHT,JEF,SJM,JNJ,JCI,JPM,JNPR,KSU,K,KEY,KEYS,KMB,KIM,KMI,KLAC,KSS,KHC,KR,LB,LLL,LH,LRCX,LEG,LEN,LLY,LNC,LIN,LKQ,LMT,L,LOW,LYB,MTB,MAC&',
			'M,MRO,MPC,MAR,MMC,MLM,MAS,MA,MAT,MKC,MCD,MCK,MDT,MRK,MET,MTD,MGM,KORS,MCHP,MU,MSFT,MAA,MHK,TAP,MDLZ,MNST,MCO,MS,MOS,MSI,MSCI,MYL,NDAQ,NOV,NKTR,NTAP,NFLX,NWL,NFX,NEM,NWSA,NWS,NEE,NLSN,NKE,NI,NBL,JWN,NSC,NTRS,NOC,NCLH,NRG,NUE,NVDA,ORLY,OXY,OMC,OKE,ORCL,PCAR,PKG,PH,PAYX,PYPL,PNR,PBCT,PEP,PKI,PRGO,PFE,PCG,PM,PSX,PNW,PXD,PNC,RL,PPG,PPL,PFG,PG,PGR,PLD,PRU,PEG,PSA,PHM,PVH,QRVO,PWR,QCOM,DGX,RJF,RTN,O,RHT,REG,REGN,RF&',
			'RSG,RMD,RHI,ROK,COL,ROL,ROP,ROST,RCL,CRM,SBAC,SCG,SLB,STX,SEE,SRE,SHW,SPG,SWKS,SLG,SNA,SO,LUV,SPGI,SWK,SBUX,STT,SRCL,SYK,STI,SIVB,SYMC,SYF,SNPS,SYY,TROW,TTWO,TPR,TGT,TEL,FTI,TXN,TXT,TMO,TIF,TWTR,TJX,TMK,TSS,TSCO,TDG,TRV,TRIP,FOXA,FOX,TSN,UDR,ULTA,USB,UAA,UA,UNP,UAL,UNH,UPS,URI,UTX,UHS,UNM,VFC,VLO,VAR,VTR,VRSN,VRSK,VZ,VRTX,VIAB,V,VNO,VMC,WMT,WBA,DIS,WM,WAT,WEC,WCG,WFC,WELL,WDC,WU,WRK,WY,WHR,WMB,WLTW,WYNN,XEL,XRX&',
			'XLNX,XYL,YUM,ZBH,ZION,ZTS,QQQ&']
	
	# Returns 5year data from a batch of symbols.
	def GetBatch(self, symbols = "SPY,APPL,F,GE,FB", window="3m"):
		#window = 5y, 3m, 1q
		yesterdayData = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols='+symbols+'&types=chart&range='+window).json()
		if not yesterdayData:
			print('Invalid Symbols')
			exit()
		else:
			return yesterdayData

	def map_to_df(self, df, stock, day):

		##got to make sure value is present, and if not set it to null, ternaries to simplify
		date = day['date'] if 'date' in day.keys() else None
		open_val = day['open'] if 'open' in day.keys() else None 
		high = day['high'] if 'high' in day.keys() else None 
		low = day['low'] if 'low' in day.keys() else None 
		close = day['close'] if 'close' in day.keys() else None 
		volume = day['volume'] if 'volume' in day.keys() else None 
		change = day['change'] if 'change' in day.keys() else None 
		changePercent = day['changePercent'] if 'changePercent' in day.keys() else None 
		vwap = day['vwap'] if 'vwap' in day.keys() else None 

		temp = iex_record(date, stock, open_val, high, low, close, volume, change, changePercent, vwap)

		if not (temp.get_date() in df.index) and temp.get_date() != None:
			new_row = pd.Series({'symbol': stock,
							'open': temp.get_open(),
							'high': temp.get_high(),
							'low': temp.get_low(),
							'close': temp.get_close(),
							'volume': temp.get_volume(),
							'change': temp.get_change(),
							'changePercent': temp.get_changePercent(),
							'vwap': temp.get_vwap()}, 
							name=pd.to_datetime(temp.get_date()))

			df = df.append(new_row)

		return df

	#download the last 'window' of data for all in S&P 500
	def Download(self, window='3m'):

		path = Path(cwd()) / (Path(__file__).parent)

		columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
		for batch in self.batches:
			json = self.GetBatch(batch, window=window)
			for stock in json:
				print(stock)

				try:
					print(path / PATH_CONFIG["StockDataPath"] / (stock + '.pkl'))
					df = pd.read_pickle(path / PATH_CONFIG["StockDataPath"] / (stock + '.pkl'))
				except IOError:
					df = pd.DataFrame(columns = columns)

				for day in json[stock]['chart']:
					df = self.map_to_df(df, stock, day)

				# df['date'] = pd.to_datetime(df['date'])
				# df = df.set_index('date')
				df.to_pickle(path / PATH_CONFIG["StockDataPath"] / (stock + '.pkl'))


	#Reads Saved Pickle and returns dataframe.
	def Get(self, symbol):
		assert isinstance(symbol, str)

		try: 
			df = pd.read_pickle(PATH_CONFIG['StockDataPath'] / (symbol) + '.pkl')
		except FileNotFoundError:
			return None

def main():
	date = StockData()
	##if you want to download 5y of data, run
	#date.Download(window='5y')
	date.Download()

if __name__ == '__main__':
	main()