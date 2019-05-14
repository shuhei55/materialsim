import numpy as np
import matplotlib.pyplot as plt

f = np.array([5.0,-1.0,4.0,1.0])
x0 = np.array([0.0,1.0,2.0,3.0])
A = np.array([[1,1,1,1],
    x0,
    x0**2,
    x0**3]).T
a = np.dot(np.linalg.inv(A),f)
x = np.arange(-1, 4,0.01)
y = a[3] * x**3 + a[2] * x**2 + a[1] * x + a[0]
plt.plot(x,y)
plt.plot(x0,f,marker='.',markersize=10,linestyle='None')

plt.show()
#plt.savefig("03-190697_Kadai3-2.png")
