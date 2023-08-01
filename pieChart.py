from matplotlib import pyplot as plt

# Learn to see all available styles
plt.style.use("fivethirtyeight")

slices  = [120, 80, 30, 20] # Don't have to add up to 100
labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
#colors = ['blue', 'red', 'yellow', 'green']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title("My Pie Chart")
plt.tight_layout()
plt.show()

# Another chart
# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 
          'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor' : 'black'})
plt.title("Language Popularity")
plt.tight_layout()
# plt.legend()
plt.show()

# Not a good idea to use pie chart when there is so many data, at most 
# 5 would be better.

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
plt.pie(slices, labels=labels, wedgeprops={'edgecolor' : 'black'})
plt.show()
