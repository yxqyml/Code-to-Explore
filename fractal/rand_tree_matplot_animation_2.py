#
# Winter is coming, let's draw a pretty fall tree.
# This time we use 'matplotlib' instead of 'turtle' 
#

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import random, cos, sin, array, pi

# Parameters for fractal tree
ITERATIONS = 14
TRUNK_COLOR = array([0.1, 0.1, 0.1])
LEAF_COLOR = array([1.0, 1.0, 0.2])
TRUNK_LEN = 200
TRUNK_RAD = 3.0
THETA = pi / 2
ANGLE = pi / 4.5
RANDOMNESS = 5.0
RATIO = 0.8

# Parameters for drawing
WIDTH = 800
HEIGHT = 800
START = 0, 0

def get_color(level):
    a = float(level) / ITERATIONS
    return a * TRUNK_COLOR + (1 - a) * LEAF_COLOR

def get_line_width(level):
    return max(1, TRUNK_RAD * level / ITERATIONS)

def fractal_tree(ax, level, start, t, r, theta, angle, randomness):
    if level == 0:
        return

    x0, y0 = start
    randt = random.random() * t
    x, y = x0 + randt * cos(theta), y0 + randt * sin(theta)

    color = get_color(level)
    ax.plot([x0, x], [y0, y], linewidth=get_line_width(level), color=color)

    theta1 = theta + random.random() * (randomness / level) * angle
    theta2 = theta - random.random() * (randomness / level) * angle

    # Draw trunk and leaves up to the current level
    fractal_tree(ax, level - 1, (x, y), t * r, r, theta1, angle, randomness)
    fractal_tree(ax, level - 1, (x, y), t * r, r, theta2, angle, randomness)

def update(frame):
    ax.cla()
    ax.set_aspect('equal')
    ax.set_axis_off()
    fractal_tree(ax, frame, START, TRUNK_LEN, RATIO, THETA, ANGLE, RANDOMNESS)
    ax.set_title(f"Drawing Progress: Level {frame} / {ITERATIONS}")

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6,6), dpi=100)
animation = FuncAnimation(fig, update, frames=range(ITERATIONS + 1), repeat=False)
plt.show()
