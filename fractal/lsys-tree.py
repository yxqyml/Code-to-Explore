#
# This python code generates a tree by using a method called L-System or Lindermayer system.
# I used 2D drawing tool - turtal to implement the drawing
#
import turtle
from random import randint 

# screen setup
WIDTH = 800
HEIGHT = 800

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, starty=0)
screen.screensize(canvheight=2*HEIGHT, canvwidth=2*WIDTH)
screen.bgcolor('black')
screen.title("Fractal Tree")
screen.delay(0)

# turtle setup
tt = turtle.Turtle()
tt.shape('turtle')
tt.pensize(3)
tt.speed(0)
tt.penup()
tt.setpos(WIDTH//6, -HEIGHT//4 - 25)
tt.pendown()

# l-system sertings
iterations = 13
axiom = 'XY'
chr1 = 'X'
rule = 'F[@[-X]+X]'
step = 85
stack = []
color = [0.34, 0.25, 0.0]
angle = lambda : randint(0, 40)
thickness = 20

# define a function to apply rule(s)
def applyyRule(axiom):
    return ''.join([rule if c == chr1 else c for c in axiom])

# create a l-system
def createLSystem(interations, axiom):
    for _ in range(iterations):
        axiom = applyyRule(axiom)
    return axiom

# call the createLSystem function to create a L system
axiom = createLSystem(iterations, axiom)

# draw the tree
tt.left(90) # this will draw the tree upwards, as the turtle's initial direction s right
tt.pensize(thickness)
for cmd in axiom:
    tt.color(color)

    match cmd:
        case 'F':
            tt.forward(step)
        case 'X':
            tt.forward(step)
        case '@':
            step -= 6
            color[1] += 0.04
            thickness -= 2
            thickness = max(1, thickness)    
            tt.pensize(thickness)
        case '+':
            tt.right(angle())
        case '-':
            tt.left(angle())
        case '[':
            dir, pos = tt.heading(), tt.pos()
            stack.append((dir, pos, thickness, step, color[1]))
        case ']':
            dir, pos, thickness, step, color[1] = stack.pop()
            tt.pensize(thickness)
            tt.setheading(dir)
            tt.penup()
            tt.goto(pos)
            tt.pendown()
screen.exitonclick()
