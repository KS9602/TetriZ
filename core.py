import pygame as pg

from blocks.IBlock import IBlock
from blocks.SBlock import SBlock
from blocks.ZBlock import ZBlock
from blocks.LBlock import LBlock
from blocks.JBlock import JBlock
from blocks.TBlock import TBlock
from blocks.SquareBlock import SquareBlock
from board.board import Board
from board.move_manager import MoveManager
from player import Player
from board_logger import BoardLogger
from controller.event_manager import EventManager
from draw_manager.draw_manager import DrawManager
from game_engine.game_engine import GameEngine


class Game:

    """TetriZ main class"""

    def __init__(self) -> None:
        """Init create basic pygame objects, player object, flags and starts game main loop.
        Loop contains control system (keyboard and mouse), second loop and methods that draw graphic.
        The second loop run evry second if game isn't stopped/over. Loop runs logger method and checked
        whether '1' is on board, which means falling block is in game. If not, program choice class from class
        attribute and create new figure object(else figure is falling).
        Then board is checked whether at the 'zero' point is space required
        for draw block. If not, game is over, else figure starts falling"""

        self.game_engine = pg.init()
        self.board = Board()
        self.move_manager = MoveManager(board=self.board.board)
        self.BLOCKS = [SquareBlock, SBlock, ZBlock, LBlock, JBlock, IBlock, TBlock]
        pg.display.set_caption("TetriZ")
        self.window = pg.display.set_mode((720, 650))
        self.player = Player()
        self.logger = BoardLogger()
        self.clock = pg.time.Clock()
        self.delta_fall = 0.0
        self.font = pg.font.Font(None, 80)
        self.nick_font = pg.font.Font(None, 40)
        self.game_over_flag = 0
        self.start_stop_flag = 1
        self.color_flag = 1
        self.figure = None

        self.draw_manager = DrawManager(window=self.window)

        self.event_manager = EventManager(self)
        self.game_engine = GameEngine(self)

    def run(self):
        while True:
            self.game_engine.main_loop()
            self.event_manager.check_event_type(pg.event.get())
            self.draw_manager.draw_boxes(self.board.board, self.figure)
            self.draw_manager.draw_menu(
                color_flag=self.color_flag,
                start_stop_flag=self.start_stop_flag,
                player_nick=self.player.nick,
                logger_score=self.logger.score,
            )
            pg.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
