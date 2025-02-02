from ai_player import AI_Player


class Debugger(AI_Player):
    def __init__(self, piece):
        super().__init__(piece)
        print("Debugger Ausgewählt")

    def make_move(self, board):
        '''Belibige Funktion aufrufen'''
        print("--------------------")
        print("HELLO WORLD")
        print(min(30,5))
        print("--------------------")