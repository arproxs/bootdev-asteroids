import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__line_width = SHOT_LINE_WIDTH
        self.__color = SHOT_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color, self.position,
                           self.radius, self.__line_width)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)
