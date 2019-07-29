from game.states.state import State
import pygame
from game.utility.misc import is_between

class MenuState(State):
    def __init__(self):
        self.play_col = [64, 64, 64]
        self.settings_col = [64, 64, 64]
    
    def render(self, window):
        font = pygame.font.Font("assets/fonts/menu.ttf", 62)
        pygame.draw.rect(window, self.play_col, [256, 240, 512, 128])
        window.blit(font.render("Play", True, (255, 255, 255)), (426, 256))
        pygame.draw.rect(window, self.settings_col, [256, 432, 512, 128])
        window.blit(font.render("Settings", True, (255, 255, 255)), (340, 448))

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                if is_between(pos, (256, 240), (768, 368)):
                    self.play_col = [128, 128, 128]
                else:
                    self.play_col = [64, 64, 64]
                if is_between(pos, (256, 432), (768, 560)):
                    self.settings_col = [128, 128, 128]
                else:
                    self.settings_col = [64, 64, 64]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_col == [128, 128, 128]:
                    # change into "play" state
                    print("Pressed 'Play'")
                    pass
                if self.settings_col == [128, 128, 128]:
                    # change into "settings" state
                    print("Pressed 'Settings'")
                    pass
