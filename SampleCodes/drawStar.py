# draw star : function
# with python turtle module

# import turtle module

# import math module
# calculate triangle ratio (sin, cos)

import turtle
import math

def drawStar(): # parameter can be : (x, y, radius, color)
    r = 200 # Circumradius
    x = r * math.sin(math.radians(36)) / math.cos(math.radians(36)) # Length

    # turtle.penup()
    turtle.color('#000000')
    turtle.goto(0, r)
    # turtle.pendown()

    turtle.setheading(252) # caution of the angle!
    turtle.begin_fill()
    for i in range(5) :
        turtle.forward(x)
        turtle.right(72)
        turtle.forward(x)
        turtle.left(144)
    turtle.end_fill()

drawStar()
turtle.done()