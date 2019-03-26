#Example Bot
from Alpaca import Alpaca

#Define API credentials, Enter your keys here
keyID = 'PKSRSFKPE467RCMPKRAQ'
secretKey = 'husqyWiH6aawS34SCYEHm0FT8eqgwTQs6utgZUQn'

#Instantiate an Alpaca object to access the API
alpaca = Alpaca(keyID, secretKey)

#Authenticate to Alpaca
print('Connecting to Alpaca API...')
account = alpaca.GetAccount()
if ('status' in account and account['status'] == 'ACTIVE'):
    print('Authenticated Successfully!')
else:
    print('Error, invalid API key or account is disabled.')
    exit()

def RefreshAccount():
    return alpaca.GetAccount()

def ShowMenu():
    account = RefreshAccount()
    option = 0;
    print('\r\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=x TradingBot x=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\r\n')
    print('Portfolio Value: ', account['portfolio_value'])
    print('Buying Power: ', account['buying_power'])
    print('\r\n     - 1) Place Order')
    print('     - 2) Get Orders')
    print('     - 3) Cancel Order')
    print('     - 4) Show Open Positions\r\n')
    while(option not in ('1','2','3','4')):
        option = input('Action: ')

    if (option == '1'):
        symbol = input('Symbol: ')
        limitPrice = 0
        stopPrice = 0
        quantity = input('Number of Shares: ')
        side = 0
        while (side not in ('buy','sell')):
            side = input('Side (buy/sell): ')
        type = 0
        while (type not in ('market','limit','stop','stop_limit')):
            type = input('Side (market/limit/stop/stop_limit): ')
        if (type in ('limit','stop_limit')):
            limitPrice = input('Limit Price: ')
        if (type in ('stop','stop_limit')):
            stopPrice = input('Stop Price: ')
        time = 0
        while (time not in ('day','gtc','opg')):
            time = input('Time in force can be  Day, good till close, or at market open (day/gtc/opg): ')

        if (not float(limitPrice) > 0):
            limitPrice = None
        if (not float(stopPrice) > 0):
            stopPrice = None
        order = Alpaca.Order(symbol,quantity,side,type,time, limitPrice, stopPrice)
        placedOrder = alpaca.CreateOrder(order)
        if ('status' in placedOrder and placedOrder['status'] == 'new'):
            print('Order Placed Successfully!')
            exit()
        else:
            print("Order Not Placed.")
            exit()

    if (option == '2'):
        orders = alpaca.GetAllOrders()
        if (len(orders) == 0):
            print('No Orders.')
            exit()
        for order in orders:
            print('\r\nID: ',  order['id'])
            print('Symbol: ', order['symbol'])
            print('Quantity: '+ order['filled_qty'] +'/' +order['qty'])
            print('AveragePrice: ', order['filled_avg_price'])
        exit()

    if (option == '3'):
        orderID = input('OrderID to Cancel: ')
        result = alpaca.CancelOrderByID(orderID)
        if (result == 1):
            print('Successfully Canceled.')
        else:
            print('Error Canceling.')

    if (option == '4'):
        openPositions = alpaca.GetOpenPositions()
        if (len(openPositions) == 0):
            print('No Open Positions.')
            exit()
        for order in openPositions:
            print('\r\nSymbol: ', order['symbol'])
            print('Quantity: ', order['qty'])
            print('Side: ', order['side'])
            print('Value: ', order['market_value'])
            print('Profit/Loss: ', order['unrealized_pl'])
            print('Percentage: ', order['unrealized_plpc'])
            print('AveragePrice: ', order['avg_entry_price'])
            print('Current Price: ', order['current_price'])
            print('Last Close: ', order['lastday_price'])
            print('Change Today: ', order['change_today'])
        exit()

ShowMenu()
