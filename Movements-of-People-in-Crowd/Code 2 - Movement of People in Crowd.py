# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 18:59:59 2018

@author: Hunor
"""

import numpy as np
from matplotlib  import pyplot as plt
from random import randint
import os

os.chdir("C:\\Users\\Hunor\\Desktop\\Fakultet\\Modeling Seminar\\151")

q=150
x=[randint(0,q-1) for p in range(0,q)]
y=[randint(0,q-1) for p in range(0,q)]
plt.scatter(x,y)
plt.xlim(-1,q+1)
plt.ylim(-1,q+1)
plt.show()

def poz():
    n = np.zeros((q,q))
    for i in range(q):
        n[x[i],y[i]] = 1
    return n

a = q-1
b = round((q/2)-1)

t = np.zeros((q,q))
for i in range(q):
    for j in range(q):
        t[i,j] = np.sqrt((i - a)**2 + (j - b)**2)
        tmax = t.max()
        

s = np.zeros((q,q))
for i in range(q):
        for j in range(q):
            s[i,j] = tmax - t[i,j]
np.round(s,2)
        
def prob(x,y,s,n):
        kd = 10
        ks = 4
        n[a,b] = 0
        if x == 0:
            u = 0
            d = ((np.e)**(kd)) * (np.e)**(ks*s[x+1,y]) * (1 - n[x+1,y])
        elif x == a:
            d = 0
            u = ((np.e)**(kd)) * (np.e)**(ks*s[x-1,y]) * (1 - n[x-1,y])
        else:
            u = ((np.e)**(kd)) * (np.e)**(ks*s[x-1,y]) * (1 - n[x-1,y])
            d = ((np.e)**(kd)) * (np.e)**(ks*s[x+1,y]) * (1 - n[x+1,y])
        if y == 0:
            l = 0
            r = ((np.e)**(kd)) * (np.e)**(ks*s[x,y+1]) * (1 - n[x,y+1])
        elif y == a:
            r = 0
            l = ((np.e)**(kd)) * (np.e)**(ks*s[x,y-1]) * (1 - n[x,y-1])
        else:
            l = ((np.e)**(kd)) * (np.e)**(ks*s[x,y-1]) * (1 - n[x,y-1])
            r = ((np.e)**(kd)) * (np.e)**(ks*s[x,y+1]) * (1 - n[x,y+1])
            
        c = ((np.e)**(kd)) * (np.e)**(ks*s[x,y]) 
        N=u+d+l+r+c
        return u/N,d/N,l/N,r/N,c/N
    
def move(m):
    z = [randint(0,a) for p in range(q)]
    for i in z:
        if (x[i],y[i]) ==(a,b):
            continue
        n = poz()
        u,d,l,r,c=prob(x[i],y[i],s,n)
        k = np.random.uniform(0,1,1)
        
        if 0<k<=u:
            x[i]= x[i] - 1
        elif u<k<=u+d:
            x[i]= x[i] + 1
        elif u+d<k<=u+d+r:
            y[i] = y[i] + 1
        elif u+d+r<k<=u+d+r+l:
            y[i] = y[i] - 1
    plt.scatter(x,y)
    plt.xlim(-1,q+1)
    plt.ylim(-1,q+1)
    plt.savefig("slika"+str(m)+".png",dpi=100)
    plt.show()
    
    
    
def ite():
    m=0
    while x.count(a)!=q and y.count(b)!=q:
        m+=1
        move(m)
    