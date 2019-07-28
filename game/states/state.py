from abc import ABC, abstractmethod


class State(ABC):
    name = ""

    @abstractmethod
    def render(self, window):
        pass

    @abstractmethod
    def update(self):
        pass
