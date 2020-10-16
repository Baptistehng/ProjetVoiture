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

#Stats

L= ["Kms_Driven","Selling_Price","Present_Price"]
L2=[car_data.Kms_Driven,car_data.Selling_Price,car_data.Present_Price]
for i in range(len(L)):
    datai=L2[i]
    print("Moyenne "+ L[i]+": "+ str(np.mean(datai)))
    print("Variance "+ L[i]+": "+str(np.var(datai)))
    print("Min "+ L[i]+": "+str(np.min(datai)))
    print("Max"+ L[i]+": "+str(np.max(datai)))
    plt.figure()
    plt.hist(datai)
    plt.title(L[i])
#%% Import SQL

con = sqlite3.connect("database.db")
cur = con.cursor()

year_a_reshape = np.array(cur.execute("SELECT Year FROM cardata").fetchall())
years=year_a_reshape.reshape(len(year_a_reshape))
price_a_reshape =np.array(cur.execute("SELECT Selling_Price FROM cardata").fetchall())
price=price_a_reshape.reshape(len(price_a_reshape))
km_a_reshape =np.array(cur.execute("SELECT Kms_Driven FROM cardata").fetchall())
km=km_a_reshape.reshape(len(km_a_reshape))
trans_a_reshape =np.array(cur.execute("SELECT Transmission FROM cardata").fetchall())
trans=trans_a_reshape.reshape(len(trans_a_reshape))


#%%Regression linéaire


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

#La régression linéaire avec plusieurs variables est beaucoup plus
#efficace que la régression avec deux variables.


# %% classe crée

from ClasseRL import RegLinManual
import numpy as np

R=RegLinManual()
R.fit(years,price)
priceman=R.predict(years)
plt.figure(4)
plt.scatter(years,price)
plt.plot(years,priceman,"y")
plt.show()



#%% Résolution par SVM

from sklearn import svm

regsvm=svm.SVR(kernel="rbf")
regsvm.fit(yearssk,price)
pricesvm=regsvm.predict(yearssk)
print(regsvm.score(yearssk,price))
plt.figure(5)
plt.scatter(years,price)
plt.plot(years,pricesvm,"r")
plt.show()

#On obtient un score moins élevé que pour la regression avec 2 variables


