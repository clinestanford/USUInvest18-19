#Class to handle the previous days data


import sys


class StockData:
    import requests
    import pandas as pd
    from record import record
    from datetime import datetime
    from chart import chart
    import os.path
    #Returns 5year data from a batch of symbols.
    def GetBatch(symbols = "SPY,APPL,F,GE,FB"):
        yesterdayData = StockData.requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols='+symbols+'&types=chart&range=5y').json()
        if not yesterdayData:
            print('Invalid Symbols')
            exit()
        else:
            return yesterdayData

    #Appends a Candle Object to a DataFrame
    def CandleToDataFrame(df, stock, candle):
        temp = StockData.chart(candle['date'], stock, candle['open'], candle['high'], candle['low'], candle['close'], candle['volume'], candle['change'], candle['changePercent'], candle['vwap'])
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

    #Run this method to get the past 5 years data or yesterday's data.
    def Download(symbols = "SPY,APPL,F,GE,FB"):
        #Usage:
        columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
        stockData = StockData.GetBatch()
        #print(stockData['SPY']['chart'][-1])

        for stock in stockData:
            try:
                df = StockData.pd.read_pickle("StockData/" + stock + ".pkl")
            except IOError:
                df = StockData.pd.DataFrame(columns=columns)

            #If we don't have a pickle, get the 5 year data
            if (not StockData.os.path.exists("StockData/" + stock + ".pkl")):
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
    StockData.Download()


if __name__ == '__main__':
    main()