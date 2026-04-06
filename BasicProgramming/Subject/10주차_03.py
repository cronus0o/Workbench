import turtle as t
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []
playerTurtles = []
swidth, sheight = 500, 500
num = int(input("거북이 개수 : "))
t.speed(0)

if __name__ == "__main__" :
    t.title("거북 리스트 활용")
    t.setup(width = swidth + 50, height = sheight + 50)
    t.screensize(swidth, sheight)
    shapeList = t.getshapes()

    for i in range(num) :
        random.shuffle(shapeList)
        myTurtle = t.Turtle(shapeList[0])
        tX = random.randrange(int(-swidth / 2), int(swidth / 2))
        tY = random.randrange(int(-sheight / 2), int(sheight / 2))
        r = random.random(); g = random.random(); b = random.random();
        tSize = random.randrange(1, 3)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles :
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])
    t.done()
