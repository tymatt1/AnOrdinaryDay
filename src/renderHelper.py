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


<<<<<<< Updated upstream
def drawImg(img: pg.Surface, pos: tuple, dims: tuple):
    img = pg.transform.scale(img, (
            width() if dims[0] == -1 else dims[0],
            height() if dims[1] == -1 else dims[1]
        ))

    screen.blit(img, (
            (width() / 2) - (img.get_size()[0] / 2) if pos[0] == -1 else pos[0],
            (height() / 2) - (img.get_size()[1] / 2) if pos[1] == -1 else pos[1]
        ))

=======
>>>>>>> Stashed changes
def drawRect(color: tuple, pos: tuple, dims: tuple):
    s = pg.Surface(dims)  # size
    s.set_alpha(color[3])
    noA = (color[0], color[1], color[2])
    s.fill(noA)
    screen.blit(s, pos)

def drawText(text: string, fontSize: int, pos: tuple, color: tuple = (255, 255, 255), font: string = "freesansbold.ttf"):
<<<<<<< Updated upstream
    if "\n" in text:
        lines: tuple = text.split("\n")
        middle = (len(lines) - 1) / 2
        for i in range(len(lines)):
            drawText(lines[i], fontSize, (pos[0], pos[1] + ((i - middle) * fontSize)), color, font)
        return

=======
>>>>>>> Stashed changes
    text = pg.font.Font(font, fontSize).render(text, True, color)
    textRect = text.get_rect()
    textRect.centerx = width() / 2 if pos[0] == -1 else pos[0]
    textRect.centery = height() / 2 if pos[1] == -1 else pos[1]
    screen.blit(text, textRect)


def render():
    pg.display.flip()