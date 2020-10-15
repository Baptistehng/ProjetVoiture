#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output
from layouts3 import car_data
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go

from app import app


@app.callback(
    Output('graph-with-2radios', 'figure'),
    [Input('year--slider','value')])
def update_figure(year):
    df = car_data[car_data.Year==year]
    x=df.Kms_Driven
    Y= df.Selling_Price
    X= [[elt] for elt in x]
    
        
    Reg =  LinearRegression().fit(X,Y)
    ybis = Reg.predict(X)
    score= Reg.score(X,Y)
    
    trace1 = go.Scatter(
                    x = x,
                    y = Y,
                    mode = "markers",
                    name = "Prix de vente en "+ str(year) ,
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
    layout = dict(title =" Prix de vente et regression linéaire en fonction du kilométrage",
                  xaxis = dict(title = 'Kilomètres parcourus',ticklen = 5,zeroline= False))
                
    fig = dict(data = data, layout = layout)
    
    return fig

@app.callback(
    Output('graph-with-radio', 'figure'),
    [Input('radio','value'),
     Input('axcisse','value')])
def update_figure(typev,ax):
    df = car_data[car_data.Transmission==typev]
    if ax=='km':
        X=df.Kms_Driven
    else:
        X=df.Year
    if typev == "Manual":
        trans=" manuelle"
    else:
        trans=" automatique"
        
    Y= df.Selling_Price
    
    trace1 = go.Scatter(
                    x = X,
                    y = Y,
                    mode = "markers",
                    name = "Prix de vente" ,
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text = df.Car_Name)
    
    data = [trace1]
    layout = dict(title =" Prix de vente pour une"+trans,
                  xaxis = dict(title = '',ticklen = 5,zeroline= False))
                
    fig = dict(data = data, layout = layout)
    
    return fig


