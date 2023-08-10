import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('dataLinePlot.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# plt.plot(ages, py_salaries, label='Python')
# plt.plot(ages, js_salaries, label='JavaScript')
# plt.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
# plt.legend()

# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
# plt.tight_layout()
# plt.show()

# We are using the plt object, the one we imported.
# Let's talk about figure and axes.
fig, ax = plt.subplots() # Create a figure and no. of axes
ax.plot(ages, py_salaries, label='Python')
ax.plot(ages, js_salaries, label='JavaScript')
ax.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax.legend()
ax.set_title('Median Salary (USD) by Age')
ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()