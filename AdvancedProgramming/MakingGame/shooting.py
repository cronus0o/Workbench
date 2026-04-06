# 심화프로그래밍 기말과제, 20252444 박지호

import pygame
import random
import time
from datetime import datetime

pygame.init()

size = [500, 900]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shooting Game")

clock = pygame.time.Clock()

pygame.mixer.music.load("tetrismusic.mp3")
pygame.mixer.music.play(-1)

class obj :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.move = 0

    def put_img(self, address) :
        if address[-3:] == "png" :
            self.img = pygame.image.load(address).convert_alpha()
        else :
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy) :
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self) :
        screen.blit(self.img, (self.x, self.y))
    
def crash(a, b) :
    if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx) :
        if (a.y - b.sy <= b.y) and (b.y <= a.y + a.sy) :
            return True
        else :
            return False
    else :
        return False

# 같은 기능을 하는 crash 함수의 다른 버전
# def crash(a, b) :
#     return (a.x < b.x + b.sx and a.x + a.sx > b.x and
#             a.y < b.y + b.sy and a.y + a.sy > b.y)

plane = obj()
plane.put_img("plane.png")
plane.change_size(50, 80)
plane.x = round(size[0]/2 - plane.sx/2)
plane.y = size[1] - plane.sy - 15
plane.move = 5

left_go = False
right_go = False
space_go = False

m_list = []
a_list = []

black = '#000000' # (0, 0, 0)
white = '#FFFFFF' # (255, 255, 255)
k = 0

GO = 0
kill = 0
loss = 0

SB = 0
while SB == 0 :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                SB = 1
    screen.fill(black)
    font = pygame.font.Font("Arial.ttf", 15) 
    text = font.render("PRESS SPACE KEY TO START THE GAME", True, white)
    screen.blit(text, (100, round(size[1]/2 - 50)))
    pygame.display.flip()

start_time = datetime.now()
SB = 0

while SB == 0 :
    clock.tick(60)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            SB = 1
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                left_go = True
            elif event.key == pygame.K_RIGHT :
                right_go = True
            elif event.key == pygame.K_SPACE :
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT :
                left_go = False
            elif event.key == pygame.K_RIGHT :
                right_go = False
            elif event.key == pygame.K_SPACE :
                space_go = False
    
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())

    if left_go == True :
        plane.x -= plane.move
        if plane.x <= 0 :
            plane.x = 0
    elif right_go == True :
        plane.x += plane.move
        if plane.x >= size[0] - plane.sx :
            plane.x = size[0] - plane.sx

    if space_go == True and k % 6 == 0 :
        mm = obj()
        mm.put_img("missile.png")
        mm.change_size(5, 15)
        mm.x = round(plane.x + plane.sx/2 - mm.sx/2)
        mm.y = plane.y - mm.sy
        mm.move = 15
        m_list.append(mm)
    k += 1

    d_list = []
    for i in range(len(m_list)) :
        m = m_list[i]
        m.y -= m.move
        if m.y < -m.sy :
            d_list.append(i)
    d_list.reverse()
    for d in d_list :
        del m_list[d]

    if random.random() > 0.98 :
        aa = obj()
        aa.put_img("alien.png")
        aa.change_size(50, 50)
        aa.x = random.randrange(0, size[0] - aa.sx - round(plane.sx/2))
        aa.y = 10
        aa.move = 1
        a_list.append(aa)

    d_list = []
    for i in range(len(a_list)) :
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1] :
            d_list.append(i)
    d_list.reverse()
    for d in d_list :
        del a_list[d]
        loss += 1

    dm_list = []
    da_list = []
    for i in range(len(m_list)) :
        for j in range(len(a_list)) :
            m = m_list[i]
            a = a_list[j]
            if crash(m, a) == True :
                dm_list.append(i)
                da_list.append(j)
    dm_list = list(set(dm_list))
    da_list = list(set(da_list))
    dm_list.reverse()
    da_list.reverse()

    try :
        for dm in dm_list :
            del m_list[dm]
        for da in da_list :
            del a_list[da]
            kill += 1
    except :
        pass

    for i in range(len(a_list)) :
        a = a_list[i]
        if crash(a, plane) == True :
            SB = 1
            GO = 1

    screen.fill(black)
    plane.show()
    for m in m_list :
        m.show()
    for a in a_list :
        a.show()

    fond = pygame.font.Font("Arial.ttf", 20)
    text_kill = fond.render("killed : {} loss : {}".format(kill, loss), True, '#FFFF00')
    screen.blit(text_kill, (10, 5))

    text_time = fond.render("time : {} s".format(delta_time), True, white)
    screen.blit(text_time, (size[0] - 100, 5))

    pygame.display.flip()

if GO == 1 :
    game_over = True
    while game_over :
        clock.tick(60)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                game_over = False

        screen.fill(black)
        font = pygame.font.Font("Arial.ttf", 40)
        text = font.render("GAME OVER", True, white)
        screen.blit(text, (130, 400))
        pygame.display.flip()
        
pygame.quit()
