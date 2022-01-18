from board.cell import Cell
from players.player import Player


class GuiHuman(Player):

    def move (self, l, c, value):
        self.validate_move(l, c, value)
        self.board.set_value(l, c, value)
        cell = Cell(l, c, value)
        lst = self.board.check_surrounding(cell)
        return [cell, cell.get_line(), cell.get_column(), lst]

    def validate_move(self, line, column, value):
        if self.board.check_cell(Cell(line, column, value)) is False:
            raise ValueError('try again')
        if self.board.check_surrounding(Cell(line, column, value)) is False:
            raise ValueError('try again')