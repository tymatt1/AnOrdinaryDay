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
<<<<<<< Updated upstream
        rh.drawImg(self.background, (-1, -1), (-1, -1))

        elemType = type(self.elements[self.index])

        if elemType is TextBox:
            boxHeight = 200
            rh.drawRect((0, 0, 0, 200), (0, rh.height() - 200), (rh.width(), boxHeight))
            rh.drawText(self.elements[self.index].text, 32, (-1, rh.height() - (boxHeight / 2)))

        if elemType is Decision:
            pass
=======
        height = 200
        rh.drawRect((0, 0, 0, 220), (0, rh.height() - 200), (rh.width(), height))

        if type(self.elements[self.index]) is TextBox:
            rh.drawText(self.elements[self.index].text, 32, (-1, rh.height() - (height / 2)))
>>>>>>> Stashed changes
