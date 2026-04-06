import turtle as t
t.shape("turtle")
t.ht()

n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for i in range(n) :
    t.circle(80)
    t.left(360/n)
