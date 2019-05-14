import matplotlib.pyplot as plt
import numpy as np

list_x = []
list_y = []

a = 0.03
b = 0.0002
c = 0.0002
d = 0.07

xi = 1000
yi = 100
h = 1

def dtdx(x,y):
    return a * x - b * x * y

def dtdy(x,y):
    return c * x * y - d * y

list_x.append(xi)
list_y.append(yi)
for t in range(0,1000,h):
    k1x = h * dtdx(xi, yi)
    k1y = h * dtdy(xi, yi)
    k2x = h * dtdx(xi + k1x / 2, yi + k1y / 2)
    k2y = h * dtdy(xi + k1x / 2, yi + k1y / 2)
    k3x = h * dtdx(xi + k2x / 2, yi + k2y / 2)
    k3y = h * dtdy(xi + k2x / 2, yi + k2y / 2)
    k4x = h * dtdx(xi + k3x, yi + k3y)    
    k4y = h * dtdy(xi + k3x, yi + k3y)
    xi += (1.0 / 6.0) * (k1x + 2 * k2x + 2 * k3x + k4x)
    yi += (1.0 / 6.0) * (k1y + 2 * k2y + 2 * k3y + k4y)
    list_x.append(xi)
    list_y.append(yi)
    
plt.plot(list_x, "o")
plt.plot(list_y, "o")
plt.show()
#plt.savefig("03-190697_Kadai4-2a.png")
