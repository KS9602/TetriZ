import pygame as pg
from controller.controller import Controller
from constants import START_BUTTON,RESTART,PLAYER
from board.board import Board


class MouseController(Controller):
    def __init__(self,game) -> None:
        self.game = game
        self.key_mapp = None
        self.buttons = (START_BUTTON,RESTART,PLAYER)

    def manage_event(self,event):
        if event.button == 1:
            self.left_click()
        elif event.button == 2:
            self.right_click()

    def left_click(self):
        pos = pg.mouse.get_pos()
        if START_BUTTON.collidepoint(pos):
            self.game.start_stop_flag = self.game.start_stop_flag % 2 + 1
        elif PLAYER.collidepoint(pos):
            self.game.color_flag = self.game.color_flag % 2 + 1
        elif RESTART.collidepoint(pos):
            self.game.start_stop_flag=1
            self.game.board = Board()
            self.game.figure = None
            self.game.logger.clear()


    def right_click(self):
        pass
