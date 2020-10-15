# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:33:30 2020

@author: Baptiste
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importation des données
car_data=pd.read_csv("carData.csv")

#%% Appropriation des données

print(np.shape(car_data))
#301 voitures et 9 colonnes

#Répartion années

plt.figure(1)
plt.hist(car_data["Year"])
plt.show()
#On constate qu'il ya énormemment de voiture de 2016

#
#%% 

#cardata=car_data.to_sql("CarData",sqlalchemy.engine.Engine)


#%%Regression linéaire

years = car_data["Year"]
price= car_data["Selling_Price"]


#numpy

fit = np.polyfit(years,price,1)
regnp = [fit[0]*year + fit[1] for year in years]
plt.figure(1)
plt.scatter(years,price)
plt.plot(years,regnp)
plt.show()

#Scipy
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(years,price)
regsp = [slope*year + intercept for year in years]
plt.figure(2)
plt.scatter(years,price)
plt.plot(years,regsp)
plt.show()

#sklearn 

from sklearn.linear_model import LinearRegression
yearssk = [[year] for year in years]

reg = LinearRegression().fit(yearssk,price)
regsk= reg.predict(yearssk)
plt.figure(3)
plt.scatter(years,price)
plt.plot(years,regsp,"r")
plt.show()


#%% Regression multiple
km = car_data["Kms_Driven"]
trans= np.array(car_data["Transmission"])
for i in range(len(trans)):
    if trans[i] == "Manual":
        trans[i]=0
    else:
        trans[i] =1
        
X = [[years[i],km[i],trans[i]] for i in range(len(years))]
regmultiple = LinearRegression().fit(X,price)
print(regmultiple.score(X,price))

# %% classe crée

from ClasseRL import RegLinManual
import numpy as np

regcree= RegLinManual()
a,b=regcree.fit(years,price)
priceman= [a*year + b for year in years]
plt.figure(4)
plt.scatter(years,price)
plt.plot(years,priceman,"y")
plt.show()

