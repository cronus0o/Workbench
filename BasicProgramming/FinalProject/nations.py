# nations module
# import turtle as t
# import math as m

from draw import *

def draw_Japan() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, -height/2, height/2, '#FFFFFF')

    t.penup()
    t.goto(0, -height * 0.3)
    t.color('#FE0000', '#FE0000')
    t.pendown()
    t.begin_fill()
    t.circle(height * 0.3)
    t.end_fill()

    t.hideturtle()
    return

def draw_China() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, -height/2, height/2, '#EE1C25')

    draw_star(-size, size/2, size * 0.3, 90, '#FFFF00')
    draw_star(-size/2, size * 0.8, size * 0.1, m.atan(0.6), '#FFFF00') # m.tan() 각 도면상의 tan값을 이용하여 각도를 구함
    draw_star(-size * 0.3, size * 0.6, size * 0.1, m.atan(1/7), '#FFFF00')
    draw_star(-size * 0.3, size * 0.3, size * 0.1, m.atan(-2/7), '#FFFF00')
    draw_star(-size/2, size * 0.1, size * 0.1, m.atan(-0.8), '#FFFF00')

    t.hideturtle()
    return

def draw_NorthKorea() :
    size, width, height = set_screen(600, 2, 1)
    fill_background(-width/2, width/2, -height/2, height/2, '#ED1C27')
    
    fill_background(-width/2, width/2, height/3, height/2, '#024FA2')
    fill_background(-width/2, width/2, -height/3, -height/2, '#024FA2')

    fill_background(-width/2, width/2, height/2 * 11/18, height/3, '#FFFFFF')
    fill_background(-width/2, width/2, -height/2 * 11/18, -height/3, '#FFFFFF')
    
    t.penup()
    t.goto(-width/6, -height/2 * 16/18 / 2)
    t.color('#FFFFFF', '#FFFFFF')
    t.pendown()
    t.begin_fill()
    t.circle(height/2 * 16/18 / 2) # height/2 이 18에 대응, 도면상 지름 16
    t.end_fill()

    draw_star(-width/6, 0, height/2 * 31/72, 90, '#ED1C27') # 16/18 / 2 - 1/4 / 18 = 31/72

    t.hideturtle()
    return

def draw_SouthKorea() : 
    size, width, height = set_screen(400, 3, 2)
    angle = m.degrees(m.atan(1.5))
    fill_background(-width/2, width/2, -height/2, height/2, '#FFFFFF')

    # 건괘 그리기
    for i in range(0, 3) : # 1, 0.875, 0.75
        t.penup()
        t.color('#FFFFFF', '#FFFFFF')
        t.goto(0, 0)
        t.pendown()
        t.setheading(180 + angle)
        t.circle((-1 + 0.125 * i) * size / 2, 180)
        t.setheading(angle)
        t.color('#000000', '#000000')
        t.begin_fill()
        for j in [4, 12, 2, 12, 4] :
            t.forward(size/j)
            t.left(90)
        t.end_fill()
    
    # 이괘 그리기
    for i in range(0, 3) : # 1, 0.875, 0.75 
        t.penup()
        t.color('#FFFFFF', '#FFFFFF')
        t.goto(0, 0)
        t.pendown()
        t.setheading(-angle)
        t.circle((-1 + 0.125 * i) * size / 2, 180)
        t.setheading(-angle)
        if i == 1 :
            t.forward(size/24 / 2)
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [11/24, 1/6, 11/24, 1/6] :
                t.forward(size * j / 2)
                t.right(90)
            t.end_fill()
            
            t.left(180)
            t.color('#FFFFFF', '#FFFFFF')
            t.forward(size/12 / 2)
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [11/24, 1/6, 11/24, 1/6] :
                t.forward(size * j / 2)
                t.left(90)
            t.end_fill()
        else :
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [2, 6, 1, 6, 2] :
                t.forward(size / j / 2)
                t.right(90)
            t.end_fill()
        
    # 감괘 그리기
    for i in range(0, 3) : # 1, 0.875, 0.75 
        t.penup()
        t.color('#FFFFFF', '#FFFFFF')
        t.goto(0, 0)
        t.pendown()
        t.setheading(-angle)
        t.circle((1 - 0.125 * i) * size / 2, 180)
        t.setheading(-angle)
        if i == 1 :
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [2, 6, 1, 6, 2] :
                t.forward(size / j / 2)
                t.left(90) 
            t.right(90)
            t.end_fill()
        else :
            t.forward(size/24 / 2)
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [11/24, 1/6, 11/24, 1/6] :
                t.forward(size * j / 2)
                t.left(90)
            t.end_fill()
            
            t.right(180)
            t.color('#FFFFFF', '#FFFFFF')
            t.forward(size/12 / 2)
            t.color('#000000', '#000000')
            t.begin_fill()
            for j in [11/24, 1/6, 11/24, 1/6] :
                t.forward(size * j / 2)
                t.right(90)
            t.end_fill()

    # 곤괘 그리기
    for i in range(0, 3) : # 1, 0.875, 0.75 
        t.penup()
        t.color('#FFFFFF', '#FFFFFF')
        t.goto(0, 0)
        t.pendown()
        t.setheading(180 + angle)
        t.circle((1 - 0.125 * i) * size / 2, 180)
        t.setheading(angle)

        t.forward(size/24 / 2)
        t.color('#000000', '#000000')
        t.begin_fill()
        for j in [11/24, 1/6, 11/24, 1/6] :
            t.forward(size * j / 2)
            t.right(90)
        t.end_fill()
            
        t.left(180)
        t.color('#FFFFFF', '#FFFFFF')
        t.forward(size/12 / 2)
        t.color('#000000', '#000000')
        t.begin_fill()
        for j in [11/24, 1/6, 11/24, 1/6] :
            t.forward(size * j / 2)
            t.left(90)
        t.end_fill()
    
    for i, j, k in [['#CD2E3A', angle, -1], ['#0047A0', angle + 180, 1]] :
        t.penup()
        t.color(i, i)
        t.goto(0, 0)
        t.pendown()
        t.begin_fill()
        t.setheading(angle + 180)
        t.circle(-size/4, 180)
        t.setheading(j)
        t.circle(k * size/2, 180)
        t.setheading(angle)
        t.circle(size/4, 180)
        t.end_fill()

    t.hideturtle()
    return

def draw_India() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, -height/2, height/2, '#FFFFFF')
    fill_background(-width/2, width/2, height/6, height/2, '#FF671F')
    fill_background(-width/2, width/2, -height/6, -height/2, '#046A38')

    # 가장 바깥 파란 원
    t.penup()
    t.goto(0, -size * 185/300 / 2) # 지름 : size = 185 : 300 
    t.setheading(0)
    t.color('#06038D','#06038D')
    t.pendown()
    t.begin_fill()
    t.circle(size * 185/300 / 2)
    t.end_fill()    

    # 파란 원 안쪽의 흰 원
    t.penup()
    t.goto(0, -size * 160/300 / 2) # 지름 : size = 160 : 300
    t.setheading(0)
    t.color('#FFFFFF','#FFFFFF')
    t.pendown()
    t.begin_fill()
    t.circle(size * 160/300 / 2)
    t.end_fill()

    # 흰 원의 둘레를 따라 파란 작은 원들 작도
    t.penup()
    t.color('#06038D','#06038D')
    t.goto(0, -size * 160/300 / 2) 
    t.setheading(0)
    for i in range(48) : 
        t.circle(size * 160/300 / 2, 7.5) # 7.5도 회전 이후 15도 마다 작도
        if i%2 == 0 :
            t.right(90)
            t.forward(size * 7/300 / 2)
            t.left(90)
            t.begin_fill()
            t.circle(size * 7/300 / 2) # 지름 : size = 7 : 300
            t.end_fill()
            t.left(90)
            t.forward(size * 7/300 / 2)
            t.right(90)

    # 가장 안쪽의 파란 원 작도
    t.penup()
    t.color('#06038D','#06038D')
    t.goto(0, -size * 32/300 / 2) # 지름 : size = 32 : 300
    t.setheading(0)
    t.begin_fill()
    t.circle(size * 32/300 / 2)
    t.end_fill()

    # 가장 안쪽 원의 둘레를 따라 가시 작도
    t.penup()
    t.color('#06038D','#06038D')
    t.goto(0, -size * 32/300 / 2) 
    t.setheading(0)
    for i in range(24) : 
        t.begin_fill()
        angle_1 = m.degrees(m.atan(1/8)) #
        angle_2 = m.degrees(m.atan(16)) #
        t.forward(size * 1/300)
        t.right(90 - angle_1)
        t.forward(size * 260**0.5 / 300) # 16**2 + 2**2 = 260
        t.right(angle_1)
        t.right(90 - angle_2)
        t.forward(size * 2313**0.5 / 300) # 48**2 + 3**2 = 2313
        t.right(angle_2 * 2)
        t.forward(size * 2313**0.5 / 300)
        t.right(90 - angle_2)
        t.right(angle_1)
        t.forward(size * 260**0.5 / 300)
        t.right(90 - angle_1)
        t.forward(size * 1/300)
        t.end_fill()
        t.circle(size * 32/300 / 2, 15)

    t.hideturtle()

def draw_Israel() :
    size, width, height = set_screen(100, 11, 8)
    fill_background(-width/2, width/2, -height/2, height/2, '#FFFFFF')
    fill_background(-width/2, width/2, height/4, height/2 * (1 - 15/80), '#0038B8')
    fill_background(-width/2, width/2, -height/4, -height/2 * (1 - 15/80), '#0038B8')

    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.pendown()

    # 다윗의 별 작도, 여섯 개의 정삼각형으로 나누어
    for i in range(6) :
        length_big = ((11 + 11/2 + 25/4) * 2 / 3**0.5) / 80
        length_small = (25 * 3**0.5 / 8) / 80

        # 파란색 정삼각형 작도
        t.color('#0038B8', '#0038B8')
        t.forward(height/2 * 47/4 / 80) # height/2 * 도면 상의 수치/80
        t.left(90)
        t.begin_fill()
        t.forward(height/2 * length_big/2) 
        t.right(120)
        t.forward(height/2 * length_big)
        t.right(120)
        t.forward(height/2 * length_big)
        t.right(120)
        t.forward(height/2 * length_big/2)
        t.end_fill()

        # 파란색 정삼각형 안쪽의 흰색 정삼각형 작도
        t.color('#FFFFFF', '#FFFFFF')
        t.right(90)
        t.forward(height/2 * 5.5 / 80)
        t.left(90)
        t.begin_fill()
        t.forward(height/2 * length_small/2)
        t.right(120)
        t.forward(height/2 * length_small)
        t.right(120)
        t.forward(height/2 * length_small)
        t.right(120)
        t.forward(height/2 * length_small/2)
        t.end_fill()
        t.left(90)
        t.color('#0038B8', '#0038B8')
        t.forward(height/2 * 5.5 / 80)
        t.pencolor('#FFFFFF')
        t.forward(height/2 * 47/4 / 80)
        t.right(180)

        t.left(60)

    t.hideturtle()

def draw_Taiwan() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, -height/2, height/2, '#FE0000')
    fill_background(-width/2, 0, 0, height/2, '#000095')
    
    t.penup()
    t.goto(-width/4, height * (1/2 - 1/16)) # 별 상단부 꼭짓점으로 이동
    t.setheading(255) # 270 - 15
    t.color('#FFFFFF','#FFFFFF')
    t.pendown()
    t.begin_fill()
    for i in range(12) :
        t.forward(height * 3/16 * (2 + 3**0.5)**0.5 ) #
        t.left(150)
    t.end_fill()

    t.penup()
    t.goto(-width/4, height/2 * (1/2 - 17/40 / 2)) # height/2 이 80에 대응, 도면상의 반지름 17
    t.setheading(0)
    t.pendown()
    t.color('#000095')
    t.begin_fill()
    t.circle(height/2 * 17/40 / 2)
    t.end_fill()

    t.penup()
    t.goto(-width/4, height/2 * (1/2 - 15/40 / 2)) # height/2 이 80에 대응, 도면상의 반지름 15
    t.setheading(0)
    t.pendown()
    t.color('#FFFFFF')
    t.begin_fill()
    t.circle(height/2 * 15/40 / 2)
    t.end_fill()

    t.hideturtle()

def draw_UK() :
    size, width, height = set_screen(600, 2, 1)
    fill_background(-width/2, width/2, -height/2, height/2, '#00247D')

    # 흰색 x자
    fill_background_extended( # 왼쪽 상단부터 오른쪽 하단으로 작도
        (-width/2, height/2), 
        (-width/2, (1 - 5**0.5/10) * height/2), 
        (width * 2/5, -height/2), 
        (width/2, -height/2), 
        (width/2, -(1 - 5**0.5/10) * height/2),
        (-width * 2/5, height/2),
        color = '#FFFFFF'
    ) 
    fill_background_extended( # 오른쪽 상단부터 왼쪽 하단으로 작도
        (width/2, height/2), 
        (width/2, (1 - 5**0.5/10) * height/2), 
        (-width * 2/5, -height/2), 
        (-width/2, -height/2), 
        (-width/2, -(1 - 5**0.5/10) * height/2),
        (width * 2/5, height/2),
        color = '#FFFFFF'
    )

    # 
    fill_background_extended((-width * 1/15, 0), (0, 0), (width/2, height/2), (width * 13/30, height/2), color = '#CF142B')
    fill_background_extended((-width/2, -height/2), (-width * 13/30, -height/2), (width/15, 0), (0, 0), color = '#CF142B')
    fill_background_extended((-width/2, height/2), (-width/2, (1 - 5**0.5/15) * height/2), (0, -5**0.5/15 * height/2), (0, 0), color = '#CF142B')
    fill_background_extended((width/2, -height/2), (width/2, -(1 - 5**0.5/15) * height/2), (0, 5**0.5/15 * height/2), (0, 0), color = '#CF142B')
    
    # 흰색 십자가
    fill_background(-width/2, width/2, -height/2 * 5/15, height/2 * 5/15, '#FFFFFF')
    fill_background(-width/2 * 5/30, width/2 * 5/30, -height/2, height/2, '#FFFFFF')
    
    # 빨간색 십자가
    fill_background(-width/2 * 3/30, width/2 * 3/30, -height/2, height/2, '#CF142B')
    fill_background(-width/2, width/2, -height/2 * 3/15, height/2 * 3/15, '#CF142B')

    t.hideturtle()
    return

def draw_USA() :
    t.clear()
    ratio = 0.2
    width = int(7410 * ratio)
    height = int(3900 * ratio)
    t.screensize(width, height)
    t.setup(width + 50, height + 50) # 7410 - 5928 = 1482
    t.speed(0)

    t.bgcolor('#000000')
    fill_background(-width/2, width/2, -height/2, height/2, '#FFFFFF')

    # Red stripe
    fill_background(-706*ratio, width/2, 1650*ratio, height/2, '#BB133E') # 3705 - 2964 = 706
    fill_background(-706*ratio, width/2, 1050*ratio, 1350*ratio, '#BB133E')
    fill_background(-706*ratio, width/2, 450*ratio, 750*ratio, '#BB133E')
    fill_background(-706*ratio, width/2, -150*ratio, 150*ratio, '#BB133E')
    fill_background(-width/2, width/2, -750*ratio, -450*ratio, '#BB133E')
    fill_background(-width/2, width/2, -1350*ratio, -1050*ratio, '#BB133E')
    fill_background(-width/2, width/2, -1650*ratio, -height/2, '#BB133E')

    # Blue part
    fill_background(-width/2, -706*ratio, -150*ratio, height/2, '#002664')

    # Star
    for i in range(-3458, -494, 494) : # 3705 - 247
        for j in range(1740, -360, -420) : # 1950 - 210 
            draw_star(i * ratio, j * ratio, 120 * ratio, 90, '#FFFFFF')
    
    for i in range(-3211, -741, 494) : # 3705 - 247 * 2
        for j in range(1530, -150, -420) : # 1950 - 210 * 2
            draw_star(i * ratio, j * ratio, 120 * ratio, 90, '#FFFFFF')

    t.hideturtle()
    return

def draw_Vietnam() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, -height/2, height/2, '#DA251D')

    draw_star(0, 0, height * 0.3, 90, '#FFFF00')

    t.hideturtle()

def draw_MyCountry() :
    size, width, height = set_screen(400, 3, 2)
    fill_background(-width/2, width/2, height/6, height/2, 'gray')
    fill_background(-width/2, width/2, -height/6, height/6, '#FFFFFF')
    fill_background(-width/2, width/2, -height/6, -height/2, 'gray')
    
    draw_star(0, 0, height/5, 90, 'black')
    t.penup()
    t.color('#06038D','#06038D')
    t.goto(0, height/3) 
    t.setheading(180)
    for i in ['red','orange','yellow','green','blue','navy','purple'] :
        t.pensize(0)
        a = t.heading()
        b = t.xcor()
        c = t.ycor()
        t.pendown()
        draw_star(b, c, height/10, a + 90, i)
        t.goto(b, c)
        t.setheading(a)
        t.penup()
        t.circle(height/3, 360/7)

    t.hideturtle()
    return
