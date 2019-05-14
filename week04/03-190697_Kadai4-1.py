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
    
    result = 0.0
    for n in range(step):
        xi = h * float(n)
        result += (h / 2) * (func(xi) + func(xi+h))
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
#plt.savefig("03-190697_Kadai4-1.png")
#よってstep=500程度がちょうどよい
