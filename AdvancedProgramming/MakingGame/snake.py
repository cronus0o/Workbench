# 심화프로그래밍 기말과제, 20252444 박지호

import pygame
import random
from datetime import datetime, timedelta

pygame.init()
pygame.mixer.init()

WHITE = '#FFFFFF' # (255, 255, 255)
RED = '#FF0000' # (225, 0, 0)
GREEN = '#00FF00' #(0, 255, 0)
size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

pygame.mixer.music.load("8bitmusic.mp3")
pygame.mixer.music.play(-1)

done = False
clock = pygame.time.Clock()
last_moved_time = datetime.now()

KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN : 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E', 
}

def draw_block(screen, color, position) :
    block = pygame.Rect((position[1] * 40, position[0] * 40), (40, 40))
    pygame.draw.rect(screen, color, block)

class Snake :
    def __init__(self) :
        self.positions = [(10, 10), (10, 9), (10, 8)]
        self.direction = 'N'
    
    def draw(self) :
        for position in self.positions :
            draw_block(screen, GREEN, position)

    def move(self) :
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N' :
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S' :
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W' :
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E' :
            self.positions = [(y, x + 1)] + self.positions[:-1]
    
    def grow(self) :
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N' :
            self.positions.append((y - 1, x))
        elif self.direction == 'S' :
            self.positions.append((y + 1, x))
        elif self.direction == 'W' :
            self.positions.append((y, x - 1))
        elif self.direction == 'E' :
            self.positions.append((y, x + 1))

class Feed :
    def __init__(self, position = (5, 5)) :
        self.position = position
    
    def draw(self) :
        draw_block(screen, RED, self.position)

    def relocate(self, snake_positions) :
        while True :
            new_position = (random.randint(0, 19), random.randint(0, 19))
            if new_position not in snake_positions :
                self.position = new_position
                break

def game_over() :
    global done
    screen.fill(WHITE)
    font = pygame.font.Font(None, 80)
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center = (size[0]//2, size[1]//2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    done = True

def runGame() :
    global done, last_moved_time
    snake = Snake()
    feed = Feed()
    
    while not done :
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                done = True
            if event.type == pygame.KEYDOWN :
                if event.key in KEY_DIRECTION :
                    new_direction = KEY_DIRECTION[event.key]
                    opposite_direction = {
                        'N': 'S',
                        'S': 'N', 
                        'W': 'E', 
                        'E': 'W'
                    }
                    if new_direction != opposite_direction[snake.direction] :
                        snake.direction = new_direction

        if timedelta(seconds = 0.1) <= datetime.now() - last_moved_time :
            snake.move()
            last_moved_time = datetime.now()

        if (snake.positions[0][0] < 0 or snake.positions[0][0] >= size[1]//40 or
            snake.positions[0][1] < 0 or snake.positions[0][1] >= size[0]//40) :
            game_over()

        if snake.positions[0] == feed.position :
            snake.grow()
            feed.relocate(snake.positions)

        snake.draw()
        feed.draw()
        pygame.display.update()

        if snake.positions[0] in snake.positions[1:] :
            game_over()

runGame()
pygame.quit()