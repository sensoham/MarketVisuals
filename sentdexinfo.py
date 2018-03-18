import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

plt.style.use('ggplot')
ts = TimeSeries(key='', output_format='pandas')
data, meta_data = ts.get_intraday('')  # put ticker here
df_meta = meta_data
df = data
df.index = pd.to_datetime(df.index)
##print(data)


#10 moving average

df['10ma'] = df['4. close'].rolling(window = 10).mean()
df.dropna(inplace = True)

ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 6, colspan=1)
ax2 = plt.subplot2grid((10,1), (7,0), rowspan = 2, colspan=1, sharex=ax1)

ax1.plot(df.index, df['4. close'])
ax1.plot(df.index, df['10ma'])
ax2.bar(df.index, df['5. volume'], width = 0.01)

plt.show()
