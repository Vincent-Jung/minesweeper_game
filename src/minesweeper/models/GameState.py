from minesweeper.models.Board import Board
from minesweeper.models.Cell import Cell

class GameState:
    def __init__(self):
        self.board = None

    def initialize(self, difficulty="normal"):
        """Initialise le plateau et prépare le jeu."""
        self.board = Board(difficulty=difficulty)
        self.board.generate_board()  # Génère le plateau
        self.board.map_mines_count_all_cells()  # Compte les mines adjacentes
        print("GameState initialized with difficulty:", difficulty)

    def reload_board(self):
        """Recharger le plateau en recréant un nouveau Board."""
        self.initialize(self.board.difficulty)  # Réinitialise avec la difficulté actuelle
        print("Board reloaded successfully!")

    def trigger_victory(self):
        """Vérifie si toutes les bombes sont cachées ou marquées et que toutes les autres cellules sont révélées."""
        for row in self.board.cells:  # Parcourt chaque ligne du plateau (self.board.cells)
            for cell in row:  # Parcourt chaque cellule
                if cell.is_a_mine and not cell.is_flagged:  # Si c'est une bombe mais qu'elle n'est pas flaguée
                    return False  # Le joueur n'a pas encore gagné
                if not cell.is_a_mine and not cell.is_revealed:  # Si ce n'est pas une bombe et que la cellule n'est pas révélée
                    return False  # Le joueur n'a pas encore gagné
        return True  # Toutes les conditions de victoire sont remplies
