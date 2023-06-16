from abc import ABC, abstractmethod
from numpy import array


class Figure(ABC):

    """Figure is parent class for all type of blocks. Contain methods which are responsible for moving and changing block.
    All method checks condition of 'move' and if it's true, return new possition, else return old possition.
    Child classes contains unique id and color. Object of child class contains 4x shape attributes with possition x,y and
    the box which is list of all shape attributes. Additionaly child classes contains change shape method
    """

    def falling(self, board: array) -> list:
        for i in self.box:
            if board[i[0], i[1]] not in (0, 1):
                return self.box
            else:
                for j in self.box:
                    j[0] = j[0] + 1
                return self.box

    def move_down(self, board: array) -> list:
        try:
            for i in self.box:
                if board[i[0] + 1, i[1]] not in (0, 1) or board[i[0] + 2, i[1]] not in (
                    0,
                    1,
                ):
                    return self.box
        except IndexError:
            return self.box

        for j in self.box:
            j[0] = j[0] + 1
        return self.box

    def move_left(self, board: array) -> list:
        for i in self.box:
            if board[i[0], i[1] - 1] not in (0, 1):
                return self.box

        for j in self.box:
            j[1] = j[1] - 1
        return self.box

    def move_right(self, board: array) -> list:
        for i in self.box:
            if board[i[0], i[1] + 1] not in (0, 1):
                return self.box

        for j in self.box:
            j[1] = j[1] + 1
        return self.box

    def pivot(self, base: list, board: array, possition: list) -> list:
        for i in base:
            if board[i[0], i[1]] not in (0, 1):
                return [self.box, self.box]

        mapping = {"up": "right", "right": "down", "down": "left", "left": "up"}
        self.possition = mapping[possition]
        self.box, old_base = base, self.box
        figure = [self.box, old_base]
        return figure

    @abstractmethod
    def change_shape(self):
        pass
