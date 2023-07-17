import pygame as pg
import os


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked

# misc
icon = pg.image.load(path + "/icon.png")
testImg = pg.image.load(path + "/phrog.png")
character = pg.image.load(path + "/characterSprite/charStill.png")

# backgrounds
diningHall = pg.image.load(path + "/backgrounds/diningHall/dininghall.png")
bedroom = pg.image.load(path + "/backgrounds/bedroom.png")
sixFlags = pg.image.load(path + "/backgrounds/Six Flags.png")