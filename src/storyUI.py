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
    def __init__(self, nextScene, background: pg.surface.Surface, *elements):
        self.nextScene = nextScene
        self.background = background
        self.elements = elements

    def start(self):
        scenes.currentScene = self

    def render(self, index):
        pass