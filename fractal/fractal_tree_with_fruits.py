#
# This python code generates a fractal tree with beautiful autumn
# colors. You can also add some fruits on it. :-)
#

import turtle as tt 
from random import randint

# Window size for the drawing
W = 900
H = 900

# Sepcify the size of the window and the position of it.
# You need to adjust your startx and starty according to 
# your setup (I'm using multiple displays), or you can just
# leave it by default and then to see how to adjust accordingly.
screen = tt.Screen()
screen.setup(W, H, startx=5960, starty=80)

# Sepcify the size of the canvas
screen.screensize(canvheight=1.5*H, canvwidth=1.5*W)
screen.bgcolor('gray')
screen.title('Autumn Tree')
screen.delay(0)

# Some parameters for the fractal tree
THICKNESS = 20
ITERATIONS = 12
AXIOM = 'CCCCA'
ANGLE = 14
STEP = 8
RAND_MIN = 0
RAND_MAX = 10

# Define colors for the trunks, branches and leaves, and of
# course the fruits. I've already found the color codes for them
# from a color system. So here I just copy and paste them.
# I put them in a dict which will help me to make the code clean.
TRUNK_COLOR = "#350B02" # kind of brown
colors = {
        0: '#228B22', # ForestGreen
        1: '#9ACD32', # YellowGreen
        2: '#FFA500', # Orange
        3: '#D2691E', # Chocolate
        4: '#556B2F', # DarkOliveGreen
        5: '#B22222', # Firebrick red
        6: '#667900', # olive(drab) green
        7: '#FFD700', # Gold yellow
        8: '#BDB76B', # DarkKhaki yellow
        9: '#DC143C', # Crimson red
        10:'#3CB371'  # LimeGreen
}

# Rules to apply to the AXIOM of the L-system.
# For more info. about L-system, please refer to 
# Wikipedia.
rules = {
    "B": "CB",
    "A": "B[-CA]+CA"
}

# Define a function to apply to the rules to AXIOM.
# This is a very simple function that will produce a sequence
# for deawing the tree (logical it is the tree w/o color rending)
def apply_rules(axiom):
    sequence = axiom
    tmp = ""
    for _ in range(ITERATIONS):
        for symbol in sequence:
            if symbol in rules:
                tmp += rules[symbol]
            else:
                tmp += symbol
        sequence = tmp
        tmp = ""
    return sequence

# Now we define the function to draw the tree according to the 
# sequence produced by applying the rules to AXIOM.
def draw_tree(seq, thickness, angle, rand_min, rand_max, step):
    stack = []
    seq = seq
    thick = thickness
    angle = angle
    rand_max = rand_max
    rand_min = rand_min
    step = step

    for symbol in seq:
        match symbol:
            case "+":
                tt.right(angle - randint(-13, 13))
            case "-":
                tt.left(angle - randint(-13, 13))
            case "C":
                if randint(rand_min, rand_max) > 4:
                    tt.forward(step)
            case "B":
                if randint(rand_min, rand_max) > 6:
                    tt.forward(step)
            case "A":
                r = randint(rand_min, rand_max)
                stack.append(tt.pensize())
                if r == 5: # we add some red fruits here
                    if randint(0, 10) > 8: # I donn't want to much
                        tt.pensize(25)
                else:
                    tt.pensize(5)
                tt.pencolor(colors[r])
                tt.forward(step)
                tt.pensize(stack.pop())
                tt.pencolor(TRUNK_COLOR)
            case "[":
                thick = thick*0.75
                tt.pensize(thick)
                stack.append(thick)
                stack.append(tt.xcor())
                stack.append(tt.ycor())
                stack.append(tt.heading())
            case "]":
                tt.penup()
                tt.setheading(stack.pop())
                tt.sety(stack.pop())
                tt.setx(stack.pop())
                thick = stack.pop()
                tt.pensize(thick)
                tt.pendown()
# Apply the rule to AXIOM
seq = apply_rules(AXIOM)

# tt.tracer(0)

tt.pencolor(TRUNK_COLOR)
tt.penup()
tt.setposition(0, -100)
tt.pensize(THICKNESS)
tt.pendown()
tt.setheading(-270)
tt.bk(200)
tt.forward(200)
tt.setposition(0, -200)

# Draw the tree according to the sequence and parameters
draw_tree(seq, THICKNESS, ANGLE, RAND_MIN, RAND_MAX, STEP)

screen.exitonclick()