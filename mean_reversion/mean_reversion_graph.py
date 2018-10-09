import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv("Spy.csv")
df = df.set_index("date")
df = df[["close", "volume"]]
df = df.reindex(index=df.index[::-1])

thirty = df.rolling(window=30).mean()

fifty = df.rolling(window=50).mean()

ten = df.rolling(window=10).mean()

thirty = thirty.rename(columns={"close":"30_close", "volume":"30_volume"})

fifty = fifty.rename(columns={"close":"50_close", "volume":"50_volume"})

ten = ten.rename(columns={"close":"100_close", "volume":"100_volume"})

thirty = pd.merge(df, thirty, how="inner", left_index=True, right_index=True)

fifty = pd.merge(df, fifty, how="inner", left_index=True, right_index=True)

ten = pd.merge(df, ten, how="inner", left_index=True, right_index=True)


thirty = thirty[["close", "30_close"]]

fifty = fifty[["close", "50_close"]]

ten = ten[["close", "100_close"]]

thirty = thirty.dropna()
fifty = fifty.dropna()
ten = ten.dropna()

thirty["over"] = thirty["30_close"]*1.03
thirty["under"] = thirty["30_close"]*.97

fifty["over"] = fifty["50_close"]*1.03
fifty["under"] = fifty["50_close"]*.97

ten["over"] = ten["100_close"]*1.03
ten["under"] = ten["100_close"]*.97

thirty.plot(title="thirty day window")
fifty.plot(title="fifty day window")
ten.plot(title="ten day window")

plt.show(block=True)





