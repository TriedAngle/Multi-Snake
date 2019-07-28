import pygame


class Snake:
    x = 128
    y = 128
    width = 64
    height = 64
    color = (255, 200, 200)

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= 64
        if key[pygame.K_s]:
            self.y += 64
        if key[pygame.K_a]:
            self.x -= 64
        if key[pygame.K_d]:
            self.x += 64
