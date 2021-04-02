
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

#  Trigonometric Function 
def f(t):
    return np.sin(t)

def g(t):
    return np.cos(t)

# Trigonometric Function ver.scipy.integrate

def integf2(x):
    return float(integrate.quad(f,0,x)[0])

def integg2(x):
    return float(integrate.quad(g,0,x)[0])    


a=np.arange(-7,7,0.1)
b=[]
c=[]
for i in a:
    b.append(integf2(i))

for i in a:
    c.append(integg2(i))


plt.plot(a,b,color="red",label='sin indefinite integral')
plt.plot(a,c,color="blue",label='cos indefinite integral')
plt.legend(loc="upper right")
plt.title("Trigonometric Function ver.scipy.integrate")
plt.xlabel("x")
plt.show( )