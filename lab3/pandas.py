import numpy as np
import pygame as pg
from pygame.draw import *
pg.init()

FPS = 30

screen = pg.display.set_mode((800,   600))

tree_color = (0, 90, 0)
screen_color = (255, 175, 128)
white = (0, 0, 0)
black = (255, 255, 255)

screen.fill(screen_color)


def log(x, y, scale_fact):
    """
    draw log of tree
    x - position in horizontal
    y - position in vertical
    scale_fact - scale of picture
    """
    surface_log = pg.Surface((800, 600))
    surface_log.set_colorkey(white)

    rect(screen, tree_color,
         (x, y, 16*scale_fact, 50*scale_fact))
    rect(surface_log, tree_color,
         (x, y - 55*scale_fact, 16*scale_fact, 50*scale_fact))
    rect(surface_log, tree_color,
         (x + 2*scale_fact, y - 80*scale_fact, 10*scale_fact, 20*scale_fact))
    rect(surface_log, tree_color,
         (x + 4*scale_fact, y - 95*scale_fact, 8*scale_fact, 10*scale_fact))

    screen.blit(surface_log, (0, 0))


def leaves(x, y, scale_fact):
    """
    draw leaves of tree
    x - position in horizontal
    y - position in vertical
    scale_fact - scale of picture
    """
    surface_leaves_r = pg.Surface((800, 600))
    surface_leaves_l = pg.Surface((800, 600))

    surface_leaves_l.set_colorkey(white)
    surface_leaves_r.set_colorkey(white)

    arc(surface_leaves_r, tree_color, (x + 20*scale_fact, y - 40*scale_fact, 60*scale_fact, 50*scale_fact), 0, np.pi, 2)
    arc(surface_leaves_r, tree_color, (x + 20*scale_fact, y - 80*scale_fact, 40*scale_fact, 25*scale_fact), 0, np.pi, 2)

    arc(surface_leaves_l, tree_color, (x - 65*scale_fact, y - 40*scale_fact, 60*scale_fact, 50*scale_fact), 0, np.pi, 2)
    arc(surface_leaves_l, tree_color, (x - 45*scale_fact, y - 80*scale_fact, 40*scale_fact, 25*scale_fact), 0, np.pi, 2)

    ellipse(surface_leaves_r, tree_color, [x + 40*scale_fact, y - 35*scale_fact, 10*scale_fact, 30*scale_fact])
    ellipse(surface_leaves_r, tree_color, [x + 50*scale_fact, y - 35*scale_fact, 8*scale_fact, 25*scale_fact])
    ellipse(surface_leaves_r, tree_color, [x + 62*scale_fact, y - 32*scale_fact, 6*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_r, tree_color, [x + 30*scale_fact, y - 33*scale_fact, 8*scale_fact, 25*scale_fact])

    ellipse(surface_leaves_l, tree_color, [x - 24*scale_fact, y - 35*scale_fact, 10*scale_fact, 30*scale_fact])
    ellipse(surface_leaves_l, tree_color, [x - 50*scale_fact, y - 35*scale_fact, 8*scale_fact, 25*scale_fact])
    ellipse(surface_leaves_l, tree_color, [x - 58*scale_fact, y - 32*scale_fact, 6*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_l, tree_color, [x - 36*scale_fact, y - 33*scale_fact, 8*scale_fact, 25*scale_fact])

    ellipse(surface_leaves_r, tree_color, [x + 36*scale_fact, y - 77*scale_fact, 8*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_r, tree_color, [x + 50*scale_fact, y - 75*scale_fact, 6*scale_fact, 15*scale_fact])
    ellipse(surface_leaves_r, tree_color, [x + 26*scale_fact, y - 73*scale_fact, 5*scale_fact, 15*scale_fact])

    ellipse(surface_leaves_l, tree_color, [x - 36*scale_fact, y - 77*scale_fact, 8*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_l, tree_color, [x - 20*scale_fact, y - 75*scale_fact, 6*scale_fact, 15*scale_fact])
    ellipse(surface_leaves_l, tree_color, [x - 26*scale_fact, y - 77*scale_fact, 5*scale_fact, 15*scale_fact])

    screen.blit(surface_leaves_l, (0, 0))
    screen.blit(surface_leaves_r, (0, 0))


def panda(x, y, scale_fact):
    """
    draw panda of tree
    x - position in horizontal
    y - position in vertical
    scale_fact - scale of picture
    """

    circle(screen, white,
           (x + 24*scale_fact, y - 35*scale_fact), scale_fact * 18)
    circle(screen, white,
           (x - 28*scale_fact, y - 33*scale_fact), scale_fact * 20)

    rect(screen, white,
         (x - 14*scale_fact, y, 18*scale_fact, 56*scale_fact))

    ellipse(screen, black,
            [x, y, 100*scale_fact, 60*scale_fact])

    rect(screen, white,
         (x + 12*scale_fact, y, 18*scale_fact, 70*scale_fact))

    circle(screen, black,
           (x, y), scale_fact * 43)

    rect(screen, white,
         (x - 12*scale_fact, y + 60*scale_fact, 42*scale_fact, 18*scale_fact))

    ellipse(screen, white,
            [x + 80*scale_fact, y + 30*scale_fact, 18*scale_fact, 49*scale_fact])

    circle(screen, white,
           (x - 34*scale_fact, y + 10*scale_fact), scale_fact * 11)
    circle(screen, white,
           (x, y + 13*scale_fact), scale_fact * 11)
    circle(screen, white,
           (x - 20*scale_fact, y + 32*scale_fact), scale_fact * 7)


def palm(x, y, scale_fact):
    """
    draw tree
    x - position in horizontal
    y - position in vertical
    scale_fact - scale of picture
    """
    log(x, y, scale_fact)

    leaves(x, y, scale_fact)


palm(200, 300, 3)
palm(50, 400, 1)
palm(600, 200, 2)
panda(500, 300, 2)
panda(300, 500, 1)
pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
