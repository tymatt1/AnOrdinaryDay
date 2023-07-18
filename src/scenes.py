from storyUI import *
import Assets


dine = Scene(None, Assets.diningHall,
              TextBox("wow theres food here aaaaaa"),
              Decision(
                  ("commit a crime", Scene(None, Assets.testImg, TextBox("jail"))),
                  ("consume a bagel",
                   Scene(Scene(None, Assets.icon, TextBox("execution")), Assets.testImg, TextBox("jail"))),
                  staticsTemp = StaticsList()
              ))


wakeAt8 = Scene(dine, Assets.bedroom,
                TextBox("You wake up feeling energized"),
                TextBox("Oh my turtles!\nIt's 8:15 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


brushTeeth = Scene(None, Assets.matthew.stillRight,
                   Decision(
                       ("Brush teeth", Scene(None, Assets.anime.stillLeft, TextBox("You brushed and have good breath"))),
                       ("Don't brush teeth", Scene(None, Assets.duy.stillLeft, TextBox("You didn't brush and have bad breath"))),
                       staticsTemp = StaticsList()
                   ))


wakeAt9 = Scene(None, Assets.bedroom,
                TextBox("You wake up feeling super energized."),
                TextBox("Diddly darn fiddlesticks!\nIt's 9:00 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


dorm = Scene(None, Assets.bedroom,
             TextBox("You wake up to the sound of your alarm.\nIt is 7:30 am."),
             Decision(
                 ("Get ready", Scene(brushTeeth, Assets.bedroom, TextBox("Getting ready"), Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 2.5)),),
                 ("Go back to sleep", Scene(wakeAt9, Assets.bedroom, TextBox("Sleeping"))),
                 ("Snooze alarm", Scene(wakeAt8, Assets.bedroom, TextBox("Sleeping"))),
                 staticsTemp = StaticsList()
             )
             )




currentScene = dorm  # make this equal to the first scene