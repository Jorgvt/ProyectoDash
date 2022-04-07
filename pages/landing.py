import dash
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html, callback

import pandas as pd
import plotly.express as px

layout = html.Div([
    html.H3('¡Bienvenide!'),
    html.Div('''
    Esta aplicación de Dash está diseñada para permitir la exploración preliminar de cualquier conjunto de datos.
    Carga tu conjunto de datos utilizando la utilidad de la parte superior y explora tus variables en las diferentes pestañas de la página.
    ''')
])