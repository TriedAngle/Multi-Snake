import pygame
from game.state_manager import StateManager


class Game:

    window = None
    running = False
    state_manager = None

    def __init__(self, is_server=False):
        self.running = True
        self.is_server = is_server
        self.state_manager = StateManager(is_server)
        if is_server:
            self.state_manager.change_state(self.state_manager.server_state)
        else:
            self.state_manager = StateManager()
            pygame.init()
            self.window = pygame.display.set_mode((1024, 768))
            pygame.display.set_caption("Snaky Snake")
            self.state_manager.change_state(self.state_manager.menu_state)
        self.mainloop()
    
    def mainloop(self):
        while self.running:
            if not self.is_server:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        self.running = False
                self.state_manager.events = events

                self.update()
                self.render(self.window)
                pygame.display.update()
                pygame.time.delay(10)
                self.window.fill((0, 0, 0))

    def update(self):
        self.state_manager.update()

    def render(self, window):
        self.state_manager.render(window)
