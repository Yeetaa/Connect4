class Player:
    def __init__(self, piece):
        self.piece = piece

    def make_move(self, board):
        while True:
            try:
                col = int(input(f"Player {self.piece}, wähle eine Spalte! (0-6): "))
                if 0 <= col < board.COLS and board.drop_piece(col, self.piece):         #checkt ob Input zwischen 0-6 liegt und ob slot voll ist
                    return
                else:
                    print("Unmöglicher Spielzug!")
            except ValueError:
                print("Bitte gib eine Nummer zwischen 0 und 6 ein!")
