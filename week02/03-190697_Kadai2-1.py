import matplotlib.pyplot as plt
x = []
y1 = []
y2 = []
h = 10000

def f(x):
    return x**4-2.65*x**2-0.66*x+0.4284

for i in range(-2*h ,2*h):
    x.append(i/h)
    y1.append(f(i/h))
    y2.append(0)
    
plt.plot(x,y1)
plt.plot(x,y2)
#plt.show()
plt.savefig('hoge.png')
