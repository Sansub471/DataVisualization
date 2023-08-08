# Line plots with fields
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('dataLinePlot.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color="#444444",
          linestyle='--', label='All Devs')
# overall_median  = 57287
# # Create fill for plot
# plt.plot(ages, py_salaries, label='Python')
# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries > overall_median), 
#                  interpolate=True, color="#cd1278", alpha=0.25)

# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries <= overall_median), 
#                  interpolate=True, alpha=0.25)
# plt.legend()
# plt.title("Median Salary (USD) by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salaries")
# plt.show()

plt.plot(ages, py_salaries, label='Python')
plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries > dev_salaries), 
                 interpolate=True, color="#cd1278", alpha=0.25,
                 label="Above Avg")

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries <= dev_salaries), 
                 interpolate=True, alpha=0.25,
                 label="Below Avg")
plt.legend()
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salaries")
plt.show()

# This is a formatted line plots.