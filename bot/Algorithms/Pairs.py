import pandas as pd
import numpy as np
from ..Utils.StockData import StockData
from ..Utils.Order import Order


# Methods:
#	trade - trade on deviations from average pair price-ratio
#
# Params:
#	pair - ticket pair as list
#	window - defines date-range for signal-generating data
class Pairs(BaseAlgorithm):
    def __init__(self, pairs, window):
        super(Pairs, self).__init__()
        self.pairs = pairs
        self.money = money
        self.window = window

    def getOrder(self):
        orders = []

        pair1 = StockData.Get(pair[0])
        pair2 = StockData.Get(pair[1])
        ratios = pair1['close'][-self.window:] / pair2['close'][-self.window:]

        # Normalize current ratio
        z = self.getZScore(ratios)

        if z < -1:
            # buy s1, sell s2
            buyOrder = Order(pair[0], 1, 'buy', 'market', 'day')
            sellOrder = Order(pair[1], np.round(ratios[-1]), 'sell', 'market', 'day')

            orders.appendAll(buyOrder, sellOrder)

        elif z > 1:
            # sell s1, buy s2
            sellOrder = Order(pair[0], 1, 'sell', 'market', 'day')
            buyOrder = Order(pair[1], np.round(ratios[-1]), 'buy', 'market', 'day')

            orders.appendAll(buyOrder, sellOrder)

        return orders


    def getZScore(self, ratios):
        zScore = (ratios[-1] - ratios.mean()) / np.std(ratios)
        return zScore
