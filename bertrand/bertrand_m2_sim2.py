#
# Bertrand's Paradox - Method 2
# This program simulates the random chord selection method 2, i.e. the random radial point
# method by using matplotlib animation tool - animation.FuncAnimation
#

import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import numpy as np 

NUM = 2000   # The total number of simulation steps 
R = 1       # The radius of the circle

# One fig with two subplots
fig, axs = plt.subplots(1, 2)
fig.suptitle("Bertrand's Paradox")

# Two subplots, one for midpoint distribution, one for chords distribution
axs[0].set_title("Midpoints distrbution")
axs[1].set_title("Chords distribution")

# Draw two circles in both subplots
circle = plt.Circle((0,0), R, fill=False)
axs[0].add_artist(circle)
axs[1].add_artist(plt.Circle((0,0), R, fill=False))

axs[0].set_xlim(-1.2, 1.2)
axs[0].set_ylim(-1.2, 1.2)
axs[1].set_xlim(-1.2, 1.2)
axs[1].set_ylim(-1.2, 1.2)

# fix the aspects of the subplots
axs[0].set_aspect('equal')
axs[1].set_aspect('equal')

# init the variables we'll use in the following steps
points = []     # to store the plots of chords enpoints
chords = []     # to store the plots of chords
midpoints = []  # to store the plots of the midpoints of chords
red_count = 0   # to store the number of red chords/midpoints
blue_count = 0  # to store the number of blue chords/midpoints

# define the update function
def update(num):
    global red_count, blue_count
    # randomly select a point (point_a) on the circle
    theta = np.random.uniform(0, 2*np.pi)
    point_a_x = np.cos(theta)
    point_a_y = np.sin(theta)

    # radomlu select a point (point_b) on the radius (which is ditermined by point_a)
    t = np.random.uniform(0, 1)
    point_b_x = point_a_x * t
    point_b_y = point_a_y * t

    # calculate the slope of the radius (who across the point_b)
    slope_radius = point_b_y / point_b_x

    # assume y = kx + c is the function of the chord line
    # then the slope k and the intercept c can be calculated as the following
    k = -1.0/slope_radius
    c = point_b_y - k*point_b_x

    # do some calculations for the coordinations of the chord endpoints
    A = 1 + k**2
    B = 2*k*c
    C = c**2 - R**2 

    # coordinations of the chord endpoints 
    x1 = (-B + np.sqrt(B**2 - A*4*C))/(2*A)
    x2 = (-B - np.sqrt(B**2 - A*4*C))/(2*A)
    y1 = k*x1 + c
    y2 = k*x2 + c

    # we put the coordinations into numpy arrays
    x = np.array([x1, x2])
    y = np.array([y1, y2])

    # calculate the lengtg of the chord
    chord_length = np.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)

    # and assign differnt color to the chords and midpoints
    color = 'red' if chord_length > R*np.sqrt(3) else 'blue'
    if color == 'red':
        red_count += 1
    else:
        blue_count += 1
    # append the plots 
    points.append(axs[1].plot(x, y, 'o', color=color, markersize=1))  # the chords endpoints
    midpoints.append(axs[0].plot(np.mean(x), np.mean(y), 'o', color=color, markersize=1))
    chords.append(axs[1].plot(x, y, color=color, linewidth=0.2))

    # we show some useful info. for the simulation
    axs[0].set_title(f"Midpoints (Red : Blue = {red_count} : {blue_count})", fontsize=10)
    axs[1].set_title(f"Chords (Red : Blue = {red_count} : {blue_count})", fontsize=10)
    fig.suptitle("Bertran's Paradox Method 2\n Estimated Probability = {:.2f} @ step {} of {}".format(red_count/(red_count+blue_count), num, NUM))
#show the animations
ani = animation.FuncAnimation(fig, update, frames=range(NUM), repeat=False)

plt.show()