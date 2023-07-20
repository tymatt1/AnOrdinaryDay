from storyUI import *
import Assets


coasterFall = Scene(None, Assets.coasterFall, StaticsList(),
                    TextBox("Somehow, your cart fell off at the highest point of the loop.\nYou go to the hospital with 206 broken bones."))

winAtLife = Scene(None, Assets.funEnding, StaticsList(),
                  TextBox("The roller coaster broke down and killed everyone on it.\nThank god you didn't go on that. Anyways, you had fun at Six Flags\nand become a winner in life."))
noCoaster = Scene(winAtLife, Assets.sixFlags, StaticsList(),
                  AttributeCheck(("anime", "true"), Scene(coasterFall, Assets.sixFlags, StaticsList(), TextBox("Anime forces you onto the roller coaster."))))

sixFlags = Scene(None, Assets.sixFlags, StaticsList(),
                 TextBox("Yay! You're at Six Flags!\nDo you want to go on the roller coaster?"),
                 Decision(
                     ("Go on roller coaster", (), coasterFall),
                     ("Don't go on roller coaster", (), noCoaster)
                 ))
terrBreath = Scene(None, Assets.shot, StaticsList(),
                  AttributeCheck(("breath", "good"), Scene(coasterFall, Assets.famous, StaticsList(), TextBox("You tropical smelling breath from your toothpaste charmed them making them turn themselves in, you are now internet famous"))),
                  TextBox("Why didn't you try anything, you got shot"))

fighter = Scene(terrBreath, Assets.shot, StaticsList(),
                  AttributeCheck(("imaginary", "true"), Scene(coasterFall, Assets.savedFriend, StaticsList(), TextBox("They were scary, but your imaginary friend defeats them all"))),
                  TextBox("It was 20v1 what were you thinking, you got shot"))


terroristsEnter = Scene(None, Assets.classroom, StaticsList(),
              TextBox("A group of people terrorize your building, fight back?"),
              Decision(
                  ("Yes, fight back", (), Scene(fighter, Assets.classroom, StaticsList(),)),
                  ("No don't do anything", (), Scene(terrBreath, Assets.classroom, StaticsList())),
              ))


goToClass = Scene(terroristsEnter, Assets.classroom, StaticsList(),
                  TextBox("Finally, you make it to class barely on time."),
                  TextBox("Hello students, today we are going to learn about-"),
                  QuickTimeEvent("AAAAAAAAAGH! A SIX FLAGS SIGN UP FORM HAS COME OUT! EVERYONE WANTS TO SIGN UP QUICKLY!!!", 3, sixFlags),
                  TextBox("You missed the opportunity for Six Flags."))