# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:24:33 2020

@author: Baptiste
"""

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


car_data = pd.read_csv("carData.csv")



layout3= html.Div([
    html.H1("Prix par kilométrage en fonction de l'année"),
    dcc.Graph(id='graph-with-2radios'),
    
    dcc.Slider(
        id='year--slider',
        min=2003,
        max=2018,
        value=2014,
        marks={str(year): str(year) for year in car_data['Year'].unique()},
        step=None
    ),
    html.Div(id='idyear'),
    dcc.Link('Différence liée à la transmission |', href='/apps/transmission'),
    
])



layout4= html.Div([
    html.H1("Différence automatique/manuel"),
    dcc.Graph(id='graph-with-radio'),
    
    html.H3("Choix de la tranmission"),
    dcc.RadioItems(
        id='radio',
        options=[
            {'label': 'Manuel', 'value': 'Manual'},
            {'label': 'Automatique', 'value':'Automatic'}
        ],
        value='Manual'
    ),
    html.H3("Choix de l'axe'"),
    dcc.RadioItems(
        id='axcisse',
        options=[
            {'label': 'Année', 'value': 'year'},
            {'label': 'Kms', 'value':'km'}
        ],
        value='year'
    ),
    html.Div(id='idtrans'),
    dcc.Link(' Différence années |', href='/apps/year'),
])





