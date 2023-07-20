import string
import pygame as pg
import Assets


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


def drawImg(img: pg.Surface, pos: tuple[float, float], dims: tuple[float, float]):
    """
    :param img: The surface taken from the Assets package
    :param pos: The position of the top left corner of the image. A value of -1 will center the image in that dimenison
    :param dims: The dimensions of the image. A value of -1 will make the image the width or height of the window
    """
    img = pg.transform.scale(img, (
            width() if dims[0] == -1 else dims[0],
            height() if dims[1] == -1 else dims[1]
        ))

    screen.blit(img, (
            (width() / 2) - (img.get_size()[0] / 2) if pos[0] == -1 else pos[0],
            (height() / 2) - (img.get_size()[1] / 2) if pos[1] == -1 else pos[1]
        ))

def drawRect(pos: tuple[float, float], dims: tuple[float, float], color: tuple[int, int, int] | tuple[int, int, int, int]):
    """
    :param color: The color of the rectangle
    :param pos: The position of the top left corner of the rectangle
    :param dims: The dimensions of the rectangle
    """
    s = pg.Surface(dims)  # size
    if len(color) > 3: s.set_alpha(color[3])
    noA = (color[0], color[1], color[2])
    s.fill(noA)
    screen.blit(s, pos)

def drawText(text: string, fontSize: int, pos: tuple[float, float], color: tuple[int, int, int] = (255, 255, 255), font: string = Assets.fontPath):
    """
    :param text: The string to be drawn. Backslash-n will automatically split the text into two lines
    :param fontSize: The size of the font in pixels
    :param pos: The position of the middle of the string
    :param color: The color of the string
    :param font: A string for the ttf file of the font
    """
    if "\n" in text:
        lines: tuple = text.split("\n")
        middle = (len(lines) - 1) / 2
        for i in range(len(lines)):
            drawText(lines[i], fontSize, (pos[0], pos[1] + ((i - middle) * fontSize)), color, font)
        return

    text = pg.font.Font(font, fontSize).render(text, True, color)
    textRect = text.get_rect()
    textRect.centerx = width() / 2 if pos[0] == -1 else pos[0]
    textRect.centery = height() / 2 if pos[1] == -1 else pos[1]
    screen.blit(text, textRect)


def renderBackground():
    c = pg.Color(0, 0, 0, 0)
    c.hsva = (pg.time.get_ticks() // 15 % 360, 100, 100, 100)  # background color
    screen.fill(c)

def render():
    pg.display.flip()