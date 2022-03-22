import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html

import pandas as pd
import plotly.express as px

from pages import overview, univariate, bivariate 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    dcc.Store(id='dataframe'),
    html.Div(id='output-data-upload'),
    html.Div([
        dcc.Link(html.Button('Clear'), href='/'),
        dcc.Link(html.Button('Overview'), href='/overview'),
        dcc.Link(html.Button('Análisis Univariante'), href='/univariate'),
        dcc.Link(html.Button('Análisis Bivariante'), href='/bivariate'),
    ]),
    html.Div(id='page-content')
])

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

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/univariate':
        return univariate.layout
    elif pathname == '/bivariate':
        return bivariate.layout
    elif pathname == '/overview':
        return overview.layout
    else:
        return html.Div("Nope.")

if __name__ == '__main__':
    app.run_server(debug=True)