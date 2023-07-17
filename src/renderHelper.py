import pygame as pg

pg.init()
screen = pg.display.set_mode((1200, 675))  # setup, 16:9 screen ratio

def init(icon: pg.Surface):
    pg.display.set_caption("Epic Game 🐸")
    pg.display.set_icon(icon)


def render():
    pass