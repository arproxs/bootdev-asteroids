import pygame
import constants as CONST


def main():
    print_start()

    game = pygame.init()
    screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))
    running = True

    while running:
        screen.fill('#000000')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return


def print_start():
    print("Starting Asteroids!")
    print(f"Screen width: {CONST.SCREEN_WIDTH}")
    print(f"Screen height: {CONST.SCREEN_HEIGHT}")


if __name__ == '__main__':
    main()
