from game.states import menu_state, game_state, server_state


class StateManager:
    menu_state = menu_state.MenuState()
    game_state = game_state.GameState()
    server_state = server_state.ServerState()

    current_state = None

    def __init__(self):
        self.current_state = self.game_state
        self.event = None

    def render(self, window):
        self.current_state.render(window)

    def update(self):
        self.current_state.update()
        self.menu_state.event = self.event
    
    def change_state(self, state):
        self.current_state = state
