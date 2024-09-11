import pygame
from os.path import join
from random import randint, sample

# Dimensions de l'écran
x_screen = 600
y_screen = 650

ORANGE = "peachpuff1"
GREEN = "chartreuse3"
BLUE = "slateblue3"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

EASY = [9, 9, 10]
MEDIUM = [16, 16, 40]
HARD = [30, 16, 99]

class Mines(pygame.sprite.Sprite):
    def __init__(self, surf, x, y):
        self.image = surf
        self.x_square = x
        self.y_square = y
        self.scale = pygame.transform.smoothscale(self.image, (self.x_square, self.y_square))

class Minesweeper:
    def __init__(self, mines:Mines, screen, reset_btn):
        self.screen = screen
        self.reset_button = reset_btn
        self.clock = pygame.time.Clock()
        self.mines = mines
        self.load_sounds()
        self.reset_game(EASY)
        
    def load_sounds(self):
        self.explosion_sound = pygame.mixer.Sound('src/demineur/asserts/audio/explosion.mp3')
        self.swip_sound = pygame.mixer.Sound('src/demineur/asserts/audio/swip.mp3')
        self.reset_sound = pygame.mixer.Sound('src/demineur/asserts/audio/wrong.mp3')
    
    def reset_game(self, level):
        self.grid = self.create_grid(level)
        self.grid_bombe = self.place_bombs(self.grid, level)
        self.start_ticks = 0
        self.timer_started = False
        self.game_over = False
        self.final_time = 0
    
    def create_grid(self, level):
        grid = []
        total_grid_width = level[1] * self.mines.x_square + (level[1] - 1) * 1
        total_grid_height = level[0] * self.mines.y_square + (level[0] - 1) * 1
        offset_x = (x_screen - total_grid_width) // 2
        offset_y = (y_screen - total_grid_height) // 2 - 20
        
        for row in range(level[0]):
            for col in range(level[1]):
                x = offset_x + col * (self.mines.x_square + 1)
                y = offset_y + row * (self.mines.y_square + 1)
                grid.append({
                    "rect": pygame.Rect(x, y, self.mines.x_square, self.mines.y_square),
                    "color": ORANGE,
                    "is_flagged": False,
                    "is_a_mine": False,
                    "is_revealed": False
                })
        return grid
    
    def place_bombs(self, grid, level):
        coordinates = sample(range(len(grid)), level[2])
        for index in coordinates:
            grid[index]["is_a_mine"] = True
        return grid
    
    def handle_click(self, square):
        if square["is_a_mine"] and square["is_revealed"]:
            print("Bombe !")
            self.explosion_sound.play()
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
    
    def draw_grid(self):
        self.screen.fill(WHITE)
        for square in self.grid:
            if square["is_a_mine"] and square["is_revealed"]:
                self.screen.blit(self.mines.scale, square["rect"])
            elif square["is_revealed"]:
                pygame.draw.rect(self.screen, square["color"], square["rect"])
            else:
                pygame.draw.rect(self.screen, square["color"], square["rect"])
        pygame.draw.rect(self.screen, BLUE, self.reset_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Reset", True, WHITE)
        self.screen.blit(text, (self.reset_button.x + 10, self.reset_button.y + 10))
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000 if self.timer_started and not self.game_over else self.final_time
        time_text = font.render(f"Temps: {seconds} sec", True, BLACK)
        self.screen.blit(time_text, (x_screen // 2 - 80, 0))
        pygame.display.flip()
    
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
            
            self.draw_grid()
            self.clock.tick(30)
        
        pygame.quit()

