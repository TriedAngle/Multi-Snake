import sys
from game.game import Game
# from game.objects.map_2 import Map

# This saves the arguments in 'args', and removes the first index
args = sys.argv[::-1][0:-1][::-1]


if not args:
    Game()

for arg in args:
    if arg == "--server":
        Game(is_server=True)
