#Notes: some tickers break the code because they do not have data
#entries for every single day e.g. in october of 2017 the 11th or 12th
#for the ticker ONCE there is no 'open' data, so it breaks


import requests
import array
import matplotlib.pyplot as plt
 
 #Some inputs needed for which data to retrieve from database
yearsofdata = input('Enter number of years of data to test (1, 2, or 5):  ')
print('\n')
rate = float(input("Enter gap percentage to trade e.g. 0.01 for 1\% increase/decrease: "))
print('\n')

#Returns 5year data from a batch of symbols. Ex: "SPY,APPL,F,GE,FB"
def GetBatchOfHistoricalData(symbols):
    yesterdayData = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols='+symbols+'&types=chart&range=%sy' % yearsofdata).json()
    if not yesterdayData:
        return 0
    else:
        return yesterdayData
 
#Start of program here
tickerarray = list(map(str, input("Enter tickers for testing algo: ").split())) 
print('\n')

for j in range(len(tickerarray)):
  ticker = tickerarray[j]

  #initialize values back to empty arrays
  #initializing the open, close, and percent change (gap)
  dayopen = []
  dayclose = []
  day = []
  percentchange = [0]
  currentgap = [0]

  #initalize money at $100 so percent increase/decrease
  #is easy to see overall
  money = [100]

  #get data for the current ticker
  candleData = GetBatchOfHistoricalData(ticker)


  #find the total number of days (minus one anyway) to use
  #for indexing things
  dayindex = len(candleData[ticker]['chart'])
  print('Actual length of time for %s is %.2f years\n' % (ticker, (dayindex/252)))

  #first get all of the data in an easier to use format
  for i in range(dayindex):
    #build arrays of open and close values for each day
    dayopen.append(candleData[ticker]['chart'][i]['open'])
    dayclose.append(candleData[ticker]['chart'][i]['close'])

  #calculate the percent change from the day before
  for x in range(1, dayindex):
    

    #Check gap looks to see what the gap from yesterday close to 
    #open today.
    #Change gets the percent change for the day to calculate
    #how much you make/lose for the day if you buy/short.
    checkgap = dayopen[x]/dayclose[x-1]
    daychange = dayclose[x]/dayopen[x]
    currentgap.append(checkgap)
    percentchange.append(daychange)

  #starting the actual trading algorithm

  shortrate = 1. + rate
  buyrate = 1. + rate

  for y in range(1, dayindex):
    #if the percent change is a jump of more than 1% shortsell
    #shortsell to end of same day
    if currentgap[y] > shortrate:
      money.append((1/percentchange[y])*money[y-1])

    #if the percent change is a drop of more than 1% buy
    #buy at open and sell at close of same day
    if (currentgap[y] < (1. - rate)) & (currentgap[y] > 0): 
      money.append(percentchange[y]*money[y-1])

    if (currentgap[y] >= (1. - rate)) & (currentgap[y] <= (1. + rate)):
      money.append(money[y-1])

    # if money < 0:
    #   print('Gone broke! On day %s' % candleData[ticker]['chart'][y]['date'])
    #   break

  notouchmoney = (dayclose[dayindex-1]/dayopen[0])*100

  print('Ended with %f trading with ticker %s after %s years' % (money[dayindex-1], ticker, yearsofdata))
  print('Compared to %f for %s years of no trading\n' % (notouchmoney, yearsofdata))

  for p in range(dayindex):
    day.append(p)

  #Plotting with two axes labeled to see actual stock prices
  fig, ax1 = plt.subplots()
  ax1.plot(day, money, "b-")
  ax1.set_xlabel('Days since %.2f years ago' % (dayindex/252))
  ax1.set_ylabel('Money in your account ($)')
  ax1.tick_params('y', colors = 'b')
  ax2 = ax1.twinx()
  ax2.set_ylabel('Market close prices')
  ax2.plot(day, dayclose, "r-")
  ax2.tick_params('y', colors = 'r')
  fig.tight_layout()
  plt.show()

exit()