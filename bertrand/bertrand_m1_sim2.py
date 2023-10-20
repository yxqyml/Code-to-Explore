#
# Bertrand's Paradox - Method 1 
# The random enpoints method simulation (with matplotlib animations)
# This method uses animation.Function. There are several other ways
# to implement animations.
#

import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation 

NUM = 3000   # Number of the total simulation steps, change to a large number when the code is completed.

# First all, to create a graph with two suplots side by side
# the left subplot will be used to display the midpoint distribution
# while the left one will be used to display the distribution of chords.
fig, axs = plt.subplots(1, 2)
fig.suptitle("Bertrand's Paradox")
axs[0].set_title("Midpoints")
axs[1].set_title("Chords")

# Plot circles in both subplots
circle = plt.Circle((0,0), 1, fill=False)
axs[0].add_artist(circle)
axs[1].add_artist(plt.Circle((0,0), 1, fill=False))

axs[0].set_xlim(-1.2, 1.2)
axs[0].set_ylim(-1.2, 1.2)
axs[1].set_xlim(-1.2, 1.2)
axs[1].set_ylim(-1.2, 1.2)

# To fix the scale and display as a square
axs[0].set_aspect('equal')
axs[1].set_aspect('equal')

# We use some variable, and initialize them
points = []
chords = []
midpoints = []
red_count = 0
blue_count = 0

# Define the update function for animation
def update(num):
    global red_count, blue_count

    # Select two points on the circle randomly
    theta = np.random.uniform(0, 2*np.pi, 2)
    x = np.cos(theta)
    y = np.sin(theta)

    # Calculate the length of the chord
    chord_length = np.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
    color = 'red' if chord_length >= np.sqrt(3) else 'blue'

    if color == 'red':
        red_count += 1
    else:
        blue_count += 1

    # Append the chord's endpoints to the subplot on the right, i.e. axs[1]
    points.append(axs[1].plot(x, y, 'o', color=color, markersize=0.1))

    # Appennd the chord's midpoint to the subplot on the left, i.e. axs[0]
    midpoints.append(axs[0].plot(np.mean(x), np.mean(y), 'o', color=color, markersize=0.1))

    # Append the chord to the subplot on the right
    chords.append(axs[1].plot(x, y, color=color, linewidth=0.2))

    # We show some information through the titles of the subplots and the suptitle
    axs[0].set_title(f"Midpoints (Red : Blue = {red_count} : {blue_count})")
    axs[1].set_title(f"Chords (Red : Blue = {red_count} : {blue_count})")
    fig.suptitle("Bertrand's Paradox Method 1\n Estimated Probability = {:.2f} @ step {} of {}".format(red_count/(red_count+blue_count), num, NUM))

ani = animation.FuncAnimation(fig, update, frames=range(NUM), repeat=False)


plt.show()