from random import Random

from board import Board
from player import Player
from ai_player import AI_Player #eig. unnötig
from random_ai_player import Random_AI_Player

def play_game():
    """Main game loop."""
    board = Board()
    player1 = Player('X')   # Spieler
    player2 = Random_AI_Player('O')  # AI Spieler

    turn = 0  # 0 = Player 1; 1 = AI

    board.print_board()

    while True:
        if turn == 0:
            player1.make_move(board)
            if board.check_win(player1.piece):
                board.print_board()
                print("Spieler X Gewinnt!")
                break
        else:
            player2.make_move(board)  # Placeholder for AI logic
            if board.check_win(player2.piece):
                board.print_board()
                print("Spieler O Gewinnt!")
                break

        board.print_board()
        turn = 1 - turn  # Switch turns


# Run the game
if __name__ == "__main__":
    play_game()
