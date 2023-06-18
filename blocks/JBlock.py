from .Figure import Figure
from numpy import array


class JBlock(Figure):
    block_id = 6
    color = (228, 231, 27)

    def __init__(self) -> None:
        self.shape_1 = [1, 4]
        self.shape_2 = [1, 5]
        self.shape_3 = [1, 6]
        self.shape_4 = [2, 6]
        self.box = [self.shape_1, self.shape_2, self.shape_3, self.shape_4]
        self.possition = "up"

    def change_shape(self, board: array) -> list:
        base = self.box.copy()
        pivot = base[1]

        if self.possition == "up":
            base[0], base[2], base[3] = (
                [pivot[0] + 1, pivot[1]],
                [pivot[0] - 1, pivot[1]],
                [pivot[0] + 1, pivot[1] - 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)

        if self.possition == "right":
            base[0], base[2], base[3] = (
                [pivot[0], pivot[1] + 1],
                [pivot[0], pivot[1] - 1],
                [pivot[0] - 1, pivot[1] - 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)

        if self.possition == "down":
            base[0], base[2], base[3] = (
                [pivot[0] - 1, pivot[1]],
                [pivot[0] + 1, pivot[1]],
                [pivot[0] - 1, pivot[1] + 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)

        if self.possition == "left":
            base[0], base[2], base[3] = (
                [pivot[0], pivot[1] - 1],
                [pivot[0], pivot[1] + 1],
                [pivot[0] + 1, pivot[1] + 1],
            )
            return self.pivot(base=base, board=board, possition=self.possition)
