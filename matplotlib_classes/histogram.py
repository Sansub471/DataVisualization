# The lesson is about histogram
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

data = pd.read_csv('dataHist.csv')
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'


# you can pass bins as a list as well
# to exclude just remove bin, e.g to remove ages < 20
# just remove bin 10
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# log = True is logarithmic scale
plt.hist(ages, bins=bins, edgecolor='black', log=True) # bins = 5 divide the data into 
# 5 beans, and plot it.

# vertical line
plt.axvline(median_age, color=color, label='Age Median', linewidth=2)
plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()
plt.show()

