import random
import numpy as np
import matplotlib.pyplot as plt 

def f(x): 
    return x**2-np.cos(10*x)+1 # 에너지
z=np.linspace(-2,2,100)
mcs=10
def mc(b,x):
    for t in range(mcs):
        newx=x+0.1*random.randint(-10,10) # 가우시안 랜덤 variable
        DE=f(newx)-f(x)
        if DE<0:
            x=newx # 상태 바꾸기
        elif random.random()<np.exp(-b*DE):
            x=newx
    return x

x, Tmax=1.5, 10
traj=[x]
y = [f(x)]
co = [0]

for i in range(50):
    T=Tmax*np.exp(-i/10) # cooling  
    x=mc(1/T,x)
    
    traj=np.append(traj,x)
    y=np.append(y,f(x))
    co=np.append(co,i+1)

plt.plot(z,f(z))
plt.scatter(traj,y,c=co,cmap='Greys')
plt.plot(traj[-1],y[-1],'o')    
plt.show()