from board.cell import Cell


class GuiBoard:
    def __init__(self, lines, columns, empty_value = '-'):
        self.__lines = lines
        self.__columns = columns
        self.__empty_value = empty_value
        self.__cells = self.__create_board()

    def get_lines(self):
        return self.__lines

    def get_columns(self):
        return self.__columns

    def get_empty_value(self):
        return self.__empty_value

    def __create_board(self):
        board = []
        for i in range(self.get_lines()):
            board_rows = []
            for j in range(self.get_columns()):
                board_rows.append(self.get_empty_value())
            board.append(board_rows)
        return board

    def get_all_cells(self):
        cells = []
        for i in range(self.__lines):
            for j in range(self.__columns):
                cells.append(Cell(i, j, self.__cells[i][j]))
        return cells

    def check_cell(self, cell):
        l = cell.get_line()
        c = cell.get_column()
        if self.__cells[l][c] == self.__empty_value:
            return True
        if self.__cells[l][c] == '/':
            return True
        return False

    def check_surrounding(self, cell):
        """
        Checks if the surrounding cells of a cell are taken
        :param cell:
        :return: true of false
        """
        surr = lambda x, y: [[a, b] for a in range(x-1, x+2)
                                    for b in range (y-1, y+2)
                                    if (-1 < a < self.__lines and
                                        -1 < b < self.__columns and
                                        (x != a or y != b))]
        lst = list(surr(cell.get_line(), cell.get_column()))
        for element in lst:
            if self.__cells[element[0]][element[1]] == 'x':
                return False
            if self.__cells[element[0]][element[1]] == '0':
                return False
        return lst

    def set_value(self, line, column, value):

        self.__cells[line][column] = value

        if line == 0 and column!=0 and column!=self.__columns-1:
            self.__cells[line + 1][column] = '/'
            self.__cells[line + 1][column + 1] = '/'
            self.__cells[line + 1][column - 1] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line][column - 1] = '/'
        elif line == 0 and column == 0:
                self.__cells[line + 1][column] = '/'
                self.__cells[line + 1][column + 1] = '/'
                self.__cells[line][column + 1] = '/'
        elif line == 0 and column==self.__columns-1:
            self.__cells[line + 1][column] = '/'
            self.__cells[line + 1][column - 1] = '/'
            self.__cells[line][column - 1] = '/'
        else:
            pass

        if line == self.__lines-1 and column!=0 and column!=self.__columns-1:
            self.__cells[line][column + 1] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line - 1][column + 1] = '/'
            self.__cells[line - 1][column - 1] = '/'
            self.__cells[line - 1][column] = '/'
        elif line == self.__lines-1 and column==0 :
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line - 1][column + 1] = '/'
        elif line == self.__lines-1 and column==self.__columns-1:
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line - 1][column - 1] = '/'
        else:
            pass


        if column == 0 and line!=0 and line!=self.__lines-1:
            self.__cells[line + 1][column] = '/'
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line + 1][column + 1] = '/'
            self.__cells[line - 1][column + 1] = '/'
        elif column == 0 and line==0:
            self.__cells[line + 1][column] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line + 1][column + 1] = '/'
        elif column == 0 and line==self.__lines-1:
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line - 1][column + 1] = '/'
        else:
            pass

        if column == self.__columns-1 and line != 0 and line != self.__lines-1:
            self.__cells[line + 1][column] = '/'
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line + 1][column - 1] = '/'
            self.__cells[line - 1][column - 1] = '/'
        elif column == self.__columns-1 and line == 0:
            self.__cells[line + 1][column] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line + 1][column - 1] = '/'
        elif column == self.__columns-1 and line == self.__lines-1:
            self.__cells[line - 1][column] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line - 1][column - 1] = '/'
        else:
            pass

        if line!=0 and line!=self.__lines-1 and column!=0 and column!=self.__columns-1:
            self.__cells[line+1][column] = '/'
            self.__cells[line-1][column] = '/'
            self.__cells[line][column + 1] = '/'
            self.__cells[line][column - 1] = '/'
            self.__cells[line+1][column+1] = '/'
            self.__cells[line+1][column-1] = '/'
            self.__cells[line-1][column+1] = '/'
            self.__cells[line-1][column-1] = '/'


    def get_empty_cells(self):
        return [cell for cell in self.get_all_cells()
                if cell.get_value() == self.__empty_value]

    def __str__(self):
        p = ""
        for line in self.__cells:
            s = " ".join([str(value) for value in line])+'\n'
            p += s
        return p