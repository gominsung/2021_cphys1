import numpy as np
import matplotlib.pyplot as plt
import math

#  Vibration in a one-dimensional system

k=1
m=1
c=1
b1=np.zeros((40,1))
b1[0][0]=c
b2=np.zeros((40,1))
b2[0][0]=c
b2[39][0]=c

def f(w):
    d=2*k-m*(w**2)
    a=np.zeros([40,40])
    b=range(40)
    for i in b:
        if i==0:
            a[i][i]=d-k
            a[i][i+1]=-k
        elif i==39:
            a[39][38]=-k
            a[39][39]=d-k
        else :
            a[i][i-1]=-k
            a[i][i]=d
            a[i][i+1]=-k
    return a
def homework1():
        y1=np.linalg.solve(f(1),b1)
        y2=np.linalg.solve(f(2),b1)
        y3=np.linalg.solve(f(3),b1)

        y11=[]
        y12=[]
        y13=[]
        for i in range(40):
            y11.append(y1[i][0])
            y12.append(y2[i][0])
            y13.append(y3[i][0])
        x=np.arange(0,40)
        plt.plot(x,y11,label="w=1")
        plt.plot(x,y12,label="w=2")
        plt.plot(x,y13,label="w=3")    
        plt.legend(loc="upper right")
        plt.xlabel("i")
        plt.ylabel("a_i")
        plt.title("Vibration of a one-dimensional system with force applied to one end")
        plt.xlim(0,40)
        plt.show()
    
def homework2():
        y1=np.linalg.solve(f(1),b2)
        y2=np.linalg.solve(f(2),b2)
        y3=np.linalg.solve(f(3),b2)

        y11=[]
        y12=[]
        y13=[]
        for i in range(40):
            y11.append(y1[i][0])
            y12.append(y2[i][0])
            y13.append(y3[i][0])
        x=np.arange(0,40)
        plt.plot(x,y11,label="w=1")
        plt.plot(x,y12,label="w=2")
        plt.plot(x,y13,label="w=3")    
        plt.legend(loc="upper right")
        plt.xlabel("i")
        plt.ylabel("a_i")
        plt.title("Vibration of a one-dimensional system with force applied to both ends")
        plt.xlim(0,40)
        plt.show()        
homework1()
homework2()
# 한쪽 끝에서만 힘을 가할경우 힘을 가하는 원천에서 멀어지면 멀어질수록 진폭이 감소한다.
# 양 끝에서 힘을 가할경우 중앙에서 진동이 상쇄되어 중앙의 진폭은 0이고 중앙에서 멀어질수록 상쇄되는 양이 줄어들어 진폭이 커진다.
