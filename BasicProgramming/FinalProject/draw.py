# draw module

import turtle as t
import math as m

# 기본 화면 설정 함수
def set_screen(size_scale, width_ratio, height_ratio) : 
    t.clear()
    size = size_scale
    width = size * width_ratio # width, height 최종값을 고려해서 파라미터 설정해야 함
    height = size * height_ratio
    t.screensize(width, height)
    t.setup(width + 50, height + 50)
    t.speed(0)
    t.bgcolor('#000000')
    return size, width, height

# 부분적 배경 색 설정 함수
def fill_background(x1, x2, y1, y2, color) : # (x1,y1),(x2,y1),(x1,y2),(x1,y2) 직사각형 색칠
    t.color(color, color) # pencolor, fillcolor
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.end_fill()

# 사용성 증가 색 설정 함수
def fill_background_extended(*xy, color): # 가변매개변수, 입력하는 순서에 유의
    t.color(color, color) # pencolor, fillcolor
    t.penup()
    t.goto(xy[0]) # 입력받은 첫 번째 위치
    t.pendown()
    t.begin_fill() 
    for i in xy[1:]: # 입력받은 순서대로 이동
        t.goto(i)
    t.end_fill()

# 별 작도 함수
def draw_star(x, y, r, angle, color) : # 중심의 x,y 좌표, 외접원 반지름 r, 별 각도, 색 지정
    t.color(color, color) # pencolor, fillcolor
    t.penup()
    t.goto(x, y)
    t.setheading(angle) # 입력 각도
    t.forward(r) # 별 상부 꼭짓점으로 이동
    t.pendown()
    t.setheading(angle + 162) # 상부 꼭짓점에서 시작 각도
    t.begin_fill()
    for _ in range(5) :
        t.forward(r * m.sin(m.radians(36)) / m.cos(m.radians(36))) # 외접원 반지름 r일 때, 별의 한 변의 길이 공식
        t.right(72)
        t.forward(r * m.sin(m.radians(36)) / m.cos(m.radians(36)))
        t.left(144)
    t.end_fill()