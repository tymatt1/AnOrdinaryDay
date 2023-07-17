import pygame as pg
import Assets
import Input
import scenes
import renderHelper as rh


FPS = 60

rh.init("Epic Game 🐸", Assets.icon)
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

    hue += 1  # important

    scenes.currentScene.update()
    scenes.currentScene.render()

    rh.render()  # maybe delete later???
    pg.time.wait(int(1000 / FPS) - (pg.time.get_ticks() - startMillis))  # do math to fps limit the game

pg.quit()