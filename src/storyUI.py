import string
import pygame as pg
import Input
import renderHelper as rh
from GameMath import *
import scenes


class StaticsList:
    def __init__(self, *statics: tuple[pg.Surface, tuple[float, float], tuple[float, float]]):
        self.statics = statics

    def renderStatics(self):
        for i in range(len(self.statics)):
            rh.drawImg(self.statics[i][0], self.statics[i][1], self.statics[i][2])


class Element:
    def __init__(self, statics: StaticsList):
        self.statics = statics


class TextBox(Element):
    def __init__(self, text: string, statics: StaticsList = None):
        super().__init__(statics)
        self.text: string = text


class Decision(Element):
    def __init__(self, *choices: tuple, staticsTemp: StaticsList):
        super().__init__(staticsTemp)
        self.choices = choices


class Character(Element):
    def __init__(self, movImg: pg.Surface, dims: tuple[float, float], start: tuple[float, float], end: tuple[float, float], duration: float, statics: StaticsList = None):
        """
        :param movImg: The image from the Assets package to be lerped
        :param start: The start of the lerptation
        :param end: The end of the lerpationification
        :param duration: The time for the lerpididilydo
        :param statics: A tuple of tuples with the image and position of static images
        """
        super().__init__(statics)
        self.movImg = movImg
        self.dims = dims
        self.start = start
        self.end = end
        self.duration = duration * 1000
        self.current = 0


class QuickTime(Element):
    def __init__(self, statics):
        super().__init__(statics)


class Scene:
    def __init__(self, nextScene, background: pg.Surface, statics: StaticsList, *elements: Element):
        self.nextScene = nextScene
        self.background = background
        self.statics = statics
        self.elements = elements
        self.index = 0

    def start(self):
        scenes.currentScene = self

    def update(self):
        elem = self.elements[self.index]

        if not Input.getKey(pg.K_SPACE): Input.allowSpace = True

        if type(elem) is TextBox and Input.allowSpace and Input.getKey(pg.K_SPACE):
            Input.allowSpace = False
            if self.index + 1 < len(self.elements): self.index += 1

            elif self.nextScene is not None: self.nextScene.start()
        if type(elem) is Decision:
            for i in range(len(elem.choices)):
                if Input.getKey(i + 49): elem.choices[i][1].start()

        if type(elem) is Character:
            elem.current += 1000 / 60
            if elem.current > elem.duration:
                if self.index + 1 < len(self.elements): self.index += 1
                elif self.nextScene is not None: self.nextScene.start()

    def render(self):
        rh.drawImg(self.background, (-1, -1), (-1, -1))
        elem = self.elements[self.index]
        if elem.statics is not None: elem.statics.renderStatics()
        self.statics.renderStatics()

        boxHeight = 200

        if type(elem) is TextBox:
            rh.drawRect((0, rh.height() - boxHeight), (rh.width(), boxHeight), (0, 0, 0, 200))
            rh.drawText(elem.text, 32, (-1, rh.height() - (boxHeight / 2)))

        if type(elem) is Decision:
            rh.drawRect((0, rh.height() - boxHeight), (rh.width(), boxHeight), (0, 0, 0, 200))

            count = len(elem.choices)
            boxWidth = rh.width() / (count + 2)
            for i in range(count):
                x = (rh.width() / (count + 1)) * (i + 1)
                rh.drawRect((x - boxWidth / 2, rh.height() - boxHeight), (boxWidth, boxHeight), (0, 0, 10, 200))
                rh.drawText(str(i + 1), 16, (x, rh.height() - (boxHeight - 16)))
                rh.drawText(elem.choices[i][0], 16, (x, rh.height() - (boxHeight / 2)))

        if type(elem) is Character:
            rh.drawImg(elem.movImg, LerpTuple(elem.start, elem.end, elem.current / elem.duration), elem.dims)