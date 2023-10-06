import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set() # seaborn theme looks better

# Set the graph window position (set as needed, or comment out for default)
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(2250, 100, 640, 800) 

NUM = 1000 # number of samples
d = 2
l = d

# Generate the middle point of the needles.
point_x = np.random.uniform(-3, 3, NUM)
point_y = np.random.uniform(-3, 3, NUM)
angle = np.random.uniform(-np.pi/2, np.pi/2, NUM)

# NOTE: The coordinations and the angle must be uniformlu distributed.


# define a function to check if a given number is between two numbers
def is_in(n, start, end):
    if start < n < end or start > n > end :
        return True

# define a function to check if the needle is intersected with the line
def intersect(p_x, p_y, theta, l):
    x1 = p_x + (l/2)*np.cos(theta)
    y1 = p_y + (l/2)*np.sin(theta)

    x2 = p_x - (l/2)*np.cos(theta)
    y2 = p_y - (l/2)*np.sin(theta)

    # (x1, y1), and (x2, y2) are the coordinations of the needle endpoints

    if is_in(0, y1, y2) or is_in(-2, y1, y2) or is_in(2, y1, y2) or is_in(4, y1, y2) or is_in(-4, y1, y2):
        return True, (x1, y1), (x2, y2)
    else:
        return False, (x1, y1), (x2, y2)

fig = plt.figure(1, figsize=(6, 15))
fig.suptitle("Buffon's Needles Problem Simulation")
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot([-4, 4],[0,0], c='b')
ax1.plot([-4, 4],[2, 2], c='b')
ax1.plot([-4, 4],[4, 4], c='b')
ax1.plot([-4, 4],[-2, -2], c='b')
ax1.plot([-4, 4],[-4, -4], c='b')

ax2 = fig.add_subplot(2, 1, 2)
num_int = 0
ratio = np.zeros(NUM)
x = np.arange(NUM)
for i in range(1, NUM):
    intersected, (x1, y1), (x2, y2) = intersect(point_x[i], point_y[i], angle[i], l)
    if intersected == True:
        color = 'red'   # intersected needles will be ploted in red, otherwise in blue
        num_int = num_int + 1.0
        ratio[i] = num_int/i
    else:
        color = 'blue'
        ratio[i] = num_int/i

    # Animated ploting
    # display the simulation steps
    ax1.title.set_text("Monte Carlo Simulation times: {}".format(i))
    
    # Dropping needles
    ax1.plot([x1, x2], [y1, y2], c= color, linewidth=0.5, alpha=0.7)
    
    # the evolution of estimation of PI
    ax2.plot(x[:i], 2/ratio[:i], c= 'r', linewidth=0.1) 
    
    # display the value
    ax2.title.set_text("Estimation of PI = {}".format(2/ratio[i]))
    plt.pause(0.001)

plt.show()
