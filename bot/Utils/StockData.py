#Class to handle the previous days data


import sys
import requests
import pandas as pd
from iex_record import iex_record
from datetime import datetime
import os.path
from Config import PATH_CONFIG


class StockData:

	def __init__(self):
		#self.batches = ['MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,
		# self.batches = ['BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&',
		# 	'CNC,CNP,CTL,CERN,CF,SCHW,CHTR,CVX,CMG,CB,CHD,CI,XEC,CINF,CTAS,CSCO,C,CFG,CTXS,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,CXO,COP,ED,STZ,COO,CPRT,GLW,COST,COTY,CCI,CSX,CMI,CVS,DHI,
		self.batches = ['DHR,DRI,DVA,DE,DAL,XRAY,DVN,DLR,DFS,DISCA,DISCK,DISH,DG,DLTR,D,DOV,DWDP,DTE,DRE,DUK,DXC,ETFC,EMN,ETN,EBAY,ECL,EIX,EW,EA,EMR,ETR,EOG,EFX,EQIX,EQR,ESS,EL,EVRG,ES,RE,EXC,EXPE,EXPD,ESRX,EXR,XOM,FFIV,FB,FAST,FRT,FDX,FIS,FITB,FE,FISV,FLT,FLIR,FLS&',
			'FLR,FMC,FL,F,FTNT,FTV,FBHS,BEN,FCX,GPS,GRMN,IT,GD,GE,GIS,GM,GPC,GILD,GPN,GS,GT,GWW,HAL,HBI,HOG,HRS,HIG,HAS,HCA,HCP,HP,HSIC,HSY,HES,HPE,HLT,HFC,HOLX,HD,HON,HRL,HST,HPQ,HUM,HBAN,HII,IDXX,INFO,ITW,ILMN,IR,INTC,ICE,IBM,INCY,IP,IPG,IFF,INTU,ISRG,IVZ,IPGP,IQV,IRM,JKHY,JEC,JBHT,JEF,SJM,JNJ,JCI,JPM,JNPR,KSU,K,KEY,KEYS,KMB,KIM,KMI,KLAC,KSS,KHC,KR,LB,LLL,LH,LRCX,LEG,LEN,LLY,LNC,LIN,LKQ,LMT,L,LOW,LYB,MTB,MAC&',
			'M,MRO,MPC,MAR,MMC,MLM,MAS,MA,MAT,MKC,MCD,MCK,MDT,MRK,MET,MTD,MGM,KORS,MCHP,MU,MSFT,MAA,MHK,TAP,MDLZ,MNST,MCO,MS,MOS,MSI,MSCI,MYL,NDAQ,NOV,NKTR,NTAP,NFLX,NWL,NFX,NEM,NWSA,NWS,NEE,NLSN,NKE,NI,NBL,JWN,NSC,NTRS,NOC,NCLH,NRG,NUE,NVDA,ORLY,OXY,OMC,OKE,ORCL,PCAR,PKG,PH,PAYX,PYPL,PNR,PBCT,PEP,PKI,PRGO,PFE,PCG,PM,PSX,PNW,PXD,PNC,RL,PPG,PPL,PFG,PG,PGR,PLD,PRU,PEG,PSA,PHM,PVH,QRVO,PWR,QCOM,DGX,RJF,RTN,O,RHT,REG,REGN,RF&',
			'RSG,RMD,RHI,ROK,COL,ROL,ROP,ROST,RCL,CRM,SBAC,SCG,SLB,STX,SEE,SRE,SHW,SPG,SWKS,SLG,SNA,SO,LUV,SPGI,SWK,SBUX,STT,SRCL,SYK,STI,SIVB,SYMC,SYF,SNPS,SYY,TROW,TTWO,TPR,TGT,TEL,FTI,TXN,TXT,TMO,TIF,TWTR,TJX,TMK,TSS,TSCO,TDG,TRV,TRIP,FOXA,FOX,TSN,UDR,ULTA,USB,UAA,UA,UNP,UAL,UNH,UPS,URI,UTX,UHS,UNM,VFC,VLO,VAR,VTR,VRSN,VRSK,VZ,VRTX,VIAB,V,VNO,VMC,WMT,WBA,DIS,WM,WAT,WEC,WCG,WFC,WELL,WDC,WU,WRK,WY,WHR,WMB,WLTW,WYNN,XEL,XRX&',
			'XLNX,XYL,YUM,ZBH,ZION,ZTS&']
	
	#Returns 5year data from a batch of symbols.
	def GetBatch(self, symbols = "SPY,APPL,F,GE,FB"):
		yesterdayData = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols='+symbols+'&types=chart&range=5y').json()
		if not yesterdayData:
			print('Invalid Symbols')
			exit()
		else:
			return yesterdayData

	#Appends a Candle Object to a DataFrame
	def CandleToDataFrame(df, stock, candle):
		temp = iex_record(candle['date'], stock, candle['open'], candle['high'], candle['low'], candle['close'], candle['volume'], candle['change'], candle['changePercent'], candle['vwap'])
		if not (temp.get_date() in df['data'].values):
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
		return df

	def map_to_df(self, df, stock, day):

		##got to make sure value is present, and if not set it to null
		if 'date' in day.keys(): 
			date = day['date']
		else: 
			date = None
		if 'open' in day.keys(): 
			open_val = day['open']
		else: 
			open_val = None
		if 'high' in day.keys(): 
			high = day['high']
		else: 
			high = None
		if 'low' in day.keys(): 
			low = day['low']
		else: low = None
		if 'close' in day.keys(): 
			close = day['close']
		else: 
			close = None
		if 'volume' in day.keys(): 
			volume = day['volume']
		else:
			volume = None
		if 'change' in day.keys(): 
			change = day['change']
		else: 
			change = None
		if 'changePercent' in day.keys(): 
			changePercent = day['changePercent']
		else: 
			changePercent = None
		if 'vwap' in day.keys(): 
			vwap = day['vwap']
		else: 
			vwap = None


		temp = iex_record(date, stock, open_val, high, low, close, volume, change, changePercent, vwap)
		if not (date in df['date'].values) and date != None:
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
		return df

	def Download_2(self):
		columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
		for batch in self.batches:
			json = self.GetBatch(batch)
			for stock in json:
				print(stock)



				try:
					df = pd.read_pickle(PATH_CONFIG["StockDataPath"] / (stock + '.pkl'))
				except IOError:
					df = pd.DataFrame(columns = columns)

				for day in json[stock]['chart']:
					df = self.map_to_df(df, stock, day)

				df.to_pickle(PATH_CONFIG["StockDataPath"] / (stock + '.pkl'))




	#Run this method to get the past 5 years data or yesterday's data.
	def Download(symbols = "SPY,APPL,F,GE,FB"):
		#Usage:
		columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
		stockData = StockData.GetBatch()
		#print(stockData['SPY']['chart'][-1])

		for stock in stockData:
			try:
				df = pd.read_pickle(PATH_CONFIG["StockDataPath"] / (stock + ".pkl"))
			except IOError:
				df = pd.DataFrame(columns=columns)

			#If we don't have a pickle, get the 5 year data

			if (not os.path.exists(PATH_CONFIG['StockDataPath'] / (stock + ".pkl"))):
				for candle in stockData[stock]['chart']:
					df = StockData.CandleToDataFrame(df,stock,candle)

			else:#We have a pickle, lets just append yesterday's data.
				candle = stockData[stock]['chart'][-1]
				df = StockData.CandleToDataFrame(df, stock, candle)

			print(df.head())
			print(df.tail())
			df.to_pickle("StockData/" + stock + ".pkl")

	#Reads Saved Pickle and returns dataframe.
	def Get(symbol):
		if (StockData.os.path.exists("StockData/" + symbol + ".pkl")):
			return StockData.pd.read_pickle("StockData/" + symbol + ".pkl")
		else:
			print('File Not Found')
			exit()

def main():
	date = StockData()
	date.Download_2()
	# StockData.Download()


if __name__ == '__main__':
	main()