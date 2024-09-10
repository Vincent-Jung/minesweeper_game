import random
from pprint import pprint

from Cell import Cell


class Board:
    # def __init__(self, cells: list[list[Cell]], difficulty: str, columns: int, rows: int, mines: int):
    def __init__(self, difficulty: str="normal", columns: int="", rows: int="", mines: int=""):
        # self.cells = cells
        self.difficulty = difficulty
        self.columns = columns
        self.rows = rows
        self.mines = mines

            # info difficulty
        # EASY = 9x9, 10 mines
        # NORMAL = 16x16, 40 mines
        # HARD = 30x16, 99 mines
    
    def distribute_random_mines(self, total_of_mines):
        
        max_row = self.rows - 1
        max_column = self.columns - 1
        print("rows = ", self.rows)
        print("columns = ", self.columns)
        print("Number of mines = ", self.mines)
        mines_in_board = 0
        while mines_in_board < total_of_mines:
            row = random.randint(0, max_row)
            column = random.randint(0, max_column)
            if board[row][column] == 1:
                continue
            else:
                board[row][column] = 1
                mines_in_board += 1
        return board
    
    
    def generate_board (self, col, row):
        return [[0 for _ in range(col)] for _ in range(row)]  # 1st range = col, 2d range = rows


    def _generate_board(self):
        global board
        board = None
        game_difficulty = self.difficulty
        match game_difficulty:
            case "easy":
                print("easy mode")
                self.columns = 9
                self.rows = 9
                self.mines = 10
                board = self.generate_board(self.columns , self.rows)
                self.distribute_random_mines(self.mines)
            case "normal":
                print("normal mode")
                self.columns = 16
                self.rows = 16
                self.mines = 40
                board = self.generate_board(self.columns , self.rows)
                self.distribute_random_mines(self.mines)
            case "hard":
                print("hard mode")
                self.columns = 20
                self.rows = 16
                self.mines = 99
                board = self.generate_board(self.columns , self.rows)
                self.distribute_random_mines(self.mines)
            case "custom":
                print("custom mode")
                board = self.generate_board(self.columns , self.rows)
                self.distribute_random_mines(self.mines)
                
        pprint(board)
        return board
    
    def map_numbers(self):
        pass
    

my_board = Board("easy")
my_board._generate_board()  # Generate NORMAL base board full of 0
print("-"*30)
my_custom_board = Board("custom", 8, 5, 15)  # Generate CUSTOM base board full of 0
my_custom_board._generate_board()