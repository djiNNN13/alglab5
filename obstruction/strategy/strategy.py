from board.cell import Cell


class Strategy:

    def move(self, board, value):
        """
        Empty is a list of empty cells. The strategy consists in the fact
        that the computer isn't placing its move on the first empty cell he finds,
        but instead, he places his move on the cell that will block the most
        surrounding cells. We return as usually the cell, its line
        and column and of list of lists(containing the lines and columns of the
        surrounding cells)
        """
        empty = board.get_empty_cells()
        if len(empty) == 0:
            return None
        max_surr = 0
        index_max = 0
        for index in range(len(empty)):
            l = len(board.check_surrounding(empty[index]))
            #l gets how many surrounding cells that specific cell has
            if l != 0: #simple algorithm for computing the max
                if l>max_surr:
                    index_max = index
                    max_surr = l
        if max_surr!=0: #we place the computer of the cell with the max l
            board.set_value(empty[index_max].get_line(), empty[index_max].get_column(), value)
            cell = Cell(empty[index_max].get_line(), empty[index_max].get_column(), value)
            lst = board.check_surrounding(cell)
            return [cell, cell.get_line(), cell.get_column(), lst]
        else:
            return None