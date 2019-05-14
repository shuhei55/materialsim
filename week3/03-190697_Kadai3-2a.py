import numpy as np
import matplotlib.pyplot as plt

data = open('input.txt','r')

f = np.array([])
x0 = np.array([])
for l in data:
    f = np.append(f,float(l.split()[1]))
    x0 = np.append(x0,float(l.split()[0]))
#print(f)
A = np.array([])
A = np.append(A,np.ones(f.size))
for i in range(1,x0.size):
    A = np.append(A,x0**(i))
A = A.reshape(x0.size,x0.size).T
#print(A)

a = np.dot(np.linalg.inv(A),f)
x = np.arange(0.0, 1.5,0.01)
y = a[0]
for i in range(1,a.size):
    y += a[i] * x**i
plt.plot(x,y)
plt.plot(x0,f,marker='.',markersize=10,linestyle='None')
plt.ylim([-0.5,2])
plt.xlim([-0.,1.1])
plt.show()
#plt.savefig('03-190697_Kadai3-2a.png')
