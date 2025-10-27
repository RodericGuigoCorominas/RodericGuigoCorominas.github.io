#Problem 17, section 1.5
#Ermentrout-Kopell model for neuron spiking

import matplotlib.pyplot as plt
import math

#the model is given by
def f(t,theta):
    return 1-math.cos(theta)+(1+math.cos(theta)*(-0.1))

#initial conditions
t0=0
theta0=0.1
#set step size 
Dt=0.1

#define lists to store points
theta=[theta0]
t=[t0]

#do Euler's method (50 times)
for i in range(50):
    theta+=[theta[i]+Dt*f(t[i],theta[i])]
    t+=[t[i]+Dt]
    
plt.plot(t,theta)
plt.show()

