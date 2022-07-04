import sys, pygame
from player import Player
from food import Food
from pygame import Color


def game():
    pygame.init()
    clock = pygame.time.Clock()

    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    player = Player(position=(100, 100), size=(10, 10), color=Color(255, 0, 0), velocity=1)
    food = Food(position=(300, 200), size=(10, 10), color=(0, 255, 0))

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    player.player_direction = "up"
               
                if keys[pygame.K_DOWN]:
                    player.player_direction = "down"

                if keys[pygame.K_RIGHT]:
                    player.player_direction = "right"

                if keys[pygame.K_LEFT]:
                    player.player_direction = "left"

        player.move_player()
        player.draw_player(game_window=screen)
        food.draw_food(game_window=screen)
        food.check_collision(pl=player)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game()