import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *

x = [0.8, 0.9, 1.2, 1.6, 2.1] 
y = [1.42, 2.34, 3.48, 1.77,2.66]
plt.scatter(x,y,label ='Значення в заданих точках', color='b')
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Интерполяция сплайнами")
spl = UnivariateSpline(x,y)
xs = linspace(-10, 10,1000)
plt.plot(x,y,"ro", xs, spl(xs), 'r', lw=2)
plt.legend()
plt.show()
