import random
from ai_player import AI_Player
import time

class Minimax_AI_Player(AI_Player):
    """Findet den besten Zug via Rekursion"""

    def __init__(self, piece, depth=3):
        super().__init__(piece)
        self.depth = depth  # How many moves ahead to calculate

    def make_move(self, board):
        valid_columns = board.get_valid_columns()
        if not valid_columns:
            print("Es gibt keine möglichen Züge mehr!")
            return

        # Nutzt Minimax um den besten Zug zu finden
        best_col = self.minimax(board, self.depth, True)[0]
        board.drop_piece(best_col, self.piece)

    def minimax(self, board, depth, maximizing):
        """Rekursiver Minimax Algorithmus"""
        valid_columns = board.get_valid_columns()

        # Base Case: Stoppt wenn das Spiel vorbei ist oder Tiefe 0 erlangt wurde (rekursionsstopp)
        if depth == 0 or not valid_columns:
            return (None, self.evaluate_board(board))

        if maximizing:
            # Maximiert die Siegeschancen
            max_score = float('-inf')
            best_col = random.choice(valid_columns) #Random, um einen Wert zu haben. Dieser wird aber überschrieben

            for col in valid_columns:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.piece)
                score = self.minimax(temp_board, depth-1, False)[1]

                if score > max_score:
                    max_score = score
                    best_col = col

            return best_col, max_score

        else:
            # Minimiert die gegnerischen Siegeschancen
            min_score = float('inf')
            best_col = random.choice(valid_columns)
            opponent_piece = 'X' if self.piece == 'O' else 'O'

            for col in valid_columns:
                temp_board = board.copy()
                temp_board.drop_piece(col, opponent_piece)
                score = self.minimax(temp_board, depth-1, True)[1]

                if score < min_score:
                    min_score = score
                    best_col = col

            return best_col, min_score

    def evaluate_board(self, board):
        """Evaluiert nächsten Züge"""
        """Zahlen sind experimentell anpassbar"""

        AI = self.piece
        OPPONENT = 'X' if self.piece == 'O' else 'O'

        #Überprüft ob AI nächsten Zug gewinnen kann
        if board.check_win(AI):
            return 1000000
        elif board.check_win(OPPONENT):
            return -1000000

        #Checkt ob Gegner nach dem Zug eine direkt gewinnende Position hat
        for col in board.get_valid_columns():
            temp_board = board.copy()
            temp_board.drop_piece(col, OPPONENT)
            if temp_board.check_win(OPPONENT):
                return -900000

        #Berechnung der Stellung anhand von 2er und 3er Reihen
        temp = (board.check_3_in_row(AI) * 100) + (board.check_2_in_row(AI) * 10)
        temp -= (board.check_3_in_row(OPPONENT) * 90) + (board.check_2_in_row(OPPONENT) * 9)  #Blockieren ist weniger wichtig, sofern Gegner nicht gewinnen kann

        return temp


