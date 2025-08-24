import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.position = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"red",[self.x,self.y],self.radius,width=2)

    def update(self,dt):
        self.position += self.velocity * dt