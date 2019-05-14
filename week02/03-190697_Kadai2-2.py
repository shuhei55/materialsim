#! /home/shuhei/anaconda3/bin/python3
import matplotlib.pyplot as plt

class Solve:
    def __init__(self,x,y,z):
        self.dt = 0.001
        self.p = 10.0
        self.r = 28.0
        self.b = 8/3
        self.step = 0
        self.x = x
        self.y = y
        self.z = z
        
    def dx(self):
        return - self.p * self.x + self.p * self.y
    
    def dy(self):
        return - self.x * self.z + self.r * self.x - self.y
    
    def dz(self):
        return self.x * self.y - self.b * self.z
    
    def TimeUpdate(self):
        self.x += self.dx() * self.dt
        self.y += self.dy() * self.dt
        self.z += self.dz() * self.dt
        self.step += 1
            
    def print_state(self):
        print(self.x,self.y,self.z)
    
        
test = Solve(1.0,10.0,10.0)
x = []
y = []
z = []

for i in range(1,100000):
    test.TimeUpdate()
    x.append(test.x)
    y.append(test.y)
    z.append(test.z)
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,z)
plt.subplot(2,2,3)
plt.plot(x,z)
#plt.show()
plt.savefig('03-190697_Kadai2-2_figure.png')
