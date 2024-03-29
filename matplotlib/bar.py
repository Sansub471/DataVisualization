from matplotlib import pyplot as plt
import numpy as np

# Built in plot styles
print(plt.style.available)

plt.style.use('bmh')
# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# To make sure that the bars don't stack up on top of each other
x_indexes = np.arange(len(ages_x))
width = 0.25 # width of the bar

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# For All Developers
plt.bar(x_indexes - width, dev_y, width = width ,color='#f5424b', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width = width ,color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373,
            62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width = width ,color="#e5ae38", label="Javascript")

# By simply plotting three bar graphs on a plot and showing it won't 
# do the job. We'll use numpy to solve this issue.

plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x) # To show correct Age labels.
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Salary (USD)")
plt.show()