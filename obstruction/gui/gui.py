import tkinter
from tkinter import Button


class Gui:
    #TODO: GUI prettier
    def __init__(self, master, game):
        self.master = master
        self.game = game
        master.title("OBSTRUCTION")
        self.start()

    def start(self):
        """
        Our board consists of buttons. When we click on a button, a specific
        function is called and is given as parameters the row and column
        of the button.
        """
        rows = self.game.board.get_lines()
        columns = self.game.board.get_columns()
        self.buttons = []
        for row in range(rows):
            button_row=[]
            for column in range(columns):
                button = Button(self.master, text="  ", bg='green', command = lambda x=row, y=column:
                                self.send_param(x, y))
                button.grid(row=row, column=column)
                button_row.append(button)
            self.buttons.append(button_row)

    def send_param(self, x, y):
        """
        This buttons receive as parameters the line and column of the cell
        the computer or used placed its move. Will switch the buttons in
        the gui accordingly.
        """
        lst1=self.game.player_move(self.game.p1, x, y)
        game_status, winner = self.game.is_over()
        if game_status is True: #checks for game over
            self.finish_frame(winner)
        lst2=self.game.computer_move(self.game.p2)
        game_status, winner = self.game.is_over()
        if game_status is True:
            self.finish_frame(winner)
        else:
            self.buttons[lst1[0]][lst1[1]]["text"] = "x"
            self.buttons[lst1[0]][lst1[1]]["bg"] = "red"
            for i, j in lst1[2]:
                self.buttons[i][j]["bg"]='white'
            self.buttons[lst2[0]][lst2[1]]["text"] = "0"
            self.buttons[lst2[0]][lst2[1]]["bg"] = "red"
            for i, j in lst2[2]:
                self.buttons[i][j]["bg"] = 'white'

    def finish_frame(self, winner):
        """
        If the game is over, the game frame is destroyed and another one appears
        with a specific message (depending on who won, user or computer)
        """
        self.master.destroy()
        window = tkinter.Tk()
        window.title("Game Over")
        if winner == "x":
            text = "You won. GG, WP!"
        else:
            text = "Computer won. Loser!"
        label = tkinter.Label(window, text = text)
        label.grid()
        window.mainloop()
