import pygame
from minesweeper.models.Board import Board
class MinefieldController:
    def __init__(self, model, view):
        self.model = model  # Board instance
        self.view = view
        self.message = ""

    def handle_click(self, pos, button):
        """Gérer le clic de l'utilisateur sur une cellule.
        
        Args:
            pos: tuple (x, y) des coordonnées du clic.
            button: bouton de la souris (1 = clic gauche, 3 = clic droit).
        """
        row = (pos[1] - self.view.offset_y) // self.view.cell_size
        col = (pos[0] - self.view.offset_x) // self.view.cell_size

        # Vérification que le clic est bien à l'intérieur du plateau
        if 0 <= row < self.model.rows and 0 <= col < self.model.columns:
            cell = self.model.cells[row][col]

            if button == 1:  # Clic gauche, révéler la cellule
                if not cell.is_flagged:  # On ne révèle pas une cellule marquée comme drapeau
                    if cell.is_a_mine and cell.is_revealed:
                        # Si c'est une mine, on termine le jeu
                        self.view.game_over = True
                        self.message = "You Lose !!!"
                        self.view.final_time = (pygame.time.get_ticks() - self.view.start_ticks) // 1000
                    else:
                        # Sinon, on appelle la fonction reveal_area pour révéler la cellule et ses adjacentes
                        self.model.reveal_area(row, col)

            elif button == 3:  # Clic droit, marquer/démarquer la cellule avec un drapeau
                cell.toggle_flag()

        
            
    def reset_game(self):
        # Régénérer le plateau (Board) et réinitialiser les paramètres de la vue
        self.model = Board(difficulty=self.model.difficulty)  # Recréer le modèle avec la même difficulté
        self.model.generate_board()  # Générer la nouvelle grille
        self.model.map_mines_count_all_cells()  # Compter les mines adjacentes
        self.view.model = self.model  # Mettre à jour le modèle dans la vue
        self.view.game_over = False 
        self.view.start_ticks = 0
        self.view.timer_started = False
        self.view.final_time = 0 # Réinitialiser le statut du jeu
        self.message = "New Game Started"  # Mettre à jour le message de réinitialisation
        print("New game started!")  # Debugging message 
        
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.view.timer_started:
                        self.view.start_ticks = pygame.time.get_ticks()
                        self.view.timer_started = True 
                        # reset button was push
                    if self.view.button_reset.collidepoint(event.pos):
                        self.reset_game()
                    else:
                        self.handle_click(event.pos, event.button)
               
                    
                    
       
            # Si le jeu est terminé, on quitte la boucle
            if self.view.game_over:
                print("** BOOM Game Over **")
                #running = False

            self.view.draw()
            self.view.update()
            clock.tick(30)

        pygame.quit()
