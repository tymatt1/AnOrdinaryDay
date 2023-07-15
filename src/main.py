import pygame as pg
import assets
# import StoryUI as s
import Input


FPS: int = 60

pg.init()
screen = pg.display.set_mode((1200, 675), pg.RESIZABLE)  # setup, 16:9 screen ratio
pg.display.set_caption("Epic Game 🐸")
pg.display.set_icon(assets.icon)

greet = pg.font.Font("freesansbold.ttf", 64).render("HELLO", True, (0, 0, 0))
greetRect = greet.get_rect()

text = pg.font.Font("freesansbold.ttf", 64).render("I'M GOING TO RGBEAT YOU", True, (0, 0, 0))
textRect = text.get_rect()

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

    greetRect.center = (screen.get_size()[0] / 2, (greetRect.size[1] / 2) + (screen.get_size()[1] / 7))
    screen.blit(greet, greetRect)

    textRect.center = (screen.get_size()[0] / 2, screen.get_size()[1] - (textRect.size[1] / 2) - (screen.get_size()[1] / 7))
    screen.blit(text, textRect)

    hue += 1  # important

    pg.display.flip()  # update display
    pg.time.wait(int(1000 / FPS) - (pg.time.get_ticks() - startMillis))  # do math to fps limit the game

pg.quit()