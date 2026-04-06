# 기초프로그래밍 02분반 중간고사 대체 프로젝트
# 자신의 왕국의 국기 만들기
# 박지호_20252444

# [국기의 의미]
# 전 세계적으로 많은 나라가 사용하는 3:2 비율을 채택하였다. 
# 국기에 사용되는 색상은 각각 여러 가지 의미를 가지는데, 배경에 사용된 흰색은 신뢰를, 노란색은 자유를, 초록색은 희망을 의미한다. 
# 또한 방패와 검을 칠하는데  사용된 파란색은 주로 정의를, 빨간색은 용기와 희생을 상징한다.
# 상단부터 순서대로 나타나는 흰색, 노란색, 초록색 바탕 위에 중앙에 위치한 파란색 방패는  
# ‘신뢰, 자유, 희망을 근간으로 정의를 지킨다’는 국가의 기본 정신을 담고 있다.  
# 또한, 방패 위에 교차하는 두 개의 붉은 검은 정의를 지키기 위해 필요한 용기와 희생을 의미하며, 국가를 수호하려는 결의를 나타낸다.
# 이렇게 구성된 국기는 신뢰를 바탕으로 정의를 수호하고, 이를 위해 용기와 희생을 감내하는 국가의 정신을 상징한다.

import turtle as t 

t.screensize(3 * 400, 2 * 400) # 화면 비율 3:2 설정
t.setup(3 * 400 + 50, 2 * 400 + 50) # 화면 보기 넓이 설정 +50
t.speed(0) 

def fill_bgcolor(x1, x2, y1, y2, color) : # 배경 색 설정 함수
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.end_fill()

# fill_bgcolor(x1, x2, y1, y2, what_color)
fill_bgcolor(-600, 600, 133, 400, 'white') # 배경 상단부 흰흰색 설정, 수직 길이 267
fill_bgcolor(-600, 600, -133, 133, 'yellow') # 배경 중단부 노란색 설정, 수직 길이 266
fill_bgcolor(-600, 600, -400, -133, 'green') # 배경 하단부 초록색 설정, 수직 길이 267

t.pencolor('blue')
t.fillcolor('blue')

t.penup() # 파랑 방패 오른쪽 만들기
t.setposition(0,-250) 
t.setheading(20)
t.pendown()
t.begin_fill() 
t.circle(400, 40)
t.left(90 - t.heading()) # 방향을 수직 위쪽으로 설정
t.forward(230)
t.setheading(160)
t.circle(-250, 30)
t.left(180 - t.heading()) # 방향을 수평 왼쪽으로 설정
t.forward(104)

t.setposition(0,-250) # 파랑 방패 왼쪽 만들기
t.setheading(160)
t.circle(-400, 40)
t.left(90 - t.heading()) # 방향을 수직 위쪽으로 설정
t.forward(230)
t.setheading(20)
t.circle(250, 30)
t.right(t.heading()) # 방향을 수평 오른쪽으로 설정
t.forward(104)
t.end_fill()

def red_sword(x, y, angle) : # 빨강 검 만들기 함수
    t.penup()
    t.pencolor('red')
    t.fillcolor('red')
    t.setposition(x, y) # 검 칼날 하단부 중앙에서 칼날 만들기 시작
    t.setheading(angle - 90) # 모든 각도에서 동작 가능
    t.pensize(1)
    t.pendown()
    t.begin_fill()
    t.forward(30) # 검의 칼날 두께 설정 (*2 가 최종 두께)
    t.left(90)
    t.forward(600) # 검의 검 끝 제외 칼날 길이 설정  
    t.left(30) # 검 끝 각도 설정(60도, 정삼각형, 각도에 맞게 길이 설정 변경) 
    t.forward(60) 
    t.left(120)
    t.forward(60)
    t.left(30)
    t.forward(600)
    t.left(90)
    t.forward(30)
    t.end_fill()

    t.pensize(15) # 검 손잡이 만들기
    t.forward(60) # 검의 칼날밑 길이 설정 
    t.backward(120)
    t.setposition(x, y)
    t.right(90)
    t.pensize(25) # 검 손잡이 두께
    t.forward(80) # 검 손잡이 길이

red_sword(-180, -200, 50) # red_sword(x, y, angle)  
red_sword(180, -200, 130)

t.hideturtle()
t.done()

