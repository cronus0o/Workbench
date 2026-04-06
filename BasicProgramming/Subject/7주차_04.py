import turtle as t
import random

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

t.title('거북이 맘대로 다니기')
t.shape('turtle')
t.pensize(pSize)
t.setup(width = swidth + 30, height = sheight + 30)
t.screensize(swidth, sheight)

while 1 :
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    t.left(angle)
    t.forward(dist)
    curX = t.xcor()
    curY = t.ycor()

    if (-swidth/2 <= curX and curX <= swidth/2) and (-sheight/2 <= curY and curY <= sheight/2) :
        pass
    else :
        t.penup()
        t.goto(0, 0)
        t.pendown()
        exitCount += 1
        if exitCount >= 5 :
            break
t.done()
