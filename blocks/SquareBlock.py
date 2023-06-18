from .Figure import Figure
from numpy import array


class SquareBlock(Figure):
    block_id = 2
    color = (231, 54, 27)

    def __init__(self) -> None:
        self.shape_1 = [1, 5]
        self.shape_2 = [1, 6]
        self.shape_3 = [2, 5]
        self.shape_4 = [2, 6]
        self.box = [self.shape_1, self.shape_2, self.shape_3, self.shape_4]
        self.possition = "up"

    def change_shape(self, board: array) -> list:
        figure = [self.box, self.box]
        return figure
