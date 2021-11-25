import matplotlib.pyplot as plt
import numpy as np
import math

def fun(x):
  return np.sin(2*x)+x
  
x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
y = np.array([fun(0.1), fun(0.15), fun(0.2), fun(0.3), fun(0.4), fun(0.5), fun(0.6), fun(0.7), fun(0.47), fun(0.5)])
x2= np.array([0.1**2, 0.15**2, 0.2**2, 0.3**2, 0.4**2, 0.5**2, 0.6**2, 0.7**2, 0.47**2, 0.5**2])
x1 = np.mean(x)
y1 = np.mean(y)
x2 = np.mean(x2)

n=len(x)
num=0
yx=0

for i in range(n):
  num+=x[i]*y[i]
  yx=num/n
  
a1 = (yx-x1*y1)/(x2-x1**2)
a0 = y1-(a1*x1)
print(y)
print('x=', x1, '\nx2=', x2, '\ny=', y1, '\nyx=', yx,'\na1=', a1, '\na0=', a0)

plt.plot(x, yx*x+a0, 'r-')
plt.scatter(x,y,label = 'sin(2x)+x')
plt.grid()
plt.title('minimum square method') 
plt.legend()
plt.show()
