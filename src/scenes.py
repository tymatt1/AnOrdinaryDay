from storyUI import *
import Assets


currentScene = None

start = Scene(None, Assets.diningHall,
        TextBox("wow theres food here aaaaaa"),
        Decision(
                ("commit a crime", Scene(None, Assets.testImg, TextBox("jail"))),
                ("consume a bagel", Scene(Scene(None, Assets.icon, TextBox("execution")), Assets.testImg, TextBox("jail")))
            )
    )