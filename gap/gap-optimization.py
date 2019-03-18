#Notes: some tickers break the code because they do not have data
#entries for every single day e.g. in october of 2017 the 11th or 12th
#for the ticker ONCE there is no 'open' data, so it breaks


import requests
import array
import matplotlib.pyplot as plt
import numpy as np

 
 #Some inputs needed for which data to retrieve from database
yearsofdata = input('Enter number of years of data to test (1, 2, or 5):  ')
print('\n')

#Returns 5year data from a batch of symbols. Ex: "SPY,APPL,F,GE,FB"
def GetBatchOfHistoricalData(symbols):
    yesterdayData = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols='+symbols+'&types=chart&range=%sy' % yearsofdata).json()
    if not yesterdayData:
        return 0
    else:
        return yesterdayData
 
#Get user inputs for which tickers to experiment with
tickerarray = list(map(str, input("Enter tickers for testing algo: ").split())) 
print('\n')

#PercentRate indicates the range of trading percents you are 
#interested in e.g. 0.08 indicates 0-8%
#npts indicates how many points for the range of interest
percentrate = 0.1
npts = 1000


for j in range(len(tickerarray)):

  ticker = tickerarray[j]

  #initialize values back to empty arrays
  #initializing the open, close, and percent change (gap)
  dayopen = []
  dayclose = []
  day = []
  percentchange = [0]
  currentgap = [0]
  profits = []

  #get data for the current ticker
  candleData = GetBatchOfHistoricalData(ticker)


  #find the total number of days (minus one anyway) to use
  #for indexing things
  dayindex = len(candleData[ticker]['chart'])
  #print('Actual length of time for %s is %.2f years\n' % (ticker, (dayindex/252)))

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

  #Initialize rate at 0 so that it will cycle through to percentrate
  rate = 0.

  #Iterate through all of the different trading percentages
  for k in range(npts):
    rate = rate + percentrate/npts


    #initalize money at $100 so percent increase/decrease
    #is easy to see overall
    money = [100]


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

    #notouchmoney = (dayclose[dayindex-1]/dayopen[0])*100

    #print('Ended with %f trading with ticker %s after %s years' % (money[dayindex-1], ticker, yearsofdata))
    #print('Compared to %f for %s years of no trading\n' % (notouchmoney, yearsofdata))

    profits.append(money[dayindex-1])
    print('%.2f percent complete' % ((k/npts)*100), end='\r')

  raterange = [0]

  for t in range(1, npts):
    raterange.append(raterange[t-1] + percentrate/npts)

  index_max = np.argmax(profits)

  #Plotting to show maximal value for trading percentage
  print('To maximize return (%.2f) for %s trade at gap of %.4f percent' % (max(profits), ticker, (index_max*(percentrate/npts))))
  plt.plot(raterange, profits)
  plt.title('Earnings after %.2f years in %s' % ((dayindex/252), ticker))
  plt.xlabel('Trade rate')
  plt.ylabel('Investment ($)')
  plt.show()

exit()