import pygame
from constants import *
from player import Player

def main():
    Black = 000000
    game_loop = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clockers = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Black)
        player1.draw(screen)
        pygame.display.flip()
        dt = Clockers.tick(60) / 1000
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
