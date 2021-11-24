import numpy as np  
import matplotlib.pyplot as plt  
from scipy.interpolate import lagrange  
   
   
x=np.array([-3,-1,1,2],dtype=float)  
y=np.array([3, 3, -13, -12],dtype=float)  
def LAG(x,y,t):  
   b=0  
   for k in range(len(y)):  
       p1=1; p2=1  
       for i in range(len(x)):  
           if i==k:  
               p1=p1*1; p2=p2*1  
           else:  
               p1=p1*(t-x[i])  
               p2=p2*(x[k]-x[i])  
       b=b+y[k]*p1/p2  
   return b  
graphX=np.linspace(np.min(x),np.max(x),100)  
graphY=[LAG(x,y,i) for i in graphX]  
plt.plot(x,y,'bo',graphX,graphY)  
plt.show()  
plt.grid() 
plt.legend(['x^3+x^2-9x-6'], loc = 'upper right') 
plt.title('Langrange') 
   
   
poly = lagrange(x, y)  
 
plt.xlabel('x') 
plt.ylabel('y') 
 
print(poly)  
   
x1 = -4 
yp = 0  
n=3  
for i in range(n):  
   p = 1  
   for k in range(n):  
       if i != k:  
           p = p * (x1 - x[k])/(x[i] - x[k])  
   yp = yp + p * y[i]  
  
x2 = -2  
for i in range(n):  
   p = 1  
   for k in range(n):  
       if i != k:  
           p = p * (x2 - x[k])/(x[i] - x[k])  
   yp = yp + p * y[i]  
 
x3 = -1.5  
for i in range(n):  
   p = 1  
   for k in range(n):  
       if i != k:  
           p = p * (x3 - x[k])/(x[i] - x[k])  
   yp = yp + p * y[i]  
 
x4 = 0.5  
for i in range(n):  
   p = 1  
   for k in range(n):  
       if i != k:  
           p = p * (x4 - x[k])/(x[i] - x[k])  
   yp = yp + p * y[i]  
   
  f = lagrange(x, y) 
fgr = plt.figure(figsize = (10, 8)) 
plt.plot(x,y,'go',graphX,graphY)  
plt.grid() 
plt.legend(['(16x^3+33x^2-31x-6)/3'], loc = 'upper right') 
plt.title('Shvets') 
plt.xlabel('x(check)') 
plt.ylabel('y(check)')
