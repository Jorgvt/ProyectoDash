import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3("Análisis Univariante"),
    html.Div(id='dd-univ-div'),
    html.Div(id='univariate-graph')
])

@callback(
    Output('dd-univ-div', 'children'),
    Input('dataframe', 'data')
)
def display_dd(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        return html.Div([
            dcc.Dropdown(df.columns, id='dd-univ'),
            dcc.RadioItems(['Histogram', 'Boxplot'],
                           'Histogram',
                           id='univariate-kind',
                           inline=True)
        ])

@callback(
    Output('univariate-graph', 'children'),
    Input('dataframe', 'data'),
    Input('dd-univ', 'value'),
    Input('univariate-kind', 'value')
)
def showcase_df_cols(data_dict, x, kind):
    if x:
        df = pd.DataFrame.from_dict(data_dict)
        if kind == 'Boxplot':
            fig = px.box(data_frame=df, y=x)
        else:
            fig = px.histogram(data_frame=df, x=x)
        return dcc.Graph(id='histogram', figure=fig)