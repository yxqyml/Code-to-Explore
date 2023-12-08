'''
This python code visualizes the Mandelbrot set by using Dash plotly
which enable us to zoom in and out interactively with the graph.
Due to the intensive computation, we use numba library to accelerate
the Python code through Just-In-Time compilation.
Please note that when you zoom in/out, you need to wait for a while
as it takes time for a desktop PC to complete the computation.
Anyway, it is worth to be patient, as you will see a really amazing
fractal when you zoom in again and again.
I'll add more interactive components which will let you change the 
colors for example.
Enjoy the fractal and the coding as well.
'''
from dash import Dash, dcc, html, callback, Input, Output 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash_daq as daq
import numpy as np
import plotly.graph_objects as go
from numba import jit

XMIN = -2.0
XMAX = 2.0
YMIN = -1.25
YMAX = 1.25
S_WIDTH = 1500  # deine the resolution of mandelbrot set (1500*1500)
S_HEIGHT = 1500
G_WIDTH = 1080   # define the size of graph
G_HEIGHT = 960

@jit
def mandelbrot(c, max_iteration, threshold=2):
    z = c
    for i in range(max_iteration):
        if(abs(z) > threshold):
            return i
        z = z**2 + c
    return 0 

@jit
def mandelbrot_set(x_min, x_max, y_min, y_max, max_iteration=300,
                  width=S_WIDTH, height=S_HEIGHT):
    r1 = np.linspace(x_min, x_max, S_WIDTH)
    r2 = np.linspace(y_min, y_max, S_HEIGHT)
    z = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            z[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iteration)    
    return r1, r2, z 
x, y, z = mandelbrot_set(XMIN, XMAX, YMIN, YMAX)
trace = go.Heatmap(x=x, y=y, z=z.T, colorscale='Blackbody')

data = [trace]
layout = go.Layout(
    width=G_WIDTH,
    height=G_HEIGHT,
    xaxis=dict(),
    yaxis=dict(scaleanchor='x')
)
fig = go.Figure(data=data, layout=layout)


load_figure_template('darkly')

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H1("Mandelbrot Set"),
            className='text-center text-primary, mt-4'
        )
    ]),

    dbc.Row([dcc.Graph(id='graph', figure=fig)]),
    dbc.Row([
        daq.Slider(
            id='iterations',
            min=0,
            max=500,
            handleLabel={'showCurrentValue': True, 'label':"VALUE"},
            step=50,
            value=500,
            size=G_WIDTH
        )
    ]),
    dbc.Row([
        dbc.Col(
            dcc.RadioItems(
                id='colorscale',
                options=[
                    'Blackbody',
                    'Bluered',
                    'Blues',
                    'Cividis',
                    'Earth',
                    'Electric',
                    'Green',
                    'Hot',
                    'RdBu',
                    'Viridis'
                ],
                value='Blackbody',
                inline=True
            ),className='mb-4'
        )
    ])
])

@callback(
    Output('graph', 'figure'),
    [
        Input('iterations', 'value'),
        Input('graph', 'relayoutData'),
        Input('colorscale', 'value')
    ],
prevent_inital_call=True
)
def zoom(iterations, relayoutData, colorscale):
    if relayoutData is None:
        x_min, x_max = XMIN, XMAX
        y_min, y_max = YMIN, YMAX
    else:
        x_min, x_max = relayoutData.get('xaxis.range[0]') or XMIN, relayoutData.get('xaxis.range[1]') or XMAX
        y_min, y_max = relayoutData.get('yaxis.range[0]') or YMIN, relayoutData.get('yaxis.range[1]') or YMAX
    x, y, z = mandelbrot_set(x_min, x_max, y_min, y_max, max_iteration=iterations)
    trace = go.Heatmap(x=x, y=y, z=z.T, colorscale=colorscale)
    data =[trace]

    layout = go.Layout(
        width=G_WIDTH,
        height=G_HEIGHT,
        xaxis=dict(),
        yaxis=dict(
            scaleanchor='x'
        )
    )
    fig = go.Figure(data=data, layout=layout)

    return fig


if __name__ == "__main__":
    app.run_server(port=8066)
