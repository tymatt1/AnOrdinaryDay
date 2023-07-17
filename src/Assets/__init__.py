import pygame as pg
import os


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked

icon = pg.image.load(path + "/icon.png")
diningHall = pg.image.load(path + "/diningHall/dininghall.png")
testImg = pg.image.load(path + "/phrog.png")
character = pg.image.load(path + "/characterSprite/charStill.png")