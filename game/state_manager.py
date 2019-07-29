from game.states import menu_state, game_state, server_state


class StateManager:

    menu_state = None
    game_state = None
    server_state = None
    events = None
    current_state = None

    def __init__(self, is_server=False):
        if is_server:
            self.server_state = server_state.ServerState()

        else:
            self.menu_state = menu_state.MenuState()
            self.game_state = game_state.GameState()

    def render(self, window):
        self.current_state.render(window)

    def update(self):
        self.current_state.update(self.events)
    
    def change_state(self, state):
        self.current_state = state
