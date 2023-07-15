import pygame as pg
import assets
# import StoryUI as s
import Input


FPS: int = 60

pg.init()
screen = pg.display.set_mode((300, 300), pg.RESIZABLE)  # setup
pg.display.set_caption("Epic Game 🐸")
pg.display.set_icon(assets.icon)

hue = 0

running = True
while running:  # start game loop
    startMillis: int = pg.time.get_ticks()  # time at start

    Input.handle()
    if Input.stop: running = False

    c = pg.Color(0, 0, 0, 0)
    c.hsva = (hue % 360, 100, 100, 100)  # background color
    screen.fill(c)

    screen.blit(assets.testImg,
                ((screen.get_size()[0] / 2) - (assets.testImg.get_size()[0] / 2),  # display phrog in middle
                 (screen.get_size()[1] / 2) - (assets.testImg.get_size()[1] / 2)))

    hue += 1  # important

    pg.display.flip()  # update display
    pg.time.wait(int(1000 / FPS) - (pg.time.get_ticks() - startMillis))  # do math to fps limit the game

pg.quit()