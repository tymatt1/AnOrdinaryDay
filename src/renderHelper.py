import string
import pygame as pg


pg.init()
screen = pg.display.set_mode((1200, 675))  # setup, 16:9 screen ratio


def size() -> tuple:
    return screen.get_size()

def width() -> int:
    return size()[0]

def height() -> int:
    return size()[1]


def init(text: string, icon: pg.Surface):
    pg.display.set_caption(text)
    pg.display.set_icon(icon)


def drawRect(color: tuple, pos: tuple, dims: tuple):
    s = pg.Surface(dims)  # size
    s.set_alpha(color[3])
    noA = (color[0], color[1], color[2])
    s.fill(noA)
    screen.blit(s, pos)

def drawText(text: string, fontSize: int, pos: tuple, color: tuple = (255, 255, 255), font: string = "freesansbold.ttf"):
    text = pg.font.Font(font, fontSize).render(text, True, color)
    textRect = text.get_rect()
    textRect.centerx = width() / 2 if pos[0] == -1 else pos[0]
    textRect.centery = height() / 2 if pos[1] == -1 else pos[1]
    screen.blit(text, textRect)


def render():
    pg.display.flip()