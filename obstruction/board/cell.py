class Cell:
    def __init__(self, line, column, value):
        self.__line = line
        self.__column = column
        self.__value = value

    def get_line(self):
        return self.__line

    def get_column(self):
        return self.__column

    def get_value(self):
        return self.__value

