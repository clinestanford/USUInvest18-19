import pandas as pd
import numpy as np
from ..Utils.StockData import StockData
from ..Utils.Order import Order

class Pairs:
    def __init__(self, pairs, money, window):
        self.pairs = [[]]
        self.money = money
        self.window = window

    def trade(self):
        orders = []

        for pair in self.pairs:
            df1 = StockData.Get(pair[0])
            df2 = StockData.Get(pair[1])
            ratios = df1['close'][-self.window:] / df2['close'][-window:]
            z = self.getZScore(ratios)

            if z < -1:
                #buy

            elif z > 1:
                #sell

    def getZScore(self, ratios):
        zScore = (ratios[-1] - ratios.mean()) / np.std(ratios)
        return zScore





