import pygame
import circleshape
from constants import *
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        self.__radius = PLAYER_RADIUS
        self.__line_width = PLAYER_LINE_WIDTH
        self.__color = PLAYER_COLOR
        super().__init__(x, y, self.__radius)
        self.rotation = 0
        self.shot_cooldown = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, self.__color,
                            self.triangle(), self.__line_width)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if self.shot_cooldown > 0:
            self.shot_cooldown -= delta_time
        else:
            self.shot_cooldown = 0

        # Move rotate() to Q and E keys
        # Implement strafe() to A and D keys

        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)

        if keys[pygame.K_d]:
            self.rotate(delta_time)

        if keys[pygame.K_w]:
            self.move(delta_time)

        if keys[pygame.K_s]:
            self.move(delta_time * -1)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, delta_time):
        vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += vector * PLAYER_MOVE_SPEED * delta_time

    def shoot(self):
        if self.shot_cooldown > 0:
            return

        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        vector = pygame.Vector2(0, 1).rotate(self.rotation)

        shot.velocity = vector * PLAYER_SHOT_SPEED

        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

        return shot
