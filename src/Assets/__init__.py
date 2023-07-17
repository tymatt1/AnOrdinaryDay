import pygame as pg
import os


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked

def load(name) -> pg.Surface:
    return pg.image.load(f"{path}/{name}.png")


# misc
icon = load("icon")
testImg = load("phrog")
character = load("characterSprite/charStill")
whiteVan = load("misc/White Van")
sword = load("misc/Sword")
waterGun = load("misc/WaterGun")

# backgrounds
diningHall = load("backgrounds/diningHall/dininghall")
bedroom = load("backgrounds/bedroom")
sixFlags = load("backgrounds/Six Flags")
classroom = load("backgrounds/classroom")