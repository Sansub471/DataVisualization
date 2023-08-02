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
plt.plot(ages, py_salaries, label='Python')
plt.legend()
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salaries")
plt.show()
