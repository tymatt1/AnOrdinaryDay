import string
from typing import Any
import random

import pygame as pg
import Input
import renderHelper as rh
from GameMath import *
import Assets
import scenes


attributes = {}


class StaticsList:
    def __init__(self, *statics: tuple[pg.Surface, tuple[float, float], tuple[float, float]]):
        """
        :param statics: Tuples of (<image from Assets>, <position tuple>, <dimensions tuple>)
        """
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
    def __init__(self, *choices: tuple[string, tuple, Any], statics: StaticsList = None):
        """
        :param choices: Tuples of (<choice name>, (<attribute name>, <attribute value>), <resulting scene>)
        :param statics: Static images present for the Decision
        """
        super().__init__(statics)
        self.choices = choices


class Character(Element):
    def __init__(self, movImg: pg.Surface, dims: tuple[float, float], start: tuple[float, float], end: tuple[float, float], duration: float, statics: StaticsList = None):
        """
        :param movImg: The image from the Assets package to be lerped
        :param start: The start of the lerptation
        :param end: The end of the lerpationification
        :param duration: The time for the lerpididilydo
        :param statics: Static images present for the movement
        """
        super().__init__(statics)
        self.movImg = movImg
        self.dims = dims
        self.start = start
        self.end = end
        self.duration = duration * 1000
        self.current = 0


class AttributeCheck(Element):
    def __init__(self, check: tuple[string, string], positiveScene):
        """
        :param check: A tuple of (key, value). If key == value, positiveScene is run, and if not, negativeScene is
        :param positiveScene: The scene to be run if key == value
        """
        super().__init__(StaticsList())
        self.check = check
        self.positiveScene = positiveScene


class RNGScene(Element):
    def __init__(self, *randomScenes):
        """
        :param scenes: A list of the potential scenes
        """
        super().__init__(StaticsList())
        self.nextScene = random.choice(randomScenes)


class QuickTimeEvent(Element):
    def __init__(self, text: string, duration: float, positiveScene, statics: StaticsList = None):
        """
        :param text: The text to be displayed during the QTE
        :param duration: The duration of the QTE
        :param positiveScene: If the QTE is successful, this scene will be run
        :param statics: Static images present during the QTE
        """
        super().__init__(statics)
        self.text = text
        self.duration = duration * 1000
        self.current = 0
        self.positiveScene = positiveScene


class Scene:
    def __init__(self, nextScene, background: pg.Surface, statics: StaticsList, *elements: Element):
        """
        :param nextScene: The scene that comes after this one finishes, use None if it ends in a Decision
        :param background: The surface that will be used as the background
        :param statics: Static images present for the whole scene
        :param elements: The elements to be iterated over during the scene
        """
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
            if self.index + 1 < len(self.elements):
                self.index += 1
            elif self.nextScene is not None: self.nextScene.start()

        if type(elem) is Decision:
            for i in range(len(elem.choices)):
                if Input.getKey(i + 49):
                    if len(elem.choices[i][1]) == 2:
                        attributes.update({str(elem.choices[i][1][0]): str(elem.choices[i][1][1])})
                    Assets.playSound(1)
                    #pg.mixer.music.play()
                    elem.choices[i][2].start()

        if type(elem) is Character:
            elem.current += 1000 / 60
            if elem.current > elem.duration:
                if self.index + 1 < len(self.elements): self.index += 1
                elif self.nextScene is not None: self.nextScene.start()

        if type(elem) is AttributeCheck:
            check = elem.check
            if check[0] in attributes.keys():
                if attributes.get(check[0]) is check[1]:
                    elem.positiveScene.start()
                    return
            if self.index + 1 < len(self.elements): self.index += 1
            elif self.nextScene is not None: self.nextScene.start()

        if type(elem) is RNGScene:
            elem.nextScene.start()

        if type(elem) is QuickTimeEvent:
            elem.current += 1000 / 60
            if Input.getKey(1 + 48):
                elem.positiveScene.start()
                return
            if elem.current > elem.duration:
                if self.index + 1 < len(self.elements):
                    self.index += 1
                    Assets.playSound(1)
                    # pg.mixer.music.play()
                elif self.nextScene is not None: self.nextScene.start()


    def render(self):
        rh.drawImg(self.background, (-1, -1), (-1, -1))
        elem = self.elements[self.index]
        if elem.statics is not None: elem.statics.renderStatics()
        self.statics.renderStatics()

        boxHeight = 150

        if type(elem) is TextBox:
            if elem.text != "": rh.drawRect((0, rh.height() - boxHeight), (rh.width(), boxHeight), (0, 0, 0, 200))
            rh.drawText(elem.text, 40, (-1, rh.height() - (boxHeight / 2)))

        if type(elem) is Decision:
            rh.drawRect((0, rh.height() - boxHeight), (rh.width(), boxHeight), (0, 0, 0, 200))

            count = len(elem.choices)
            # boxWidth = rh.width() / (count + 2)
            for i in range(count):
                x = (rh.width() / (count + 1)) * (i + 1)
                # rh.drawRect((x - boxWidth / 2, rh.height() - boxHeight), (boxWidth, boxHeight), (0, 0, 10, 200))
                # rh.drawText(str(i + 1) + ":", 16, (x, rh.height() - (boxHeight - 16)))
                rh.drawText("Press " + str(i + 1) + ":\n\n" + elem.choices[i][0], 32, (x, rh.height() - (boxHeight / 2)))

        if type(elem) is Character:
            rh.drawImg(elem.movImg, LerpTuple(elem.start, elem.end, elem.current / elem.duration), elem.dims)

        if type(elem) is QuickTimeEvent:
            rh.drawRect((0, rh.height() - boxHeight), (rh.width(), boxHeight), (0, 0, 0, 200))
            rh.drawText(f"Press 1:\nSeconds left: {((elem.duration - elem.current) / 1000):.2f}\n\n" + elem.text, 32, (rh.width() / 2, rh.height() - (boxHeight / 2)))