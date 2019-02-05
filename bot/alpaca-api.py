
import requests as r
import pandas as pd
from record import record
from datetime import datetime

#headers = {"APCA-API-KEY-ID":PKSRSFKPE467RCMPKRAQ, "APCA-API-SECRET-KEY": husqyWiH6aawS34SCYEHm0FT8eqgwTQs6utgZUQn}

urlTypes = 'types=chart&'
urlRange = 'range=1d'
# first100 = 'MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&'url = "https://paper-api.alpaca.markets"
# url = 'https://data.alpaca.markets/v1'

"https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote,news,chart&range=1m&last=5"
url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
symbols = 'MMM,ABT&' #,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&'

r = r.get(url+symbols+urlTypes+urlRange)
print(r.json())

# for stock in r.json():
# 	print(stock)










