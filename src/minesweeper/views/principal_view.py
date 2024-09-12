import pygame
#--------------- constants colors ---------------#
SQUARE = "peachpuff1"
FLAG = "tomato1"
RESET = "darkseagreen1"
GREY = "seashell1"
BG ="grey100"
BLACK = "black"
BG_BOX = "antiquewhite1"
#--------------- class views ---------------#

class PrincipalView:
    def __init__(self, model, state, cell_size=30):
        self.model = model  # Board instance
        self.state = state  # GameState instance
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
        self.bomb_image = pygame.image.load('src/minesweeper/assets/image/cute_skull.png')
        self.bomb_image = pygame.transform.smoothscale(self.bomb_image, (self.cell_size, self.cell_size))
        self.flag_image = pygame.image.load('src/minesweeper/assets/image/bones2.png')
        self.flag_image = pygame.transform.smoothscale(self.flag_image, (self.cell_size, self.cell_size))
        self.reset_image = pygame.image.load('src/minesweeper/assets/image/reset.png')
        self.reset_image = pygame.transform.smoothscale(self.reset_image, ((self.cell_size-5), (self.cell_size-5)))
        self.game_over = False
        
        
        # select image Box
        self.coor_x_box = self.width + self.offset_x + 30
        self.coor_y_box_level = 124
        self.image_box = pygame.Rect(self.coor_x_box, self.coor_y_box_level, 300 , 120)
        
        self.love_skull = pygame.image.load('src/minesweeper/assets/image/love_skull.png')
        self.love_skull = pygame.transform.smoothscale(self.love_skull, (self.image_box.width//2, self.image_box.height))
        self.lose_skull = pygame.image.load('src/minesweeper/assets/image/pirate_skull.png')
        self.lose_skull = pygame.transform.smoothscale(self.lose_skull, (self.image_box.width//2, self.image_box.height))

        # reset button parameters
        self.x_button_reset = ((self.width+self.offset_x)//2)
        self.y_button_restet = self.height+self.offset_y+self.cell_size//2
        self.button_reset = pygame.Rect(self.x_button_reset, self.y_button_restet, self.cell_size, self.cell_size)
        
        # timer game
        self.start_ticks = 0
        self.timer_started = False
        self.final_time = 0
        self.position_timer = (self.width + self.offset_x + 127, 92)
        
        # title position
        self.position_title = (self.width + self.offset_x + 102, 30)
        
        # Message of message Box
        self.message_box_rect = pygame.Rect(self.coor_x_box, 247, 300, 63)
        self.message = "Good luck!"
        
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
        self.screen.fill((BG))  # Background color
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
                        # Afficher l'image du drapeau au lieu du cercle
                        flag_rect = self.flag_image.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
                        self.screen.blit(self.flag_image, flag_rect)


                # Contours des cases
                pygame.draw.rect(self.screen, (GREY), rect, 1)
                
        # Vérifier la victoire
        if self.state.trigger_victory():  # Si le joueur a gagné
            self.message = "Congratulations!"  # Mettre à jour le message
            pygame.draw.rect(self.screen, BG_BOX, self.image_box)
            # Create a rectangle for the lose_skull image
            love_skull_rect = self.love_skull.get_rect(center=self.image_box.center)
            
            # Draw the lose_skull image centered in the image_box
            self.screen.blit(self.love_skull, love_skull_rect)

        if self.game_over:
            # draw the image box
            pygame.draw.rect(self.screen, BG_BOX, self.image_box)
            # Create a rectangle for the lose_skull image
            lose_skull_rect = self.lose_skull.get_rect(center=self.image_box.center)
            
            # Draw the lose_skull image centered in the image_box
            self.screen.blit(self.lose_skull, lose_skull_rect)
            
        # draw the title
        font = pygame.font.SysFont('rage', 36)
        title = font.render("Minesweeper", True, BLACK)
        self.screen.blit(title, self.position_title)
        
        # draw reset button
        self.button_reset=pygame.draw.rect(self.screen, (RESET), self.button_reset)
        self.image_rect = self.center_image_in_button(self.button_reset, self.reset_image)
        self.screen.blit(self.reset_image, self.image_rect)
        
        # draw the game timer
        font = pygame.font.Font(None, 30)
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000 if self.timer_started and not self.game_over else self.final_time
        txt = f"Time: {seconds} sec"
        time_text = font.render(txt, True, BLACK)
        self.screen.blit(time_text, self.position_timer)
        
        
        # draw the message box
        pygame.draw.rect(self.screen, BG_BOX, self.message_box_rect)
        font = pygame.font.SysFont('rage', 30)
        message_text = font.render(self.message, True, BLACK)
        text_rect = message_text.get_rect(center=self.message_box_rect.center)
        self.screen.blit(message_text, text_rect)
        
    def update(self):
        pygame.display.flip()
