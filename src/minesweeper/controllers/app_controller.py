import pygame
from minesweeper.models.GameState import GameState
from minesweeper.views.principal_view import PrincipalView
from minesweeper.controllers.controller_view import MinefieldController

class AppController:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        
    def load_app(self):
        game_state = GameState()
        game_state.initialize(self.difficulty)

        view = PrincipalView(game_state.board, game_state)
        controller = MinefieldController(game_state.board, view,self)
        controller.run()