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

# fig, ax = plt.subplots() # Create a figure and no. of axes
# ax.plot(ages, py_salaries, label='Python')
# ax.plot(ages, js_salaries, label='JavaScript')
# ax.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
# ax.legend()
# ax.set_title('Median Salary (USD) by Age')
# ax.set_xlabel('Ages')
# ax.set_ylabel('Median Salary (USD)')

# plt.tight_layout()
# plt.show()

# Let's try with many rows and columns.
# fig, ax = plt.subplots(nrows=2, ncols=1) # Create a figure and no. of axes
# print(f'The returned figure looks like : {ax}')
# (ax1, ax2) = ax
# ax2.plot(ages, py_salaries, label='Python')
# ax2.plot(ages, js_salaries, label='JavaScript')
# ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
# ax2.set_xlabel('Ages')
# ax2.set_ylabel('Median Salary (USD)')

# ax1.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
# ax1.legend()
# ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
# ax1.set_ylabel('Median Salary (USD)')

# plt.tight_layout()
# plt.show()

# Create two figure now
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
