import pygame
from random import sample

EASY = [9, 9, 10, 450, 450]
def create_grid(level, x_screen, y_screen):
        grid = []
        total_grid_width = level[1] * 30 + (level[1] - 1) * 1
        total_grid_height = level[0] * 30 + (level[0] - 1) * 1
        offset_x = (x_screen - total_grid_width) // 2
        offset_y = (y_screen - total_grid_height) // 2 - 20
        
        for row in range(level[0]):
            for col in range(level[1]):
                x = offset_x + col * (30 + 1)
                y = offset_y + row * (30 + 1)
                grid.append({
                    "rect": pygame.Rect(x, y, 30,30),
                    "is_a_mine": False
                })
        return grid
    
def place_bombs(grid, level):
        coordinates = sample(range(len(grid)), level)
        for index in coordinates:
            grid[index]["is_a_mine"] = True
        return grid
    
    
grid = create_grid(EASY,200,200)
bombs = place_bombs(grid, 10)
print(bombs)