from minesweeper.models.Board import Board
from minesweeper.models.Cell import Cell

class GameState:
    def __init__(self):
        """
        Initialize the GameState class with no board.
        """
        self.board = None

    def initialize(self, difficulty="normal"):
        """
        Initialize the board and prepare the game.

        Args:
            difficulty (str): The difficulty level of the game.
        """
        self.board = Board(difficulty=difficulty)
        self.board.generate_board()  # Generate the board
        self.board.map_mines_count_all_cells()  # Count adjacent mines
        print("GameState initialized with difficulty:", difficulty)

    def reload_board(self):
        """
        Reload the board by creating a new Board instance with the current difficulty.
        """
        self.initialize(self.board.difficulty)  # Reinitialize with the current difficulty
        print("Board reloaded successfully!")

    def trigger_victory(self):
        """
        Check if all mines are either hidden or flagged and all other cells are revealed.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        for row in self.board.cells:  # Iterate over each row of the board (self.board.cells)
            for cell in row:  # Iterate over each cell
                if cell.is_a_mine and not cell.is_flagged:  # If it's a mine but not flagged
                    return False  # The player has not won yet
                if not cell.is_a_mine and not cell.is_revealed:  # If it's not a mine and the cell is not revealed
                    return False  # The player has not won yet
        return True  # All win conditions are met
