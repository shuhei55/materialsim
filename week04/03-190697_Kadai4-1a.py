import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3 + x

xmax = 1.0
xmin = 0.0
lstep = []
sekibun = []

for m in range(1,20):
    step = 100*m
    h = (xmax-xmin)/step
    
    result = (h/3.0) * func(xmin)
    for n in range(1,step):
        xi = xmin + h * float(n)
        if(n % 2 == 0):
            result += (h/3.0) * 2 * func(xi)
        else:
            result += (h/3.0) * 4 * func(xi)
    result += (h/3.0) * func(xmax)
    print(step,result,0.75-result)
    lstep.append(step)
    sekibun.append(result)
plt.ylim(0.7499,0.7501)
plt.yticks([0.7499,0.75])
plt.xlabel("#steps",fontsize=20)
plt.ylabel("Result",fontsize=20)
plt.tick_params(labelsize=18)
plt.plot(lstep,sekibun,"o")
plt.plot([0,2000],[0.75,0.75])
plt.show()
#plt.savefig("03-190697_Kadai4-1a.png")
