import numpy as np


class Player:

    """Simple player class. Contains logger :)"""

    def __init__(self) -> None:
        self._nick = "nick"
        self.score = 0
        self.full_log = ""
        self.current_log = ""

    def _clear(self) -> None:
        self._score = 0
        self.full_log = ""
        self.current_log = ""

    @property
    def nick(self) -> str:
        return self._nick

    @nick.getter
    def nick(self) -> str:
        return self._nick

    @nick.setter
    def nick(self, value) -> None:
        if isinstance(value, str):
            self._nick = value
        else:
            raise TypeError

    def add_log(self, board: np.array) -> None:
        self.current_log = ""
        for row in board:
            for i in row:
                self.full_log += str(i)
                self.current_log += str(i)
        self.current_log += ";"
