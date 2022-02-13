import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3("Análisis Bivariante"),
    html.Div(id='dd-biv-div'),
    html.Div(id='bivariate-graph')
])

@callback(
    Output('dd-biv-div', 'children'),
    Input('dataframe', 'data')
)
def create_dropdowns(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        return html.Div([
            html.Div([
                html.Div('x', style={'textAlign':'center'}),
                dcc.Dropdown(df.columns,
                             id='dropdown-1-x')
            ], style={'width': '33%', 'display': 'inline-block'}
            ),
            html.Div([
                html.Div('y', style={'textAlign':'center'}),
                dcc.Dropdown(df.columns,
                        id='dropdown-2-y'),
            ], style={'width': '33%', 'display': 'inline-block'}
            ),
            html.Div([
                html.Div('color', style={'textAlign':'center'}),
                dcc.Dropdown(df.columns,
                        id='dropdown-3-color'), 
            ], style={'width': '33%', 'display': 'inline-block'}
            )
        ]) 

@callback(
    Output('bivariate-graph', 'children'),
    Input('dataframe', 'data'),
    Input('dropdown-1-x', 'value'),
    Input('dropdown-2-y', 'value'),
    Input('dropdown-3-color', 'value')
)
def make_bivariate_graph(data_dict, x, y, color):
    ## De esta forma solamente aparece el plot una vez hemos seleccionado
    ## dos columnas en los dropdows. Así nos evitamos algunos errores.
    if (x is not None) and (y is not None):
        df = pd.DataFrame.from_dict(data_dict)
        fig = px.scatter(data_frame=df, x=x, y=y, color=color)
        return dcc.Graph(figure=fig, id='a')