class AI_Player:

    def __init__(self, piece):
        self.piece = piece
        if self.piece == 'X':
            self.opponent_piece = 'O'
        elif self.piece == 'O':
            self.opponent_piece = 'X'

    def make_move(self, board):
        pass

    def append_to_log(self, message):
        with open("log.txt", "a") as log:
            log.write(f"Player {self.piece}: Column {message}\n ")
            return