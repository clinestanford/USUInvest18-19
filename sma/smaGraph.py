import pandas as pd 
import matplotlib.pyplot as plt

#set the style of matplotlib graph
pd.set_option('display.mpl_style', 'default')

#read in the csv as a dataframe and save it to variable nvidia
nvidia = pd.read_csv("Nvidia.csv", header=0, index_col=0)

#flip the dataframe to go from oldest to newest
nvidia = nvidia.reindex(index=nvidia.index[::-1])

#caluclate the simple moving average
sma = nvidia.rolling(window=10).mean()

#change the name of the columns to make joining easier
sma.rename(columns = {'close':'sma_close', 'voluem':'sma_volume'}, inplace=True)

#drop the open high and low for the nvidia and sma
sma.drop(labels=["open", "high", "low"], axis=1, inplace=True)
nvidia.drop(labels=["open", "high", "low"], axis=1, inplace=True)

#merge the two dataframes, inner means they are joined on indexes where
#both have that value. Look into types of joins if you don't understand
merge = pd.merge(nvidia, sma, how="inner", left_index=True, right_index=True)

#drop all values NaN (where the window was unable to caculate the mean over
#the last ten values)
merge=merge.dropna()

#not sure if this line even changes anything
plt.style.use('ggplot')
merge[['close','sma_close']].plot(title="nvidia")

#if you don't include this line, graph will pop up and exit immediately
plt.show(block=True)

