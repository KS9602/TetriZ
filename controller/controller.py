from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def manage_event(self):
        pass
