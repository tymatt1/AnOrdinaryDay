import pygame as pg


stop = False

def handle():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            global stop
            stop = True

def getKey(key: int):
    return pg.key.get_pressed()[key]