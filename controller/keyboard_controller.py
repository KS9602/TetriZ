import pygame as pg
from controller.controller import Controller

class KeyboardController(Controller):
    def __init__(self,game) -> None:
        self.game = game

    def manage_event(self,event):

        if event.key == pg.K_BACKSPACE:
            self.game.player.nick = self.game.player.nick[:-1]
        elif len(self.game.player.nick) < 19:
                    self.game.player.nick += event.unicode

        if all((self.game.start_stop_flag == 2,self.game.game_over_flag == 0)):    
 
            if event.key == pg.K_LEFT:
                self.game.move_manager.draw_move_left(self.game.figure.move_left(self.game.board.board))
            elif event.key == pg.K_RIGHT:
                self.game.move_manager.draw_move_right(self.game.figure.move_right(self.game.board.board))
            elif event.key == pg.K_UP:
                self.game.move_manager.draw_change(self.game.figure.change_shape(self.game.board.board))
            elif event.key == pg.K_DOWN:
                self.game.move_manager.draw_move_down(self.game.figure.move_down(self.game.board.board)),












