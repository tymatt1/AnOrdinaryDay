import string
import Assets


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
    def __init__(self, nextScene, *elements):
        self.elements = elements
        self.nextScene = nextScene

    def start(self):
        # do stuff

        if self.nextScene is not None:
            self.nextScene.start()

    def render(self, index):
        pass