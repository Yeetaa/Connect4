import random
from ai_player import AI_Player

class Random_AI_Player(AI_Player):

    def __init__(self, piece):
        super().__init__(piece)

    def make_move(self, board):
        col = random.choice(board.get_valid_columns())
        board.drop_piece(col, self.piece)
        print(f"Random AI placed in Spalte {col}")
