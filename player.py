from turtle import position
import pygame

class Player:
    def __init__(self, position: tuple, size: tuple, color: pygame.Color):
        self.position = position
        self.size = size
        self.color = color
    
    def draw_player(self, game_window):
        player_rect = pygame.Rect(self.position[0], self.position[1],
                                  self.size[0], self.size[1])

        pygame.draw.rect(surface=game_window, color=self.color, rect=player_rect)