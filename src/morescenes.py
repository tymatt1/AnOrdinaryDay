from storyUI import *
import Assets



alienLose = Scene(None, Assets.gameOver, StaticsList((Assets.sus, (1175, 0), (25, 20))), TextBox("The aliens were dissapointed that you got it wrong and evaporated you"))
alienWin = Scene(None, Assets.gameOver, StaticsList((Assets.sus, (1175, 0), (25, 20))), TextBox("The aliens were so overjoyed by your intellect and let you go home.\nYou are now a celebrity on Earth."))

alienQuiz = Scene(None, Assets.ufoWithAlien, StaticsList((Assets.sus, (1175, 0), (25, 20))),
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