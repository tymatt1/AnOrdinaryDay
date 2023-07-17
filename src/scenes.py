from storyUI import *
import Assets


currentScene = None
<<<<<<< Updated upstream

start = Scene(None, Assets.testImg,
        # TextBox("this is a long string of text that i am writing\nfor demonstration purposes wow"),
        Decision(
                ("commit a crime", Scene(None, Assets.testImg, TextBox("jail")))
            )
    )
=======
start = Scene(None, Assets.testImg, TextBox("You wake up in a laaaaaaaaaaaaaaaaaaaaaaaateyrsetdrydtesrtdfkyutrd\nfcgjhvtufyaaaaaaaaaarge room"))  # make first scene current so it starts
>>>>>>> Stashed changes
