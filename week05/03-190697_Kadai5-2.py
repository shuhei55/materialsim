import math 
import matplotlib.pyplot as plt
from numpy import arange,linspace

def gaussian(width, var):
    prefactor=1.0/width/math.sqrt(2.0*math.pi)
    return prefactor*math.exp(-var*var/2.0/width/width)

def Ek(kx, ky, V, Es):
    return Es+2.0*V*(math.cos(kx))+2.0*V*(math.cos(ky))

sample=4000
Vss=-0.1
Ess=0
Esample=100
GaussianWidth=0.01
kmesh=[]
kx=linspace(-math.pi,math.pi,sample)
ky=linspace(-math.pi,math.pi,sample)

energy=[]
for i in kx:
    for j in ky:
        energy.append(Ek(i,j,Vss,Ess))

Eval=linspace(-1,1,Esample)
dos=[]
for i in Eval:
    value=0.0
    for j in energy:
        value=value+gaussian(GaussianWidth,j-i)/float(len(energy))
    dos.append(value)
    
plt.plot(Eval,dos)
plt.show()
