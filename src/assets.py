import pygame as pg
import os


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked

icon = pg.image.load(path + "/assets/icon.png")
testImg = pg.image.load(path + "/assets/phrog.png")