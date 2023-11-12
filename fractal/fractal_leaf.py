#
# The following python code generates a fractal fern,
#
import numpy as np 
import matplotlib.pyplot as plt 

# We use the settings introduced in Wikipedia 
# Plese refer to Wikipedia for the value of the transformation matrix
# https://en.wikipedia.org/wiki/Barnsley_fern
#

# Transformation matrix
A1 = np.array([[0.0, 0.0], [0.0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])

C1 = np.array([0.0, 0.0])
C2 = np.array([0.0, 1.6])
C3 = np.array([0.0, 1.6])
C4 = np.array([0.0, 0.44])

# we define four funtions to perform transformation

# f1 - generates stems
def f1(X):
    return np.dot(A1, X) + C1
# f2 - generates successively smaller leaflets
def f2(X):
    return np.dot(A2, X) + C2
# f3 - generates largest left-hand leaflets
def f3(X):
    return np.dot(A3, X) + C3
# f4 - generates largest right-hand leaflets
def f4(X):
    return np.dot(A4, X) + C4


# we put all the functions into a list, then
# we can select one of them to perform transformation
functions = [f1, f2, f3,f4]

# the probability to apply a function in the funciton list 
P = [0.01, 0.85, 0.07, 0.07]

# number of the points to draw 
NUM = 100000

# the starting points
A = np.array([0, 0])

# the list of the points generated 
x = []
y = []

# generate the points 
for _ in range(NUM):
    f = np.random.choice(functions, p=P)
    A = f(A)
    x.append(A[0])
    y.append(A[1])

# draw the fern
plt.style.use('dark_background')
plt.figure(figsize=(6,8))
plt.axis('off')
plt.scatter(x, y, s = 0.1, color='green')
plt.show()

