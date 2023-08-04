import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates # chage date format

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

# For real life data
# data = pd.read_csv('dataTimeSeries.csv')
# price_date = data['Date']
# price_close = data['Close']

plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate() # get current figure (gcf) and auto format.
date_format = mpl_dates.DateFormatter('%b, %d, %Y') # Documentation
plt.gca().xaxis.set_major_formatter(date_format)
# gca  : get current axes

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.show()