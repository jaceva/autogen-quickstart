# filename: stock_chart.py

import matplotlib.pyplot as plt
import pandas_datareader as pdr

# Step 2: Retrieve historical stock price data
nvda_data = pdr.get_data_yahoo('NVDA')
tesla_data = pdr.get_data_yahoo('TSLA')

# Step 3: Filter the data to include only YTD data
nvda_ytd = nvda_data[nvda_data.index.year == nvda_data.index.max().year]
tesla_ytd = tesla_data[tesla_data.index.year == tesla_data.index.max().year]

# Step 4: Plot the YTD stock price change for both NVDA and TESLA
plt.plot(nvda_ytd.index, nvda_ytd['Adj Close'], label='NVDA')
plt.plot(tesla_ytd.index, tesla_ytd['Adj Close'], label='TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('NVDA and TESLA Stock Price Change YTD')
plt.legend()
plt.show()
