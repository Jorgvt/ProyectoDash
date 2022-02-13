import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3("Análisis Univariante"),
    html.Div(id='showcase')
])

@callback(
    Output('showcase', 'children'),
    Input('dataframe', 'data')
)
def showcase_df_cols(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        fig = px.histogram(data_frame=df, x='TALLAcm')
        return dcc.Graph(id='histogram', figure=fig)