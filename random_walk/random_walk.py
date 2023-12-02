'''
A drunk man will find his way home, but a drunk bird may get lost forever. --- Kakutani
Today, I'm gonna demonstrate the random walk by using animation and Mote Carlo simulation. This simulation and animation will help to explain why it
is harder for a higher dimensional random walk to get back to its origin
than a lower dimensional one.
'''
from os import POSIX_SPAWN_OPEN
from pathlib import PosixPath
import random
import matplotlib.pyplot as plt     # We use matplotlib as the graphic tool
from matplotlib.animation import FuncAnimation  # and we need animations

# For a random walk, the basic movements are 'Foreward' and 'Backward'
# on the axises. So we define these two.
FORWARD = -1
BACKWARD = 1

# Then we define some constants that we can change them for different
# simulation runs.
DIM = 3 # dimension, it could be 1/2/3, but for the sake of visulization
        # it should not be larger than 3.
STEPS = 100      # the maximum steps for the simulation
ITERATIONS = 100 # times for the simulation runs

'''
Now we define the rand_walk function
'''
def random_walk(n, s):
    """
    n - dimension of the random walk
    s - the maximum number of steps for the simulation
    The output of this funciton are:
    return_status which is either True or False. The walker may return to 
    the origin or it may not be able to return to the origin within the
    maximum number of step in our simulation. The other ouput is 'trace'
    in which we store the whole walking positions.
    """
    position = [0 for _ in range(n)]  # init the current position
    trace = [[0 for _ in range(n)]]   # init the trace
    for _ in range(s):
        # update the position with a random movement. The chance for
        # FORWARD or BACKWARD are equal. for 2D, 3D cases, the movements
        # on x, y, z axises are also equal.
        position[random.randrange(n)] += random.choice((FORWARD, BACKWARD))
        trace.append(position.copy()) # add the currewnt position to trace
        if not any(position):  # return to the origin (e.g. [0,0] in 2D)
            return True, trace
    return False, trace

# Now we call the function 
returned, trace = random_walk(DIM, STEPS)
# To make the output information more readable
if returned:
    ret_status = "Returned in " + str(len(trace)-1) + " steps"
else:
    ret_status = "Not returned " + str(STEPS) + ' steps'

# Now we plot the trace in 3D graph for all 1/2/3-D random walks.
# Please note that for a 1D random walk, the x-axis display the step(time), 
# while the y-axis display the position of the walker
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mngr = plt.get_current_fig_manager()
mngr.set_window_title("Random Walk Simulation")
mngr.window.setGeometry(1200, 120, 600, 680)

# we need tree update functions for animations.
def update_1d(frame):
    ax.cla()
    x = [i for i in range(frame+1)]
    y = [0 for _ in range(frame+1)]
    z = [pos[0] for pos in trace[:frame+1]]
    ax.plot(x, y, z, marker='o', markersize=2, linewidth=1, c='red')
    ax.set_xlabel('X - Step')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z - Position')
    ax.set_title(f'Step {frame}')
    ax.view_init(elev=10, azim=frame)

def update_2d(frame):
    ax.cla()

    x = [pos[0] for pos in trace[:frame+1]]
    y = [pos[1] for pos in trace[:frame+1]]
    z = [0 for _ in range(frame+1)]
    ax.plot(x, y, z, marker='o', markersize=2, linewidth=1, c='red')
    ax.set_xlabel('X - Position X')
    ax.set_ylabel('Y - Position Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Step {frame}')
    ax.view_init(elev=10, azim=frame)

def update_3d(frame):
    ax.cla()
    x = [pos[0] for pos in trace[:frame+1]]
    y = [pos[1] for pos in trace[:frame+1]]
    z = [pos[2] for pos in trace[:frame+1]]
    ax.plot(x, y, z, marker='o', markersize=2, linewidth=1, c='red')
    ax.set_xlabel('X - x cordination')
    ax.set_ylabel('Y - y cordination')
    ax.set_zlabel('Z - z cordination')
    ax.set_title(f'Step {frame}')
    ax.view_init(elev=10, azim=frame)

# We put all the above update functions into a list
functions = [update_1d, update_2d, update_3d]

fig.suptitle(f'{DIM}-D random walk. {ret_status}')

ani = FuncAnimation(
        fig,
        functions[DIM-1],
        frames=len(trace),
        repeat=False
        )
plt.show()


# Let's try to find the probability for the random walk to return to the 
# origin. Here we define a function to calculate it by a random simulation.
def sim(n_dim, n_steps, n_repeats):
    returned = [random_walk(n_dim, n_steps)[0] for _ in range(n_repeats)]
    prob = sum(returned) / (1.*n_repeats)
    return prob

# Now we do a Monte Carlo simulation to calculate the probability for 
# the random walk to return home.
p1 = sum([sim(1, 1000, 1000) for _ in range(10)]) / 10.0
p2 = sum([sim(2, 1000, 1000) for _ in range(10)]) / 10.0
p3 = sum([sim(3, 1000, 1000) for _ in range(10)]) / 10.0

print('For 1-D random walk, the probability of return home is: ', p1)
print('For 2-D random walk, the probability of return home is: ', p2)
print('For 3-D random walk, the probability of return home is: ', p3)


