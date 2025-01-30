import random
from ai_player import AI_Player

class Random_AI_Player(AI_Player):

    def __init__(self, piece):
        super().__init__(piece)

    def make_move(self, board):
        valid_columns = board.get_valid_columns()  # Get available columns

        if not valid_columns:  # Crashvorbeugung bei keinen möglichen Spalten
            print("Ai hat keine Züge mehr!")
            return False

        col = random.choice(valid_columns)  # Pick a random valid column
        board.drop_piece(col, self.piece)
        print(f"Random AI placed in Spalte {col}")
