# SuperTrendIndicator
This code demonstrates how to use the Alpha Vantage API to retrieve historical stock price data for IBM, calculate the Super Trend Indicator, and plot it over time using Python.

Here is a breakdown of the code:

Import the required Python modules: requests for sending HTTP requests, pandas for data manipulation, numpy for numerical computations, and matplotlib for data visualization.

Set the API endpoint URL and parameters. In this case, the function parameter is set to "TIME_SERIES_INTRADAY" to retrieve intraday (5-minute) stock price data for IBM, the symbol parameter is set to "IBM", the interval parameter is set to "5min", and the apikey parameter is set to a demo key provided by Alpha Vantage.

Send an HTTP GET request to the API and retrieve the response using the requests.get() method.

Parse the JSON data in the response into a Python dictionary using the response.json() method.

Convert the data dictionary into a pandas DataFrame using the pd.DataFrame.from_dict() method, setting the orient parameter to "index" to indicate that the dictionary keys should be used as row labels.

Rename the columns of the DataFrame to be more descriptive.

Convert the data types of the columns to be more usable, using the pd.to_numeric() method to convert the Open, High, Low, Close, and Volume columns to numeric data types.

Calculate the Average True Range (ATR) using a rolling window, using the following formula:

TR1 = abs(High - Low)
TR2 = abs(High - Close.shift())
TR3 = abs(Low - Close.shift())
TR = max(TR1, TR2, TR3)
ATR = rolling_mean(TR, window=7)

Calculate the Super Trend Indicator using the following formula:
Upper Basic = (High + Low) / 2 + multiplier * ATR
Lower Basic = (High + Low) / 2 - multiplier * ATR
Upper Final = min(Upper Basic, Upper Final(previous)) if Close <= Upper Final(previous) else Upper Basic
Lower Final = max(Lower Basic, Lower Final(previous)) if Close >= Lower Final(previous) else Lower Basic
Super Trend = Upper Final if Close <= Upper Final else Lower Final

Plot the Super Trend Indicator over time using the matplotlib.pyplot.plot() method, with the Closing Price and Super Trend plotted on the y-axis and time plotted on the x-axis. The plot is labeled with a title and legend using the pyplot.title() and pyplot.legend() methods, and displayed using the pyplot.show() method.

Output:

![Screenshot (100)](https://user-images.githubusercontent.com/110590945/236888263-31768720-52b2-4117-93f7-a76ed3bfebb4.png)
