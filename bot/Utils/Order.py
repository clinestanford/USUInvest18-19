# An Order Model used by the Alpaca API class
class Order:
    def __init__(self, symbol, quantity, side, type, timeInForce, limitPrice = None, stopPrice = None):
        self.symbol = symbol #Symbol or Asset ID being traded
        self.qty = quantity #Number of shares to trade
        self.side = side #buy or sell
        self.type = type #market, limit, stop, or stop_limit
        self.time_in_force = timeInForce #day, gtc, opg
        if (limitPrice is not None):
            self.limit_price = limitPrice #Required if type is limit or stop_limit.
        if (stopPrice is not None):
            self.stop_price = stopPrice #Required if type is stop or stop_limit
