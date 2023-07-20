import pygame as pg
import Assets
import Input
import scenes
import renderHelper as rh

FPS = 60

rh.init("An Ordinary Day", Assets.icon)
Assets.loopSound(3)

running = True
while running:  # start game loop
    startMillis: int = pg.time.get_ticks()  # time at start

    Input.handle()
    if Input.stop: running = False
    if Input.getKey(pg.K_r): scenes.title.start()

    rh.renderBackground()
    scenes.currentScene.update()
    scenes.currentScene.render()

    rh.render()
    pg.time.wait(int(1000 / FPS) - (pg.time.get_ticks() - startMillis))  # do math to fps limit the game

pg.quit()