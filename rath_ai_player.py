import random
from ai_player import *


class Rath_AI_Player(AI_Player):
    def __init__(self, piece):
        super().__init__(piece)


    def make_move(self, board):

        valid_columns = board.get_valid_columns()
        if not valid_columns:
            print(f"Es gibt keine möglichen Züge mehr!")

        for col in valid_columns:
            temp_board = self.simulate_move(board, col, self.piece)
            #Simuliert den Zug auf einem kopierten Board
            #Geht jede Spalte einmal durch
            if temp_board:
                board.drop_piece(col, self.piece)
        col = random.choice(valid_columns)
        board.drop_piece(col, self.piece)







    def simulate_move(self, board, col, piece):
        """Simuliert Zug mit Hilfe von kopiertem Board"""
        temp_board = board.copy()  # Kopiert Board
        temp_board.drop_piece(col, piece)  # Simuliert den Move
        if temp_board.check_win(self.piece):
            return True
        else:
            opponent_piece = 'X' if self.piece == 'O' else 'O'
            temp_board.remove_last_piece()
            temp_board.drop_piece(col, opponent_piece)
            if temp_board.check_win(opponent_piece):
                return True
            else:
                return False
            #Baisicly Greedy





