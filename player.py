



class Player:

    def __init__(self,nick):

        self.nick = 'nick'
        self.score = 0
        self.log = ''
    # @property
    # def score(self):
    #     return self.score
    # @score.setter
    # def score(self,points):
    #     self._score = self._score + points
    # @score.getter
    # def score(self):
    #     return self._score


    def add_log(self,board):

        for row in board:
            for i in row:
                self.log += str(i)
        self.log += ';'
