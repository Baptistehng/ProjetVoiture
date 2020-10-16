# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:24:33 2020

@author: Baptiste
"""

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd




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
    dcc.Link('Différence liée à la transmission |', href='/apps/transmission'),
    dcc.Link(' Estimateur de prix', href='/apps/estimateur')
    
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
    dcc.Link(' Différence années |', href='/apps/year'),
    dcc.Link(' Estimateur de prix', href='/apps/estimateur')
])


layout5= html.Div([
    html.H1("Estimateur de prix"),
    html.H3("Choix de l'année"),
    dcc.Slider(
        id='annee',
        min=2008,
        max=2018,
        value=2014,
        marks={str(year): str(year) for year in range(2008,2019)},
        step=None
    ),
    html.H3("Nombre de kilomètres parcourus"),
    dcc.Input(
        id='kmdriven',
        type='number',
        value=100
    ),
    html.H3("Choix de la tranmission"),
    dcc.RadioItems(
        id='transmi',
        options=[
            {'label': 'Manuel', 'value': 0},
            {'label': 'Automatique', 'value':1}
        ],
        value=0
    ),
    html.P("\n"),
    html.P("\n"),
    html.P(id="prix"),
    
    dcc.Link(' Différence années |', href='/apps/year'),
    dcc.Link(' Différence liée à la transmission |', href='/apps/transmission')
    
])




