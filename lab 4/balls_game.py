import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0
BALLS = []
time_of_previous_spawn = 0
spawn_time = 1000
speed_min = -10
speed_max = 10


def new_ball():
    """рисует новый шарик """
    global x, y, r, Vx, Vy
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    Vx = randint(speed_min, speed_max)
    Vy = randint(speed_min, speed_max)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    k = 0
    while k <= 200:
        circle(screen, BLACK, (x, y), r)
        x += Vx
        y += Vy
        circle(screen, color, (x, y), r)
        if x + r >= 1200 or x - r <= 0:
            Vx = -Vx
        elif y + r >= 900 or y - r <= 0:
            Vy = -Vy
    k += 1
    BALLS.append([x, y, r])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    time = pygame.time.get_ticks()
    if time - time_of_previous_spawn >= spawn_time:
        new_ball()
        pygame.display.update()
        time_of_prev_spawn = time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            a, b = event.pos
            for i, stats in enumerate(BALLS):
                x, y, r = stats
                if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
                    pygame.draw.circle(screen, BLACK, (x, y), r)
                    score += 1
                    BALLS.pop(i)
                    pygame.display.update()
pygame.quit()
