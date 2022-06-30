import sys, pygame
from player import Player
from pygame import Color


def game():
    pygame.init()
    clock = pygame.time.Clock()

    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    player = Player(position=(100, 100), size=(10, 10), color=Color(255, 0, 0), velocity=10)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    player.move_down()

        player.draw_player(game_window=screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game()