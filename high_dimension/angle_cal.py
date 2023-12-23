#
# This program is about to calculate the angle between any two vectors on
# the high-dimensional spherical surface by using random simulation.
#

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

NUM = 500       # number of the simulation runs
N = 10000       # the dimension

# define a unction to generate random vectors in N-dimensioanl space
# then we normalized it.
def random_vector(N):
    # generate a random vector in N-D space.
    vec = np.random.randn(N)

    # normalize it
    vec /= np.linalg.norm(vec)

    return vec

# define a function to calculate the angle between two vectors.
# the two vectors must be in the same N-D space, otherwise an ERROR will be returned
def angle(a, b):
    if len(a) != len(b):
        print("ERROR: the two vectors in considerations have different dimensions")
        exit()
    dot_prod = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    return np.arccos(dot_prod/(norm_a*norm_b))

# let's test it
#a = random_vector(N)
#b = random_vector(N)
#print(angle(a,b)*180/np.pi)

# Now, I'm b=gonna plot the calculated values for all the simulation runs
# and the averaged value which is expectec to be very close to 90 degrees.

fig, ax = plt.subplots()
fig.canvas.manager.window.setGeometry(800, 620, 840, 400)
y = []      # stores the caculated values for nagles
av = 0.0

for i in range(NUM):
    x = range(i+1)
    v1 = random_vector(N)
    v2 = random_vector(N)
    a = angle(v1, v2)*180/np.pi
    y.append(a)
    av = np.sum(y)/len(y)
    ax.title.set_text("Averahed angle between 2 vectors: {:.2f}".format(av))
    ax.title.set_fontsize(18)
    ax.plot(x, y, linewidth=0.5, c='red')
    plt.pause(0.01)

plt.show()





