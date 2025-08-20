import pygame
from constants import *

def main():
    Black = 000000
    game_loop = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Black)
        pygame.display.flip()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
