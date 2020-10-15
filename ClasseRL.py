# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:29:25 2020

@author: Baptiste
"""

import numpy as np

def gradient(a,b,x,y):
    Der_a = np.sum([x[i]*(a*x[i]+b -y[i]) for i in range(len(x))])
    Der_b = np.sum([(a*x[i]+b -y[i]) for i in range(len(x))])
    return Der_a,Der_b



class RegLinManual:
    def __init__(self):
        return
        
    def fit(self,x,y,Nite=100,tol=10**(-2),pas=10**(-8)):
        a=0.5
        b=-1000
        Fonction = np.sum([1/2*(a*x[i]+b -y[i])**2 for i in range(len(x))])
        for i in range(Nite): #Descente de gradient
            aold,bold=a,b
            grada,gradb=gradient(a,b,x,y)
            print(grada,gradb)
            a-=pas*grada
            b-=pas*gradb
            if np.linalg.norm([a-aold,b-bold])<tol:
                print("Seuil de tolérance atteint en "+str(i)+" itérations")
                break
        return a,b
        

        