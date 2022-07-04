from tkinter import Y
from turtle import position
import pygame

class Player:
    def __init__(self, position: tuple, size: tuple, color: pygame.Color, velocity):
        self.size = size
        self.color = color
        self.velocity = velocity
        self.player_direction = "down"
        self.x = position[0]
        self.y = position[1]

        self.player_rect = pygame.Rect(self.x, self.y,
                                       size[0], size[1])
   
    def draw_player(self, game_window):
        pygame.draw.rect(surface=game_window, color=self.color, rect=self.player_rect)

    def enlarge_player(self):
        self.player_rect.width += 10
        self.size = ((self.player_rect.width, self.size[1]))
    
    def move_player(self):
        if self.player_direction == "up":
            self.player_rect.move_ip(0, -self.velocity)

        elif self.player_direction == "down":
            self.player_rect.move_ip(0, self.velocity)

        elif self.player_direction == "right":
            self.player_rect.move_ip(self.velocity, 0)

        elif self.player_direction == "left":
            self.player_rect.move_ip(-self.velocity, 0)