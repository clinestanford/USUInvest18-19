import pandas as pd 
import matplotlib.pyplot as plt 


file = "ARE.csv"

over = 1.02
under = .98

df = pd.read_csv(file)
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

thirty["over"] = thirty["30_close"]*over
thirty["under"] = thirty["30_close"]*under

fifty["over"] = fifty["50_close"]*over
fifty["under"] = fifty["50_close"]*under

ten["over"] = ten["10_close"]*over
ten["under"] = ten["10_close"]*under

thirty.plot(title="thirty day window")
fifty.plot(title="fifty day window")
ten.plot(title="ten day window")

plt.show(block=True)





