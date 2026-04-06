import turtle as t
import random 
from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 300, 300
tX, tY, txtSize = [0] * 3

t.title('거북이 글자쓰기')
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

for i in inStr  :
    tX = random.randrange(int(-swidth/2) , int(swidth/2))
    tY = random.randrange(int(-sheight/2) , int(sheight/2))
    r = random.random(); g = random.random(); b = random.random()
    t.goto(tX, tY)
    t.pencolor((r, g, b))
    t.write(i, font = ('맑은고딕', txtSize, 'bold'))

t.done()
