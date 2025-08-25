
import pygame as pygame

class Balle:
    def __init__(self,ball_radius, ball_color):
        self.ball_position = [960, 540];
        self.ball_velocity = [0, 0]
        self.ball_radius = ball_radius;
        self.ball_color = ball_color;

    def draw(self,screen):   

        pygame.draw.circle(screen, self.ballColor, self.ball_color, self.ball_radius)