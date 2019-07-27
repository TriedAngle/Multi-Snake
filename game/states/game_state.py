from game.states.state import State

from game.objects.map import Map
from game.objects.snake import Snake


class GameState(State):
    map = None
    snakes = []

    def __init__(self):
        self.map = Map()
    
    def render(self):
        self.map.render()
        for snake in self.snakes:
            snake.render()

    def update(self):
        self.map.update()
        for snake in self.snakes:
            snake.update()

    def add_snake(self):
        self.snakes.append(Snake())