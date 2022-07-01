from turtle import position
import pygame

class Player:
    def __init__(self, position: tuple, size: tuple, color: pygame.Color, velocity):
        self.size = size
        self.color = color
        self.velocity = velocity
        self.player_direction = "down"

        self.player_rect = pygame.Rect(position[0], position[1],
                                       size[0], size[1])
   
    def draw_player(self, game_window):
        pygame.draw.rect(surface=game_window, color=self.color, rect=self.player_rect)
    
    def move_player(self):
        if self.player_direction == "up":
            self.player_rect.move_ip(0, -self.velocity)
        elif self.player_direction == "down":
            self.player_rect.move_ip(0, self.velocity)
        elif self.player_direction == "right":
            self.player_rect.move_ip(self.velocity, 0)
        elif self.player_direction == "left":
            self.player_rect.move_ip(-self.velocity, 0)