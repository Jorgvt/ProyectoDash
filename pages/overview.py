import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3("Overview"),
    html.Div(id='describe'),
])

# @callback(
#     Output('describe', 'children'),
#     Input('dataframe', 'data')
# )
# def display_dd(data_dict):
#     if data_dict:
#         df = pd.DataFrame.from_dict(data_dict)
#         return html.Div(df.describe(), id='paparrapa')

@callback(
    Output('describe', 'children'),
    Input('dataframe', 'data')
)
def show_describe(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict).describe()
        df['metric'] = df.index
        return html.Div([
            dash_table.DataTable(
                df.to_dict('records'),
                [{'name': i, 'id': i} for i in df.columns],
                page_size=10, # Cantidad de columnas que se muestran
                # virtualization=True,
                # fixed_rows={'headers':True},
                style_table={#'height':'330px', 
                            #  'overflowY': 'auto', # Scroll vertical
                            'overflowX': 'auto'} # Scroll horizontal
            ),
        ])