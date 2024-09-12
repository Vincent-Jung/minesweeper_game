from src.minesweeper.views.controller_view import MinefieldController
from src.minesweeper.views.principal_view import PrincipalView
from src.minesweeper.models.Board import Board

class AppView:
    def __init__(self):
        self.board = Board(difficulty="normal")
        self.board.generate_board()
        self.board.map_mines_count_all_cells()  # Compte les mines adjacentes

        self.view = PrincipalView(self.board)
        self.controller = MinefieldController(self.board, self.view)
    def run(self):
        return self.controller.run()