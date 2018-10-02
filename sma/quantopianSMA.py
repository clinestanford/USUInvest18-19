# This algo demostrates how to run a daily strategy in quantopian
# Quantopian runs before_trading_start every morning, however you cannot
# place orders in this function.  So we will set variables, so the first 
# time handle_data runs in the morning, it places our order.

def initialize(context):
    # initializing varables
  	# scheduling before_trading_start
    schedule_function(before_trading_start, date_rules.every_day(), time_rules.market_open(hours=1))
    context.msft=sid(5061)
    context.buy=0.0
    context.buyToday=False
    context.sellToday=False
    
def before_trading_start(context, data):
    # Checking each morning to see if current price has risen above 5 day avg
    # if so, setting variable buyToday to True, so we buy the first time handle_data runs
    # if current has gone below the 5 day avg, then sell
    curr= data.current(context.msft, 'price')
    hist= data.history(context.msft, 'price', 5, '1d')
    avg=hist.mean()
    
    print "before day curr: ",curr
    print "before day hist, 5 day avg: ",avg
    if(curr>avg and context.buy==0.0):
        context.buyToday=True
        context.buy=curr
        print "buying at price: ",curr
        
	if(curr<avg and context.buy!=0.0): #sell signal detected, selling...
		context.sellToday=True
        context.buy=0.0
        print "selling at price: ",curr
 
def handle_data(context,data):
    # This function runs every minute, however our logic to buy/sell
    # will only run the first time, then the buy/sell variables will
    # be set to false, and we're done trading for today.  Note: this is 
    # a daily trading strategy
    if(context.buyToday): 
        order_target_percent(context.msft,1)
        context.buytoday=False
    if(context.sellToday):
        order_target_percent(context.msft,-1)
        context.sellToday=False
