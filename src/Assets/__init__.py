import os
import string
import pygame as pg


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked
def load(name: string) -> pg.Surface:
    return pg.image.load(f"{path}/{name}.png")

class Character:
    def __init__(self, name: string):
        self.stillLeft: pg.Surface = load(f"character/{name}StillLeft")
        self.stillRight: pg.Surface = load(f"character/{name}StillRight")


# characters
main = Character("Main")
zach = Character("Zach")
anime = Character("Anime")
matthew = Character("Matthew")
alex = Character("Alex")
duy = Character("Duy")
jerry = Character("Jerry")
imaginaryFriend = Character("ImaginaryFriend")
vanGuy = Character("VanGuy")
spiderman = Character("Spiderman")
alien = Character("Alien")

# backgrounds
diningHall = load("backgrounds/diningHall/dininghall")
bedroom = load("backgrounds/bedroom")
road = load("backgrounds/Road")
roadCharacters = load("backgrounds/Road with Characters")
sixFlags = load("backgrounds/Six Flags")
classroom = load("backgrounds/classroom")
vanFight = load("backgrounds/VanFight")
ufoWithAlien = load("backgrounds/UFO with Alien")
newUFO = load("backgrounds/New UFO")
gameOver = load("backgrounds/Game Over")
poopDeath = load("backgrounds/PoopDeath")
depressionEnding = load("backgrounds/Depression Ending")
ditchDeathHead = load("backgrounds/Ditch Death From Hitting Head")
ditchDeathMatthew = load("backgrounds/Ditch Death MC and Matthew")
fireBuilding = load("backgrounds/bigfirebuilding")
chaseVan = load("backgrounds/Chase White Van")
bathroom = load("backgrounds/Bathroom")
vanDeath = load("backgrounds/Van Death")

# misc
icon = load("misc/icon")
testImg = load("misc/phrog")
whiteVan = load("misc/White Van")
sword = load("misc/Sword")
waterGun = load("misc/WaterGun")
sus = load("misc/ඩ")