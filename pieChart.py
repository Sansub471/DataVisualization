from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices  = [120, 80, 30, 20] # Don't have to add up to 100
labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
#colors = ['blue', 'red', 'yellow', 'green']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title("My Pie Chart")
plt.tight_layout()
plt.show()

