import pygame
from game.state_manager import StateManager


class Game:
    pygame.init()
    window = None
    running = False
    state_manager = None

    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        self.running = True
        self.state_manager = StateManager()
        self.mainloop()
    
    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()
            pygame.display.update()
            pygame.time.delay(10)
            self.window.fill((0, 0, 0))

    def update(self):
        self.state_manager.update()

    def render(self):
        self.state_manager.render()
