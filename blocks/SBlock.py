from .Figure import Figure
from numpy import array


class SBlock(Figure):
    block_id = 7
    color = (154, 243, 74)

    def __init__(self) -> None:
        self.shape_1 = [1, 5]
        self.shape_2 = [1, 6]
        self.shape_3 = [2, 4]
        self.shape_4 = [2, 5]
        self.box = [self.shape_1, self.shape_2, self.shape_3, self.shape_4]
        self.possition = "up"

    def change_shape(self, board: array) -> list:
        base = self.box.copy()
        pivot = base[1]

        if self.possition == "up" or self.possition == "down":
            base[0], base[2], base[3] = (
                [pivot[0] - 1, pivot[1]],
                [pivot[0], pivot[1] + 1],
                [pivot[0] + 1, pivot[1] + 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)

        if self.possition == "right" or self.possition == "left":
            base[0], base[2], base[3] = (
                [pivot[0], pivot[1] + 1],
                [pivot[0] + 1, pivot[1]],
                [pivot[0] + 1, pivot[1] - 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)