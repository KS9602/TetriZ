import pygame as pg
import json
from sys import exit
from random import choice
import requests

from figure import SquareBlock,SBlock,ZBlock,LBlock,JBlock,IBlock,TBlock
from board import Board
from player import Player

class Game:

    """TetriZ main class. Class attributes create board object, blocks class list, vectors and rectangle objects"""

    board = Board()
    BLOCKS = [SquareBlock,SBlock,ZBlock,LBlock,JBlock,IBlock,TBlock]

    GAME_VEC = pg.math.Vector2(100,100)
    VECTOR_MENU = pg.math.Vector2(390,1)
    MENU = pg.Rect(VECTOR_MENU.x,VECTOR_MENU.y,320,640) 
    START_BUTTON = pg.Rect(VECTOR_MENU.x + 10,VECTOR_MENU.y + 10,300,54)
    RESTART = pg.Rect(VECTOR_MENU.x + 10, VECTOR_MENU.y + 80, 300,54)
    SCORE = pg.Rect(VECTOR_MENU.x + 10, VECTOR_MENU.y + 140, 300,60)
    PLAYER = pg.Rect(VECTOR_MENU.x + 10, VECTOR_MENU.y + 210, 300,44)
    SEND = pg.Rect(VECTOR_MENU.x + 10, VECTOR_MENU.y + 290, 300,44)
    PLAYER_COLOR = {1:(70,150,111),2:(190,22,200)}
    
    def __init__(self):

        """Init create basic pygame objects, player object, flags and starts game main loop.
        Loop contains control system (keyboard and mouse), second loop and methods that draw graphic.
        The second loop run evry second if game isn't stopped/over. Loop runs logger method and checked
        whether '1' is on board, which means falling block is in game. If not, program choice class from class
        attribute and create new figure object(else figure is falling). 
        Then board is checked whether at the 'zero' point is space required
        for draw block. If not, game is over, else figure starts falling  """

        pg.init()
        pg.display.set_caption('TetriZ')
        self.window = pg.display.set_mode((720,650))
        self.player = Player()

        self.clock = pg.time.Clock()
        self.delta_fall = 0.0

        self.font = pg.font.Font(None,80)
        self.nick_font = pg.font.Font(None,40)

        self.game_over_flag = 0
        self.start_stop_flag = 1
        self.color_flag = 1
        self.api_flag = 0

        while True:
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                try:
                    if event.type == pg.QUIT: 
                        pg.quit()
                        exit() 
                    if event.type == pg.KEYDOWN and event.key == pg.K_LEFT and self.start_stop_flag == 2 and self.game_over_flag == 0:
                        Game.board.draw_move_left(self.figure.move_left(Game.board.board))
                    if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and self.start_stop_flag == 2 and self.game_over_flag == 0:
                        Game.board.draw_move_right(self.figure.move_right(Game.board.board))   
                    if event.type == pg.KEYDOWN and event.key == pg.K_UP and self.start_stop_flag == 2 and self.game_over_flag == 0:
                        Game.board.draw_change(self.figure.change_shape(Game.board.board)) 
                    if event.type == pg.KEYDOWN and event.key == pg.K_DOWN and self.start_stop_flag == 2 and self.game_over_flag == 0:
                        Game.board.draw_move_down(self.figure.move_down(Game.board.board))
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.START_BUTTON.collidepoint(pos):
                        self.start_stop_flag = self.start_stop_flag % 2 + 1
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.PLAYER.collidepoint(pos):
                        self.color_flag = self.color_flag % 2 + 1
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.RESTART.collidepoint(pos):
                        self.start_stop_flag = 1
                        Game.board = Board()
                        self.player._clear()
                        self.figure = None
                    if event.type == pg.KEYDOWN :
                        if event.key == pg.K_BACKSPACE:
                            self.player.nick = self.player.nick[:-1]
                        else:
                            if len(self.player.nick) < 19:
                                self.player.nick += event.unicode
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.SEND.collidepoint(pos) and self.api_flag == 1:
                        self.api_send()
                        self.api_flag = 0

                except (UnboundLocalError,AttributeError):
                    pass

            if self.start_stop_flag != 1 and self.game_over_flag == 0:
                self.delta_fall  += self.clock.tick() / 1000
                while self.delta_fall > 0.25 and self.game_over_flag == 0:

                    self.player.add_log(Game.board.board)
                    if 1 not in Game.board.board:
                        block = choice(Game.BLOCKS)
                        self.figure = block()

                        for i in self.figure.box:
                            if Game.board.board[i[0]+1,i[1]] not in (0,1) :
                                self.game_over_flag = 1                      # gameover
                                self.api_flag = 1

                        for i in self.figure.box:
                            Game.board.board[i[0],i[1]] = 1
                        self.delta_fall = 0.0
                        self.player.score += 10
                    else :
                        cords = self.figure.falling(Game.board.board)
                        Game.fall_checking(self,cords=cords)

            self.draw_boxes()
            self.draw_menu()
            pg.display.flip()

    def draw_boxes(self):
        """Draw boxes mathod based on board object. 0 - empyt space, 1 - falling figure ,
          2-8 individual color of figure, 9 - frame"""

        for row_en,row in enumerate(self.board.board):
            for pos_en,i in enumerate(row):

                Game.GAME_VEC.x = 32 * pos_en
                Game.GAME_VEC.y = 32 * row_en
                rect = pg.Rect(Game.GAME_VEC.x,Game.GAME_VEC.y,30,30)

                if i == 1:                            
                    pg.draw.rect(self.window,self.figure.color,rect,0,5)
                elif i == 9:
                    pg.draw.rect(self.window,(150,0,255),rect,0,5)
                elif i == 0:
                    pg.draw.rect(self.window,(255,255,255),rect,0,5)
                else:
                    for block in Game.BLOCKS:
                        if i == block.block_id:
                            pg.draw.rect(self.window,block.color,rect,0,5)

    def draw_menu(self):
        
        pg.draw.rect(self.window,(200,200,200),Game.MENU,0)
        pg.draw.rect(self.window,(100,100,200),Game.START_BUTTON,0)
        pg.draw.rect(self.window,Game.PLAYER_COLOR[self.color_flag],Game.PLAYER,0)
        pg.draw.rect(self.window,(200,100,200),Game.SCORE,0)
        pg.draw.rect(self.window,(250,80,120),Game.RESTART,0)
        pg.draw.rect(self.window,(250,80,120),Game.SEND,0)
        status = {1:'    START',2:'    STOP'}

        surface_start_stop = self.font.render(f'{status[self.start_stop_flag]}',True,'white')
        surface_score = self.font.render(f'P: {self.player.score}',True,'white')
        surface_restart = self.font.render('RESTART',True,'white')
        nick_surface = self.nick_font.render(self.player.nick,True,(255,255,255))
        surface_send = self.nick_font.render('wyslij wynik',True,'white')

        self.window.blit(surface_start_stop,(Game.START_BUTTON))
        self.window.blit(surface_score,(Game.SCORE))
        self.window.blit(surface_restart,(Game.RESTART))
        self.window.blit(surface_send,(Game.SEND))
        self.window.blit(nick_surface,(Game.PLAYER))

    def fall_checking(self,cords):
        """ Fall_checking method checks whether figure can continue to fall (if block below is not fall figure or free space,
        it cant). Then figure is freezed and if blocks create line on all row, row disapear. """

        for i in cords:
            if Game.board.board[i[0],i[1]] not in (0,1):
                Game.board.freez_figure(cords,self.figure.block_id)
                Game.board.one_line_disapear(self.player)
                return 

        Game.board.draw_falling(cords)
        self.delta_fall = 0.0

    def send_log():
        """placeholder"""
        pass

if __name__ == '__main__':
    Game()

