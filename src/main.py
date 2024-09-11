import pygame
from view.undermine import Mines, Minesweeper

# Dimensions des carrés et de l'écran
WIDTH_SQUARE = 50
HEIGHT_SQUARE = 50
WIDTH_SCREEN = 600
HEIGHT_SCREEN = 650
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    reset_button = pygame.Rect((WIDTH_SCREEN // 2) - (BUTTON_WIDTH // 2), HEIGHT_SCREEN - 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    mines_surf = pygame.image.load('src/demineur/asserts/image/mine.png').convert_alpha()
    mine_model = Mines(mines_surf, WIDTH_SQUARE, HEIGHT_SQUARE)
    game = Minesweeper(mine_model, screen, reset_button)
    game.run()
