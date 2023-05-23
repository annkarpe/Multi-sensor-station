from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

import arduino_python


app = Dash(__name__, suppress_callback_exceptions=True)


app.layout = html.Div([
    dcc.Interval(id='update_value', interval=1 * 5000, n_intervals=0),
    html.H1('Multi-sensor station'),
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Temperature/Humidity', value='tab1'),
        dcc.Tab(label='Pressure', value='tab2'),
        dcc.Tab(label='Sound', value='tab3'),
        dcc.Tab(label='Distance', value='tab4'),
        dcc.Tab(label='Light', value='tab5')
    ]),
    html.Div(id='tabs_content')
])


@app.callback(Output('tabs_content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            dcc.Graph(id='temp_hum')
        ])
    elif tab == 'tab2':
        return html.Div([
            dcc.Graph(id='pressure')
        ])
    elif tab == 'tab3':
        return html.Div([
            dcc.Graph(id='sound')
        ])
    elif tab == 'tab4':
        return html.Div([
            dcc.Graph(id='dist')              
        ])
    elif tab == 'tab5':
        return html.Div([
            dcc.Graph(id='light')              
        ])


@app.callback(Output('temp_hum', 'figure'),
              Input('update_value', 'n_intervals'))
def update_hum_temp(n_intervals):
    arduino_python.serial_to_csv()
    df = pd.read_csv('home_data.csv')
    fig = px.line(df, x='time', y=['temperature', 'humidity'])
    return fig


@app.callback(Output('pressure', 'figure'),
              Input('update_value', 'n_intervals'))
def update_pressure(n_intervals):
    arduino_python.serial_to_csv()
    df = pd.read_csv('home_data.csv')
    fig = px.line(df, x='time', y=['pressure'])
    return fig


@app.callback(Output('sound', 'figure'),
              Input('update_value', 'n_intervals'))
def update_sound(n_intervals):
    arduino_python.serial_to_csv()
    df = pd.read_csv('home_data.csv')
    fig = px.line(df, x='time', y=['sound'])
    return fig


@app.callback(Output('dist', 'figure'),
              Input('update_value', 'n_intervals'))
def update_dist(n_intervals):
    arduino_python.serial_to_csv()
    df = pd.read_csv('home_data.csv')
    fig = px.line(df, x='time', y=['distance'])
    return fig


@app.callback(Output('light', 'figure'),
              Input('update_value', 'n_intervals'))
def update_light(n_intervals):
    arduino_python.serial_to_csv()
    df = pd.read_csv('home_data.csv')
    fig = px.line(df, x='time', y=['light'])
    return fig


if __name__ == '__main__':
    f = open('home_data.csv', "w+")
    f.close()
    app.run_server(debug=True)