import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import math as m

#Error Function
def exp(t):
    a=np.exp((t^2))
    a=a^(-1)
    return a
def errf(x):
    a=integrate.quad(exp,0,x)[0]
    return (2*a)/((np.pi)^0.5)    

def taylor(n,x):
    a=np.arange(0,n+1,1)
    f=0
    for i in a:
        a_n1=((-1)^i)*x^(2*i+1)
        a_n2=(2*i+1)*m.factorial(i)
        an=a_n1/a_n2
        f=f+an
    return (2/(np.pi))*f    

x=np.arange(-2.5,2.5,0.01)
b=[]
c1=[]
c2=[]
c3=[]
for i in x:
    b.append(errf(i))
plt.subplot(411)
plt.plot(x,b,label="errof function")   
plt.xlabel("x")
plt.legend(loc="upper right") 

plt.subplot(412)
for i in x:
    c1.append(taylor(1,i))
plt.plot(x,c1,label="errof function's Talor expension n=1")   
plt.xlabel("x")
plt.legend(loc="upper right")    

plt.subplot(413)
for i in x:
    c2.append(taylor(8,i))
plt.plot(x,c2,label="errof function's Talor expension n=8")   
plt.xlabel("x")
plt.legend(loc="upper right") 

plt.subplot(413)
for i in x:
    c3.append(taylor(15,i))
plt.plot(x,c3,label="errof function's Talor expension n=8")   
plt.xlabel("x")
plt.legend(loc="upper right") 
plt.show()


