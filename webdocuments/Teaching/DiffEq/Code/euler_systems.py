import matplotlib.pyplot as plt
#Van der Pol equation
#define system
def f(x,y):
    return y
def g(x,y):
    return -x+(1-x*x)*y

#time step
Dt=0.1
#initial values
x0=1
y0=0.25
#store points in a list
x=[x0]
y=[y0]

#ten steps
for i in range(100):
    m=f(x[i],y[i])
    n=g(x[i],y[i])
    x+=[Dt*m+x[i]]
    y+=[Dt*n+y[i]]
#print x,y
plt.plot(x,y)
plt.show() 
