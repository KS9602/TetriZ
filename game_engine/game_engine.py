from random import choice


class GameEngine:
    def __init__(self, game) -> None:
        self.game = game

    def main_loop(self) -> None:
        """Main game loop"""
        self.game.delta_fall += self.game.clock.tick() / 1000
        while (
            self.game.delta_fall > 0.25
            and self.game.start_stop_flag == 2
            and self.game.game_over_flag == 0
        ):
            self.game.logger.add_log(self.game.board.board)
            self.create_figure()
            print("XXX")

    def create_figure(self) -> None:
        """Create new figure on bard or run falling function"""

        if 1 not in self.game.board.board:
            block = choice(self.game.BLOCKS)
            self.game.figure = block()
            self.game_over_check()
            self.stack_figure()
        else:
            cords = self.game.figure.falling(self.game.board.board)
            self.fall_checking(cords)

    def game_over_check(self) -> None:
        """Check space, if there is no empty box or self figure box, then game is over"""

        for i in self.game.figure.box:
            if self.game.board.board[i[0] + 1, i[1]] not in (0, 1):
                self.game.game_over_flag = 1

    def stack_figure(self) -> None:
        """Set falling figure at start possition"""

        for i in self.game.figure.box:
            self.game.board.board[i[0], i[1]] = 1
        self.game.delta_fall = 0.0
        self.game.logger.score += 10

    def fall_checking(self, cords: list) -> None:
        """Fall_checking method checks whether figure can continue to fall (if block below is not fall figure or free space,
        it cant). Then figure is freezed and if blocks create line on all row, row disapear.
        """

        for i in cords:
            if self.game.board.board[i[0], i[1]] not in (0, 1):
                self.game.move_manager.freez_figure(cords, self.game.figure.block_id)
                self.game.board.one_line_disapear(self.game.logger)
                return

        self.game.move_manager.draw_falling(cords)
        self.game.delta_fall = 0.0
