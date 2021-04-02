import numpy as np
def integf(x):
    a=np.arange(0,x,0.001)
    f=0
    for i in a:
        f=f+(np.cos(i+0.001)+np.cos(i))*((0.0005))
        return f
print(integf(np.pi))