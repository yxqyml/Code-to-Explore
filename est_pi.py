# Estimation of Pi 
# To draw a circle of radius 0.5, enclosed by a 1x1 sqaure on the 2D plane. If the area 
# of the circle (pi*0.5^2 = pi/4) is divided by that of the square (1), we get pi/4.
#
# With this idea in mind, we then generate a large number of uniformaly distributed random 
# points within the sqaure. The random points can be in any position within the square.
# If the point falls within the circle, it is colored in blue, otherwise in blue. We keep
# trackof the total number of points and the number of points that are inside the circle.
# then the approximation of pi can be calculated by the following
#  
# pi= 4*(no. of points inside the circle) / (no. of points inside the square)
#
import numpy as np 
import plotly.graph_objects as go 
from numpy import random, pi, sin, cos      # to avoid using np.pi, np.sin and np.cos

NUM = 1000   # Number of random samplings
x = random.uniform(-1, 1, NUM) # NUM points of random numbers uniformly distributed between (-1,1)
y = random.uniform(-1, 1, NUM) # NUM points of random numbers uniformly distributed between (-1,1)

# color map: the points will be ploted in 'red' if it is within the unit circle, otherwise in blue.
colors = np.where(x**2 + y**2 > 1,'red', 'blue')

# Calculate the ratio of the number of red points to that of the blue points
ratio = np.zeros(NUM)  # ratio is an numpy array contains ratios for each time a random point is sampled
for i in range(1, NUM):
    ratio[i] = np.count_nonzero(colors[:i] == 'blue') / i

# Generate the coordinations for a circle (radius=0.5) and a square (edge=1) arounding the circle
beta = np.linspace(0, 2*pi, 1000)
c_x, c_y = cos(beta), sin(beta)
s_x = [-1, -1, 1, 1, -1]
s_y = [-1, 1, 1, -1, -1]

# Drwawing
# two subplots side by side with a space of 0.05
fig = go.Figure().set_subplots(rows=1, cols=2, horizontal_spacing=0.05, subplot_titles=('Simulation of dropping points', 'Estimation of pi'))
# set the poistions and fonts size for subplots' title
fig.layout.annotations[0].update(x=0.15, font_size=12)
fig.layout.annotations[1].update(x=0.65, font_size=12)

# Add the square to the left subplot
fig.add_trace(go.Scatter(x=s_x, y=s_y, mode='lines', marker=dict(color='green')), row=1, col=1)
fig.add_trace(go.Scatter(x=c_x, y=c_y, mode='lines', marker=dict(color='red')), row=1, col=1)
fig.add_trace(go.Scatter(x=[], y=[], mode='markers', marker=dict(color=colors)),row=1, col=1)
fig.add_trace(go.Scatter(x=[0], y=[0], mode='lines'), row=1, col=2)

fig.update_layout(width=800, height=450,
                  xaxis=dict(range=[-1.1,1.1], autorange=False, zeroline=False),
                  yaxis=dict(range=[-1.1,1.1], autorange=False, zeroline=False),
                  )
fig['layout']['xaxis1'].update(domain=[0, 0.35])
fig['layout']['xaxis2'].update(domain=[0.4, 1])


frame_ind = np.arange(1, NUM)
frames = [
    go.Frame(
        data=[
            go.Scatter(visible=True),
            go.Scatter(visible=True),
            go.Scatter(x=x[:k+1], y=y[:k+1], mode='markers', marker=dict(color=colors, size=3)),
            go.Scatter(x=frame_ind[:k+1], y=4*ratio[:k+1], mode='lines')
        ],
        layout=go.Layout(title_text='Simulation Times:{}, Est-pi={:.2f}'.format(k, ratio[k]*4)),
        name=f'fr{k}',
        traces=[0,1,2,3]
    ) for k in range(NUM)]
fig.update(frames=frames)

# Animation preparation
def frame_args(duration):
    return {
        'frame': {'duration': duration},
        'mode': 'immediate',
        'fromcurrent': True,
        'transaction': {'duration': duration, 'easing': 'linear'}
    }

fr_duration = 50
sliders = [
    {
        'pad': {'b':10, 't':50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'steps': [
            {
                'args': [[f.name], frame_args(fr_duration)],
                'label': f'fr{k+1}',
                'method': 'animate'
            } for k, f in enumerate(fig.frames)
        ]
    }
]

# Show the animation
fig.update_layout(showlegend=False, sliders=sliders,
                  updatemenus=[
                      {
                              'buttons': [
                                    {
                                      'args': [None, frame_args(fr_duration)],
                                      'label': '&#9654;', # Play button
                                      'method': 'animate'
                                    },
                                    {
                                      'args': [None, frame_args(fr_duration)],
                                      'label': '&#9724;', # Pause button
                                      'method': 'animate'
                                    },
                              ],
                            'direction': 'left',
                            'pad': {'r':10, 't':70},
                            'type': 'buttons',
                            'x':0.1,
                            'y':0
                      }
                      ]
                  )
