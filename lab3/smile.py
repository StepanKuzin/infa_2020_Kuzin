import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 120)
circle(screen, (0, 0, 0), (200, 200), 120, 1)
circle(screen, (255, 0, 0), (150, 170), 20)
circle(screen, (0, 0, 0), (150, 170), 10)
circle(screen, (255, 0, 0), (250, 170), 15)
circle(screen, (0, 0, 0), (250, 170), 7)
line(screen, (0, 0, 0), (90, 100), (190,170), 10)
line(screen, (0, 0, 0), (210, 170), (310,135), 10)
line(screen, (0, 0, 0), (150, 260), (250,260), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()