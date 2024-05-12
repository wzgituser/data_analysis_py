import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
from fredapi import Fred

from dotenv import load_dotenv 

load_dotenv()


# print(plt.style.available)

plt.style.use('fivethirtyeight')
# pd.set_option('max_columns', 500)
# color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]

KEY = os.getenv("API_KEY")

fred = Fred(api_key= KEY)
# 1.Data heads
# f = fred.search('S&P',order_by='popularity')
# data = f.head() 
# print(data)
#2.Ploting
# sp500 = fred.get_series(series_id='SP500')
# sp500.plot(figsize=(10, 5), title='S&P 500', lw=2)
# plt.show()
# 3.Unemployment data-pulling up
unemp_result = fred.search('unemployment')
print(unemp_result)