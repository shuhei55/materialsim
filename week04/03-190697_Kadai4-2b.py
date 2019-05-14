import matplotlib.pyplot as plt
import numpy as np

r = float(input())

list_x = []
list_y = []
list_vx = []
list_vy = []

x = 1
y = 0
vx = 0
vy = 1

h = 0.1

list_x.append(x)
list_y.append(y)
list_vx.append(vx)
list_vy.append(vy)

ddx = (lambda x : - (x / r**3))
ddy = (lambda y : - (y / r**3))

def runge(func,x,v):
    k1v = h * func(x) #v
    k1x = h * v #x
    k2v = h * func(x + k1x / 2)
    k2x = h * (v + k1v / 2)
    k3v = h * func(x + k2x / 2)
    k3x = h * (v + k2v / 2)
    k4v = h * func(x + k3x)
    k4x = h * (v + k3v)
    return [(1.0 / 6.0) * (k1x + 2 * k2x + 2 * k3x + k4x),(1.0 / 6.0) * (k1v + 2 * k2v + 2 * k3v + k4v)]
    
def eluer(func, x,v):
    return [h * v, h * func(x)]

for i in range(100):
    hoge = runge(ddx, x, vx)
    x += hoge[0]
    vx += hoge[1]
    hoge = runge(ddy, y, vy)
    y += hoge[0]
    vy += hoge[1]
    list_x.append(x)
    list_y.append(y)
    list_vx.append(vx)
    list_vy.append(vy)
    
plt.plot(list_x,list_y,"o")
plt.show()
#今はルンゲクッタになってるが、for文のrungeのところをeluerにしたらオイラー法で計算される
