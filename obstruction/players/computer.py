from board.cell import Cell
from players.player import Player


class Computer(Player):
    def __init__(self, name, board, strategy):
        super().__init__(name, board)
        self.__strategy = strategy
        self.count=0

    def move(self, line, column, value):
        if line==-1 and column==-1:
            return self.__strategy.move(self.board, value)
        else:
            self.board.set_value(line, column, value)
            cell = Cell(line, column, value)
            lst = self.board.check_surrounding(cell)
            return [cell, cell.get_line(), cell.get_column(), lst]
