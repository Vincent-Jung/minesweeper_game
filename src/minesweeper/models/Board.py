import random
from pprint import pprint

class Board:
    def __init__(self, difficulty: str, mines: int):
        self.difficulty = difficulty
        self.mines = mines
        self._generate_board(self.difficulty)
        
        # difficulty
        # EASY = 9x9, 10 mines
        # NORMAL = 16x16, 40 mines
        # HARD = 30x16, 99 mines
    
    def generate_board (self, col , row):
        return [[0 for _ in range(col)] for _ in range(row)]

    def _generate_board(self, game_difficulty):
        board = None
        match game_difficulty:
            case "easy":
                board = self.generate_board(9 , 9)  # 1st range = col, 2d range = rows
            case "normal":
                board = self.generate_board(16 , 16) 
            case "hard":
                board = self.generate_board(20 , 16) 
                
        pprint(board)
        return board

    def random_mines(self):
        pass
    
    def map_numbers(self):
        pass
    
my_board = Board("easy", 10)