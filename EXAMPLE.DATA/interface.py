#import necessary modules for creating Dash application.
import dash
import pandas as pd
import plotly.graph_objs as go

from datetime import datetime
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State


#read data from CSV
observation_data = pd.read_csv('/Users/amyo/Documents/research-training/basic-interface/EXAMPLE.DATA/observation.csv')
navigation_data = pd.read_csv('/Users/amyo/Documents/research-training/basic-interface/EXAMPLE.DATA/navigation.csv')
nmea_data = pd.read_csv('/Users/amyo/Documents/research-training/basic-interface/EXAMPLE.DATA/nmea.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('GNSS data visualization'),
    html.Div([
        html.Button('Measurement Tab', id='measurement-tab'),
        html.Button('Map Tab', id='map-tab'),
        html.Button('Setting Tab', id='setting-tab')
    ]),
    html.Div([
        html.Label('Select Data Type'),
        dcc.Dropdown(
            id='data-type-selector',
            options=[
                {'label': 'Longitude', 'value': 'longitude'},
                {'label': 'Latitude', 'value': 'latitude'},
                {'label': 'Altitude', 'value': 'altitude'}
            ],
            value='longitude'
        ),
    ], style={'display': 'inline-block', 'margin-right': '10px'}),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('measurement-tab', 'n_clicks'),
               Input('map-tab', 'n_clicks'),
               Input('setting-tab', 'n_clicks')],
              [State('data-type-selector', 'value'),
               State('start-date-picker', 'date'),
               State('start-hour-dropdown', 'value'),
               State('start-minute-dropdown', 'value'),
               State('start-second-dropdown', 'value'),
               State('stop-date-picker', 'date'),
               State('stop-hour-dropdown', 'value'),
               State('stop-minute-dropdown', 'value'),
               State('stop-second-dropdown', 'value')])
def display_page(measurement_clicks, map_clicks, setting_clicks, data_type, start_date, start_hour, start_minute, start_second, stop_date, stop_hour, stop_minute, stop_second):
    ctx = dash.callback_context
    if not ctx.triggered:
        tab_id = 'measurement-tab'
    else:
        tab_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if tab_id == 'measurement-tab':
        start_time = datetime.strptime(f'{start_date} {start_hour}:{start_minute}:{start_second}', '%Y-%m-%d %H:%M:%S')
        stop_time = datetime.strptime(f'{stop_date} {stop_hour}:{stop_minute}:{stop_second}', '%Y-%m-%d %H:%M:%S')

        # filter the data based on selected data type
        if data_type == 'longitude':
            data = nav_data[['time', 'longitude']]
        elif data_type == 'latitude':
            data = nav_data[['time', 'latitude']]
        elif data_type == 'altitude':
            data = nav_data[['time', 'altitude']]

        # filter the data based on start and stop times
        data = data[(data['time'] >= start_time) & (data['time'] <= stop_time)]

        # plot the data against time
        plot_data = [go.Scatter(x=data['time'], y=data[data_type])]
        plot_layout = go.Layout(title=f'{data_type.capitalize()} vs Time')
        plot_figure = go.Figure(data=plot_data, layout=plot_layout)
        plot_figure.update_xaxes(title_text='Time')
        plot_figure.update_yaxes(title_text=data_type.capitalize())


        return html.Div([
            html.H2('Measurement Tab'),
            html.Div([            
                html.Button('Start Datetime Selector', id='start-datetime-selector'),
                html.Div([
                    html.Label('Date'),
                    dcc.DatePickerSingle(
                        id='start-date-picker',
                        display_format='YYYY-MM-DD',
                        placeholder='Select a date'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Hour'),
                    dcc.Dropdown(
                        id='start-hour-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(24)],
                        placeholder='Select an hour'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Minute'),
                    dcc.Dropdown(
                        id='start-minute-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                        placeholder='Select a minute'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Second'),
                    dcc.Dropdown(
                        id='start-second-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                        placeholder='Select a second'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),




                html.Button('Stop Datetime Selector', id='stop-datetime-selector'),
                html.Div([
                    html.Label('Date'),
                    dcc.DatePickerSingle(
                        id='stop-date-picker',
                        display_format='YYYY-MM-DD',
                        placeholder='Select a date'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Hour'),
                    dcc.Dropdown(
                        id='stop-hour-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(24)],
                        placeholder='Select an hour'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Minute'),
                    dcc.Dropdown(
                        id='stop-minute-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                        placeholder='Select a minute'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),

                html.Div([
                    html.Label('Second'),
                    dcc.Dropdown(
                        id='stop-second-dropdown',
                        options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                        placeholder='Select a second'
                    ),
                ], style={'display': 'inline-block', 'margin-right': '10px'}),






                dcc.Dropdown(
                    id='data-selector',
                    options=[
                        {'label': 'Longitude', 'value': 'longitude'},
                        {'label': 'Latitude', 'value': 'latitude'},
                        {'label': 'Altitude', 'value': 'altitude'}
                    ],
                    value='longitude') 
                                       
            ], className='button-container'),
            html.Div(id='measurement-plot-area', className='plot-area')
        ], id='measurement-content', className='content')
    
    
    elif tab_id == 'map-tab':
        return html.Div([
            html.H2('Map Tab'),
            html.Div([            
                html.Button('Start Datetime Selector', id='start-datetime-selector'),
                dcc.DatePickerSingle(
                    id='start-date-picker',
                    display_format='YYYY-MM-DD',
                    placeholder='Select a date'
                ),
                dcc.Dropdown(
                    id='start-hour-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(24)],
                    placeholder='Select an hour'
                ),
                dcc.Dropdown(
                    id='start-minute-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                    placeholder='Select a minute'
                ),
                dcc.Dropdown(
                    id='start-second-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                    placeholder='Select a second'
                ),

                html.Button('Stop Datetime Selector', id='stop-datetime-selector'),
                dcc.DatePickerSingle(
                    id='stop-date-picker',
                    display_format='YYYY-MM-DD',
                    placeholder='Select a date'
                ),
                dcc.Dropdown(
                    id='stop-hour-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(24)],
                    placeholder='Select an hour'
                ),
                dcc.Dropdown(
                    id='stop-minute-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                    placeholder='Select a minute'
                ),
                dcc.Dropdown(
                    id='stop-second-dropdown',
                    options=[{'label': f'{i:02d}', 'value': f'{i:02d}'} for i in range(60)],
                    placeholder='Select a second'
                ),

                html.Button('Selector of Data', id='data-selector')
            ], className='button-container'),
            html.Div([
                html.Label('Longitude'),
                dcc.Input(id='longitude', type='number', value=0, step=0.000001),
                html.Br(),
                html.Br(),
                html.Label('Latitude'),
                dcc.Input(id='latitude', type='number', value=0, step=0.000001),
                html.Br(),
                html.Br()
            ], className='parameter-container'),
            html.Div(id='map-area', className='map-area')
        ], id='map-content', className='content')

    
    
    
    else:
        return html.Div([
            html.H2('Setting Tab'),
            html.Div([
                html.Label('Satellite count:'),
                dcc.Input(id='satellite-count', type='number', min=1, max=24, value=12),
                html.Br(),
                html.Br(),
                html.Label('Constellation'),
                dcc.Dropdown(id='constellation', options=[
                    {'label': 'GPS', 'value': 'gps'},
                    {'label': 'GLONASS', 'value': 'glonass'},
                    {'label': 'Galileo', 'value': 'galileo'},
                    {'label': 'Beidou', 'value': 'beidou'}
                ], value='gps'),
                html.Br(),
                html.Br()
            ], className='setting-container')
        ], id='setting-content', className='content')


#BUILD THE APP
if __name__ == '__main__':
    app.run_server(debug=True)
    
