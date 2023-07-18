from storyUI import *
import Assets

currentScene = None


dine = Scene(None, Assets.diningHall,
              TextBox("wow theres food here aaaaaa"),
              Decision(
                  ("commit a crime", Scene(None, Assets.testImg, TextBox("jail"))),
                  ("consume a bagel",
                   Scene(Scene(None, Assets.icon, TextBox("execution")), Assets.testImg, TextBox("jail")))
              )
              )


dorm = Scene(None, Assets.bedroom,
             TextBox("Good Morning"),
             Character(Assets.Character.zachStillLeft, (500, 500), (900, 70), (10, 70), 2.5, (Assets.sword, (-1, -1), (500, 500))),
             Decision(
                 ("Get Ready", Scene(dine, Assets.bedroom, TextBox("Getting Ready"))),
                 ("Sleep Longer Without Alarm", Scene(None, Assets.bedroom, TextBox("Sleeping"))),
                 ("Sleep Longer With Alarm", Scene(None, Assets.bedroom, TextBox("Sleeping"))),
             )
             )