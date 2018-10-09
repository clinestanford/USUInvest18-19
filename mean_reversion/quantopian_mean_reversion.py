import talib  
import numpy as np
# --------------------------  
stock = symbol('TSLA')  
#Fast, Slow, Sig = 2, 6, 1 
# --------------------------  
def initialize(context):  
    schedule_function(trade, date_rules.every_day(), time_rules.market_open(minutes = 65))
    context.buy=True

def trade(context,data):  
    #bars = Fast + Slow + Sig  
    prices = data.history(stock, 'price', 21, '1d')  
    avg = np.mean(prices)
    current = data.current(stock,'price')
    #macd, signal, hist = talib.MACD(prices, Fast, Slow, Sig)  
    if current < avg * .97 and context.buy:  
        order_target_percent(stock, 1.0)  
        context.buy = False
        print("bought at: ",current, " average is: ", avg)
    elif current > avg * 1.03 and not context.buy:  
        order_target_percent(stock, 0) 
        context.buy = True
        print("sold at: ",current, " average is: ", avg)
    else:
        pass