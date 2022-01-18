

from board.cell import Cell


class Board:
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
        #Will return a list of cell objects
        cells = []
        for i in range(self.__lines):
            for j in range(self.__columns):
                cells.append(Cell(i, j, self.__cells[i][j]))
        return cells

    def get_cell(self, line, column):
        #returns a cell object specified by line and column
        return Cell(line, column, self.__cells[line][column])

    def check_cell(self, cell):
        #check if the cells is occupied by anything except the empty value or '/'
        #'/' means that a cell is blocked since we placed something near it
        l = cell.get_line()
        c = cell.get_column()
        if self.__cells[l][c] == self.__empty_value:
            return True
        if self.__cells[l][c] == '/':
            return True
        return False

    def check_surrounding(self, cell):
        """
        Checks if the surrounding cells of a cell are taken and returns a list
        of lists...every sublist contains the line of column of every surrounding
        cell (of the specific cell the function receives as a parameter)
        :param cell:
        :return: false(if occupied) or a list of lists if  not
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
        """
        We set a specific cell to a certain value and also, we block its surrounding
        cells by setting their value to '/'. With a series of if_else, we check if the
        cell we want to modify is not placed on a margin or 2.
        """

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
        "return a list of cells objects that are not occupied or blocked"
        return [cell for cell in self.get_all_cells()
                if cell.get_value() == self.__empty_value]

    def __str__(self):
        # t = Texttable()
        # res = []
        # for line in range(self.__lines):
        #     res.append(self.__cells[line][:])
        #     for column in range(self.__columns):
        #         res[line][column] = self.__cells[line][column]
        # for row in res:
        #     t.add_row(row)
        # return t.draw()

        p = ""
        for line in self.__cells:
            s = " ".join([str(value) for value in line])+'\n'
            p += s
        return p