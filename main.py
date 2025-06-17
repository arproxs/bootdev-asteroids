import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print_start()

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(CENTER_WIDTH, CENTER_HEIGHT)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asterid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    delta_time = 0
    running = True
    while running:
        screen.fill(SCREEN_COLOR)

        updatable.update(delta_time)

        for roid in asteroids:
            if roid.detect_collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if roid.detect_collision(bullet):
                    roid.split()
                    bullet.kill()

        for item in drawable:
            item.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        tick = clock.tick(60.0)
        delta_time = tick / 1000.0

        pygame.display.flip()


def print_start():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == '__main__':
    main()
