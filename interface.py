import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('GNSS data visualization'),
    html.Div([
        html.Button('Measurement Tab', id='measurement-tab'),
        html.Button('Map Tab', id='map-tab'),
        html.Button('Setting Tab', id='setting-tab')
    ]),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('measurement-tab', 'n_clicks'),
               Input('map-tab', 'n_clicks'),
               Input('setting-tab', 'n_clicks')])
def display_page(measurement_clicks, map_clicks, setting_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        tab_id = 'measurement-tab'
    else:
        tab_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if tab_id == 'measurement-tab':
        return html.Div([
            html.H2('Measurement Tab'),
            html.Div([
                html.Button('Start Datetime Selector', id='start-datetime-selector'),
                html.Button('Stop Datetime Selector', id='stop-datetime-selector'),
                html.Button('Selector of Data', id='data-selector')
            ], className='button-container'),
            html.Div(id='measurement-plot-area', className='plot-area')
        ], id='measurement-content', className='content')
    elif tab_id == 'map-tab':
        return html.Div([
            html.H2('Map Tab'),
            html.Div([
                html.Button('Start Datetime Selector', id='start-datetime-selector'),
                html.Button('Stop Datetime Selector', id='stop-datetime-selector')
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

if __name__ == '__main__':
    app.run_server(debug=True)
    