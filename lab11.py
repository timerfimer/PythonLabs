import matplotlib.pyplot as plt
from numpy import *
import math

#sin(2x)+x
def fun(x):
  f = (3*x-4*x**3)/3
  return f

x = linspace(-5, 5, 1000)
y = x+sin(2*x)
yx = fun(x)

plt.plot(x, y, label = 'sin(2x)+x' )
plt.plot(x, yx, label = '(3*x-4*x**3)/3' )
plt.legend()
plt.title('Taylor') 
plt.grid()
plt.show()
