from moreScenes import *
import Assets



badStomach = Scene(None, Assets.diningHall, StaticsList(),
              TextBox("Your stomach doesn't feel so good..."),
              Decision(
                  ("Go to the bathroom", (), Scene(walkToClass, Assets.diningHall, StaticsList(), TextBox("Much better, time to go to class"))),
                  ("Go to class", (), Scene(None, Assets.poopDeath, StaticsList(), TextBox("You Pooped your pants"))),
              ))


dine = Scene(None, Assets.diningHall, StaticsList(),
              TextBox("What do you want to eat"),
              Decision(
                  ("Cereal", ("jerry", "true"), Scene(walkToClass, Assets.road, StaticsList(), TextBox("Time to go to class"))),
                  ("Pancakes", ("matthew", "true"), Scene(walkToClass, Assets.road, StaticsList(), TextBox("Time to go to class"))),
                  ("Oatmeal", ("duy", "true"), Scene(walkToClass, Assets.road, StaticsList(), TextBox("Time to go to class"))),
                  ("Eggs and Sausage", (), Scene(badStomach, Assets.icon, StaticsList(), TextBox("Uh Oh"))),
              ))
# new branch example

wakeAt8 = Scene(dine, Assets.bedroom, StaticsList(),
                TextBox("You wake up feeling energized"),
                TextBox("Oh my turtles!\nIt's 8:15 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


wakeRoommate = Scene(None, Assets.bedroom, StaticsList(),
                     Decision(
                         ('Wake Up Your Roommate', ("anime", "true"), Scene(dine, Assets.bedroom, StaticsList(), TextBox("You woke up your rooommate"))),
                         ("Don't wake up your roommate", ("imaginary", "true"), Scene(dine, Assets.bedroom, StaticsList(), TextBox("You Roomate remains asleep"))),
                     ))

brushTeeth = Scene(None, Assets.bathroom, StaticsList(),
                   Decision(
                       ("Brush teeth", ("breath", "good"), Scene(wakeRoommate, Assets.anime.stillLeft, StaticsList(), TextBox("You brushed and have good breath"))),
                       ("Don't brush teeth", ("breath", "bad"), Scene(wakeRoommate, Assets.duy.stillLeft, StaticsList(), TextBox("You didn't brush and have bad breath"))),
                   ))


wakeAt9 = Scene(walkToClass, Assets.bedroom, StaticsList(),
                TextBox("You wake up feeling super energized."),
                TextBox("Diddly darn fiddlesticks!\nIt's 9:00 am!"),
                Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 1))


dorm = Scene(None, Assets.bedroom, StaticsList(),
             TextBox("You wake up to your alarm.\nIt is 7:30 am."),
             Decision(
                 ("Get ready", ("energy", "none"), Scene(brushTeeth, Assets.bedroom, StaticsList(), TextBox("Getting ready"), Character(Assets.main.stillLeft, (100, 80), (900, 260), (100, 260), 2.5)),),
                 ("Go back to sleep", ("energy", "very"), Scene(wakeAt9, Assets.bedroom, StaticsList(), TextBox("Sleeping"))),
                 ("Snooze alarm", ("energy", "some"), Scene(wakeAt8, Assets.bedroom, StaticsList(), TextBox("Sleeping")))
             )
             )


title = Scene(dorm, Assets.title, StaticsList(), TextBox(""))

currentScene: Scene = title  # make this equal to the first scene