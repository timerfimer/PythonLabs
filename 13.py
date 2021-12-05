from math import *
from scipy import integrate
import numpy as np
from math import *
from pylab import *


print('1.Ractangle method') 
def calculate_dx (a, b, n):
  return (b-a)/float(n)

def rect_rule (f, a, b, n):
  er = 0.0001
  dx = calculate_dx(a, b, n)
  for k in range (0, n):
          er = er + f((a + (k*dx)))
  return dx*er

def f1(x):
    return 1/sqrt(0.5*x + 1.5)
def f2(x):
    return log1p((x*x + 3))/2*x
def f3(x):
    return 1 / sqrt(0.6 + x*x)

print('Answer:',rect_rule(f1, 1.2, 2.0, 1000))
v,err = integrate.quad(f1, 1.2, 2.0)
print('Check:', v)

print("\n2.Simpson's method")

def simps(f, a, b, n):
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3
    
print('Answer:', simps(f2, 1.2, 2.0, 8))
v,err = integrate.quad(f2, 1.2, 2.0)
print('Check:', v)

print("\n3.Trapezoidal method")

def trapezoidal(f, a, b, n):
    deltax = float(b - a)/(n)
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h
    
print('Answer:', trapezoidal(f3, 1.2, 2.6, 20))
v,err = integrate.quad(f3, 1.2, 2.6)
