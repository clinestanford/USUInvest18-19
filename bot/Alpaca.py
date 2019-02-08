
#Provides access to the Alpaca API functions
class Alpaca:
    import requests
    from Order import Order
    import json

    def __init__(self, keyID, secretKey, isPaper = True):
        self.keyID = keyID
        self.secretKey = secretKey
        self.headers = {'APCA-API-KEY-ID': keyID, 'APCA-API-SECRET-KEY': secretKey}
        self.isPaper = isPaper
        if (isPaper == True):
            self.url = 'https://paper-api.alpaca.markets/v1/'
        else:
            self.url = 'https://api.alpaca.markets/v1/'

    #Returns account info
    def GetAccount(self):
        return self.requests.get(self.url + 'account', headers=self.headers).json()

    #Returns a list of all current orders
    def GetAllOrders(self):
        return self.requests.get(self.url + 'orders', headers=self.headers).json()

    #Returns an order by OrderID
    def GetOrderByID(self, orderID):
        return self.requests.get(self.url + 'orders/' + orderID, headers=self.headers).json()

    #Place an order, returns the placed order.
    def CreateOrder(self, order):
        return self.requests.post(self.url + 'orders', headers=self.headers, data=self.json.dumps(order.__dict__)).json()

    #Cancel a placed order by orderID
    def CancelOrderByID(self, orderID):
        if (self.requests.delete(self.url + 'orders/' + orderID, headers=self.headers).status_code == 204):
            return 1 #Success
        else:
            return 0 #Failure

    #Returns a list of all open positions
    def GetOpenPositions(self):
        return self.requests.get(self.url + 'positions', headers=self.headers).json()

    #Returns a list of open positions by symbol or assetID
    def GetOpenPositionsBySymbol(self, symbol):
        return self.requests.get(self.url + 'positions/' + symbol, headers=self.headers).json()

    #Returns a list of all assets
    def GetAllAssets(self):
        return self.requests.get(self.url + 'assets', headers=self.headers).json()

    #Returns a list of all assets
    def GetAssetBySymbol(self, symbol):
        return self.requests.get(self.url + 'assets/' + symbol, headers=self.headers).json()

    #Returns the current market time, is_open, next_open, and next_close
    def GetMarketClock(self):
        return self.requests.get(self.url + 'clock', headers=self.headers).json()

    #Todo: Add Calendar and Streaming if we end up needing it.
