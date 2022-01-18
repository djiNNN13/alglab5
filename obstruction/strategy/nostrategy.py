from board.cell import Cell


class NoStrategy:

    def move(self, board, value):
        """
        Empty is a list of empty cell and the computer will place its move on
        the first empty cell we find. We return as usually the cell, its line
        and column and of list of lists(containing the lines and columns of the
        surrounding cells)
        """
        empty = board.get_empty_cells() #gets a list of cell objects
        if len(empty) == 0:
            return None #if the list is empty, there are no cells left => Game over
        for cell in empty:
            if len(board.check_surrounding(cell))!=0:
                board.set_value(cell.get_line(), cell.get_column(), value)
                cell = Cell(cell.get_line(), cell.get_column(), value)
                lst = board.check_surrounding(cell)
                return [cell, cell.get_line(), cell.get_column(), lst]
        return None