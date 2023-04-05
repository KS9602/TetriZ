import numpy as np
from time import sleep

class Board:
    
    def __init__(self,x=20,y=12):

        self.board = np.zeros((x, y), dtype='O') 
        self.board[0],self.board[-1],self.board[:,0],self.board[:,-1] = 9,9,9,9

        self.new_row = np.array([[0 for i in range(y)]])
        self.new_row[0][0],self.new_row[0][-1] = 9,9

    def draw_falling(self,figure):

        for i in figure:
            self.board[i[0] -1,i[1]] = 0
        for i in figure:
            self.board[i[0],i[1]] = 1

    def freez_figure(self,figure,block_id):

        for i in figure:
            self.board[i[0] -1,i[1]] = 0
        for i in figure:
            self.board[i[0],i[1]] = block_id

    def draw_move_left(self,figure):

        for i in figure:
            self.board[i[0],i[1]+1] = 0
        for i in figure:
            self.board[i[0],i[1]] = 1

    def draw_move_right(self,figure):

        for i in figure:
            self.board[i[0],i[1]-1] = 0
        for i in figure:
            self.board[i[0],i[1]] = 1

    def draw_move_down(self,figure):

        for i in figure:
            self.board[i[0]-1,i[1]] = 0
        for i in figure:
            self.board[i[0],i[1]] = 1

    def draw_change(self,figure):
        
        for i in figure[1]:
            self.board[i[0],i[1]] = 0
        for i in figure[0]:
            self.board[i[0],i[1]] = 1



    def one_line_disapear(self,player):
        
 
        for e,row in enumerate(self.board):
            if 0 not in row and row[5] != 9:
                box_above = self.board[:e]
                new_above = np.concatenate((self.new_row,box_above))          ## sprawdzic czy mozna self.board[:e+1] = np.concatenate((self.new_row,box_above))  
                self.board[:e+1] = new_above
                player.score += 100
                









# sufit opada XDDD