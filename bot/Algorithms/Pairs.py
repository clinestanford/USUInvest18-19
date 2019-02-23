import pandas as pd
import numpy as np
from ..Utils.StockData import StockData
from ..Utils.Order import Order


# Methods:
#	trade - trade on deviations from average pair price-ratio
#
# Params:
#	pairs - 2D list containing list of ticker pairs
#	window - defines date-range for signal-generating data
class Pairs:
    def __init__(self, pairs, window):
        self.pairs = pairs
        self.money = money
        self.window = window

    def trade(self):
        orders = []

        for pair in self.pairs:
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
