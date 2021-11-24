import math 
x0 = 0. 
y0 = -0.8 
 
def f1(y): 
    return  math.cos(y+1)/2 
def f2(x): 
    return -0.4-math.sin(x) 
 
def iteration(x, y, e): 
    xn = x 
    yn = y 
    xn1 = f2(x) 
    yn1 = f1(y) 
    n = 1 
    while((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)): 
        xn = xn1 
        yn = yn1 
        xn1 = f2(yn) 
        yn1 = f1(xn1) 
        n = n + 1 
    print('Method of simple iteration:\n','x1 = ', xn, '   y1 = ', yn1, '  Number of iteration = ', n) 
iteration(x0, y0, 0.0001)
