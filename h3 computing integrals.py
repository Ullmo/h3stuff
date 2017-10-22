# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:48:42 2017

@author: aetum
"""
import math
import numpy as np
from random import *
from matplotlib import pyplot as plt

def estm(N):
    S=0
    for i in range (N):
        x=random()
        y=(1-math.exp(-1))*random()
        if y<1-math.exp(-x):
            S=S+1
    m=float(S)/N
    return m*(1-math.exp(-1))
    
def precestm(N):
    S2=0
    for i in range (N):
        x=random()**(1./2)
        y=random()*x
        if y<1-math.exp(-x):
            S2=S2+1
    m2=float(S2)/N
    return m2*1./2
    
def mv(n):
    d=0
    M=0
    d2=0
    M2=0
    for j in range (0,1000):
        d=d+(estm(n)-math.exp(-1))**2
        M=M+estm(n)
        d2=d2+(precestm(n)-math.exp(-1))**2
        M2=M2+precestm(n)
    return "mean:",M/1000, "variance:",d/1000,"precmean:",M2/1000, "precvariance:",d2/1000
    

n1=100
n2=1000
     

print mv(n1)
print mv(n2)
print math.exp(-1)

def plotter(n):
    k=[None]*n
    for i in range (n):
        x=random()**(1./2)
        y=random()*2*x
        if y<1-math.exp(-x):
            k[i]=[x,y]
    k=filter(None, k)
    k=np.transpose(k)
    return k

ex= plotter(6000)

plt.scatter(ex[0],ex[1])
plt.show()

print plotter(10)