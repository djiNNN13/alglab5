import copy
MIN_EVAL = -2
MAX_EVAL = 2
class Minimax:


    # TODO: Check Winning Function
   def __minimax(grid, turn, depth, alpha, beta, is_maximizer):

    end_state = check_game_over(grid, turn)


    if end_state == NO_WIN:
        return end_state

    best_move = None
    best_evaluation = None

    if is_maximizer:
        best_evaluation = MIN_EVAL
    else:
        best_evaluation = MAX_EVAL

    for r,row in ipairs(grid):
        for c,cell in ipairs(row):
            if cell == EMPTY:
                new_grid = deep_copy_matrix(grid)
                place_marker(new_grid, turn, r, c)
                new_turn = switch_turn(turn)

                evaluation = minimax(new_grid, new_turn, depth + 1, alpha, beta, not is_maximizer)
                if is_maximizer and evaluation > best_evaluation:
                    best_evaluation = evaluation
                    best_move = {r, c}
                    
                    alpha = max(alpha, evaluation)
                    if alpha >= beta:
                    	break
                    return best_evaluation
                elif not is_maximizer and evaluation < best_evaluation:
                    best_evaluation = evaluation
                    best_move = {r, c}

                    beta = min(beta, evaluation)
                    if beta <= alpha:
                    	break
                    return best_evaluation
















def check_winning(self, or_board, empty): #check if the comp can win with a single move
        new_board = copy.deepcopy(or_board)
        print(len(empty))
        for cell in empty:
            print("check win")
            new_board.set_value(cell.get_line(), cell.get_column(), '0')
            if len(new_board.get_empty_cells()) == 0:
                return True, cell
        return False, None

def best_move(self, board, empty, depth):
        best_move_depth = depth
        winning_cell = None
        parsing_cell = None
        for cell in empty:
            new_board = copy.deepcopy(board)
            count, score = 0, 0
            while score==0:
                if count%2==0:
                    value = '0'
                else:
                    value = 'x'
                new_board.set_value(cell.get_value(), cell.get_column(), value)
                count+=1
                if len(new_board.get_empty_cells()) == 0:
                    if value == '0':
                        score = 10
                        parsing_cell = cell
                    else:
                        score = -10
                else:
                    cell = new_board.get_empty_cells()[0]
            if count<best_move_depth:
                winning_cell = parsing_cell
                best_move_depth = count
        if winning_cell is not None:
            return winning_cell
        else:
            return None

def minimax(self, board):
        original_board = copy.deepcopy(board) #original board
        empty = board.get_empty_cells() #list of empty cells
        depth = len(board.get_empty_cells()) #how many empty cells there are

        status, cell = self.check_winning(original_board , empty)
        if status is True:
            return cell.get_line(), cell.get_column()

        winning_cell = self.best_move(original_board , empty, depth)
        if winning_cell is not None:
            return winning_cell.get_line(), winning_cell.get_column(), original_board
        else:
            return empty[0].get_line(), empty[0].get_column()