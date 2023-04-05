import pygame as pg
import json
from sys import exit
from figure import SquareBlock,SBlock,ZBlock,LBlock,JBlock,IBlock,TBlock
from board import Board
from random import choice
from player import Player


class Game:

    board = Board()
    BLOCKS = [SquareBlock,SBlock,ZBlock,LBlock,JBlock,IBlock,TBlock]

    vec_menu = pg.math.Vector2(390,1)
    MENU = pg.Rect(vec_menu.x,vec_menu.y,320,640) 
    START_BUTTON = pg.Rect(vec_menu.x + 10,vec_menu.y + 10,300,54)
    RESTART = pg.Rect(vec_menu.x + 10, vec_menu.y + 80, 300,54)
    SCORE = pg.Rect(vec_menu.x + 10, vec_menu.y + 140, 300,60)
    PLAYER = pg.Rect(vec_menu.x + 10, vec_menu.y + 210, 300,44)
    PLAYER_COLOR = {1:(70,150,111),2:(190,22,200)}
    

    def __init__(self):
        pg.init()
        pg.display.set_caption('TetriZ')
        self.window = pg.display.set_mode((720,650))
        self.clock = pg.time.Clock()
        self.delta_fall = 0.0
        self.start_stop_flag = 1
        self.color_flag = 1
        self.player = Player('')
        self.game_over = 0
        self.font = pg.font.Font(None,80)
        self.nick_font = pg.font.Font(None,40)

        while True:
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                try:
                    if event.type == pg.QUIT: 
                        pg.quit()
                        exit() 
                    if event.type == pg.KEYDOWN and event.key == pg.K_LEFT and self.game_over == 0:
                        Game.board.draw_move_left(self.figure.move_left(Game.board.board))
                    if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and self.game_over == 0:
                        Game.board.draw_move_right(self.figure.move_right(Game.board.board))   
                    if event.type == pg.KEYDOWN and event.key == pg.K_UP and self.game_over == 0:
                        Game.board.draw_change(self.figure.change_shape(Game.board.board)) 
                    if event.type == pg.KEYDOWN and event.key == pg.K_DOWN and self.game_over == 0:
                        Game.board.draw_move_down(self.figure.move_down(Game.board.board))
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.START_BUTTON.collidepoint(pos):
                        self.start_stop_flag = self.start_stop_flag % 2 + 1
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.PLAYER.collidepoint(pos):
                        self.color_flag = self.color_flag % 2 + 1
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and Game.RESTART.collidepoint(pos):
                        self.start_stop_flag = 1
                        Game.board = Board()
                        self.player.score = 0
                        self.player.log = ''
                    if event.type == pg.KEYDOWN :
                        if event.key == pg.K_BACKSPACE:
                            self.player.nick = self.player.nick[:-1]
                        else:
                            if len(self.player.nick) < 19:
                                self.player.nick += event.unicode
                except (UnboundLocalError,AttributeError):
                    pass

            if self.start_stop_flag != 1 and self.game_over == 0:
                self.delta_fall  += self.clock.tick() / 1000
                while self.delta_fall > 0.5 and self.game_over == 0:
                    self.player.add_log(Game.board.board)

                    if 1 not in Game.board.board:
                        block = choice(Game.BLOCKS)
                        self.figure = block()

                        for i in self.figure.box:
                            if Game.board.board[i[0]+1,i[1]] not in (0,1) :
                                self.game_over = 1                      # gameover
                                self.api_send()

                        for i in self.figure.box:
                            Game.board.board[i[0],i[1]] = 1
                        self.delta_fall = 0.0
                        self.player.score += 10
                    else :
                        cords = self.figure.falling()
                        Game.fall_checking(self,cords=cords)

            self.drow_boxes()
            self.draw_menu()
            pg.display.flip()

    def drow_boxes(self):
        """rysuje bloki. 1 = zamrozone bloki 2 = lecace blocki 0 = przestrzec 9 = ramka"""
        vec = pg.math.Vector2(100,100)

        for row_en,row in enumerate(self.board.board):
            for pos_en,i in enumerate(row):

                vec.x = 32 * pos_en
                vec.y = 32 * row_en
                rect = pg.Rect(vec.x,vec.y,30,30)
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
        status = {1:'    START',2:'    STOP'}


        surface_start_stop = self.font.render(f'{status[self.start_stop_flag]}',True,'white')
        surface_score = self.font.render(f'P: {self.player.score}',True,'white')
        surface_restart = self.font.render('RESTART',True,'white')

        self.window.blit(surface_start_stop,(Game.START_BUTTON))
        self.window.blit(surface_score,(Game.SCORE))
        self.window.blit(surface_restart,(Game.RESTART))

        nick_surface = self.nick_font.render(self.player.nick,True,(255,255,255))
        self.window.blit(nick_surface,Game.PLAYER)

    def fall_checking(self,cords):
        """ metoda do sprawdzenia czy klocek moze dalej opadac. jesli po klockiem jest 1 to znaczy ze ma sie zatrzymac.
            jesli w rzedzie sa same jedynki odpala sie funkcja ktora czysci wiersz"""

        for i in cords:
            if Game.board.board[i[0]+1,i[1]] not in (0,1):
                Game.board.freez_figure(cords,self.figure.block_id)
                Game.board.one_line_disapear(self.player)
                return 

        Game.board.draw_falling(cords)
        self.delta_fall = 0.0


    def api_send(self):
        
        pack = {'player':self.player.nick,'score':str(self.player.score),'log':self.player.log}
        json_object = json.dumps(pack)
   

if __name__ == '__main__':
    Game()

