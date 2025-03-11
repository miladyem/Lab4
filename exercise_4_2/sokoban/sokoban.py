import os
from sokoban_controller import SokobanController

# use os.path.join for portable code (so it works on Mac/Windows/Linux)
path = r"C:\Users\lemor\Dropbox\Emma epfl\Cours\GoodNotes 5\GoodNotes\BA2\Prog\Lab4\exercise_4_2\sokoban\levels\level1.xsb.txt"
sokoban = SokobanController(path)
sokoban.game_loop()