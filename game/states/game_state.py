from game.states.state import State

from game.objects.map import Map
from game.objects.snake import Snake


class GameState(State):
    map = None
    snakes = []

    def __init__(self):
        self.map = Map()
        self.add_snake()
    
    def render(self, window):
        self.map.render(window)
        for snake in self.snakes:
            snake.render(window)

    def update(self):
        self.map.update()
        for snake in self.snakes:
            snake.update()

    def add_snake(self):
        self.snakes.append(Snake())
