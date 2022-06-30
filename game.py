import sys, pygame
from pygame import Color


def game():
    pygame.init()

    width, height = 400, 500
    screen = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    game()