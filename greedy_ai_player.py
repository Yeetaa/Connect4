import random

import board
from ai_player import AI_Player

class Greedy_AI_Player(AI_Player):

    #So wie Random AI, spielt aber auf Win und Block sofern möglich

    def __init__(self, piece):
        super().__init__(piece)

    def simulate_move(self, board, col, piece):
        """Simuliert Zug mit Hilfe von kopiertem Board"""
        temp_board = board.copy()  # Make a copy of the board
        temp_board.drop_piece(col, piece)  # Simulate the move
        return temp_board

    def make_move(self, board):

        valid_columns = board.get_valid_columns()
        if not valid_columns:
            print(f"Es gibt keine möglichen Züge mehr!")

            # 1. AI überprüft Instant-Win
        for col in valid_columns:
            temp_board = self.simulate_move(board, col, self.piece)
            #Simuliert den Zug auf einem kopierten Board
            #Geht jede Spalte einmal durch
            if temp_board.check_win(self.piece):
                self.drop_piece(col, self.piece)
                print(f"AI hat gewonnen!")
                return

            # 2. AI überprüft Block-Chancen
        opponent_piece = 'X' if self.piece == 'O' else 'O'
        for col in valid_columns:
            temp_board = self.simulate_move(board, col, opponent_piece)
            #Simuliert den Zug auf einem kopierten Board
            #Geht jede Spalte einmal durch
            if temp_board.check_win(opponent_piece):
                self.drop_piece(col, self.piece)
                return

        # 3. Spielt random
        col = random.choice(valid_columns)
        self.drop_piece(col, self.piece)


    def drop_piece(self, col, piece):
        '''Um Ins Log einzutragen'''
        self.append_to_log(col)
        board.drop_piece(col, piece)