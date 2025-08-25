import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2()

    def draw(self,screen):
        pygame.draw.circle(screen,'aqua',self.position,self.radius,self.radius)

    def update(self,dt):
        self.position += self.velocity * dt