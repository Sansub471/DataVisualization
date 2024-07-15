from matplotlib import pyplot as plt

# Built in plot styles
print(plt.style.available)

plt.style.use('bmh')
# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# plt.plot(ages_x, py_dev_y,'b' ,label='Python Devs')
plt.plot(ages_x, py_dev_y, color='#5a7bce', marker='*', linestyle=':', linewidth=2 ,label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373,
            62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#adad3b', marker='+', linestyle='-.' , linewidth=2,label='Javascript')


dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, 'r+:', label='All Devs')
# To make it more redable
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')

plt.xlabel("Age(years)")
plt.ylabel("Salary in US$")
plt.title('Developer Salary by Age in USD')

plt.legend()
# plt.grid(True)

# Padding
plt.tight_layout()

# Save the plot
plt.savefig('plot.png')
plt.show()

# Format strings
# fmt = '[marker][line][color]'
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# Link to format strings
# Hex color values can be used for color