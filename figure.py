class Figure:

    def falling(self):


        for i in self.box:
            if i[0] == 20:
                break
            else:
                for j in self.box:
                    j[0] = j[0] +1
                return self.box

        return self.box    


    def move_down(self,board):

        try:
            for i in self.box:
                if board[i[0] + 1,i[1]] not in (0,1) or board[i[0]+2,i[1]] not in (0,1):  
                    return self.box
        except IndexError:
            return self.box
            
        for j in self.box:
            j[0] = j[0] + 1
        return self.box       
        

    def move_left(self,board):

        for i in self.box:
            if board[i[0],i[1] - 1] not in (0,1):  
                return self.box
            
        for j in self.box:
            j[1] = j[1] - 1
        return self.box

    def move_right(self,board):


        for i in self.box:
            if board[i[0],i[1] + 1] not in (0,1):   
                return self.box
            
        for j in self.box:
            j[1] = j[1] + 1
        return self.box
    

    def pivot(self,base,board,possition):
        for i in base:
            if board[i[0],i[1]] not in (0,1) :
                return [self.box,self.box]
            
        mapping = {'up':'right','right':'down','down':'left','left':'up'}
        self.possition = mapping[possition]
        self.box,old_base = base,self.box
        figure = [self.box,old_base]
        return figure


class SquareBlock(Figure):

    block_id = 2
    color = (231, 54, 27 )

    def __init__(self):
        self.shape_1 = [1,5] 
        self.shape_2 = [1,6] 
        self.shape_3 = [2,5] 
        self.shape_4 = [2,6]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'

    def change_shape(self,board):
        figure = [self.box,self.box]
        return figure

class IBlock(Figure):

    block_id = 3
    color = (99, 225, 211)

    def __init__(self):
        self.shape_1 = [1,4] 
        self.shape_2 = [1,5] 
        self.shape_3 = [1,6] 
        self.shape_4 = [1,7]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'

    def change_shape(self,board):
        base = self.box.copy()
        pivot = base[1] 

        if self.possition == 'up' or self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0]+1,pivot[1]], [pivot[0]+2,pivot[1]]
            return self.pivot(base=base,board=board,possition=self.possition)
        
        if self.possition == 'right' or self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]-1], [pivot[0],pivot[1]+1], [pivot[0],pivot[1]+2]
            return self.pivot(base=base,board=board,possition=self.possition)

class ZBlock(Figure):

    block_id = 4
    color = (231, 27, 176 )
   
    def __init__(self):
        self.shape_1 = [1,4] 
        self.shape_2 = [1,5] 
        self.shape_3 = [2,5] 
        self.shape_4 = [2,6]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'
    
    def change_shape(self,board):
        base = self.box.copy()
        pivot = base[1]

        if self.possition == 'up' or self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0],pivot[1]-1], [pivot[0]+1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)
        
        if self.possition == 'right' or self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]-1], [pivot[0]+1,pivot[1]], [pivot[0]+1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)
        
class LBlock(Figure):

    block_id = 5
    color = (58, 231, 27 )

    def __init__(self):
        self.shape_1 = [1,6] 
        self.shape_2 = [1,5] 
        self.shape_3 = [1,4] 
        self.shape_4 = [2,4]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'


    def change_shape(self,board):

        base = self.box.copy()
        pivot = base[1]       

        if self.possition == 'up':
            base[0],base[2],base[3] = [pivot[0]+1,pivot[1]], [pivot[0]-1,pivot[1]], [pivot[0]-1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'right':
            base[0],base[2],base[3] = [pivot[0],pivot[1]-1], [pivot[0],pivot[1]+1], [pivot[0]-1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)
        
        if self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0]+1,pivot[1]], [pivot[0]+1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]+1], [pivot[0],pivot[1]-1], [pivot[0]+1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)
                
class JBlock(Figure):
    
    block_id = 6
    color = (228, 231, 27 )
        
    def __init__(self):
        self.shape_1 = [1,4] 
        self.shape_2 = [1,5] 
        self.shape_3 = [1,6] 
        self.shape_4 = [2,6]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'


    def change_shape(self,board):

        base = self.box.copy()
        pivot = base[1]       

        if self.possition == 'up':
            base[0],base[2],base[3] = [pivot[0]+1,pivot[1]], [pivot[0]-1,pivot[1]], [pivot[0]+1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'right':
            base[0],base[2],base[3] = [pivot[0],pivot[1]+1], [pivot[0],pivot[1]-1], [pivot[0]-1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)
        


        if self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0]+1,pivot[1]], [pivot[0]-1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]-1], [pivot[0],pivot[1]+1], [pivot[0]+1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)
                
class SBlock(Figure):

    block_id = 7
    color = (154, 243, 74 )
        
    def __init__(self):
        self.shape_1 = [1,5] 
        self.shape_2 = [1,6] 
        self.shape_3 = [2,4] 
        self.shape_4 = [2,5]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'

    def change_shape(self,board):
        base = self.box.copy()
        pivot = base[1]

        if self.possition == 'up' or self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0],pivot[1]+1], [pivot[0]+1,pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)
        
        if self.possition == 'right' or self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]+1], [pivot[0]+1,pivot[1]], [pivot[0]+1,pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)
        
class TBlock(Figure):

    block_id = 8
    color = (246, 138, 17 )

    def __init__(self):
        self.shape_1 = [1,4] 
        self.shape_2 = [1,5] 
        self.shape_3 = [1,6] 
        self.shape_4 = [2,5]
        self.box = [self.shape_1,self.shape_2,self.shape_3,self.shape_4] 
        self.possition = 'up'


    def change_shape(self,board):

        base = self.box.copy()
        pivot = base[1]       

        if self.possition == 'up':
            base[0],base[2],base[3] = [pivot[0]-1,pivot[1]], [pivot[0]+1,pivot[1]], [pivot[0],pivot[1]-1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'right':
            base[0],base[2],base[3] = [pivot[0],pivot[1]+1], [pivot[0],pivot[1]-1], [pivot[0]-1,pivot[1]]
            return self.pivot(base=base,board=board,possition=self.possition)
        


        if self.possition == 'down':
            base[0],base[2],base[3] = [pivot[0]+1,pivot[1]], [pivot[0]-1,pivot[1]], [pivot[0],pivot[1]+1]
            return self.pivot(base=base,board=board,possition=self.possition)

        if self.possition == 'left':
            base[0],base[2],base[3] = [pivot[0],pivot[1]-1], [pivot[0],pivot[1]+1], [pivot[0]+1,pivot[1]]
            return self.pivot(base=base,board=board,possition=self.possition)