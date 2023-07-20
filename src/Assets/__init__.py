import os
import string
import pygame as pg
import pygame.mixer as sfx

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
kidnapping = load("backgrounds/Kidnapping")
bathroom = load("backgrounds/Bathroom")
vanDeath = load("backgrounds/Van Death")
fallConcrete = load("backgrounds/Fall On Concrete")
savedFriend = load("backgrounds/Saved Your Friend")
famous = load("backgrounds/famousEndings")
coasterFall = load("backgrounds/rollerCoasterLoopDeath")
funEnding = load("backgrounds/sixFlagsFunEnding")
title = load("backgrounds/TitleScreen")
shooting = load("backgrounds/shooting")
shot = load("backgrounds/Shot by Terrorists")

# misc
icon = load("misc/icon")
testImg = load("misc/phrog")
whiteVan = load("misc/White Van")
sword = load("misc/Sword")
waterGun = load("misc/WaterGun")
sus = load("misc/ඩ")
gameOverLabel = load("misc/gameOverLabel")

# fonts
fontPath = path + "/fonts/VT323-Regular.ttf"

# audio
sfx.init()
sfx.set_num_channels(10)
sounds: list[sfx.Sound] = [
    sfx.Sound(path + "/audio/optionSelected.mp3"),
    sfx.Sound(path + "/audio/goodEnding.mp3"),
    sfx.Sound(path + "/audio/badEnding.mp3"),
    sfx.Sound(path + "/audio/Theme Song.mp3")
]

def playSound(index: int) -> None:
    """
    :param index: The index of the sound to be played. 0: select, 1: good ending, 2: bad ending, 3: theme song
    """
    pg.mixer.Channel(index).play(sounds[index])