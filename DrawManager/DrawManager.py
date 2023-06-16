import pygame as pg
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

from blocks.IBlock import IBlock
from blocks.SBlock import SBlock
from blocks.ZBlock import ZBlock
from blocks.LBlock import LBlock
from blocks.JBlock import JBlock
from blocks.TBlock import TBlock
from blocks.SquareBlock import SquareBlock


class DrawManager:
    def __init__(self,window) -> None:
        self.window = window
        self.BLOCKS = [SquareBlock, SBlock, ZBlock, LBlock, JBlock, IBlock, TBlock]
        self.font = pg.font.Font(None, 80)
        self.nick_font = pg.font.Font(None, 40)



    def draw_boxes(self,board,figure) -> None:
        """Draw boxes mathod based on board object. 0 - empyt space, 1 - falling figure ,
        2-8 individual color of figure, 9 - frame"""

        for row_en, row in enumerate(board):
            for pos_en, i in enumerate(row):
                GAME_VEC.x = 32 * pos_en
                GAME_VEC.y = 32 * row_en
                rect = pg.Rect(GAME_VEC.x, GAME_VEC.y, 30, 30)

                if i == 1:
                    pg.draw.rect(self.window, figure.color, rect, 0, 5)
                elif i == 9:
                    pg.draw.rect(self.window, (150, 0, 255), rect, 0, 5)
                elif i == 0:
                    pg.draw.rect(self.window, (255, 255, 255), rect, 0, 5)
                else:
                    for block in self.BLOCKS:
                        if i == block.block_id:
                            pg.draw.rect(self.window, block.color, rect, 0, 5)




    def draw_menu(self,color_flag,start_stop_flag,player_nick,logger_score) -> None:
        pg.draw.rect(self.window, (200, 200, 200), MENU, 0)
        pg.draw.rect(self.window, (100, 100, 200), START_BUTTON, 0)
        pg.draw.rect(self.window, PLAYER_COLOR[color_flag], PLAYER, 0)
        pg.draw.rect(self.window, (200, 100, 200), SCORE, 0)
        pg.draw.rect(self.window, (250, 80, 120), RESTART, 0)
        status = {1: "    START", 2: "    STOP"}

        surface_start_stop = self.font.render(
            f"{status[start_stop_flag]}", True, "white"
        )
        surface_score = self.font.render(f"P: {logger_score}", True, "white")
        surface_restart = self.font.render("RESTART", True, "white")
        nick_surface = self.nick_font.render(player_nick, True, (255, 255, 255))

        self.window.blit(surface_start_stop, (START_BUTTON))
        self.window.blit(surface_score, (SCORE))
        self.window.blit(surface_restart, (RESTART))
        self.window.blit(nick_surface, (PLAYER))