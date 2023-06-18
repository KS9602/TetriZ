import numpy as np


class BoardLogger:
    def __init__(self) -> None:
        self.full_log: str = ""
        self.current_log: str = ""
        self.score: int = 0

    def clear(self) -> None:
        self._score = 0
        self.full_log = ""
        self.current_log = ""

    def add_log(self, board: np.array) -> None:
        self.current_log = ""
        for row in board:
            for i in row:
                self.full_log += str(i)
                self.current_log += str(i)
        self.current_log += ";"
