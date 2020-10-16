#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output
from layouts3 import car_data
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go
from app import app
import numpy as np

@app.callback(
    Output('graph-with-2radios', 'figure'),
    [Input('year--slider','value')])
def update_figure(year):
    df = car_data[car_data.Year==year]
    x=df.Kms_Driven
    Y= df.Selling_Price
    fig =regression(x,Y,"Prix de vente en "+ str(year),"Kilomètres parcourus","Prix de vente et regression linéaire en fonction du kilométrage",df)
    
    return fig

@app.callback(
    Output('graph-with-radio', 'figure'),
    [Input('radio','value'),
     Input('axcisse','value')])
def update_figure(typev,ax):
    df = car_data[car_data.Transmission==typev]
    if ax=='km':
        x=df.Kms_Driven
    else:
        x=df.Year
    if typev == "Manual":
        trans=" manuelle"
    else:
        trans=" automatique"
        
    Y= df.Selling_Price
    fig=regression(x,Y,"Prix de vente pour une "+trans,"","Regression linéaire pour une "+trans,df)
    
    
    return fig
    
    
@app.callback(
    Output('prix', 'children'),
    [Input('annee','value'),
     Input('kmdriven','value'),
     Input('transmi','value')])
def calcul_prix(year,km,transmi):
    if km not in range(0,150001):
        return "Le kilométrage doit être compris entre 0 et 150000km"
    kms = car_data["Kms_Driven"]
    trans= np.array(car_data["Transmission"])
    years= car_data["Year"]
    price=car_data["Selling_Price"]
    for i in range(len(trans)):
        if trans[i] == "Manual":
            trans[i]=0
        else:
            trans[i] =1
    X = [[years[i],kms[i],trans[i]] for i in range(len(years))]
    regmultiple = LinearRegression().fit(X,price)
    prix=regmultiple.predict([[year,km,transmi]])
    prix= float(prix)*1000
    return "La voiture est estimée à %.2f €"% prix


def regression(x,Y,name_axe,name_axe2,title2,df):
    X= [[elt] for elt in x]
    Reg =  LinearRegression().fit(X,Y)
    ybis = Reg.predict(X)
    score= Reg.score(X,Y)
    
    trace1 = go.Scatter(
                    x = x,
                    y = Y,
                    mode = "markers",
                    name = name_axe ,
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text = df.Car_Name)
    # Création de la trame 2
    trace2 = go.Scatter(
                        x = x,
                        y = ybis,
                        mode = "lines+markers",
                        name = "Regression linéaire | R^2="+str(score),
                        marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                        text = df.Car_Name)
    
    data = [trace1, trace2]
    layout = dict(title =title2,
                  xaxis = dict(title = name_axe2,ticklen = 5,zeroline= False))
                
    fig = dict(data = data, layout = layout)
    
    return fig
    



