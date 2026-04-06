import turtle as t
swidth, sheight = 500, 500

t.title('무지개색 원그리기')
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.goto(0, -sheight/2)
t.pendown()
t.speed(0)

for r in range(1, 250) :
    if r % 7 == 0 :
        t.pencolor('red')
    elif r % 7 == 1 :
        t.pencolor('orange')
    elif r % 7 == 2 :
        t.pencolor('yellow')
    elif r % 7 == 3 :
        t.pencolor('green')
    elif r % 7 == 4 :
        t.pencolor('blue')
    elif r % 7 == 5 :
        t.pencolor('navyblue')
    else :
        t.pencolor('purple')

    t.circle(r)
t.done()
