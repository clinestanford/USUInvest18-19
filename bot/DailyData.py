

class DailyData:

    import requests
    import pandas as pd
    from chart import chart
    from record import record
    from datetime import datetime

    #Takes interval which is how often, symbols, and the time you want back. Time MUST be in hh:mm format.
    #Ex: eleven am = 11:00
    def get_data(interval,symbols,time):
        url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
        urlTypes = 'types=chart&'
        #symbols = "AAPL,F,GE,SPY,FB&"
        urlRange = 'range=1d&chartInterval='+interval



        symbols = 'MMM,ABT&'  # ,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&'

        r = DailyData.requests.get(url + symbols + urlTypes + urlRange)
        json = r.json()
        columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
        pd = DailyData.pd.DataFrame(columns=columns)

        for stock in json:
            print(stock)
            for chart in json[stock]['chart']:
                if chart['minute'] == time:
                    pd = DailyData.map_to_chart(chart,pd,stock)

        print(pd.head())
        print(pd.tail())
        pd.to_pickle("StockDataDaily/" + stock + ".pkl")

    def map_to_chart(candle,pd,stock):
        temp = DailyData.chart(candle['date'], stock, candle['open'], candle['high'], candle['low'], candle['close'],
                               candle['volume'], "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE")
        pd = pd.append({'date': temp.get_date(),
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
        return pd