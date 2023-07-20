from storyUI import *
import Assets


coasterFall = Scene(None, Assets.coasterFall, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))),
                    Sound(2),
                    TextBox("Somehow, your cart fell off at the highest point of the loop.\nYou go to the hospital with 206 broken bones."))

winAtLife = Scene(None, Assets.funEnding, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))),
                  Sound(1),
                  TextBox("The roller coaster broke down and killed everyone on it.\nThank god you didn't go on that. Anyways, you had fun at Six Flags\nand become a winner in life."))
noCoaster = Scene(winAtLife, Assets.sixFlags, StaticsList(),
                  AttributeCheck(("anime", "true"), Scene(coasterFall, Assets.sixFlags, StaticsList(), TextBox("Anime forces you onto the roller coaster."))))

sixFlags = Scene(None, Assets.sixFlags, StaticsList(),
                 TextBox("Yay! You're at Six Flags!\nDo you want to go on the roller coaster?"),
                 Decision(
                     ("Go on roller coaster", (), coasterFall),
                     ("Don't go on roller coaster", (), noCoaster)
                 ))
terrBreath = Scene(None, Assets.fireBuilding, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))),
                  AttributeCheck(("breath", "good"), Scene(None, Assets.famous, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))), Sound(1),
                                                           TextBox("Your tropical smelling breath from brushing your teeth charmed them,\nmaking them turn themselves in. You are now internet famous."))),
                  Sound(2),
                  TextBox("They didn't listen...\nIt's up to the archaeologists to find your remains."))

fighter = Scene(None, Assets.shot, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))),
                  AttributeCheck(("imaginary", "true"), Scene(None, Assets.savedFriend, StaticsList((Assets.gameOverLabel, (-1, 50), (420, 210))), Sound(1),
                                                              TextBox("They were scary, but your imaginary friend defeats them all.\nEveryone now thinks you have telekinesis powers."))),
                  Sound(2),
                  TextBox("It was 20 vs 1. What were you thinking??? You got shot."))


terroristsEnter = Scene(None, Assets.classroom, StaticsList(),
              TextBox("A group of people terrorize your building.\nWhat do you do?"),
              Decision(
                  ("Fight back", (), fighter),
                  ("Try to reason with them", (), terrBreath),
              ))


goToClass = Scene(terroristsEnter, Assets.classroom, StaticsList(),
                  TextBox("Finally, you make it to class barely on time."),
                  TextBox("Hello students, today we are going to learn about-"),
                  QuickTimeEvent("AAAAAAAAAGH! A SIX FLAGS SIGN UP FORM HAS COME OUT! EVERYONE WANTS TO SIGN UP QUICKLY!!!", 3, sixFlags),
                  TextBox("You missed the opportunity for Six Flags."))