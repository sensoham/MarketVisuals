##import datetime as dt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from plotly.offline import plot
import plotly.graph_objs as go




ts = TimeSeries(key='PJUU2VHAO4BAVEMU', output_format='pandas')
data, meta_data = ts.get_intraday('BOMDYEING')
df_meta = meta_data
df = data
df.index = pd.to_datetime(df.index)




trace = go.Candlestick(x=df.index, open=df['1. open'], high=df['2. high'], low=df['3. low'], close=df['4. close'])
data = [trace]
fig = go.Figure(data = data)
plot(fig,show_link = False)

##https://plot.ly/python/candlestick-charts/
