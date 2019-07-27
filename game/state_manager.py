from game.states import menu_state, game_state, server_state


class StateManager:
    menu_state = menu_state.MenuState()
    game_state = game_state.GameState()
    server_state = server_state.ServerState()

    current_state = None

    def __init__(self, network_manager):
        self.current_state = self.menu_state
        self.network_manager = network_manager
        self.event = None

    def render(self):
        self.current_state.render()

    def update(self):
        self.current_state.update()
        self.menu_state.event = self.event
    
    def change_state(self, state):
        self.current_state = state
