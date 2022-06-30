from turtle import position
import pygame

class Player:
    def __init__(self, position: tuple, size: tuple, color: pygame.Color, velocity):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color = color
        self.velocity = velocity

        self.player_rect = pygame.Rect(position[0], position[1],
                                       size[0], size[1])
   
    def draw_player(self, game_window):
        pygame.draw.rect(surface=game_window, color=self.color, rect=self.player_rect)
    
    def move_down(self):
        self.player_rect.move_ip(0, self.velocity)
        