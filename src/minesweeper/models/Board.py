import random
from pprint import pprint

class Board:
    def __init__(self, difficulty: str, size: int, mines: int):
        self.difficulty = difficulty
        self.size = size
        self.mines = mines
        
            # difficulty
        # EASY = 9x9, 10 mines
        # NORMAL = 16x16, 40 mines
        # HARD = 30x16, 99 mines

    def generate_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]  # 1st range = col, 2d range = rows. Hard=30, 16
        pprint(board)
    
    def random_mines(self):
        pass
    
    def map_numbers(self):
        pass
    


my_board = Board("easy", 9, 10)
my_board.generate_board()