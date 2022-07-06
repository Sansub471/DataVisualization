from matplotlib import pyplot as plt

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Add legend to identify which line is which
#plt.plot(ages_x, dev_y, py_dev_y)
#plt.xlabel("Age(years)")
#plt.ylabel("Salary in US$")
#plt.title('Developer Salary by Age in USD')
#plt.show()

for i in range(9):
    print(i%3)
