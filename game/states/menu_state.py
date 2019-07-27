from game.states.state import State
import pygame
from game.utility.misc import is_between

class MenuState(State):
    def __init__(self):
        self.event = None
    
    def render(self):
        pass

    def update(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if is_between()

