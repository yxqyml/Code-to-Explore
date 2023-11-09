#
# Bertrand's Paradox - Method 3
# This program simulates the random chord selection method 3, i.e. the random midpoint
# method by using matplotlib animation tool - animation.FuncAnimation
# 
# I'd like to reuse the code for method2.

import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import numpy as np
import seaborn as sns
sns.set()


NUM = 2000   # The total number of simulation steps, before we complete debugging, we set this number to a small one 
R = 1       # The radius of the circle

# One fig with two subplots
fig, axs = plt.subplots(1, 2)
fig.suptitle("Bertrand's Paradox")

# Two subplots, one for midpoint distribution, one for chords distribution
axs[0].set_title("Midpoints distrbution")
axs[1].set_title("Chords distribution")

# Draw two circles in both subplots
circle = plt.Circle((0,0), R, fill=False, color='green')
axs[0].add_artist(circle)
axs[1].add_artist(plt.Circle((0,0), R, fill=False, color='green'))

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


# to define a function generating uniformly distributed points within the area of a circle with radius of R 
def rand_point_in_circle(R):
    while(True):
        x = np.random.uniform(-R, R)
        y = np.random.uniform(-R, R)
        if(np.sqrt(x*x + y*y)) <= R:
            return x, y

# Here is a way to find the chord acrossing the random point as its midpoint 
# First of all, we need to find the perpendicular line to the line taht connects the random point and the circle center
def perpendicular_points(x1, y1):
    k = -x1/y1
    c = y1 - k*x1
    x2 = 1 
    y2 = k*x2 + c 
    return np.array([x1, x2]), np.array([y1, y2])

# Again, it is a little bit complex to calculate the intersection points of a line and a circle.
# anyway you can find it in the textbook or juest search the Internet.

# to maike the code clean, we define a sign function 
def sign(x):
    if x < 0:
        return -1 
    else:
        return 1 

# Now define the function to calculate the coordinations for the two intersection points 
def intersection_points(x, y, R):
    r = R 
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    dr = np.sqrt(dx*dx + dy*dy)
    D = x[0]*y[1] - x[1]*y[0]
    
    x1 = (D*dy + sign(dy)*dx*np.sqrt(r*r*dr*dr - D*D))/(dr*dr)
    x2 = (D*dy - sign(dy)*dx*np.sqrt(r*r*dr*dr - D*D))/(dr*dr)

    y1 = (-D*dx + np.abs(dy)*np.sqrt(r*r*dr*dr - D*D))/(dr*dr)
    y2 = (-D*dx - np.abs(dy)*np.sqrt(r*r*dr*dr - D*D))/(dr*dr)

    return np.array([x1, x2]), np.array([y1, y2])



# define the update function
def update(num):
    global red_count, blue_count
    # randomly select a point (point_a)  within the area the circle

    x1, y1 = rand_point_in_circle(R)

    x, y = perpendicular_points(x1, y1)

    x, y = intersection_points(x, y, R)

    # calculate the lengtg of the chord
    chord_length = np.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)

    # and assign differnt color to the chords and midpoints
    color = 'red' if chord_length > R*np.sqrt(3) else 'blue'
    if color == 'red':
        red_count += 1
    else:
        blue_count += 1

    # append the plots 
    midpoints.append(axs[0].plot(x1, y1,'o', color=color, markersize=0.2))

    chords.append(axs[1].plot(x, y, color=color, linewidth=0.2))

    # we show some useful info. for the simulation
    axs[0].set_title(f"Midpoints (Red : Blue = {red_count} : {blue_count})", fontsize=10)
    axs[1].set_title(f"Chords (Red : Blue = {red_count} : {blue_count})", fontsize=10)
    fig.suptitle("Bertran's Paradox Method 3\n Estimated Probability = {:.2f} @ step {} of {}".format(red_count/(red_count+blue_count), num, NUM))
#show the animations
ani = animation.FuncAnimation(fig, update, frames=range(NUM), repeat=False)

plt.show()
