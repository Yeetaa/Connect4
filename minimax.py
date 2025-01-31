import random
from ai_player import AI_Player

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
            best_col = random.choice(valid_columns) #Random falls es keinen guten Zug gibt

            for col in valid_columns:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.piece)
                score = self.minimax(temp_board, depth-1, False)[1]

                if score > max_score:
                    max_score = score
                    best_col = col

            return best_col, max_score

        else:
            # Minimiert den gegnerischen besten Zug
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
        """Assigns a score based on AI's advantage."""
        if board.check_win(self.piece):
            return 1000  # AI gewinnt
        elif board.check_win('X' if self.piece == 'O' else 'O'):
            return -1000  # Gegner gewinnt
        else:
            return random.randint(-10, 10)  # Evaluation TBD

