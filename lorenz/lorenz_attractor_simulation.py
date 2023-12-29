#
# The code to simulate lorenz attractor with two very close initial states.
#

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numba import jit

# two initial states
x1, y1, z1 = 8.0, 1.0, 1.0
x2, y2, z2 = 8.0, 1.0, 1.01

rho, sigma, beta = 28, 10, 8/3

t0 = 0
tf = 100
dt = 0.008
t = np.arange(t0, tf, dt)
n = len(t)

@jit
def lorenz(t, r):
    x, y, z = r

    return np.array([
        sigma*(y - x),      # dx/dt
        (rho - z)*x - y,    # dy/dt
        x*y - beta*z        # dz/dt
        ])
@jit
def runge_kutta(t, r, f, dt):
    k1 = dt*f(t, r)
    k2 = dt*f(t+dt/2, r+k1/2)
    k3 = dt*f(t+dt/2, r+k2/2)
    k4 = dt*f(t+dt, r+k3)

    return r + (k1 + 2*k2 + 2*k3 + k4)/6

r1 = [x1, y1, z1]
r2 = [x2, y2, z2]

evol1 = np.zeros((n,3))
evol1[0,0], evol1[0,1], evol1[0,2] = r1[0], r1[1], r1[2]

evol2 = np.zeros((n,3))
evol2[0,0], evol2[0,1], evol2[0,2] = r2[0], r2[1], r2[2]

for i in range(n-1):
    evol1[i+1] = runge_kutta(t[i], [evol1[i,0], evol1[i,1], evol1[i,2]], lorenz, dt)
    evol2[i+1] = runge_kutta(t[i], [evol2[i,0], evol2[i,1], evol2[i,2]], lorenz, dt)

fig = plt.figure("Lorenz Attrator", facecolor='k')
fig.canvas.manager.window.setGeometry(200, 100, 500, 600)
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

def update(frame):
    ax.clear()
    ax.view_init(-6, -50 + frame/2)
    ax.set(facecolor='k')

    ax.set_axis_off()
    ax.plot(evol1[:frame, 0], evol1[:frame, 1], evol1[:frame, 2], color='red', lw=1)
    ax.plot(evol1[frame, 0], evol1[frame, 1], evol1[frame, 2],'ro') 
    ax.plot(evol2[:frame, 0], evol2[:frame, 1], evol2[:frame, 2], color='blue', lw=1)
    ax.plot(evol2[frame, 0], evol2[frame, 1], evol2[frame, 2],'bo') 
ani = animation.FuncAnimation(fig, update, np.arange(15000), interval=2, repeat=False)

plt.show()

