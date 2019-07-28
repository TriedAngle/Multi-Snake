from game.states.state import State
from server import server


class ServerState(State):
    def __init__(self):
        self.event = None
        self.server = server.Server()

    def render(self, window):
        pass

    def update(self):
        pass
