import pygame
from minesweeper.models.Cell import Cell
from minesweeper.models.Board import Board

#--------------- constants colors ---------------#
SQUARE = "peachpuff1"
FLAG = "tomato1"
RESET = "darkseagreen1"
GREY = "seashell1"
BG ="grey100"
#--------------- class views ---------------#

class PrincipalView:
    def __init__(self, model, cell_size=30):
        self.model = model  # Board instance
        self.cell_size = cell_size
        self.width = (self.model.columns * self.cell_size)
        self.height = (self.model.rows * self.cell_size)
        self.screen = pygame.display.set_mode((self.width+380, self.height+90))
        
                        #----Setup view-----#
                        
        # size and offset for the grid
        self.total_grid_width = self.width + (self.model.columns - 1) * 1
        self.total_grid_height = self.height + (self.model.rows - 1) * 1
        self.offset_x = (self.width - self.total_grid_width) // 2 +30
        self.offset_y = (self.height - self.total_grid_height) // 2 +30
        
        # load images data
        self.bomb_image = pygame.image.load('src/minesweeper/assets/image/mine.png')
        self.bomb_image = pygame.transform.smoothscale(self.bomb_image, (self.cell_size, self.cell_size))
        self.reset_image = pygame.image.load('src/minesweeper/assets/image/reset.png')
        self.reset_image = pygame.transform.smoothscale(self.reset_image, ((self.cell_size-5), (self.cell_size-5)))
        self.game_over = False

        # reset button parameters
        self.x_button_reset = ((self.width+self.offset_x)//2)
        self.y_button_restet = self.height+self.offset_y+self.cell_size//2
        self.button_reset = pygame.Rect(self.x_button_reset, self.y_button_restet, (self.cell_size), self.cell_size)
        
        # offset image buttons
    def center_image_in_button(self,button_rect, image):
        """
        Center an image inside a button using get_rect().

        Args:
            button_rect (pygame.Rect): The rectangle of the button.
            image (pygame.Surface): The image to center.

        Returns:
            pygame.Rect: A rectangle with the image centered inside the button.
        """
        image_rect = image.get_rect(center=button_rect.center)
        return image_rect

        
    def draw(self):
        self.screen.fill((FLAG))  # Background color
        for row in range(self.model.rows):
            for col in range(self.model.columns):
                cell = self.model.cells[row][col]
                x, y = (col * self.cell_size) + self.offset_x, (row * self.cell_size) + self.offset_y
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                
                # Affichage des cellules en fonction de leur état
                if cell.is_revealed:
                    if cell.is_a_mine:
                        self.screen.blit(self.bomb_image, (x, y))
                        self.game_over = True
                    else:
                        pygame.draw.rect(self.screen, (GREY), rect)  # Gris clair pour les cases révélées
                        if cell.adjacent_mines > 0:
                            font = pygame.font.Font(None, 36)
                            text = font.render(str(cell.adjacent_mines), True, (0, 0, 0))
                            self.screen.blit(text, (x + 10, y + 5))
                else:
                    pygame.draw.rect(self.screen, (SQUARE), rect)  # Gris foncé pour les cases non révélées

                    if cell.is_flagged:
                        pygame.draw.circle(self.screen, (FLAG), (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 4)  # Jaune pour les drapeaux

                # Contours des cases
                pygame.draw.rect(self.screen, (GREY), rect, 1)
        # draw reset button
        self.button_reset=pygame.draw.rect(self.screen, (RESET), self.button_reset)
        self.image_rect = self.center_image_in_button(self.button_reset, self.reset_image)
        self.screen.blit(self.reset_image, self.image_rect)
        
    def update(self):
        pygame.display.flip()
