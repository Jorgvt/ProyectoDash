import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3("Overview"),
    html.Div(id='shape'),
    html.Div(id='ranges'),
    html.Div(id='nans'),
])

@callback(
    Output('shape', 'children'),
    Input('dataframe', 'data')
)
def show_shape(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        return html.Div([
            html.Div('El dataframe cargado tiene {} filas y {} columnas.'.format(*df.shape)),
        ])

@callback(
    Output('ranges', 'children'),
    Input('dataframe', 'data')
)
def show_ranges(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict).melt()
        fig = px.box(df, x='variable', y='value')
        fig.update_layout(
            xaxis_title='Variable',
            yaxis_title=''
        )
        fig.update_xaxes(tickangle=45)
        return html.Div([
            html.H4('Distribuciones'),
            dcc.Graph(figure=fig, id='box')
        ])

@callback(
    Output('nans', 'children'),
    Input('dataframe', 'data')
)
def plot_nans(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        fig = px.bar(data_frame=df.isna().sum(),
                     title='NaNs por variable')
        fig.update_layout(
            xaxis_title='Variable',
            yaxis_title='Cantidad de NaNs',
            showlegend=False,
        )
        fig.update_xaxes(tickangle=45)
        return html.Div([
            html.H4('Datos faltantes'),
            dcc.Graph(figure=fig, id='fig_nan')
        ])