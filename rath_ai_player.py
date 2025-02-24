import random

import game_board
from ai_player import *


class Rath_AI_Player(AI_Player):
    def __init__(self, piece):
        super().__init__(piece)

    def make_move(self, board):
        valid_columns = board.get_valid_columns()
        if not valid_columns:
            print("Es gibt keine möglichen Züge mehr!")
            return

        #Nutzt Minimax, um den besten Zug zu finden
        best_col, _ = self.rath_minimax(board, 5, float('-inf'), float('inf'), True)  #Rückgabe von (best_col, eval)
        self.append_to_log(best_col)
        board.drop_piece(best_col, self.piece)

    def rath_minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.check_win(self.piece) or board.check_win(self.opponent_piece):
            return None, self.static_evaluation(board)  #Rückgabe von (None, eval)

        valid_columns = board.get_valid_columns()
        if maximizing_player:
            maxEval = float('-inf')
            best_col = valid_columns[0]  #Standardwert, falls keine gültigen Züge
            for col in valid_columns:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.piece)
                _, eval = self.rath_minimax(temp_board, depth - 1, alpha, beta, False)  #Rückgabe von (best_col, eval)
                if eval > maxEval:
                    maxEval = eval
                    best_col = col
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return best_col, maxEval  #Rückgabe von (best_col, maxEval)

        else:
            minEval = float('inf')
            best_col = valid_columns[0]  #Standardwert, falls keine gültigen Züge
            for col in valid_columns:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.opponent_piece)  #Gegnerzug simuliert
                _, eval = self.rath_minimax(temp_board, depth - 1, alpha, beta, True)  #Rückgabe von (best_col, eval)
                if eval < minEval:
                    minEval = eval
                    best_col = col
                beta = min(beta, eval)  #Beta wird geupdated
                if beta <= alpha:
                    break
            return best_col, minEval  #Rückgabe von (best_col, minEval)

    def static_evaluation(self, board):
        if board.check_win(self.piece):
            return 1000000

        if board.check_win(self.opponent_piece):
            return -1000000

        eval = board.check_3_in_row(self.piece) + board.check_2_in_row(self.piece)
        eval -= board.check_3_in_row(self.opponent_piece) + board.check_2_in_row(self.opponent_piece)
        return eval