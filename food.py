from random import random
import pygame
import random
from player import Player

class Food:
    def __init__(self, position: tuple, size: tuple, color: tuple):
        self.size = size
        self.color = color
        self.food_rect = pygame.Rect(position[0], position[1],
                                     size[0], size[1])
   
    def draw_food(self, game_window):
        pygame.draw.rect(surface=game_window, color=self.color, rect=self.food_rect)
    
    def check_collision(self, pl: Player):
        if self.food_rect.colliderect(pl.player_rect):
            pl.enlarge_player()
            self.food_rect = pygame.Rect(random.randrange(30, 550), random.randrange(20, 380),
                                         self.size[0], self.size[1])
            