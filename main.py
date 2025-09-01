import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    Black = 000000
    game_loop = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    Clockers = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field1 = AsteroidField()

    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for flying_rock in asteroids:
            if player1.collision(flying_rock):
                print("Game over!")
                return
            for bullet in shots:
                if flying_rock.collision(bullet):
                    bullet.kill()
                    flying_rock.split()


        screen.fill(Black)
        for needs_drawing in drawable:
            needs_drawing.draw(screen)
        pygame.display.flip()

        dt = Clockers.tick(60) / 1000
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
