from matplotlib import pyplot as plt

x=0
xc=[]
yc=[]
for x in range(0,10):
    x=x+0.01
    xc.append(x)
    y=4*x+3
    yc.append(y)

plt.plot(xc,yc)
plt.show()