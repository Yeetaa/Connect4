import random
from ai_player import AI_Player

class Greedy_AI_Player(AI_Player):

    #So wie Random AI, spielt aber auf Win und Block sofern möglich

    def __init__(self, piece):
        super().__init__(piece)

    def make_move(self, board):

        valid_columns = board.valid_columns
        if not valid_columns:
            print(f"Es gibt keine möglichen Züge mehr!")

            # 1. AI überprüft Instant-Win
        for col in valid_columns:
            temp_board = self.simulate_move(board, col, self.piece)
            #Simuliert den Zug auf einem kopierten Board
            #Geht jede Spalte einmal durch
            if temp_board.check_win(self.piece):
                board.drop_piece(col, self.piece)
                print(f"AI hat gewonnen!")
                return

            # 2. AI überprüft Block-Chancen
        opponent_piece = 'X' if self.piece == 'O' else 'O'
        for col in valid_columns:
            temp_board = self.simulate_move(board, col, opponent_piece)
            #Simuliert den Zug auf einem kopierten Board
            #Geht jede Spalte einmal durch
            if temp_board.check_win(opponent_piece):
                board.drop_piece(col, self.piece)
                return

        # 3. Spielt random
        col = random.choice(valid_columns)
        board.drop_piece(col, self.piece)
        print(f"🤖 AI (Greedy) placed at column {col}")


def simulate_move(self, board, col, piece):
    """Simulates dropping a piece in a column and returns a temporary board."""
    temp_board = board.copy()  # Make a copy of the board
    temp_board.drop_piece(col, piece)  # Simulate the move
    return temp_board