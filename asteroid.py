import pygame
from constants import *
from circleshape import CircleShape
import random


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

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        self._spawn_child(new_radius, random_angle)
        self._spawn_child(new_radius, -random_angle)

    def _spawn_child(self, radius, angle):
        new_asteroid = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid.velocity = self.velocity.rotate(
            angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
        new_asteroid.containers = self.containers
