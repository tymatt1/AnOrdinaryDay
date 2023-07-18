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
             Decision(
                 ("Get Ready", Scene(dine, Assets.bedroom, TextBox("Getting Ready")), Character(Assets.zach.stillLeft, (100, 80), (900, 260), (10, 260), 2.5)),
                 ("Sleep Longer Without Alarm", Scene(None, Assets.bedroom, TextBox("Sleeping"))),
                 ("Sleep Longer With Alarm", Scene(None, Assets.bedroom, TextBox("Sleeping")))
             )
             )