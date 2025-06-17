import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__line_width = ASTEROID_LINE_WIDTH
        self.__color = ASTEROID_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color, self.position,
                           self.radius, self.__line_width)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)
