from evenMoreScenes import *
import Assets


alienLose = Scene(None, Assets.gameOver, StaticsList((Assets.sus, (1165, -5), (20, 50))), TextBox("The aliens were dissapointed that you got it wrong and evaporated you"))
alienWin = Scene(None, Assets.famous, StaticsList((Assets.sus, (1165, -5), (20, 50))), TextBox("The aliens were so overjoyed by your intellect and let you go home.\nYou are now a celebrity on Earth."))

alienQuiz = Scene(None, Assets.ufoWithAlien, StaticsList((Assets.sus, (1150, 0), (50, 20))),
                  TextBox("HELLO\nI am Xorp, this is Zzxoxzjozfoozp, and this is Terry"),
                  TextBox("We have brough you here on our quest for infinite knowledge.\nIf you can answer our riddles one, you can leave our ship."),
                  TextBox("How many endings does this game have?"),
                  Decision(
                      ("17", (), alienLose),
                      ("15", (), alienWin),
                      ("18", (), alienLose),
                      ("21", (), alienLose),
                      ("π", (), alienLose),
                      ("10", (), alienLose)
                  ))



jumpIntoVan = Scene(None, Assets.chaseVan, StaticsList(),
                    AttributeCheck(("energy", "none"), Scene(None, Assets.vanDeath, StaticsList(),
                                                             TextBox("You bend your knees and jump as hard as you can.\nYou miss the van and fall onto the concrete.\nMaybe you should have slept in."))),
                    AttributeCheck(("energy", "some"), Scene(None, Assets.vanDeath, StaticsList(),
                                                             TextBox("You manage to jump into the van, but you are exhausted.\nThe van people beat you and throw you out the back."))),
                    AttributeCheck(("energy", "very"), Scene(None, Assets.savedFriend, StaticsList(),
                                                             TextBox("Since you slept in, you have lots of energy.\nYou jump into the van and easily defeat the van people.\nYou save your friend and you become internet famous\nbecause someone was recording."))))

loseFriendCry = Scene(None, Assets.depressionEnding, StaticsList(), TextBox("You missed the chance to save your friend. You live the rest of\nyour life with the agony and guilt,\nknowing they trusted you and you failed them."))
friendKidnapped = Scene(loseFriendCry, Assets.kidnapping, StaticsList(),
                        TextBox("Oh no!\nYour friend was kidnapped by some guys in a nondescript white van!"),
                        TextBox("You decide to try to rescue them instead of going to class."),
                        QuickTimeEvent("The van is actually pretty slow.\nYou might be able to jump in!", 2.5, jumpIntoVan))


jerrySaved = Scene(goToClass, Assets.road, StaticsList(), TextBox("Oh no! You almost fell into a ditch, but\nJerry saved you and you go to class."))
ditchMatthew = Scene(None, Assets.ditchDeathMatthew, StaticsList(), TextBox("You fell into a ditch and crack your head. Oh no.\nMatthew tried saving you, but he also fell into the ditch.\nAt least you don't die alone!"))
fallIntoDitch = Scene(None, Assets.ditchDeathHead, StaticsList(),
                      AttributeCheck(("jerry", "true"), jerrySaved),
                      AttributeCheck(("matthew", "true"), ditchMatthew),
                      TextBox("You fell into a ditch and crack your head. Oh no."))



walkToClass = Scene(None, Assets.roadCharacters, StaticsList(),
                       TextBox("You walk to class."),
                       TextBox("Suddenly..."),
                       RNGScene(alienQuiz, friendKidnapped, fallIntoDitch))