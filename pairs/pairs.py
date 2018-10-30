import numpy as np

def initialize(context):
    context.fnv=sid(44089)#BCC Boise Cascade Lumber
    context.rgld=sid(5969)#PHM Pulte Home Building
    
    schedule_function(trade, date_rules.every_day(), time_rules.market_open(minutes = 65))
    
def trade(context, data):
    rgld_avg = np.mean(data.history(context.rgld,'price',5,'1d'))
    fnv_avg = np.mean(data.history(context.fnv,'price',5,'1d'))
    spread_avg = (rgld_avg - fnv_avg)
    
    rgld_curr = data.current(context.rgld,'price')
    fnv_curr = data.current(context.fnv,'price')
    spread_curr = (rgld_curr - fnv_curr)
    print("rgld_curr, fnv_curr, spread_avg, spread_curr,spread_curr/spread_avg: ",rgld_curr,fnv_curr,spread_avg,spread_curr,spread_curr/spread_avg)
          
    if spread_curr > spread_avg*1.10:#detect a wide spread
        print("wide: spread_avg, spread_curr: ",spread_avg,spread_curr)
    
        order_target_percent(context.rgld,0)
        order_target_percent(context.fnv,1)
    elif spread_curr < spread_avg*.90:#detect a tight spread
        print("tight: spread_avg, spread_curr: ",spread_avg,spread_curr)
        order_target_percent(context.rgld,1)
        order_target_percent(context.fnv,0)
    else:
        pass