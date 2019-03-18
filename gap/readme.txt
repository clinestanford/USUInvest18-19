The files written in this folder are to test the gap trading algorithm. 

gap.py
This program trades by finding a gap between the opening of the current day compared to the close of the day before. If the gap is of a certain percentage (input) then the stock will either be bought at open then sold at closed, or shorted from open to close for the same day. 
inputs: number of years to test data, percentage to trade at (as decimal), and tickers to test (e.g. SPY AAPL, don't use comma in list).
outputs: graph of money made (initialized at 100), stock market prices, end amount of money you have compared to if you would have just kept the stock for the entirety of time tested
 

gap-optimization.py
This program finds the optimum trading percentage for the specified tickers over the specified historical time.
inputs: number of years of historical data to test on, tickers (e.g. SPY AAPL, don't use comma in list)
outputs: graph of investment using specified trading percentage at the end of testing period, the max return amount and trading rate.


Notes: Programs will crash if ticker has missing data point. This could be taken further by applying to live data, as well as independently optimizing short and buy/sell rates rather than keeping them the same rate.