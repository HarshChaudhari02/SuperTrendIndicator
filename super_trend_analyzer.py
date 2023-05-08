import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setting the API endpoint URL
endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"

# Sending an HTTP GET request to the API and retrieve the response
response = requests.get(endpoint)

# Parsing the JSON data in the response into a Python dictionary
data = response.json()

# Converting the data dictionary into a pandas DataFrame
df = pd.DataFrame.from_dict(data["Time Series (5min)"], orient="index")

# Rename the columns to be more descriptive
df.columns = ["Open", "High", "Low", "Close", "Volume"]

# Converting the data types of the columns to be more usable
df["Open"] = pd.to_numeric(df["Open"])
df["High"] = pd.to_numeric(df["High"])
df["Low"] = pd.to_numeric(df["Low"])
df["Close"] = pd.to_numeric(df["Close"])
df["Volume"] = pd.to_numeric(df["Volume"])

# Calculating the Average True Range (ATR) using a rolling window
df["TR1"] = abs(df["High"] - df["Low"])
df["TR2"] = abs(df["High"] - df["Close"].shift())
df["TR3"] = abs(df["Low"] - df["Close"].shift())
df["TR"] = df[["TR1", "TR2", "TR3"]].max(axis=1)
df["ATR"] = df["TR"].rolling(window=7).mean()

# Calculating the Super Trend Indicator
multiplier = 3
df["Upper Basic"] = (df["High"] + df["Low"]) / 2 + multiplier * df["ATR"]
df["Lower Basic"] = (df["High"] + df["Low"]) / 2 - multiplier * df["ATR"]
df["Upper Final"] = df["Upper Basic"]
df["Lower Final"] = df["Lower Basic"]

for i in range(1, len(df)):
    if df["Close"][i] <= df["Upper Final"][i - 1]:
        df["Upper Final"][i] = min(df["Upper Basic"][i], df["Upper Final"][i - 1])
    else:
        df["Upper Final"][i] = df["Upper Basic"][i]
    if df["Close"][i] >= df["Lower Final"][i - 1]:
        df["Lower Final"][i] = max(df["Lower Basic"][i], df["Lower Final"][i - 1])
    else:
        df["Lower Final"][i] = df["Lower Basic"][i]
df["Super Trend"] = np.nan

for i in range(len(df)):
    if df["Close"][i] <= df["Upper Final"][i]:
        df["Super Trend"][i] = df["Upper Final"][i]
    else:
        df["Super Trend"][i] = df["Lower Final"][i]


# Plot the Super Trend Indicator over time
plt.plot(df["Close"], label="Closing Price")
plt.plot(df["Super Trend"], label="Super Trend")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.title("IBM Stock Price with Super Trend Indicator")
plt.legend()
plt.show()