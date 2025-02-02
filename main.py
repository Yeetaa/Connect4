from random import Random
import time
import constants

from board import Board
from constants import debug_mode
from player import Player
from random_ai_player import Random_AI_Player
from greedy_ai_player import Greedy_AI_Player
from rath_ai_player import Rath_AI_Player
from minimax import Minimax_AI_Player
from debugger import Debugger


def play_game():
    """Main game loop."""

    open('log.txt', 'w').close()

    board = Board()
    player1 = Player('X')  # Spieler

    player2_selection = input(f"Random(1), Greedy(2), Minimax(3), Rath(4) oder Spieler(5): ")
    print(player2_selection)

    if player2_selection == "1":
        player2 = Random_AI_Player('O')
        print(f"Du spielst gegen Random_AI")
    elif player2_selection == "2":
        player2 = Greedy_AI_Player('O')
        print(f"Du spielst gegen Greedy_AI")
    elif player2_selection == "3":
        player2 = Minimax_AI_Player('O')
        print("Du spielst gegen Minimax_AI")
    elif player2_selection == "4":
        player2 = Rath_AI_Player('O')
        print(f"Du spielst gegen Rath_AI")
    elif player2_selection == "5":
        player2 = Player('O')
        print(f"Du spielst gegen einen anderen Spieler")
    elif player2_selection == "360":
        player2 = Debugger('O')
    else:
        print("Fehler")
    if not debug_mode:
        time.sleep(2)

    turn = 0  # 0 = Player 1; 1 = AI

    board.print_board()

    while True:
        if turn == 0:
            player1.make_move(board)
            if board.check_win(player1.piece):
                board.print_board()
                print("Spieler X Gewinnt!")
                time.sleep(1)
                break
        else:
            if not debug_mode:
                time.sleep(0.7) #FAKE Delay um Zug zu visualisieren
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
