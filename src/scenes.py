from storyUI import *
import Assets


currentScene = None

start = Scene(None, Assets.testImg,
        # TextBox("this is a long string of text that i am writing\nfor demonstration purposes wow"),
        Decision(
                ("commit a crime", Scene(None, Assets.testImg, TextBox("jail")))
            )
    )