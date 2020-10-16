# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:29:25 2020

@author: Baptiste
"""

import numpy as np


class RegLinManual:
    def __init__(self,alpha=0,beta=0):
        self.alpha=alpha
        self.beta= beta
        
        return
        
    def fit(self,X,Y):
        moyx=np.mean(X)
        moyy=np.mean(Y)

        alphanum=0
        alphaden=0
        for i in range(len(Y)):
            alphanum+=(X[i]-moyx)*(Y[i]-moyy)
            alphaden+= (X[i]-moyx)**2

        alpha= alphanum/alphaden
        beta=moyy-alpha*moyx
        self.alpha=alpha
        self.beta=beta
        return 
    
    def predict(self,X):
        return [self.alpha*x+self.beta for x in X]
    
    
        

        