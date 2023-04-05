class Player:

    """ Simple player class. Contains logger :)"""

    def __init__(self):

        self._nick = 'nick'
        self.score = 0
        self.log = ''

    def _clear(self):
        self._score = 0
        self.log = ''

    @property
    def nick(self):
        return self._nick
    @nick.getter
    def nick(self):
        return self._nick
    @nick.setter
    def nick(self,value): 

        if isinstance(value,str):
            self._nick = value
        else:
            raise TypeError 

    def add_log(self,board):

        for row in board:
            for i in row:
                self.log += str(i)
        self.log += ';'
