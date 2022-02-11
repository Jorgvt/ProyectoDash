import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html

import pandas as pd

def parse_contents_to_df(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df.to_dict()

@app.callback(
    Output('dataframe', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents_to_df(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        
        return children[0]

@app.callback(
    Output('output-data-upload', 'children'),
    Input('dataframe', 'data')
)
def show_table(data_dict):
    df = pd.DataFrame.from_dict(data_dict)
    return html.Div([
        dash_table.DataTable(
            df.head().to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns],
            style_table={'overflowX': 'auto'} # Esto es lo que permite scroll horizontal
        ),
    ])

@app.callback(
    Output('column-dropdown', 'children'),
    Input('dataframe', 'data')
)
def show_column_dropdown(data_dict):
    if data_dict:
        df = pd.DataFrame.from_dict(data_dict)
        return dcc.Dropdown(df.columns)