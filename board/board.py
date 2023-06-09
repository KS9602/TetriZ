import numpy as np
from player.player import Player


class Board:

    """Board class is responsible for create numpy array on which game will be played.
    All methods expect one_line_disapear works similary. From outer method gets shape od figure, destroy previous
    shape and draw new"""

    def __init__(self, x=20, y=12) -> None:
        self.board = np.zeros((x, y), dtype="O")
        self.board[0], self.board[-1], self.board[:, 0], self.board[:, -1] = 9, 9, 9, 9
        self.new_row = np.array([[0 for i in range(y)]])
        self.new_row[0][0], self.new_row[0][-1] = 9, 9

    def one_line_disapear(self, logger: Player) -> None:
        """This method is responsible for destroy row which if full of block 'boxes/numbers' (except two '9' of frames).
        When row is detected upper frame turns into clear row, method create copy of all rows above destroyed row, add
        new rows to copy and paste to board attribute (and gains 100 points :))."""

        for e, row in enumerate(self.board):
            if 0 not in row and row[5] != 9:
                self.board[0, 1:-1] = 0
                box_above = self.board[:e]
                new_above = np.concatenate((self.new_row, box_above))
                self.board[: e + 1] = new_above
                self.board[0, 1:-1] = 9
                logger.score += 100
