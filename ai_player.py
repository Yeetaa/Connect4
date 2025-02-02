class AI_Player:

    def __init__(self, piece):
        self.piece = piece
        if self.piece == 'X':
            self.opponent_piece = 'O'
        elif self.piece == 'O':
            self.opponent_piece = 'X'

    def make_move(self, board):
        pass

