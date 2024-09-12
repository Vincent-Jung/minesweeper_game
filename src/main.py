from minesweeper.views.controller_view import MinefieldController
from minesweeper.views.principal_view import PrincipalView
from minesweeper.models.Board import Board

if __name__ == '__main__':
    board = Board(difficulty="normal")
    board.generate_board()
    board.map_mines_count_all_cells()  # Compte les mines adjacentes

    view = PrincipalView(board)
    controller = MinefieldController(board, view)
    controller.run()