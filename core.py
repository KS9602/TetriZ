import pygame as pg
from sys import exit
from random import choice

from blocks.IBlock import IBlock
from blocks.SBlock import SBlock
from blocks.ZBlock import ZBlock
from blocks.LBlock import LBlock
from blocks.JBlock import JBlock
from blocks.TBlock import TBlock
from blocks.SquareBlock import SquareBlock
from board import Board
from player import Player
from BoardLogger import BoardLogger

from constants import (
    GAME_VEC,
    VECTOR_MENU,
    MENU,
    START_BUTTON,
    RESTART,
    SCORE,
    PLAYER,
    PLAYER_COLOR ,
)

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
        pg.init()
        self.board = Board()
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


        while True:
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if (
                    event.type == pg.KEYDOWN
                    and event.key == pg.K_LEFT
                    and self.start_stop_flag == 2
                    and self.game_over_flag == 0
                ):
                    self.board.draw_move_left(self.figure.move_left(self.board.board))
                if (
                    event.type == pg.KEYDOWN
                    and event.key == pg.K_RIGHT
                    and self.start_stop_flag == 2
                    and self.game_over_flag == 0
                ):
                    self.board.draw_move_right(self.figure.move_right(self.board.board))
                if (
                    event.type == pg.KEYDOWN
                    and event.key == pg.K_UP
                    and self.start_stop_flag == 2
                    and self.game_over_flag == 0
                ):
                    self.board.draw_change(self.figure.change_shape(self.board.board))
                if (
                    event.type == pg.KEYDOWN
                    and event.key == pg.K_DOWN
                    and self.start_stop_flag == 2
                    and self.game_over_flag == 0
                ):
                    self.board.draw_move_down(self.figure.move_down(self.board.board))
                if (
                    event.type == pg.MOUSEBUTTONDOWN
                    and event.button == 1
                    and START_BUTTON.collidepoint(pos)
                ):
                    self.start_stop_flag = self.start_stop_flag % 2 + 1
                if (
                    event.type == pg.MOUSEBUTTONDOWN
                    and event.button == 1
                    and PLAYER.collidepoint(pos)
                ):
                    self.color_flag = self.color_flag % 2 + 1
                if (
                    event.type == pg.MOUSEBUTTONDOWN
                    and event.button == 1
                    and RESTART.collidepoint(pos)
                ):
                    self.start_stop_flag = 1
                    self.board = Board()
                    self.logger._clear()
                    self.figure = None
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.player.nick = self.player.nick[:-1]
                    else:
                        if len(self.player.nick) < 19:
                            self.player.nick += event.unicode



            if self.start_stop_flag != 1 and self.game_over_flag == 0:
                self.delta_fall += self.clock.tick() / 1000
                while self.delta_fall > 0.25 and self.game_over_flag == 0:
                    self.logger.add_log(self.board.board)
                    if 1 not in self.board.board:
                        block = choice(self.BLOCKS)
                        self.figure = block()

                        for i in self.figure.box:
                            if self.board.board[i[0] + 1, i[1]] not in (0, 1):
                                self.game_over_flag = 1  # gameover


                        for i in self.figure.box:
                            self.board.board[i[0], i[1]] = 1
                        self.delta_fall = 0.0
                        self.logger.score += 10
                    else:
                        cords = self.figure.falling(self.board.board)
                        Game.fall_checking(self, cords=cords)

            self.draw_boxes()
            self.draw_menu()
            pg.display.flip()

    def draw_boxes(self) -> None:
        """Draw boxes mathod based on board object. 0 - empyt space, 1 - falling figure ,
        2-8 individual color of figure, 9 - frame"""

        for row_en, row in enumerate(self.board.board):
            for pos_en, i in enumerate(row):
                GAME_VEC.x = 32 * pos_en
                GAME_VEC.y = 32 * row_en
                rect = pg.Rect(GAME_VEC.x, GAME_VEC.y, 30, 30)

                if i == 1:
                    pg.draw.rect(self.window, self.figure.color, rect, 0, 5)
                elif i == 9:
                    pg.draw.rect(self.window, (150, 0, 255), rect, 0, 5)
                elif i == 0:
                    pg.draw.rect(self.window, (255, 255, 255), rect, 0, 5)
                else:
                    for block in self.BLOCKS:
                        if i == block.block_id:
                            pg.draw.rect(self.window, block.color, rect, 0, 5)

    def draw_menu(self) -> None:
        pg.draw.rect(self.window, (200, 200, 200), MENU, 0)
        pg.draw.rect(self.window, (100, 100, 200), START_BUTTON, 0)
        pg.draw.rect(self.window, PLAYER_COLOR[self.color_flag], PLAYER, 0)
        pg.draw.rect(self.window, (200, 100, 200), SCORE, 0)
        pg.draw.rect(self.window, (250, 80, 120), RESTART, 0)
        status = {1: "    START", 2: "    STOP"}

        surface_start_stop = self.font.render(
            f"{status[self.start_stop_flag]}", True, "white"
        )
        surface_score = self.font.render(f"P: {self.logger.score}", True, "white")
        surface_restart = self.font.render("RESTART", True, "white")
        nick_surface = self.nick_font.render(self.player.nick, True, (255, 255, 255))

        self.window.blit(surface_start_stop, (START_BUTTON))
        self.window.blit(surface_score, (SCORE))
        self.window.blit(surface_restart, (RESTART))
        self.window.blit(nick_surface, (PLAYER))

    def fall_checking(self, cords: list) -> None:
        """Fall_checking method checks whether figure can continue to fall (if block below is not fall figure or free space,
        it cant). Then figure is freezed and if blocks create line on all row, row disapear.
        """

        for i in cords:
            if self.board.board[i[0], i[1]] not in (0, 1):
                self.board.freez_figure(cords, self.figure.block_id)
                self.board.one_line_disapear(self.player)
                return

        self.board.draw_falling(cords)
        self.delta_fall = 0.0




if __name__ == "__main__":
    Game()
