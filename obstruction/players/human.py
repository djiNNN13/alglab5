from board.cell import Cell
from players.player import Player


class Human(Player):

    def move (self, l, c, value):
        line, column = self.validate_move(l, c, value)
        self.board.set_value(line, column, value)
        cell = Cell(line, column, value)
        lst = self.board.check_surrounding(cell)
        return [cell, cell.get_line(), cell.get_column(), lst]

    def validate_move(self, l, c, value):
        if l < 0:
            raise ValueError("index out of range")
        if l >= self.board.get_lines():
            raise ValueError("index out of range")
        if c < 0:
            raise ValueError("index out of range")
        if c >= self.board.get_columns():
            raise ValueError("index out of range")
        line = int(l)
        column = int(c)
        if self.board.check_cell(Cell(line, column, value)) is False:
            raise ValueError('try again')
        if self.board.check_surrounding(Cell(line, column, value)) is False:
            raise ValueError('try again')
        return line, column