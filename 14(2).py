import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def f(x,y):
 return x+sin(y/sqrt(2))
x0=0.8
p=1.8
h=0.1
x=np.arange(x0,p+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=1.3
for i in range(n):
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2

print('xi=',x)
print('yi=',y)
plt.plot(x, y,'ro-')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('method of euler-koshi') 
plt.legend(['x+sin(y/sqrt(2))'])
plt.grid()
plt.show()
