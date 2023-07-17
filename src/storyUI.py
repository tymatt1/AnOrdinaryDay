import string
import pygame as pg
import renderHelper as rh
import scenes


class UIElement:
    def __init__(self):
        pass


class TextBox(UIElement):
    def __init__(self, text: string, speed: float = 1, skippable: bool = True):
        super().__init__()
        self.text: string = text
        self.speed: float = speed
        self.skippable = skippable
        self.progress: int = 0
        self.completed: bool = False


class Decision(UIElement):
    def __init__(self, *choices):
        super().__init__()
        self.choices = choices


class Scene:
    def __init__(self, nextScene, background: pg.Surface, *elements):
        self.nextScene = nextScene
        self.background = background
        self.elements = elements
        self.index = 0

    def start(self):
        scenes.currentScene = self

    def update(self):
        pass

    def render(self):
        rh.drawImg(self.background, (-1, -1), (-1, -1))
        boxHeight = 200

        elem = self.elements[self.index]

        if type(elem) is TextBox:
            rh.drawRect((0, 0, 0, 200), (0, rh.height() - boxHeight), (rh.width(), boxHeight))
            rh.drawText(elem.text, 32, (-1, rh.height() - (boxHeight / 2)))

        if type(elem) is Decision:
            rh.drawRect((0, 0, 100, 150), (0, rh.height() - boxHeight), (rh.width(), boxHeight))

            boxWidth = 300
            count = len(elem.choices)
            for i in range(count):
                x = (rh.width() / (count + 1)) * (i + 1)
                rh.drawRect((0, 0, 0, 200), (x - boxWidth / 2, rh.height() - boxHeight), (boxWidth, boxHeight))
                rh.drawText(elem.choices[i][0], 16, (x, rh.height() - (boxHeight / 2)))