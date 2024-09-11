import pygame
from os.path import join
from random import randint, sample

# Dimensions de l'écran
x_screen = 450
y_screen = 450

ORANGE = "peachpuff1"
GREEN = "chartreuse3"
BLUE = "slateblue3"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

EASY = [9, 9, 10, 450, 450] # wigth/heigh/nb_mines/ wigth_window/ height_window
MEDIUM = [16, 16, 40, 600, 600] # wigth/heigh/nb_mines/ wigth_window/ height_window
HARD = [30, 16, 99, 800, 600] # wigth/heigh/nb_mines/ wigth_window/ height_window
def offset(self, level)->list:
    list_offsets = []
    total_grid_width = level[1] * self.mines.x_square + (level[1] - 1) * 1
    total_grid_height = level[0] * self.mines.y_square + (level[0] - 1) * 1
    offset_x = (self.width - total_grid_width) // 2
    offset_y = (self.height - total_grid_height) // 2 - 20
    list_offsets.append(offset_x, offset_y)
    return list_offsets
    
class Mines():
    def __init__(self, surf, x, y):
        self.image = surf
        self.x_square = x
        self.y_square = y
        self.scale = pygame.transform.smoothscale(self.image, (self.x_square, self.y_square))
        
class Cell(object):
    def __init__(self, cell_wigth, cell_heigth, color=ORANGE): 
        self.color= color
        self.is_flagged = False
        self.is_a_mine = False
        self.is_revealed = False
        self.wigth = cell_wigth
        self.heigth = cell_heigth    
        
    def draw_cell(self, x_position, y_position):
        return pygame.Rect(x_position, y_position, self.wigth, self.heigth)
        
class Grid():
    def __init__(self, width, height, nb_mines, mines:Mines, cell:Cell):
        self.width = width
        self.height = height
        self.mines = mines
        self.cell = cell
        self.nb_mines = nb_mines
        
        
    def create_grid(self, offsets:list):
        grid = []
        x = offsets[0] + col * (self.cell.wigth + 1)
        y = offsets[1]+ row * (self.cell.heigth + 1)
        for row in range(self.width):
            for col in range(self.height):
                grid.append(self.cell.draw_cell(x,y))
        return grid
        # TODO: show if the methods under work
    
    
        
    def draw_timer(self, screen):
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000 if self.timer_started and not self.game_over else self.final_time
        font = pygame.font.Font(None, 36)
        time_text = font.render(f"Temps: {seconds} sec", True, BLACK)
        screen.blit(time_text, (x_screen // 2 - 80, 0))
        
    def draw_button(self, x_screen, y_screen, screen):
        pygame.draw.rect(self.screen, BLUE, self.reset_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Reset", True, WHITE)
        screen.blit(text, (self.reset_button.x + 10, self.reset_button.y + 10))
        
class Minesweeper:
    def __init__(self, mines:Mines,grid:Grid, screen, reset_btn):
        self.screen = screen
        self.reset_button = reset_btn
        self.clock = pygame.time.Clock()
        self.mines = mines
        self.grid = grid
        self.load_sounds()
        self.reset_game(EASY)
    
    def draw_grid(self, screen, grid:Grid):
        for square in grid:
            pygame.draw.rect(screen, square["color"], square["rect"])   
    
    def update_grid(self, screen):
        if self.grid.cell.is_a_mine and self.grid.cell.is_revealed:
                screen.blit(self.mines.scale, self.grid.cell.draw_cell()) # change the square with mine when reveled
        elif square["is_revealed"]:
                pygame.draw.rect(screen, square["color"], square["rect"]) # change the color of the selected square
                     #self.reveal_adjacent_cells(square) #self.reveal_empty_cells(square)
                             
    def load_sounds(self):
        self.explosion_sound = pygame.mixer.Sound('src/demineur/asserts/audio/explosion.mp3')
        self.swip_sound = pygame.mixer.Sound('src/demineur/asserts/audio/swip.mp3')
        self.reset_sound = pygame.mixer.Sound('src/demineur/asserts/audio/wrong.mp3')
    
    def reset_game(self, level):
        self.grid = self.grid
        self.grid_bombe = self.place_bombs(self.grid, level)
        self.start_ticks = 0
        self.timer_started = False
        self.game_over = False
        self.final_time = 0
    
    
    
    def handle_click(self, square):
        if square["is_a_mine"] and square["is_revealed"]:
            print("Bombe !")
            self.load_sounds.explosion_sound.play()
            self.game_over = True
            self.final_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
        elif square["is_revealed"]:
            square["color"] = WHITE
            print("Pas de bombe ici.")
            self.swip_sound.play()
    
    def change_color(self, square):
        if square["color"] == ORANGE:
            square["color"] = GREEN
            square["is_flagged"] = True
        else:
            square["color"] = ORANGE
            square["is_flagged"] = False
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.timer_started:
                        self.start_ticks = pygame.time.get_ticks()
                        self.timer_started = True
                    
                    if pygame.mouse.get_pressed()[0]:  # Clic gauche
                        for square in self.grid:
                            if square["rect"].collidepoint(event.pos) and not square["is_flagged"]:
                                square["is_revealed"] = True
                                self.handle_click(square)
                        
                    elif pygame.mouse.get_pressed()[2]:  # Clic droit
                        for square in self.grid:
                            if square["rect"].collidepoint(event.pos):
                                self.change_color(square)
                    
                    if self.reset_button.collidepoint(event.pos):
                        self.reset_game(EASY)
                        self.reset_sound.play()
            
            self.draw_grid(EASY)
            self.clock.tick(30)
        
        pygame.quit()

