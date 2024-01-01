#
# This python code visualizes the global monthly temperatures since
# year 1880 to 2023. We'll plot the data in a kind of sprial graph
# in 3D.
#

import pandas as pd
import plotly.graph_objects as go
import numpy as np
import calendar

# Load the data
# The data can be downloaded from the following URL:
# https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'
# I've rennamed it to 'global_temp.csv'
df = pd.read_csv('global_temp.csv', skiprows=1) # to remove the first raw

# Drop the unnecessay columns
col_drop = ['J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON']
df = df.drop(col_drop, axis=1)

# Clean the data.
# As of today (Ded 30, 2023), there is no latest update of the temperature
# of Dec 2023. We need to remove the *** 
def clean_data(value):
    try:
        return float(value)
    except ValueError:
        return None

df = df.applymap(clean_data)

MONTHS = list(calendar.month_abbr)[1:]

# Covert the month into radian, e.g. Jan -> 0, July-> 3.14
def month_to_radian(month):
    return MONTHS.index(month)*np.pi/6.0

# Function to norm a column
def norm_col(col):
    min_val = col.min()
    max_val = col.max()

    return (col-min_val) / (max_val - min_val)

# Normalize the value of the 'Year' column
df['Year'] = norm_col(df['Year'])

#Change to column 'Year; to index
df.set_index('Year', inplace=True)

# Calculate the 3D coordinations for the data points
xs, ys, zs = [], [], []
months = []

for month in df:
    for year, temp in zip(df.index, df[month]):
        r = temp
        theta = month_to_radian(month)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        z = year

        xs.append(x)
        ys.append(y)
        zs.append(z)
        months.append(theta)

coord = pd.DataFrame({'x': xs, 'y':ys, 'z':zs, 'months': months})
coord = coord.sort_values(by=['z','months'], ascending=True)

# Create 3D scatter plot with lines using Plotly
color_map='jet'
fig = go.Figure()

# Scatter plot
scatter_trace = go.Scatter3d(
    x=coord['x'],
    y=coord['y'],
    z=coord['z'],
    mode='markers',
    marker=dict(
        size=4,
        color=np.sqrt(coord['x']**2 + coord['y']**2),
        colorscale = color_map,
        colorbar=dict(title='Color Scale')
    ),
    name = "Scatter Plot"
)
# Line plot
line_trace= go.Scatter3d(
    x=coord['x'],
    y=coord['y'],
    z=coord['z'],
    mode='lines',
    line=dict(
        color=np.sqrt(coord['x']**2 + coord['y']**2),
        colorscale = color_map,
        width=2
    ),
    name = "Line Plot"
)
fig.add_trace(scatter_trace)
fig.add_trace(line_trace)


fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z= 1.5)))
fig.update_layout(showlegend=False)

fig.show()
