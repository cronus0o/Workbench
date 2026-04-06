import turtle as t
import random

def screenLeftClick(x, y) :
    global r, g, b
    t.pencolor((r, g, b))
    t.pendown()
    t.goto(x, y)

def screenRightClick(x, y) :
    t.penup()
    t.goto(x, y)

def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

pSize = 10
r, g, b = 0.0, 0.0, 0.0
t.title("거북이로 그림 그리기")
t.shape('turtle')
t.pensize(pSize)

t.onscreenclick(screenLeftClick, 1)
t.onscreenclick(screenMidClick, 2)
t.onscreenclick(screenRightClick, 3)

t.done()
