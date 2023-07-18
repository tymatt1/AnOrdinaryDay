import string
import pygame as pg
import Input
import renderHelper as rh
from GameMath import Lerp
import scenes


class Element:
    def __init__(self):
        pass


class TextBox(Element):
    def __init__(self, text: string):
        super().__init__()
        self.text: string = text


class Decision(Element):
    def __init__(self, *choices):
        super().__init__()
        self.choices = choices


class Character(Element):
    def __init__(self, movImg: pg.Surface, start: tuple, end: tuple, duration: int, *imgs):
        super().__init__()
        self.movImg = movImg
        self.start = start
        self.end = end
        self.imgs = imgs
        self.duration = duration
        self.time = 0


class Scene:
    def __init__(self, nextScene, background: pg.Surface, *elements):
        self.nextScene = nextScene
        self.background = background
        self.elements = elements
        self.index = 0

    def start(self):
        scenes.currentScene = self

    def update(self):
        elem = self.elements[self.index]

        if type(elem) is TextBox and Input.getKey(pg.K_SPACE):
            if self.index + 1 < len(self.elements): self.index += 1
            elif self.nextScene is not None: self.nextScene.start()
        if type(elem) is Decision:
            for i in range(len(elem.choices)):
                if Input.getKey(i + 49): elem.choices[i][1].start()

    def render(self):
        rh.drawImg(self.background, (-1, -1), (-1, -1))
        boxHeight = 200

        elem = self.elements[self.index]

        if type(elem) is TextBox:
            rh.drawRect((0, 0, 0, 200), (0, rh.height() - boxHeight), (rh.width(), boxHeight))
            rh.drawText(elem.text, 32, (-1, rh.height() - (boxHeight / 2)))

        if type(elem) is Decision:
            rh.drawRect((0, 0, 0, 200), (0, rh.height() - boxHeight), (rh.width(), boxHeight))

            count = len(elem.choices)
            boxWidth = rh.width() / (count + 2)
            for i in range(count):
                x = (rh.width() / (count + 1)) * (i + 1)
                rh.drawRect((0, 0, 10, 200), (x - boxWidth / 2, rh.height() - boxHeight), (boxWidth, boxHeight))
                rh.drawText(str(i + 1), 16, (x, rh.height() - (boxHeight - 16)))
                rh.drawText(elem.choices[i][0], 16, (x, rh.height() - (boxHeight / 2)))