##import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from finance import candlestick_ohlc
import matplotlib.dates as mdates
plt.style.use('ggplot')
ts = TimeSeries(key='', output_format='pandas')
data, meta_data = ts.get_intraday('')  #put ticker here
df_meta = meta_data
df = data
df.index = pd.to_datetime(df.index)
df_vol = df['5. volume']

df.reset_index(inplace=True)
df['date'] = df['date'].map(mdates.date2num)
dfy = df[['date','1. open','2. high','3. low','4. close']].copy()


ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 6, colspan=1)
ax2 = plt.subplot2grid((10,1), (7,0), rowspan = 2, colspan=1, sharex=ax1)
ax1.xaxis_date()   #reconverting date from the wierd mdate format


candlestick_ohlc(ax1,dfy.values, width = 0.001, colorup = 'g')
ax2.fill_between(df_vol.index.map(mdates.date2num), df_vol.values,0)


plt.show()
