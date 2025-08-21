#this is a simple implementation of Euler's Method in python. Page 57 textbook

#import library to make the plots
import matplotlib.pyplot as plt
import numpy as np


#the function defining the differential equation y'=f(t,y)
def f(t,y):
    return -2*t*y*y
#initial conditions
t0=0
y0=1
#set step size 
Dt=0.5

#define lists to store points
y=[y0]
t=[t0]

#do Euler's method (5 times)
for i in range(5):
    y+=[y[i]+Dt*f(t[i],y[i])]
    t+=[t[i]+Dt]

#plot of the analytic solution
x=[float(l)/100 for l in range(0,250)]
fx=[1./(1+s*s) for s in x]
plt.plot(x,fx)

plt.plot(t,y)
plt.show()

