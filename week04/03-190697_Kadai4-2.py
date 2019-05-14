import matplotlib.pyplot as plt
import numpy as np

list_x = []
list_y = []

xi = 1
yi = 0
h = 0.01

def func(x):
    return (1.0 / 3.0) * x**2 + (1.0 / 2.0) * x - 5.0 / (6 * x)

def diff(x,y):
    return -(y / x) + x + 1

list_x.append(xi)
list_y.append(yi)
for i in range(200):
    k1 = h * diff(xi, yi)
    k2 = h * diff(xi + h / 2, yi + k1 / 2)
    k3 = h * diff(xi + h / 2, yi + k2 / 2)
    k4 = h * diff(xi + h, yi + k3)
    xi += h
    yi += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    list_x.append(xi)
    list_y.append(yi)
    
plt.plot(list_x, list_y, "o")
x = np.linspace(1,3,100)
plt.plot(x,func(x))
plt.show()
#plt.savefig("03-190697_Kadai4-2.png")
