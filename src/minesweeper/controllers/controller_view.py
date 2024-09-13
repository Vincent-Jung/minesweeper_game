import pygame
from minesweeper.models.Board import Board

class MinefieldController:
    def __init__(self, model, view,app):
        """
        Initialize the MinefieldController class.

        Args:
            model (Board): The game board instance.
            view (PrincipalView): The game view instance.
        """
        self.model = model  # Board instance
        self.view = view
        self.app = app # AppController instance
        self.message = ""

    def handle_click(self, pos, button):
        """
        Handle the user's click on a cell.

        Args:
            pos (tuple): (x, y) coordinates of the click.
            button (int): Mouse button (1 = left click, 3 = right click).
        """
        row = (pos[1] - self.view.offset_y) // self.view.cell_size
        col = (pos[0] - self.view.offset_x) // self.view.cell_size

        # Check if the click is outside the board boundaries
        if row < 0 or row >= self.model.rows or col < 0 or col >= self.model.columns:
            return  
        
        cell = self.model.cells[row][col]

        if button == 1:  # Left click, reveal the cell
            if not cell.is_flagged:
                if cell.is_a_mine:
                    self.reveal_all_bombs()  # Reveal all bombs
                    self.view.game_over = True
                    self.view.message = "Game over!"
                    self.view.final_time = (pygame.time.get_ticks() - self.view.start_ticks) // 1000
                else:
                    self.model.reveal_area(row, col)  # Reveal the area

        elif button == 3:  # Right click, toggle flag on the cell
            cell.toggle_flag()

    def reveal_all_bombs(self):
        """
        Reveal all cells containing bombs.
        """
        for row in range(self.model.rows):
            for col in range(self.model.columns):
                cell = self.model.cells[row][col]
                if cell.is_a_mine:
                    cell.reveal_cell()  # Reveal the bomb
            
    def reset_game(self):
        """
        Regenerate the board and reset the view parameters.
        """
        self.model = Board(difficulty=self.model.difficulty)  # Create a new model with the same difficulty
        self.model.generate_board()  # Generate the new board
        self.model.map_mines_count_all_cells()  # Count adjacent mines
        self.view.model = self.model  # Update the model in the view
        self.view.game_over = False 
        self.view.start_ticks = 0
        self.view.timer_started = False
        self.view.final_time = 0  # Reset game status
        self.view.message = "New Game Started"  # Update reset message
        
    def new_screen(self, difficulty):
        """
        Create a new game screen for the selected level
        """
        app_controller = self.app(difficulty)
        app_controller.load_app()
        
    def run(self):
        """
        Run the main game loop.
        """
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
                        self.view.message = "Good luck!"
                        # Reset button was pushed
                    if self.view.button_reset.collidepoint(event.pos):
                        self.reset_game()
                    else:
                        self.handle_click(event.pos, event.button)

            self.view.draw()
            self.view.update()
            clock.tick(30)

        pygame.quit()
