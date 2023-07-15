import pygame as pg
import StoryUI as s
import Input


screen = pg.display.set_mode((300, 300), pg.RESIZABLE)
pg.display.set_caption("Epic Game 🐸")

running = True
while running:     # start game loop
    Input.handle()
    if Input.stop: running = False

    test = s.TextBox("hi")

    screen.fill((255, 0, 0))
    pg.display.flip()

pg.quit()