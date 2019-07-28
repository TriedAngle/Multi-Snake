import pygame
from game.state_manager import StateManager


class Game:
    pygame.init()
    window = None
    running = False
    state_manager = None

    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Snaky Snake")
        self.running = True
        self.state_manager = StateManager()
        self.mainloop()
    
    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.state_manager.event = event

            self.update()
            self.render(self.window)
            pygame.display.update()
            pygame.time.delay(10)
            self.window.fill((0, 0, 0))

    def update(self):
        self.state_manager.update()

    def render(self, window):
        self.state_manager.render(window)
