from storyUI import *
import Assets


sixFlags = None

terroristsEnter = None

goToClass = Scene(terroristsEnter, Assets.classroom, StaticsList(),
                  TextBox("Finally, you make it to class barely on time."),
                  TextBox("Hello students, today we are going to learn about-"),
                  QuickTimeEvent("AAAAAAAAAGH!\nA SIX FLAGS SIGN UP FORM HAS COME OUT!\nEVERYONE WANTS TO SIGN UP QUICKLY!!!", 3, sixFlags),
                  TextBox("You missed the opportunity for Six Flags."))