import sys
#from game.game import Game

# This saves the arguments in 'args', and removes the first index
args = sys.argv[::-1][0:-1][::-1]

#game = Game()
###
from game.objects import map

mp = map.Map("test_map")