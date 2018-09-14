import pandas as pd 
import matplotlib.pyplot as plt


pd.set_option('display.mpl_style', 'default')
nvidia = pd.read_csv("Nvidia.csv", header=0, index_col=0)
nvidia = nvidia.reindex(index=nvidia.index[::-1])

sma = nvidia.rolling(window=10).mean()

sma.rename(columns = {'close':'sma_close', 'voluem':'sma_volume'}, inplace=True)

sma.drop(labels=["open", "high", "low"], axis=1, inplace=True)
nvidia.drop(labels=["open", "high", "low"], axis=1, inplace=True)

print(nvidia.head())
print(sma.head())

merge = pd.merge(nvidia, sma, how="inner",left_index=True, right_index=True)
merge=merge.dropna()
print(merge.head(15))

plt.style.use('ggplot')
merge[['close','sma_close']].plot()

plt.show(block=True)

