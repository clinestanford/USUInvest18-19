import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv("Ford.csv")
df = df.set_index("date")
df = df[["close", "volume"]]
df = df.reindex(index=df.index[::-1])

thirty = df.rolling(window=30).mean()

fifty = df.rolling(window=50).mean()

hundred = df.rolling(window=10).mean()

thirty = thirty.rename(columns={"close":"30_close", "volume":"30_volume"})

fifty = fifty.rename(columns={"close":"50_close", "volume":"50_volume"})

hundred = hundred.rename(columns={"close":"100_close", "volume":"100_volume"})

thirty = pd.merge(df, thirty, how="inner", left_index=True, right_index=True)

fifty = pd.merge(df, fifty, how="inner", left_index=True, right_index=True)

hundred = pd.merge(df, hundred, how="inner", left_index=True, right_index=True)


thirty = thirty[["close", "30_close"]]

fifty = fifty[["close", "50_close"]]

hundred = hundred[["close", "100_close"]]

thirty = thirty.dropna()
fifty = fifty.dropna()
hundred = hundred.dropna()

thirty["over"] = thirty["30_close"]*1.03
thirty["under"] = thirty["30_close"]*.97

fifty["over"] = fifty["50_close"]*1.05
fifty["under"] = fifty["50_close"]*.95

hundred["over"] = hundred["100_close"]*1.05
hundred["under"] = hundred["100_close"]*.95

thirty.plot(title="thirty day window")
fifty.plot(title="fifty day window")
hundred.plot(title="hundred day window")

plt.show(block=True)





