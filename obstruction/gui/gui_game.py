from gui.gui import Gui


class GuiGame:
    def __init__(self, p1, p2, board):
        self.p1 = p1
        self.p2 = p2
        self.board = board
        self.__last_move = None

    def player_move(self, player, x, y):
        #the move to be made by the player, constantly checks if game over
        if len(self.board.get_empty_cells()) != 0:
            lst = player.move(x, y, 'x')
            self.__last_move = lst[0]
            game_status, winner_value = self.is_over()
            if game_status is True:
                self.__game_over(winner_value)
            return lst[1:]

    def computer_move(self, player):
        #the move to be made by the user, constantly checks if game over
        if len(self.board.get_empty_cells()) != 0:
            if self.__last_move.get_value() == 'x':
                lst = player.move(-1, -1, '0')
                self.__last_move = lst[0]
            game_status, winner_value = self.is_over()
            if game_status is True:
                self.__game_over(winner_value)
            return lst[1:]

    def is_over(self):
        if len(self.board.get_empty_cells()) == 0:
            return True, self.__last_move.get_value()
        return False, self.__last_move.get_value()

    def __game_over(self, winner_value):
        pass
