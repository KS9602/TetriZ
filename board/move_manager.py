from board.board import Board

class MoveManager:

    def __init__(self, board: Board) -> None:
        self.board = board

    def clear_figuer(self,figure: list) -> None:
        for i in figure:
            self.board[i[0], i[1]] = 1

    def draw_falling(self, figure: list) -> None:
        for i in figure:
            self.board[i[0] - 1, i[1]] = 0
        self.clear_figuer(figure)

    def freez_figure(self, figure: list, block_id: int) -> None:
        for i in figure:
            self.board[i[0] - 1, i[1]] = block_id

    def draw_move_left(self, figure: list) -> None:
        for i in figure:
            if self.board[i[0], i[1] + 1] == 1:
                self.board[i[0], i[1] + 1] = 0
        self.clear_figuer(figure)

    def draw_move_right(self, figure: list) -> None:
        for i in figure:
            if self.board[i[0], i[1] - 1] == 1:
                self.board[i[0], i[1] - 1] = 0
        self.clear_figuer(figure)

    def draw_move_down(self, figure: list) -> None:
        for i in figure:
            if self.board[i[0] - 1, i[1]] == 1:
                self.board[i[0] - 1, i[1]] = 0
        self.clear_figuer(figure)

    def draw_change(self, figure: list) -> None:
        for i in figure[1]:
            self.board[i[0], i[1]] = 0
        for i in figure[0]:
            self.board[i[0], i[1]] = 1