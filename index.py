#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import server


from app import app
from layouts3 import layout3,layout4

import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/year':
        return layout3
    elif pathname == '/apps/transmission':
        return layout4
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

