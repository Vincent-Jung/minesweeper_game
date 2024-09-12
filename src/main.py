from minesweeper.controllers.controller_view import MinefieldController
from minesweeper.views.principal_view import PrincipalView
from minesweeper.models.GameState import GameState

if __name__ == '__main__':
    game_state = GameState()
    game_state.initialize(difficulty="easy")

    view = PrincipalView(game_state.board, game_state)
    controller = MinefieldController(game_state.board, view)
    controller.run()