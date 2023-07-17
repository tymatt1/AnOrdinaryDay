import pygame as pg
import Assets
import Input
import scenes
import renderHelper as rh


FPS: int = 60

rh.init(Assets.icon)

greet = pg.font.Font("freesansbold.ttf", 64).render("HELLO", True, (0, 0, 0))
greetRect = greet.get_rect()

text = pg.font.Font("freesansbold.ttf", 64).render("I'M GOING TO RGBEAT YOU", True, (0, 0, 0))
textRect = text.get_rect()

scenes.start.start()

hue = 0
running = True
while running:  # start game loop
    startMillis: int = pg.time.get_ticks()  # time at start

    Input.handle()
    if Input.stop: running = False

    c = pg.Color(0, 0, 0, 0)
    c.hsva = (hue % 360, 100, 100, 100)  # background color
    rh.screen.fill(c)

    rh.screen.blit(Assets.testImg,
                ((rh.screen.get_size()[0] / 2) - (Assets.testImg.get_size()[0] / 2),  # display phrog in middle
                 (rh.screen.get_size()[1] / 2) - (Assets.testImg.get_size()[1] / 2)))

    greetRect.center = (rh.screen.get_size()[0] / 2, (greetRect.size[1] / 2) + (rh.screen.get_size()[1] / 7))
    rh.screen.blit(greet, greetRect)

    textRect.center = (rh.screen.get_size()[0] / 2, rh.screen.get_size()[1] - (textRect.size[1] / 2) - (rh.screen.get_size()[1] / 7))
    rh.screen.blit(text, textRect)

    hue += 1  # important

    pg.display.flip()  # update display

    rh.render()  # render everything from frame
    pg.time.wait(int(1000 / FPS) - (pg.time.get_ticks() - startMillis))  # do math to fps limit the game

pg.quit()