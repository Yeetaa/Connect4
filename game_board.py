import copy
import constants
from constants import debug_mode


class Game_Board:
    ROWS = 6
    COLS = 7
    EMPTY = '.'

    def __init__(self):
        self.grid = [[self.EMPTY for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.last_piece_row = None
        self.last_piece_col = None
        #Initialisierung mit "." in jedem Slot

    def print_board(self):
        if not debug_mode:
            print("\033c", end="")  #Cleared die Konsole zwischen Zügen
        print("Vier In Einer Reihe Gewinnt Das Spiel!")
        for row in reversed(self.grid):  # Print top-down Board
            for part in row:
                if part == ".":
                    print("\033[97m●\033[0m", end=" ")
                if part == "X":
                    print("\033[91mX\033[0m", end=" ")
                if part == "O":
                    print("\033[32mO\033[0m", end=" ")

            print("\n", end="")

        print("-------------")
        print("0 1 2 3 4 5 6")  #Spalten Nummern

    def drop_piece(self, col, piece):
        for row in range(self.ROWS):
            if self.grid[row][col] == self.EMPTY:
                self.last_piece_row = row
                self.last_piece_col = col
                self.grid[row][col] = piece
                return True
        return False  # Spalte ist voll
        #Setzt das Piece oder gibt FALSE zurück

    def remove_last_piece(self):
        self.grid[self.last_piece_row][self.last_piece_col] = self.EMPTY

    def get_valid_columns(self):
        return [col for col in range(self.COLS) if self.grid[5][col] == self.EMPTY]
        #Gibt LISTE an validen Columns zurück

    def get_columns(self):
        return self.COLS

    def copy(self):
        return copy.deepcopy(self)
        #Gibt Kopie des gegenwertigen Boards zurück um KI Züge simulieren zu lassen

    def check_win(self, piece):
        #!!!wenn´s funktioniert, nicht anrühren!!!

        # Check horizontal
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row][col + i] == piece for i in range(4)):
                    return True

        # Check vertical
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.grid[row + i][col] == piece for i in range(4)):
                    return True

        # Check diagonal (\)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(4)):
                    return True

        # Check diagonal (/)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(4)):
                    return True

        return False

    def check_3_in_row(self, piece):
        #!!!wenn´s funktioniert, nicht anrühren!!!

        counter = 0

        # Check horizontal
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row][col + i] == piece for i in range(3)):
                    counter += 3

        # Check vertical
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.grid[row + i][col] == piece for i in range(3)):
                    counter += 3

        # Check diagonal (\)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(3)):
                    counter += 3

        # Check diagonal (/)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(3)):
                    counter += 3

        return counter

    def check_2_in_row(self, piece):
        #!!!wenn´s funktioniert, nicht anrühren!!!

        counter = 0

        # Check horizontal
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row][col + i] == piece for i in range(2)):
                    counter += 2

        # Check vertical
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.grid[row + i][col] == piece for i in range(2)):
                    counter += 2

        # Check diagonal (\)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(2)):
                    counter += 2

        # Check diagonal (/)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(2)):
                    counter += 2

        return counter