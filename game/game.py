import pygame

class Game():
    
    pygame.init()
    window = None
    run = False

    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        self.run = True
        self.mainloop()
    
    def mainloop(self):
        while self.run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


    def render(self):
        pass

    def update(self):
        pass