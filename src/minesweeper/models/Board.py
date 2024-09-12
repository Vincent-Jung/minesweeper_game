import random
from Cell import Cell

class Board:
    def __init__(self, difficulty: str = "normal", rows: int = None, columns: int = None, mines: int = None, cells: list[list[Cell]] = None):
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
    
    
    def run_through_board(self):  # Print list of all cells objects and parameters
        """Check function. Not used in running the game.
        Vizualise all cells with their parameters info:
        is_revealed, is_flagged, is_a_mine, adjacent_mines.
        """
        for row in self.cells:
            for cell in row:
                print(cell)
                
                
    def count_adjacent_mines(self, x, y):
        """Count all mines in the 8 adjacent cells of a cell.
        Use the x, y coordinates of a cell to check the surrounding.
        The count of mines (0 to 8) is then attributed to the specific cell.
        """
        mines_count = 0
        adjacent_positions = [(-1, -1), (-1, 0), (-1, 1), 
                              (0, -1),          (0, 1), 
                              (1, -1), (1, 0), (1, 1)]
        
        for delta_x, delta_y in adjacent_positions:
            new_x, new_y = x + delta_x, y + delta_y
            if 0 <= new_x < self.rows and 0 <= new_y < self.columns:
                if self.cells[new_x][new_y].is_a_mine:
                    mines_count += 1
        print(f"Cell ({x}, {y}) has {mines_count} adjacent mines")
        self.cells[x][y].adjacent_mines = mines_count
                
                
    def map_mines_count_all_cells(self):
        """Run the count mines function through all board
        Check all cells by rows and columns, count mines and attribute int to each one.
        """
        for x in range(self.rows):
            for y in range(self.columns):
                self.count_adjacent_mines(x, y)
        # return print("*** END OF SETUP ***")
                
    def ready_board(self):
        my_custom_board = Board("custom", 4, 8, 15)  # Generate CUSTOM board, rows x col x mines
        my_custom_board.generate_board()
        my_custom_board.display_board()
        my_custom_board.map_mines_count_all_cells()
        my_custom_board.run_through_board()
        
    def click_a_cell(self, x, y):
        clicked_cell = self.cells[x][y]
        clicked_cell.reveal_cell()

                
    # tests
# my_board = Board("hard")
# my_board.generate_board()  # Generate premade board based on difficulty of Board
# my_board.display_board()
# my_board.map_mines_count_all_cells()
# my_board.run_through_board()
# print("-"*30)
my_custom_board = Board("custom", 3, 3, 3)  # Generate CUSTOM board, rows x col x mines
my_custom_board.generate_board()
my_custom_board.display_board()
my_custom_board.map_mines_count_all_cells()

my_custom_board.click_a_cell(0, 0)
# my_custom_board.click_a_cell(1, 2)
# my_custom_board.click_a_cell(2, 0)
print("*** check board ***")
my_custom_board.run_through_board()
