from storyUI import *
import Assets


dine = Scene(None, Assets.diningHall, StaticsList(),
              TextBox("wow theres food here aaaaaa"),
              Decision(
                  ("commit a crime", (), Scene(None, Assets.testImg, StaticsList(), TextBox("jail"))),
                  ("consume a bagel", (), Scene(Scene(None, Assets.icon, StaticsList(), TextBox("execution")), Assets.testImg, StaticsList(), TextBox("jail")))
              ))


wakeAt8 = Scene(dine, Assets.bedroom, StaticsList(),
                TextBox("You wake up feeling energized"),
                TextBox("Oh my turtles!\nIt's 8:15 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


wakeRoommate = Scene(None, Assets.matthew.stillRight, StaticsList(),
                     Decision(
                         ('Wake Up Your Roommate', (), Scene(None, Assets.anime.stillLeft, StaticsList(), TextBox("You woke up your rooommate"))),
                         ("Don't wake up your roommate", (), Scene(None, Assets.duy.stillLeft, StaticsList(), TextBox("You Roomate remains asleep"))),
                     ))

brushTeeth = Scene(None, Assets.matthew.stillRight, StaticsList(),
                   Decision(
                       ("Brush teeth", ("breath", "good"), Scene(wakeRoommate, Assets.anime.stillLeft, StaticsList(), TextBox("You brushed and have good breath"))),
                       ("Don't brush teeth", ("breath", "bad"), Scene(wakeRoommate, Assets.duy.stillLeft, StaticsList(), TextBox("You didn't brush and have bad breath"))),
                   ))


wakeAt9 = Scene(None, Assets.bedroom, StaticsList(),
                TextBox("You wake up feeling super energized."),
                TextBox("Diddly darn fiddlesticks!\nIt's 9:00 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


dorm = Scene(None, Assets.bedroom, StaticsList(),
             TextBox("You wake up to the sound of your alarm.\nIt is 7:30 am."),
             Decision(
                 ("Get ready", (), Scene(brushTeeth, Assets.bedroom, StaticsList(), TextBox("Getting ready"), Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 2.5)),),
                 ("Go back to sleep", (), Scene(wakeAt9, Assets.bedroom, StaticsList(), TextBox("Sleeping"))),
                 ("Snooze alarm", (), Scene(wakeAt8, Assets.bedroom, StaticsList(), TextBox("Sleeping")))
             )
             )




currentScene = dorm  # make this equal to the first scene