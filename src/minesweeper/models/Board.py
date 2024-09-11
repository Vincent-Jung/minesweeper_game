import random
from Cell import Cell

class Board:
    def __init__(self, difficulty: str="normal", rows: int=None, columns: int=None, mines: int=None, cells: list[list[Cell]]=None):
        self.difficulty = difficulty
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.cells = cells if cells is not None else []

    
    def distribute_random_mines(self, total_of_mines):
        """Randomly add mines to the game board
        
        Args:
            total_of_mines (int): number of mines max to be displayed regarding difficulty chosen.
            
        Returns:
            self.cells: return cells, the "board" with a number of cells where the is_a_mine == True
            equal to total_of_mines.
        """
        max_row = self.rows - 1
        max_column = self.columns - 1
        print("rows = ", self.rows)
        print("columns = ", self.columns)
        print("Number of mines = ", self.mines)
        
        mines_in_board = 0
        while mines_in_board < total_of_mines:
            row = random.randint(0, max_row)
            column = random.randint(0, max_column)

            selected_cell = self.cells[row][column]
            if selected_cell.is_a_mine == True:  # Avoid multiple mines on same cell. Position it on another cell.
                continue
            else:
                selected_cell.is_a_mine = True
                mines_in_board += 1
        return self.cells
    

    def _generate_board(self, row, col):
        """Generate the basic matrix of the game. 
        Called in generate_board function based on parameters selected.

        Returns:
            List: Matrix as the "board" of the game. List (col)of list(row) of Cell()
        """
        return [[Cell() for _ in range(col)] for _ in range(row)]


    def generate_board(self):
        """Generate the board using parameters
        Difficulties have premade rows, col and number of mines. Custom mode allows
        for specific entries and shape a custom game.
        Returns:
            List: List of list of Cell() with exact number of mines on random positions.
        """
        game_difficulty = self.difficulty
        if game_difficulty == "easy":
            print("easy mode")
            self.columns = 9
            self.rows = 9
            self.mines = 10
        elif game_difficulty == "normal":
            print("normal mode")
            self.columns = 16
            self.rows = 16
            self.mines = 40
        elif game_difficulty == "hard":
            print("hard mode")
            self.columns = 20
            self.rows = 16
            self.mines = 99
        elif game_difficulty == "custom":
            print("custom mode")
                
        self.cells = self._generate_board( self.rows, self.columns)
        self.distribute_random_mines(self.mines)
        return self.cells
    
    
    def display_board(self):
        """Display the game board in terminal
        Used to check the right size of the matrix, number of mines 
        and their random positions in a visual way.
        """
        for row in self.cells:
            row_terminal_display = ["M" if cell.is_a_mine else "-" for cell in row]
            print(" ".join(row_terminal_display))
    
        
    def map_numbers(self):
        pass
    

    # tests
my_board = Board("easy")
my_board.generate_board()  # Generate premade board based on difficulty of Board
my_board.display_board()
print("-"*30)
my_custom_board = Board("custom", 3, 10, 8)  # Generate CUSTOM board, rows x col x mines
my_custom_board.generate_board()
my_custom_board.display_board()
