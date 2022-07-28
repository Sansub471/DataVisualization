from matplotlib import pyplot as plt
import numpy as np

# Let's plot quadratic and cubic equations
x = np.linspace(0,3.5*np.pi,1000)
a = 0.5
b = 0.23
y = a * np.sin(x) * np.cos(x) + b * np.cos(x)

leg = 'y= ' + str(a)+'sinx cosx + ' + str(b) + 'cosx'
plt.plot(x,y, color='c', marker='', linestyle='-', linewidth=1.25 ,label=leg)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
