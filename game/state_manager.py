from game.states import menu_state, game_state, server_state


class StateManager:
    menu_state = menu_state.MenuState()
    game_state = game_state.GameState()
    server_state = server_state.ServerState()

    current_state = None

    def __init__(self):
        self.current_state = self.menu_state

    def render(self):
        self.current_state.render()

    def update(self):
        self.current_state.update()
    
    def change_state(self, state):
        self.current_state = state
